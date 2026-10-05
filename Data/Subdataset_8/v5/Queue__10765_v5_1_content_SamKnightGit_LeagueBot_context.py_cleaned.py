from enum import Enum
from datetime import datetime
import response
import league
import parse_data
class Context(Enum):
    BASE = 0
    REGISTER_PROMPT = 1
    LEAGUE_IGN_PROMPT = 2
    LEAGUE_IGN_CONFIRM = 3
    DEREGISTER_PROMPT = 4
class ContextManager:
    def __init__(self):
        self.user_contexts = {}
        self.games = {}
    def add_game(self, game_id):
        self.games[game_id] = datetime.now()
    def purge_games(self):
        now = datetime.now()
        self.games = {game_id: game_time for game_id, game_time in self.games.items()
                      if (now - game_time).days > 0}
    async def update_context(self, user_id, message):
        user_context = self.user_contexts.get(user_id)
        if user_context:
            await user_context.update(message)
        else:
            self.user_contexts[user_id] = await UserContext.create(message, user_id)
class UserContext:
    def __init__(self, user_id):
        self.user_id = user_id
        self.summoner_name = None
        self.account_id = None
        self.summoner_id = None
        self.is_registered = False
        self.context = Context.BASE
    @classmethod
    async def create(cls, message, user_id):
        self = cls(user_id)
        if message.content.lower() == "register":
            self.context = Context.LEAGUE_IGN_PROMPT
            await response.league_ign_prompt(message)
        else:
            self.context = Context.REGISTER_PROMPT
            await response.register_prompt(message)
        return self
    async def update(self, message):
        if self.context == Context.BASE:
            await self.handle_base_context(message)
        elif self.context == Context.REGISTER_PROMPT:
            await self.handle_register_prompt_context(message)
        elif self.context == Context.LEAGUE_IGN_PROMPT:
            await self.handle_league_ign_prompt_context(message)
        elif self.context == Context.LEAGUE_IGN_CONFIRM:
            await self.handle_league_ign_confirm_context(message)
        elif self.context == Context.DEREGISTER_PROMPT:
            await self.handle_deregister_prompt_context(message)
    async def handle_base_context(self, message):
        if self.is_registered:
            if message.content.lower() == "deregister":
                self.context = Context.DEREGISTER_PROMPT
                await response.deregister_prompt(message)
            else:
                await self.handle_game_data_message(message)
        else:
            self.context = Context.REGISTER_PROMPT
            await response.register_prompt(message)
    async def handle_game_data_message(self, message):
        game_data = league.get_current_game(self.summoner_id)
        if game_data is None:
            await response.game_not_found(message)
        else:
            stats = await parse_data.parse_game_data(game_data, self.summoner_id)
            await response.game_data(message, stats)
    async def handle_register_prompt_context(self, message):
        if message.content.lower() in ['y', 'yes']:
            self.context = Context.LEAGUE_IGN_PROMPT
            await response.league_ign_prompt(message)
        else:
            self.context = Context.BASE
            await response.cancel_operation(message)
    async def handle_league_ign_prompt_context(self, message):
        result = league.get_summoner_by_name(message.content)
        if result is None:
            self.context = Context.BASE
            await response.league_ign_not_found(message)
        else:
            self.summoner_name = message.content.lower()
            self.summoner_id = result["id"]
            self.account_id = result["accountId"]
            self.context = Context.LEAGUE_IGN_CONFIRM
            await response.league_ign_confirm(message)
    async def handle_league_ign_confirm_context(self, message):
        if message.content.lower() in ["y", "yes"]:
            self.is_registered = True
            self.context = Context.BASE
            await response.register_successful(message)
        else:
            self.reset()
            self.context = Context.BASE
            await response.cancel_operation(message)
    async def handle_deregister_prompt_context(self, message):
        if message.content.lower() in ["y", "yes"]:
            self.reset()
            self.context = Context.BASE
            await response.deregister_successful(message)
        else:
            self.context = Context.BASE
            await response.cancel_operation(message)
    def reset(self):
        self.summoner_name = None
        self.summoner_id = None
        self.account_id = None
        self.is_registered = False
from enum import Enum
from datetime import datetime
import response
import league
import parse_data
class class1(Enum):
    a1 = 0
    a2 = 1
    a3 = 2
    a4 = 3
    a5 = 4
class class2:
    def fonk1(self):
        self.b1 = {}
        self.b2 = {}
    def fonk2(self, game_id):
        self.b2[game_id] = datetime.b3()
    def fonk3(self):
        b3 = datetime.b3()
        b4 = [game_id for game_id, game_time in self.b2.items() if (b3 - game_time).days > 0]
        for game_id in b4:
            del self.b2[game_id]
    async def fonk4(self, b5, message):
        if b5 in self.b1:
            await self.b1[b5].fonk7(message)
        else:
            self.b1[b5] = await class3.fonk6(message, b5)
class class3:
    def fonk5(self, b5):
        self.b5 = b5
        self.b6 = None
        self.b7 = None
        self.b8 = None
        self.b9 = False
        self.b10 = class1.a1
    @classmethod
    async def fonk6(cls, message, b5):
        b11 = cls(b5)
        if message.content.lower() == "register":
            b11.b10 = class1.a3
            await response.league_ign_prompt(message)
        else:
            b11.b10 = class1.a2
            await response.register_prompt(message)
        return b11
    async def fonk7(self, message):
        if self.b10 = = class1.a1:
            await self.fonk8(message)
        elif self.b10 = = class1.a2:
            await self.fonk9(message)
        elif self.b10 = = class1.a3:
            await self.fonk10(message)
        elif self.b10 = = class1.a4:
            await self.fonk11(message)
        elif self.b10 = = class1.a5:
            await self.fonk12(message)
    async def fonk8(self, message):
        if self.b9:
            if message.content.lower() == "deregister":
                self.b10 = class1.a5
                await response.deregister_prompt(message)
            else:
                b12 = league.get_current_game(self.b8)
                if b12 is None:
                    await response.game_not_found(message)
                else:
                    b13 = await parse_data.parse_game_data(b12, self.b8)
                    await response.b12(message, b13)
        else:
            self.b10 = class1.a2
            await response.register_prompt(message)
    async def fonk9(self, message):
        if message.content.lower() in ['y', 'yes']:
            self.b10 = class1.a3
            await response.league_ign_prompt(message)
        else:
            self.b10 = class1.a1
            await response.cancel_operation(message)
    async def fonk10(self, message):
        b14 = league.get_summoner_by_name(message.content)
        if b14 is None:
            self.b10 = class1.a1
            await response.league_ign_not_found(message)
        else:
            self.b6 = message.content.lower()
            self.b8 = b14["id"]
            self.b7 = b14["accountId"]
            self.b10 = class1.a4
            await response.league_ign_confirm(message)
    async def fonk11(self, message):
        if message.content.lower() in ["y", "yes"]:
            self.b9 = True
            self.b10 = class1.a1
            await response.register_successful(message)
        else:
            self.fonk13()
            self.b10 = class1.a1
            await response.cancel_operation(message)
    async def fonk12(self, message):
        if message.content.lower() in ["y", "yes"]:
            self.fonk13()
            self.b10 = class1.a1
            await response.deregister_successful(message)
        else:
            self.b10 = class1.a1
            await response.cancel_operation(message)
    def fonk13(self):
        self.b6 = None
        self.b8 = None
        self.b7 = None
        self.b9 = False
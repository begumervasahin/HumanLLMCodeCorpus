from enum import Enum
from datetime import datetime
class class1(Enum):
    a1 = 0
    a2 = 1
    a3 = 2
    a4 = 3
    a5 = 4
class class2:
    def fonk1(b12):
        b12.b1 = {}
        b12.b2 = {}
    def fonk2(b12, game_id):
        b12.b2[game_id] = datetime.b3()
    def fonk3(b12):
        b3 = datetime.b3()
        for game_id, game_time in list(b12.b2.items()):
            b4 = b3 - game_time
            if b4.days > 0:
                del b12.b2[game_id]
    async def fonk4(b12, b6, message):
        b5 = b12.b1.get(b6)
        if b5:
            await b5.fonk7(message)
        else:
            b12.b1[b6] = await class3.fonk6(message, b6)
class class3:
    def fonk5(b12):
        b12.b6 = None
        b12.b7 = None
        b12.b8 = None
        b12.b9 = None
        b12.b10 = False
        b12.b11 = class1.a1
    @classmethod
    async def fonk6(cls, message, b6):
        b12 = class3()
        b12.b6 = b6
        if message.content.lower() == "register":
            b12.b11 = class1.a3
            await response.league_ign_prompt(message)
        else:
            b12.b11 = class1.a2
            await response.register_prompt(message)
        return b12
    async def fonk7(b12, message):
        if b12.b11 = = class1.a1:
            if b12.b10:
                if message.content.lower() == "deregister":
                    b12.b11 = class1.a5
                    await response.deregister_prompt(message)
                else:
                    b13 = league.get_current_game(b12.b9)
                    if b13 is None:
                        await response.game_not_found(message)
                    else:
                        b14 = await parse_data.parse_game_data(b13, b12.b9)
                        await response.b13(message, b14)
            else:
                b12.b11 = class1.a2
                await response.register_prompt(message)
        elif b12.b11 = = class1.a2:
            if message.content.lower() in ['y', 'yes']:
                b12.b11 = class1.a3
                await response.league_ign_prompt(message)
            else:
                b12.b11 = class1.a1
                await response.cancel_operation(message)
        elif b12.b11 = = class1.a3:
            b15 = league.get_summoner_by_name(message.content)
            if b15 is None:
                b12.b11 = class1.a1
                await response.league_ign_not_found(message)
            else:
                b12.b7 = message.content.lower()
                b12.b9 = b15["id"]
                b12.b8 = b15["accountId"]
                b12.b11 = class1.a4
                await response.league_ign_confirm(message)
        elif b12.b11 = = class1.a4:
            if message.content.lower() in ["y", "yes"]:
                b12.b10 = True
                b12.b11 = class1.a1
                await response.register_successful(message)
            else:
                b12.fonk8()
                b12.b11 = class1.a1
                await response.cancel_operation(message)
        elif b12.b11 = = class1.a5:
            if message.content.lower() in ["y", "yes"]:
                b12.fonk8()
                b12.b11 = class1.a1
                await response.deregister_successful(message)
            else:
                b12.b11 = class1.a1
                await response.cancel_operation(message)
    def fonk8(b12):
        b12.b7 = None
        b12.b9 = None
        b12.b8 = None
        b12.b10 = False
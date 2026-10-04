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
    def fonk1(b11):
        b11.b1 = {}
        b11.b2 = {}
    def fonk2(b11, game_id):
        b11.b2[game_id] = datetime.b3()
    def fonk3(b11):
        b3 = datetime.b3()
        for game_time in b11.b2.values():
            b4 = b3 - game_time
            if b4.days > 0:
                del b11.b2[game_time]
    async def fonk4(b11, b5, message):
        if b10 := b11.b1.get(b5, None):
            await b10.fonk7(message)
        else:
            b11.b1[b5] = await class3.fonk6(message, b5)
class class3:
    def fonk5(b11):
        b11.b5 = None
        b11.b6 = None
        b11.b7 = None
        b11.b8 = None
        b11.b9 = False
        b11.b10 = class1.a1
    @classmethod
    async def fonk6(cls, message, b5):
        b11 = class3()
        b11.b5 = b5
        b11.b6 = None
        b11.b7 = None
        b11.b8 = None
        b11.b9 = False
        if message.content.lower() == "register":
            b11.b10 = class1.a3
            await response.a3(message)
        else:
            b11.b10 = class1.a2
            await response.a2(message)
        return b11
    async def fonk7(b11, message):
        if b11.b10 = = class1.a1:
            if b11.b9:
                if message.content.lower() == "deregister":
                    b11.b10 = class1.a5
                    await response.a5(message)
                else:
                    b12 = league.get_current_game(b11.b8)
                    if b12 is None:
                        await response.game_not_found(message)
                    else:
                        b13 = await parse_data.parse_game_data(b12, b11.b8)
                        await response.b12(message, b13)
            else:
                b11.b10 = class1.a2
                await response.a2(message)
        elif b11.b10 = = class1.a2:
            if message.content.lower() in ['y', 'yes']:
                b11.b10 = class1.a3
                await response.a3(message)
            else:
                b11.b10 = class1.a1
                await response.cancel_operation(message)
        elif b11.b10 = = class1.a3:
            b14 = league.get_summoner_by_name(message.content)
            if b14 is None:
                b11.b10 = class1.a1
                await response.league_ign_not_found(message)
            else:
                b11.b6 = message.content.lower()
                b11.b8 = b14["id"]
                b11.b7 = b14["accountId"]
                b11.b10 = class1.a4
                await response.a4(message)
        elif b11.b10 = = class1.a4:
            if message.content.lower() in ["y", "yes"]:
                b11.b9 = True
                b11.b10 = class1.a1
                await response.register_successful(message)
            else:
                b11.fonk8()
                b11.b10 = class1.a1
                await response.cancel_operation(message)
        elif b11.b10 = = class1.a5:
            if message.content.lower() in ["y", "yes"]:
                b11.fonk8()
                b11.b10 = class1.a1
                await response.deregister_successful(message)
            else:
                b11.b10 = class1.a1
                await response.cancel_operation(message)
    def fonk8(b11):
        b11.b6 = None
        b11.b8 = None
        b11.b7 = None
        b11.b9 = False
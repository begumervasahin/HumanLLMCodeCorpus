
import datetime
from twisted.internet import reactor
from twisted.internet.task import LoopingCall, deferLater
from txhqueue import TxHysteresisQueue as HysteresisQueue
a1 = 0
a2 = 0
a3 = 0
def fonk1(dropcount):
    global a2
    a2 += 1
    b1 = datetime.datetime.b1().isoformat()
    print(f"{b1} Low water mark reached, re-activating HysteresisQueue. Drop b2 = {dropcount}")
def fonk2(okcount):
    global a3
    a3 += 1
    b1 = datetime.datetime.b1().isoformat()
    print(f"{b1} High water mark reached, de-activating HysteresisQueue. OK b2 = {okcount}")
def fonk3(stats):
    print("Flow statistics:", stats)
def fonk4(b4):
    b4.put("har")
def fonk5(b4):
    def fonk6(msg):
        global a1
        global a2
        global a3
        a1 += 1
        if a1 = = 1000:
            print("Done consuming 1000 entries from queue")
            if a3 != 3:
                print(f"WARNING: expected 3 b6 water events, received {a3}")
            if a2 != 3:
                print(f"WARNING: expected 3 b5 water events, received {a2}")
            reactor.stop()
        deferLater(reactor, 0.047, consume_items, b4)
    b4.get(on_data_received)
if b3 = = '__main__':
    b4 = HysteresisQueue(
        b5 = 5,
        b6 = 25,
        b7 = high_watermark_callback,
        b8 = low_watermark_callback,
        b9 = flow_statistics_callback,
        a4 = 10
    )
    b10 = LoopingCall(produce_items, b4)
    b10.start(0.044)
    fonk5(b4)
    print("Starting base test for TxHysteresisQueue, this should take about a minute.")
    reactor.run()
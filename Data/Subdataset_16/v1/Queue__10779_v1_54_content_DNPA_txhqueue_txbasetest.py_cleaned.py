
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
    print(b1, "Low water mark reached, re-activating HysteresisQueue. Drop b2 = ", dropcount)
def fonk2(okcount):
    global a3
    a3 += 1
    b1 = datetime.datetime.b1().isoformat()
    print(b1, "High water mark reached, de-activating HysteresisQueue. OK b2 = ", okcount)
def fonk3(obj):
    print("Flowstat:", obj)
def fonk4(hqueue):
    hqueue.put("har")
def fonk5(hqueue):
    def fonk6(msg):
        global a1
        global a2
        global a3
        a1 += 1
        if a1 = = 1000:
            print("Done consuming 1000 entries from queue")
            if a3 != 3:
                print("WARNING: expected 3 b5 water events, received", a3)
            if a2 != 3:
                print("WARNING: expected 3 b4 water events, received", a2)
            reactor.stop()
        deferLater(reactor, 0.047, consume, hqueue)
    hqueue.get(cb1)
b3 = HysteresisQueue(
    b4 = 5,
    b5 = 25,
    b6 = high_watermark,
    b7 = low_watermark,
    b8 = flowstat,
    a4 = 10
)
b9 = LoopingCall(produce, b3)
b9.start(0.044)
fonk5(b3)
print("Starting base test for TxHysteresisQueue, this should take about a minute.")
reactor.run()
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
def fonk3(obj):
    print("Flow Statistics:", obj)
def fonk4(h_queue):
    h_queue.put("har")
def fonk5(h_queue):
    global a1
    global a2
    global a3
    def fonk6(msg):
        nonlocal a1
        a1 += 1
        if a1 = = 1000:
            print("Done consuming 1000 entries from the queue")
            if a3 != 3:
                print("WARNING: Expected 3 high water events, received", a3)
            if a2 != 3:
                print("WARNING: Expected 3 low water events, received", a2)
            reactor.stop()
        deferLater(reactor, 0.047, consume, h_queue)
    h_queue.get(consume_callback)
b3 = HysteresisQueue(low=5, high=25, highwater=high_watermark, lowwater=low_watermark,
                           b4 = flow_statistics, flowstat_interval=10)
b5 = LoopingCall(produce, b3)
b5.start(0.044)
fonk5(b3)
print("Starting the base test for TxHysteresisQueue. This should take about a minute.")
reactor.run()
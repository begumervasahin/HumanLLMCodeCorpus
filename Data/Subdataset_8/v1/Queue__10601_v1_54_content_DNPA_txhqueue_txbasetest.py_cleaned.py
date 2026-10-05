import datetime
from twisted.internet import reactor
from twisted.internet.task import LoopingCall, deferLater
from txhqueue import TxHysteresisQueue as HysteresisQueue
consume_count = 0
low_water_count = 0
high_water_count = 0
def lowwatermark(dropcount):
    global low_water_count
    low_water_count += 1
    now = datetime.datetime.now().isoformat()
    print(now, "Low water mark reached, re-activating HysteresisQueue. Drop count =", dropcount)
def highwatermark(okcount):
    global high_water_count
    high_water_count += 1
    now = datetime.datetime.now().isoformat()
    print(now, "High water mark reached, de-activating HysteresisQueue. OK count =", okcount)
def flowstat(obj):
    print("Flowstat:", obj)
def produce(hqueue):
    hqueue.put("har")
def consume(hqueue):
    def cb1(msg):
        global consume_count
        global low_water_count
        global high_water_count
        consume_count += 1
        if consume_count == 1000:
            print("Done consuming 1000 entries from queue")
            if high_water_count != 3:
                print("WARNING: expected 3 high water events, received", high_water_count)
            if low_water_count != 3:
                print("WARNING: expected 3 low water events, received", low_water_count)
            reactor.stop()
        deferLater(reactor, 0.047, consume, hqueue)
    hqueue.get(cb1)
HQUEUE = HysteresisQueue(low=5, high=25, highwater=highwatermark, lowwater=lowwatermark,
                         flowstat_cb=flowstat, flowstat_interval=10)
LC = LoopingCall(produce, HQUEUE)
LC.start(0.044)
consume(HQUEUE)
print("Starting base test for TxHysteresisQueue, this should take about a minute.")
reactor.run()

import datetime
from twisted.internet import reactor
from twisted.internet.task import LoopingCall, deferLater
from txhqueue import TxHysteresisQueue as HysteresisQueue
consume_count = 0
low_water_count = 0
high_water_count = 0
def low_watermark(dropcount):
    global low_water_count
    low_water_count += 1
    now = datetime.datetime.now().isoformat()
    print(f"{now} Low water mark reached, re-activating HysteresisQueue. Drop count = {dropcount}")
def high_watermark(okcount):
    global high_water_count
    high_water_count += 1
    now = datetime.datetime.now().isoformat()
    print(f"{now} High water mark reached, de-activating HysteresisQueue. OK count = {okcount}")
def flow_statistics(stats):
    print(f"Flow statistics: {stats}")
def produce(hqueue):
    hqueue.put("har")
def consume(hqueue):
    def data_callback(msg):
        global consume_count
        global low_water_count
        global high_water_count
        consume_count += 1
        if consume_count == 1000:
            print("Done consuming 1000 entries from queue")
            if high_water_count != 3:
                print(f"WARNING: expected 3 high water events, received {high_water_count}")
            if low_water_count != 3:
                print(f"WARNING: expected 3 low water events, received {low_water_count}")
            reactor.stop()
        deferLater(reactor, 0.047, consume, hqueue)
    hqueue.get(data_callback)
hqueue = HysteresisQueue(
    low=5,
    high=25,
    highwater=high_watermark,
    lowwater=low_watermark,
    flowstat_cb=flow_statistics,
    flowstat_interval=10
)
producer_loop = LoopingCall(produce, hqueue)
producer_loop.start(0.044)
consume(hqueue)
print("Starting base test for TxHysteresisQueue, this should take about a minute.")
reactor.run()
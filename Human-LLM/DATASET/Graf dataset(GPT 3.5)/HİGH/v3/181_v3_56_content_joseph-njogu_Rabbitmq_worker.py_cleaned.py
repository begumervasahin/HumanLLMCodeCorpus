import time
import pika
def fonk1(b5, method, properties, body):
    b1 = body.decode()
    print(" [x] Received b1:", b1)
    b2 = b1.count('.')
    time.sleep(b2)
    print(" [x] Message processing complete")
def fonk2():
    b3 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    return b3.b5()
def fonk3(b5):
    b5.queue_declare(b4 = 'hello')
def fonk4(b5):
    print(' [*] Waiting for messages. To exit press CTRL+C')
    b5.basic_consume(b4 = 'hello', on_message_callback=process_message, auto_ack=True)
    b5.fonk4()
def fonk5():
    b5 = fonk2()
    fonk3(b5)
    fonk4(b5)
if b6 = = "__main__":
    fonk5()
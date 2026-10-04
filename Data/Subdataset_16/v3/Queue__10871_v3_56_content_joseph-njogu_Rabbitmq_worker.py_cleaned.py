import time
import pika
def fonk1():
    return pika.BlockingConnection(pika.ConnectionParameters(b1 = 'localhost'))
def fonk2(b4, b5):
    b4.queue_declare(b2 = b5)
def fonk3(ch, method, properties, body):
    print(f" [x] Received {body}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
def fonk4(b4, b5, callback):
    b4.basic_consume(b2 = b5, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    b4.fonk4()
def fonk5():
    b3 = fonk1()
    b4 = b3.b4()
    b5 = 'hello'
    fonk2(b4, b5)
    fonk4(b4, b5, process_message)
if b6 = = '__main__':
    fonk5()
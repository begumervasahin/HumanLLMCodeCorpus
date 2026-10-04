import time
import pika
def fonk1():
    b1 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    return b1.b4()
def fonk2(b4, b5):
    b4.queue_declare(b2 = b5)
def fonk3(ch, method, properties, body):
    print(f" [x] Received {body!r}")
    b3 = body.count(b'.')
    time.sleep(b3)
    print(" [x] Done")
def fonk4(b4, b5, callback):
    b4.basic_consume(b2 = b5, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    b4.start_consuming()
def fonk5():
    b4 = fonk1()
    b5 = 'hello'
    fonk2(b4, b5)
    fonk4(b4, b5, message_callback)
if b6 = = '__main__':
    fonk5()
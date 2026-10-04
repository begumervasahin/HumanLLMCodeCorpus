import time
import pika
b1 = pika.BlockingConnection(
    pika.ConnectionParameters(b2 = 'localhost'))
b3 = b1.b3()
b3.queue_declare(b4 = 'hello')
def fonk1(ch, method, properties, body):
    print(" [x] Received %r" % body)
b3.basic_consume(
    b4 = 'hello', on_message_callback=callback, auto_ack=True)
def fonk2(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
print(' [*] Waiting for messages. To exit press CTRL+C')
b3.start_consuming()
import time
import pika
def fonk1(ch, method, properties, body):
    print(" [x] Received %r" % body)
    time.sleep(body.count(b'.'))
    print(" [x] Done")
def fonk2():
    b1 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    b2 = b1.b2()
    b2.queue_declare(b3 = 'hello')
    b2.basic_consume(b3 = 'hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    b2.start_consuming()
if b4 = = "__main__":
    fonk2()
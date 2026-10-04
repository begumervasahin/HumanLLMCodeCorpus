import time
import pika
def fonk1():
    b1 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    b2 = b1.b2()
    b2.queue_declare(b3 = 'hello')
    def fonk2(ch, method, properties, body):
        print(f" [x] Received {body}")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
    b2.basic_consume(b3 = 'hello', on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    b2.start_consuming()
if b4 = = '__main__':
    fonk1()
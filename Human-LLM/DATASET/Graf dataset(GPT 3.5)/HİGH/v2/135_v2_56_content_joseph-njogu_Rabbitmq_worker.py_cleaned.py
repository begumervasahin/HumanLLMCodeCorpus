import time
import pika
def fonk1(b2, method, properties, body):
    print(" [x] Received message:", body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Message processing complete")
def fonk2():
    b1 = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    b2 = b1.b2()
    b2.queue_declare(b3 = 'hello')
    print(' [*] Waiting for messages. To exit press CTRL+C')
    b2.basic_consume(b3 = 'hello', on_message_callback=process_message, auto_ack=True)
    b2.start_consuming()
if b4 = = "__main__":
    fonk2()
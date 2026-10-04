import time
import pika
def establish_connection():
    return pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
def declare_queue(channel, queue_name):
    channel.queue_declare(queue=queue_name)
def process_message(ch, method, properties, body):
    print(f" [x] Received {body}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
def start_consuming(channel, queue_name, callback):
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
def main():
    connection = establish_connection()
    channel = connection.channel()
    queue_name = 'hello'
    declare_queue(channel, queue_name)
    start_consuming(channel, queue_name, process_message)
if __name__ == '__main__':
    main()
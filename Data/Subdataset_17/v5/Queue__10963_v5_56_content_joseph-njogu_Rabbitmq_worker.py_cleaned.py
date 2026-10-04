import time
import pika
def establish_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    return connection.channel()
def declare_queue(channel, queue_name):
    channel.queue_declare(queue=queue_name)
def message_callback(ch, method, properties, body):
    print(f" [x] Received {body!r}")
    time_to_sleep = body.count(b'.')
    time.sleep(time_to_sleep)
    print(" [x] Done")
def start_consumer(channel, queue_name, callback):
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
def main():
    channel = establish_connection()
    queue_name = 'hello'
    declare_queue(channel, queue_name)
    start_consumer(channel, queue_name, message_callback)
if __name__ == '__main__':
    main()
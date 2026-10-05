import time
import pika
def process_message(channel, method, properties, body):
    message = body.decode()
    print(" [x] Received message:", message)
    processing_time = message.count('.')
    time.sleep(processing_time)
    print(" [x] Message processing complete")
def establish_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    return connection.channel()
def declare_queue(channel):
    channel.queue_declare(queue='hello')
def start_consuming(channel):
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(queue='hello', on_message_callback=process_message, auto_ack=True)
    channel.start_consuming()
def main():
    channel = establish_connection()
    declare_queue(channel)
    start_consuming(channel)
if __name__ == "__main__":
    main()
import time
import pika
def process_message(channel, method, properties, body):
    print(" [x] Received message:", body.decode())
    time.sleep(body.count(b'.'))
    print(" [x] Message processing complete")
def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.basic_consume(queue='hello', on_message_callback=process_message, auto_ack=True)
    channel.start_consuming()
if __name__ == "__main__":
    main()
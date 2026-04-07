import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(f" [x] Received Body {body.decode()}")
    print(f" [x] Received Method {method}")
    print(f" [x] Received Channel {channel}")
    print(f" [x] Received Properties {properties}")

channel.basic_consume(queue='user_email', on_message_callback=callback, auto_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

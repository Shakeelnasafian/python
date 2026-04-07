import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='user_email')

email = "shakeelnasafian@gmail.com"

channel.basic_publish(exchange='', routing_key='user_email', body=email)

print(f" [x] Sent {email}")

connection.close()
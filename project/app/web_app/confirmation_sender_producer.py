import pika
import sys
import json

def send_confirmation(email, html, subject):
	conn_params = pika.ConnectionParameters('rabbit', 5672)
	connection = pika.BlockingConnection(conn_params)
	channel = connection.channel()

	channel.queue_declare(queue='queue')

	sys.stdout.flush()
	channel.basic_publish(exchange='',
				  routing_key='queue',
				  body=json.dumps((email, html, subject))
			     )
	connection.close()

from flask import Flask
from config import Config
from flask_mail import Mail
from flask_mail import Message
import re
import json
import sys
import re
import pika
import traceback, sys
import datetime 



app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)


def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)

def callback(ch, method, properties, body):
    with app.app_context(): 
        b = str(body)[2:-1]
        sys.stdout.flush()
        params = re.split("\", ",b[1:-1])
        email = params[0][1:]
        html = re.sub("\\\\n",'\n', params[1][1:])
        subject = params[2][1:-1]

        send_email(email, subject, html)
        channel.basic_ack(delivery_tag=method.delivery_tag)




if __name__ == "__main__":

    conn_params = pika.ConnectionParameters('rabbit', 5672)
    connection = pika.BlockingConnection(conn_params)
    channel = connection.channel()
    channel.queue_declare(queue='queue')



    channel.basic_consume(on_message_callback=callback, queue='queue')
   
    while(True):
        try:
   
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
        except Exception:
            channel.stop_consuming()
            traceback.print_exc(file=sys.stdout)
            break           
   

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='172.17.0.2'))
channel = connection.channel()

channel.exchange_declare(exchange='build',
                         exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='build',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()


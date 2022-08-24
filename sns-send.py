#!/usr/bin/python3.8
# Sample Code to send message to a SQS queue
import boto3
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='TradeStatus.fifo')
#print(queue.url)
#print(queue.attributes.get('DelaySeconds'))

response = queue.send_message(MessageBody='world', MessageGroupId='messageGroup1')
print(response.get('MessageId'))
print(response.get('MD5OfMessageBody'))

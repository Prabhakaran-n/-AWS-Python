#!/usr/bin/python3.8
# Sample Code to receive and delete message from SQS queue
import time
import boto3
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='TradeStatus.fifo')

while True:
    messages = queue.receive_messages()
    print('Amount of existing queue messages',len(messages))
    for message in messages:
        print('msg:', message.body)
        message.delete()
    time.sleep(2)

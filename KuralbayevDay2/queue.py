from azure.storage.queue import QueueService



queue_service = QueueService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')


############# Create queue #############

# queue_service.create_queue('taskqueue')





############# Insert a Message into a Queue #############

# queue_service.put_message('taskqueue', u'Hello World')

# queue_service.put_message('taskqueue', u'Hello World1')
# queue_service.put_message('taskqueue', u'Hello World2')
# queue_service.put_message('taskqueue', u'Hello World3')
# queue_service.put_message('taskqueue', u'Hello World4')
# queue_service.put_message('taskqueue', u'Hello World5')
# queue_service.put_message('taskqueue', u'Hello World6')




############# Peek at the Next Message #############

# messages = queue_service.peek_messages('taskqueue')
# for message in messages:
#     print(message.content)




############# Dequeue Messages #############

# messages = queue_service.get_messages('taskqueue', num_messages=16, visibility_timeout=5*60)
# for message in messages:
#     print(message.content)
#     queue_service.delete_message('taskqueue', message.id, message.pop_receipt)




############# Change the Contents of a Queued Message #############


# messages = queue_service.get_messages('taskqueue')
# for message in messages:
#     queue_service.update_message('taskqueue', message.id, message.pop_receipt, 0, u'Hello World Again')




############# Get the Queue Length #############


# metadata = queue_service.get_queue_metadata('taskqueue')
# count = metadata.approximate_message_count
# print(count)



############# Delete a Queue #############


# queue_service.delete_queue('taskqueue')






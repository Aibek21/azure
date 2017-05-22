from azure.storage.queue import QueueService



queue_service = QueueService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')

messages = queue_service.get_messages('taskqueue', visibility_timeout=5*60)
url = ''
for message in messages:
    print(message.content)
    url = message.content
    queue_service.delete_message('taskqueue', message.id, message.pop_receipt)


import urllib2
response = urllib2.urlopen(url)
html = response.read()



sum = 0

a = html.splitlines()
for i in a:
        sum += int(i)

print sum


from azure.storage.table import TableService, Entity
import datetime

table_service = TableService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')
now = datetime.datetime.now()

date = str(now.year)+str(now.month)+str(now.day)


xml = '<?xml version="1.0" encoding="UTF-8"?>\n<Root>\n<Sum>'+str(sum)+'</Sum>\n</Root>'
task = {'PartitionKey': 'G1', 'RowKey': 'D_'+date, 'status' : '1', 'sum' : xml}
table_service.update_entity('tasktable', task)

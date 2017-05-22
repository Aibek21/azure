from azure.storage.blob import BlockBlobService
import datetime

now = datetime.datetime.now()

date = str(now.year)+str(now.month)+str(now.day)
block_blob_service = BlockBlobService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')

from azure.storage.blob import PublicAccess


block_blob_service.set_container_acl('mycontainer', public_access=PublicAccess.Container)



from azure.storage.blob import ContentSettings
block_blob_service.create_blob_from_path(
    'mycontainer',
    'block_blob',
    'g1.txt',
    content_settings=ContentSettings(content_type='text/plain')
            )


url = block_blob_service.make_blob_url('mycontainer',
    'block_blob')


print url

from azure.storage.table import TableService, Entity
table_service = TableService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')



task = Entity()
task.PartitionKey = 'G1'
task.RowKey = 'D_'+date
task.status = 0
task.sum = ''
table_service.insert_or_replace_entity('tasktable', task)




from azure.storage.queue import QueueService
queue_service = QueueService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')



queue_service.put_message('taskqueue', url.decode('unicode-escape'))





from azure.storage.blob import BlockBlobService



block_blob_service = BlockBlobService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')



############# Create blob container #############

# block_blob_service.create_container('mycontainer')




############# PublicAccess #############

from azure.storage.blob import PublicAccess

# block_blob_service.create_container('mycontainer', public_access=PublicAccess.Container)



block_blob_service.set_container_acl('mycontainer', public_access=PublicAccess.Container)




############# Upload file #############

# from azure.storage.blob import ContentSettings
# block_blob_service.create_blob_from_path(
#     'mycontainer',
#     'myblockblob',
#     'sunset.png',
#     content_settings=ContentSettings(content_type='image/png')
#             )





############# List the blobs in a container #############

# generator = block_blob_service.list_blobs('mycontainer')
# for blob in generator:
#     print(blob.name)




############# Download blobs #############


# block_blob_service.get_blob_to_path('mycontainer', 'myblockblob', 'out-sunset.png')



############# Delete a blob #############

# block_blob_service.delete_blob('mycontainer', 'myblockblob')



############# Writing to an append blob #############


# from azure.storage.blob import AppendBlobService
# append_blob_service = AppendBlobService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')

# # The same containers can hold all types of blobs
# append_blob_service.create_container('appendcontainer')

# # Append blobs must be created before they are appended to
# append_blob_service.create_blob('appendcontainer', 'myappendblob')
# append_blob_service.append_blob_from_text('appendcontainer', 'myappendblob', u'Hello, world!')

# append_blob = append_blob_service.get_blob_to_text('appendcontainer', 'myappendblob')



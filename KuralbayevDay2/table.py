from azure.storage.table import TableService, Entity



table_service = TableService(account_name='kuralbayevday1', account_key='8onfJI8YYDJ9pB+SLOcFycntsRnL+iJm6y7R0mhTk8mSKZs9bXBo1v19bdwYOW4ts09440t6Gct2H2JtvjosRQ==')



############# Create table #############

# table_service.create_table('tasktable')



############# Create entity #############

# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'Take out the trash', 'priority' : 200}
# table_service.insert_entity('tasktable', task)


# task = Entity()
# task.PartitionKey = 'tasksSeattle'
# task.RowKey = '002'
# task.description = 'Wash the car'
# task.priority = 100
# table_service.insert_entity('tasktable', task)





############# Update entity #############

# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'Take out the garbage', 'priority' : 250}
# table_service.update_entity('tasktable', task)


# # Replace the entity created earlier
# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '001', 'description' : 'Take out the garbage again', 'priority' : 250}
# table_service.insert_or_replace_entity('tasktable', task)

# # Insert a new entity
# task = {'PartitionKey': 'tasksSeattle', 'RowKey': '003', 'description' : 'Buy detergent', 'priority' : 300}
# table_service.insert_or_replace_entity('tasktable', task)





############# Modify multiple entities #############

# from azure.storage.table import TableBatch
# batch = TableBatch()
# task004 = {'PartitionKey': 'tasksSeattle', 'RowKey': '004', 'description' : 'Go grocery shopping', 'priority' : 400}
# task005 = {'PartitionKey': 'tasksSeattle', 'RowKey': '005', 'description' : 'Clean the bathroom', 'priority' : 100}
# batch.insert_entity(task004)
# batch.insert_entity(task005)
# table_service.commit_batch('tasktable', batch)


# task006 = {'PartitionKey': 'tasksSeattle', 'RowKey': '006', 'description' : 'Go grocery shopping', 'priority' : 400}
# task007 = {'PartitionKey': 'tasksSeattle', 'RowKey': '007', 'description' : 'Clean the bathroom', 'priority' : 100}

# with table_service.batch('tasktable') as batch:
#     batch.insert_entity(task006)
#     batch.insert_entity(task007)





############# Query for an entity #############

# task = table_service.get_entity('tasktable', 'tasksSeattle', '001')
# print(task.description)
# print(task.priority)




############# Query a set of entities #############

# tasks = table_service.query_entities('tasktable', filter="PartitionKey eq 'tasksSeattle'")
# for task in tasks:
#     print(task.description)
#     print(task.priority)





############# Query a subset of entity properties #############

# tasks = table_service.query_entities('tasktable', filter="PartitionKey eq 'tasksSeattle'", select='description')
# for task in tasks:
#     print(task.description)





############# Delete an entity #############

# table_service.delete_entity('tasktable', 'tasksSeattle', '001')


############# Delete an entity #############

# table_service.delete_table('tasktable')






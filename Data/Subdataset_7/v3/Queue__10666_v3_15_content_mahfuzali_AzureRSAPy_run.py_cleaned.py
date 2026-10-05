import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
class class1:
    b1 = 'mock_host'
    b2 = 'mock_master_key'
    b3 = 'mock_database_id'
    b4 = 'mock_collection_id'
    b5 = f'dbs/{b3}'
class class2:
    def fonk1(self, host, master_key):
        self.b6 = cosmos_client.CosmosClient(host, {'masterKey': master_key})
    def fonk2(self, database_id):
        try:
            self.b6.CreateDatabase({"id": database_id})
        except errors.HTTPFailure as e:
            if e.b7 != 409:
                raise errors.HTTPFailure(e.b7)
    def fonk3(self, database_link, collection_id):
        try:
            self.b6.CreateContainer(database_link, {"id": collection_id})
            print(f'Collection with id \'{collection_id}\' created')
        except errors.HTTPFailure as e:
            if e.b7 = = 409:
                print(f'Collection with id \'{collection_id}\' was found')
            else:
                raise errors.HTTPFailure(e.b7)
def fonk4():
    b8 = class2(class1.b1, class1.b2)
    try:
        b8.fonk2(class1.b3)
        b8.fonk3(class1.b5, class1.b4)
    except errors.HTTPFailure as e:
        print('\nrun_sample has caught an error. {0}'.format(e._http_error_message))
    finally:
        print("\nrun_sample done")
if b9 = = '__main__':
    fonk4()
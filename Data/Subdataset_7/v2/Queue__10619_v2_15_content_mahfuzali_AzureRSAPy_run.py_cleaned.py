import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        return self.b1
    def fonk3(self, exc_type, exc_value, traceback):
        self.b1.Close()
class class2:
    pass
class class3:
    def fonk4(self):
        return {'publicKey': 'mock_public_key', 'privateKey': 'mock_private_key'}
class class4:
    pass
class class5:
    pass
class class6:
    def fonk5(self, b2, b3):
        self.b2 = b2
        self.b3 = b3
class class7:
    b4 = 'mock_host'
    b5 = 'mock_master_key'
    b6 = 'mock_database_id'
    b7 = 'mock_collection_id'
    b8 = f'dbs/{b6}'
def fonk6():
    b9 = cosmos_client.CosmosClient(class7.b4, {'masterKey': class7.b5})
    with class1(b9) as client:
        try:
            try:
                client.CreateDatabase({"id": class7.b6})
            except errors.HTTPFailure as e:
                if e.b10 = = 409:
                    pass
                else:
                    raise errors.HTTPFailure(e.b10)
            try:
                client.CreateContainer(class7.b8, {"id": class7.b7})
                print('Collection with id \'{0}\' created'.format(class7.b7))
            except errors.HTTPFailure as e:
                if e.b10 = = 409:
                    print('Collection with id \'{0}\' was found'.format(class7.b7))
                else:
                    raise errors.HTTPFailure(e.b10)
        except errors.HTTPFailure as e:
            print('\nrun_sample has caught an error. {0}'.format(e._http_error_message))
        finally:
            print("\nrun_sample done")
if b11 = = '__main__':
    fonk6()
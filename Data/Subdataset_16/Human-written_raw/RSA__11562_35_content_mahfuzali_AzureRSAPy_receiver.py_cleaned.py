import crypto.hashing as hashing
import crypto.keys as keys
import users.user as user
import crypto.signature as signature
import crypto.encrypt as encrypt
import database.db as d
import json
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
def fonk1():
    print("Running receiver")
    with d.IDisposable(cosmos_client.CosmosClient(d.HOST, {'masterKey': d.MASTER_KEY} )) as client:
        try:
            ''''''
            try:
                client.CreateDatabase({"id": d.DATABASE_ID})
            except errors.HTTPFailure as e:
                if e.b1 = = 409:
                    pass
                else:
                    raise errors.HTTPFailure(e.b1)
            try:
                client.CreateContainer(d.database_link, {"id": d.COLLECTION_ID})
                print('Collection with id \'{0}\' created'.format(d.COLLECTION_ID))
            except errors.HTTPFailure as e:
                if e.b1 = = 409:
                    print('Collection with id \'{0}\' was found'.format(d.COLLECTION_ID))
                else:
                    raise errors.HTTPFailure(e.b1)
            b2 = d.DocumentManagement.ReadDocument(client,'0376af03-9620-4980-a905-dbfa6b189495')
            b3 = keys.Key().read_key(b2['b3'])
            b4 = keys.Key().read_key_from_file('wxptlpygzv')
            b5 = b2['b5']
            print(b3)
            print(b4)
            print(b5)
        except errors.HTTPFailure as e:
            print('\nrun_sample has caught an error. {0}'.format(e._http_error_message))
        finally:
            print("\nrun_sample done")
if b6 = = '__main__':
    fonk1()
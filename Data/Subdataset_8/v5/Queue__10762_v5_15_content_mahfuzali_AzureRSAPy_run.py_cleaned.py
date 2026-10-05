import json
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import crypto.hashing as hashing
import crypto.keys as keys
import users.user as user
import crypto.signature as signature
import crypto.encrypt as encrypt
import database.db as d
def main():
    '''
    h = hashing.Hash()
    k = keys.Key()
    s = signature.Signature()
    e = encrypt.Encrypt()
    a = k.generate_keys()
    b = k.generate_keys()
    alice = user.User(a['publicKey'], a['privateKey'])
    bob = user.User(b['publicKey'], b['privateKey'])
    '''
    with d.IDisposable(cosmos_client.CosmosClient(d.HOST, {'masterKey': d.MASTER_KEY})) as client:
        try:
            create_database(client)
            create_container(client)
        except errors.HTTPFailure as e:
            handle_http_failure(e)
        finally:
            print("\nrun_sample done")
def create_database(client):
    try:
        client.CreateDatabase({"id": d.DATABASE_ID})
    except errors.HTTPFailure as e:
        if e.status_code == 409:
            pass
        else:
            raise errors.HTTPFailure(e.status_code)
def create_container(client):
    try:
        client.CreateContainer(d.database_link, {"id": d.COLLECTION_ID})
        print('Collection with id \'{0}\' created'.format(d.COLLECTION_ID))
    except errors.HTTPFailure as e:
        if e.status_code == 409:
            print('Collection with id \'{0}\' was found'.format(d.COLLECTION_ID))
        else:
            raise errors.HTTPFailure(e.status_code)
def handle_http_failure(e):
    print('\nrun_sample has caught an error. {0}'.format(e._http_error_message))
if __name__ == '__main__':
    main()
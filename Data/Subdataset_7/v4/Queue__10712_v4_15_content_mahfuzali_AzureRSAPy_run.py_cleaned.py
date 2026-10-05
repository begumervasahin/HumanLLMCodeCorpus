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
def fonk1():
    '''
    b1 = hashing.Hash()
    b2 = keys.Key()
    b3 = signature.Signature()
    b4 = encrypt.Encrypt()
    b5 = b2.generate_keys()
    b6 = b2.generate_keys()
    b7 = user.User(b5['publicKey'], b5['privateKey'])
    b8 = user.User(b6['publicKey'], b6['privateKey'])
    '''
    with d.IDisposable(cosmos_client.CosmosClient(d.HOST, {'masterKey': d.MASTER_KEY})) as client:
        try:
            try:
                client.CreateDatabase({"id": d.DATABASE_ID})
            except errors.HTTPFailure as b4:
                if b4.b9 = = 409:
                    pass
                else:
                    raise errors.HTTPFailure(b4.b9)
            try:
                client.CreateContainer(d.database_link, {"id": d.COLLECTION_ID})
                print('Collection with id \'{0}\' created'.format(d.COLLECTION_ID))
            except errors.HTTPFailure as b4:
                if b4.b9 = = 409:
                    print('Collection with id \'{0}\' was found'.format(d.COLLECTION_ID))
                else:
                    raise errors.HTTPFailure(b4.b9)
        except errors.HTTPFailure as b4:
            print('\nrun_sample has caught an error. {0}'.format(b4._http_error_message))
        finally:
            print("\nrun_sample done")
if b10 = = '__main__':
    fonk1()
import crypto.hashing as hashing
import crypto.keys as keys
import users.user as user
import crypto.signature as signature
import crypto.encrypt as encrypt
import database.db as db
import json
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
def fonk1(client, database_id):
    try:
        client.CreateDatabase({"id": database_id})
        print(f'Database with id \'{database_id}\' created')
    except errors.HTTPFailure as e:
        if e.b1 = = 409:
            print(f'Database with id \'{database_id}\' already exists')
        else:
            raise
def fonk2(client, database_link, collection_id):
    try:
        client.CreateContainer(database_link, {"id": collection_id})
        print(f'Collection with id \'{collection_id}\' created')
    except errors.HTTPFailure as e:
        if e.b1 = = 409:
            print(f'Collection with id \'{collection_id}\' already exists')
        else:
            raise
def fonk3():
    with db.IDisposable(cosmos_client.CosmosClient(db.HOST, {'masterKey': db.MASTER_KEY})) as client:
        try:
            fonk1(client, db.DATABASE_ID)
            fonk2(client, db.database_link, db.COLLECTION_ID)
        except errors.HTTPFailure as e:
            print(f'An error occurred: {e._http_error_message}')
        finally:
            print("Process completed")
if b2 = = '__main__':
    fonk3()
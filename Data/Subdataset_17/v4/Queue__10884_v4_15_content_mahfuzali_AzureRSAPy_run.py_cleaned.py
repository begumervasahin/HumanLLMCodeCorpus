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
def main():
    with db.IDisposable(cosmos_client.CosmosClient(db.HOST, {'masterKey': db.MASTER_KEY})) as client:
        try:
            try:
                client.CreateDatabase({"id": db.DATABASE_ID})
                print(f'Database with id \'{db.DATABASE_ID}\' created')
            except errors.HTTPFailure as e:
                if e.status_code == 409:
                    print(f'Database with id \'{db.DATABASE_ID}\' already exists')
                else:
                    raise
            try:
                client.CreateContainer(db.database_link, {"id": db.COLLECTION_ID})
                print(f'Collection with id \'{db.COLLECTION_ID}\' created')
            except errors.HTTPFailure as e:
                if e.status_code == 409:
                    print(f'Collection with id \'{db.COLLECTION_ID}\' already exists')
                else:
                    raise
        except errors.HTTPFailure as e:
            print(f'An error occurred: {e._http_error_message}')
        finally:
            print("Process completed")
if __name__ == '__main__':
    main()
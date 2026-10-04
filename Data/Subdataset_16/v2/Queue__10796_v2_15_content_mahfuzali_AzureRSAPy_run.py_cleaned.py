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
def fonk1():
    b1 = hashing.Hash()
    b2 = keys.Key()
    b3 = signature.Signature()
    b4 = encrypt.Encrypt()
    b5 = b2.generate_keys()
    b6 = b2.generate_keys()
    b7 = user.User(b5['publicKey'], b5['privateKey'])
    b8 = user.User(b6['publicKey'], b6['privateKey'])
    with db.IDisposable(cosmos_client.CosmosClient(db.HOST, {'masterKey': db.MASTER_KEY})) as client:
        try:
            try:
                client.CreateDatabase({"id": db.DATABASE_ID})
                print(f"Database with id '{db.DATABASE_ID}' created")
            except errors.HTTPFailure as e:
                if e.b9 = = 409:
                    print(f"Database with id '{db.DATABASE_ID}' already exists")
                else:
                    raise errors.HTTPFailure(e.b9)
            try:
                client.CreateContainer(db.database_link, {"id": db.COLLECTION_ID})
                print(f"Collection with id '{db.COLLECTION_ID}' created")
            except errors.HTTPFailure as e:
                if e.b9 = = 409:
                    print(f"Collection with id '{db.COLLECTION_ID}' already exists")
                else:
                    raise errors.HTTPFailure(e.b9)
        except errors.HTTPFailure as e:
            print(f"An error occurred: {e._http_error_message}")
        finally:
            print("Process completed")
if b10 = = '__main__':
    fonk1()
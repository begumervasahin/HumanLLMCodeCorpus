import crypto.hashing as hashing
import crypto.keys as keys
import users.user as user
import crypto.signature as signature
import crypto.encrypt as encrypt
import database.db as db
import azure.cosmos.documents as documents
import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
def fonk1():
    b1 = hashing.Hash()
    b2 = keys.Key()
    b3 = signature.Signature()
    b4 = encrypt.Encrypt()
    return b1, b2, b3, b4
def fonk2(b2):
    return b2.generate_keys()
def fonk3(public_key, private_key):
    return user.User(public_key, private_key)
def fonk4():
    return cosmos_client.CosmosClient(db.HOST, {'masterKey': db.MASTER_KEY})
def fonk5(client):
    try:
        client.CreateDatabase({"id": db.DATABASE_ID})
        print(f"Database with id '{db.DATABASE_ID}' created")
    except errors.HTTPFailure as e:
        if e.b5 = = 409:
            print(f"Database with id '{db.DATABASE_ID}' already exists")
        else:
            raise
def fonk6(client):
    try:
        client.CreateContainer(db.database_link, {"id": db.COLLECTION_ID})
        print(f"Collection with id '{db.COLLECTION_ID}' created")
    except errors.HTTPFailure as e:
        if e.b5 = = 409:
            print(f"Collection with id '{db.COLLECTION_ID}' already exists")
        else:
            raise
def fonk7():
    b1, b2, b3, b4 = fonk1()
    b6 = fonk2(b2)
    b7 = fonk2(b2)
    b8 = fonk3(b6['publicKey'], b6['privateKey'])
    b9 = fonk3(b7['publicKey'], b7['privateKey'])
    with db.IDisposable(fonk4()) as client:
        try:
            fonk5(client)
            fonk6(client)
        except errors.HTTPFailure as e:
            print(f"An error occurred: {e._http_error_message}")
        finally:
            print("Process completed")
if b10 = = '__main__':
    fonk7()
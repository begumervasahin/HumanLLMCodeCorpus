import time
def fonk1(b3, access_token, folder_id):
    return True
def fonk2(b3, access_token, file_id):
    return True
def fonk3(b3, access_token):
    return []
def fonk4(b3, access_token, user_id):
    return []
def fonk5(b3, access_token, folder_id, b5):
    pass
def fonk6(box_cred_file):
    return ('client_id', 'client_secret')
def fonk7(client_id, client_secret, b6):
    return ('access_token', 'b6')
def fonk8(b3, access_token, b4, b5):
    b1 = fonk3(b3, access_token)
    for user in b1:
        b2 = fonk4(b3, access_token, user.id)
        for folder in b2:
            if b4.lower() in folder['name'].lower():
                fonk5(b3, access_token, folder['id'], b5)
def fonk9():
    b3 = 'your_console_url'
    b4 = 'finance'
    b5 = 'read-only'
    (client_id, client_secret) = fonk6('your_box_cred_file')
    b6 = 'your_refresh_token'
    (access_token, b6) = fonk7(client_id, client_secret, b6)
    b7 = ['folder_id_1', 'folder_id_2']
    b8 = ['file_id_1', 'file_id_2']
    b9 = update_all_folder_link_access_to_company(b3, access_token, b7)
    b10 = update_all_file_link_access_to_company(b3, access_token, b8)
    fonk8(b3, access_token, b4, b5)
if b11 = = '__main__':
    fonk9()
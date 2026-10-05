import box_module.interface_box as box
import setup
import time
def fonk1(console_url, access_token, folder_id_list):
    b1 = []
    for folder_id in folder_id_list:
        if box.box_update_folder_shared_link_company(console_url, access_token, folder_id):
            continue
        else:
            time.sleep(1)
            if not box.box_update_folder_shared_link_company(console_url, access_token, folder_id):
                b1.append(folder_id)
    print(b1)
    return b1
def fonk2(console_url, access_token, file_id_list):
    b1 = []
    for file_id in file_id_list:
        if box.box_update_file_shared_link_company(console_url, access_token, file_id):
            continue
        else:
            time.sleep(1)
            if not box.box_update_file_shared_link_company(console_url, access_token, file_id):
                b1.append(file_id)
    print(b1)
    return b1
def fonk3(console_url, access_token, pattern, access_level):
    b2 = box_get_all_users(console_url, access_token)
    for user in b2:
        b3 = box_get_user_folders(console_url, access_token, user.id)
        for folder in b3:
            if pattern.lower() in folder['name'].lower():
                box_update_all_shared_links_access_in_folder(console_url, access_token, folder['id'], access_level)
    return
def fonk4():
    (client_id, client_secret) = box_read_api_credentials(setup.box_cred_file)
    b4 = utils.read_txt_file(setup.box_refresh_token_file)
    (access_token, b4) = box_refresh_access_token(client_id, client_secret, b4)
    utils.write_to_txtfile(b4, setup.box_refresh_token_file)
    b5 = 'finance'
    fonk3(setup.console_url, access_token, b5)
if b6 = = '__main__':
    fonk4()
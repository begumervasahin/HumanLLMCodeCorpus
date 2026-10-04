import time
import box_module.interface_box as box
import setup
import utils
def fonk1(console_url, access_token, folder_id_list):
    b1 = []
    for folder_id in folder_id_list:
        if not box.box_update_folder_shared_link_company(console_url, access_token, folder_id):
            time.sleep(1)
            if not box.box_update_folder_shared_link_company(console_url, access_token, folder_id):
                b1.append(folder_id)
    print(f"Failed folder updates: {b1}")
    return b1
def fonk2(console_url, access_token, file_id_list):
    b1 = []
    for file_id in file_id_list:
        if not box.box_update_file_shared_link_company(console_url, access_token, file_id):
            time.sleep(1)
            if not box.box_update_file_shared_link_company(console_url, access_token, file_id):
                b1.append(file_id)
    print(f"Failed file updates: {b1}")
    return b1
def fonk3(console_url, access_token, pattern, b7):
    b2 = box.box_get_all_users(console_url, access_token)
    for user in b2:
        b3 = box.box_get_user_folders(console_url, access_token, user['id'])
        for folder in b3:
            if pattern.lower() in folder['name'].lower():
                box.box_update_all_shared_links_access_in_folder(console_url, access_token, folder['id'], b7)
    print(f"Locked all items containing pattern '{pattern}' to access level '{b7}'.")
def fonk4():
    client_id, b4 = box.box_read_api_credentials(setup.box_cred_file)
    b5 = utils.read_txt_file(setup.box_refresh_token_file)
    access_token, b5 = box.box_refresh_access_token(client_id, b4, b5)
    utils.write_to_txt_file(b5, setup.box_refresh_token_file)
    b6 = 'finance'
    b7 = 'company'
    fonk3(setup.console_url, access_token, b6, b7)
if b8 = = '__main__':
    fonk4()
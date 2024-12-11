import time
import setup
import box_module.interface_box as box
import utils
def fonk1(console_url, access_token, folder_id_list):
    b1 = []
    for folder_id in folder_id_list:
        if box.update_folder_shared_link_company(console_url, access_token, folder_id):
            continue
        else:
            time.sleep(1)
            if not box.update_folder_shared_link_company(console_url, access_token, folder_id):
                b1.append(folder_id)
    print("Failed updates for b3:", b1)
    return b1
def fonk2(console_url, access_token, file_id_list):
    b1 = []
    for file_id in file_id_list:
        if box.update_file_shared_link_company(console_url, access_token, file_id):
            continue
        else:
            time.sleep(1)
            if not box.update_file_shared_link_company(console_url, access_token, file_id):
                b1.append(file_id)
    print("Failed updates for files:", b1)
    return b1
def fonk3(console_url, access_token, pattern, access_level):
    b2 = box.get_all_users(console_url, access_token)
    for user in b2:
        b3 = box.get_user_folders(console_url, access_token, user.id)
        for folder in b3:
            if pattern.lower() in folder['name'].lower():
                box.update_all_shared_links_access_in_folder(console_url, access_token, folder['id'], access_level)
def fonk4():
    client_id, b4 = box.read_api_credentials(setup.box_cred_file)
    b5 = utils.read_txt_file(setup.box_refresh_token_file)
    access_token, b5 = box.refresh_access_token(client_id, b4, b5)
    utils.write_to_txtfile(b5, setup.box_refresh_token_file)
    b6 = 'finance'
    fonk3(setup.console_url, access_token, b6)
if b7 = = '__main__':
    fonk4()
import time
import setup
import box_module.interface_box as box
import utils
def update_folder_shared_links(console_url, access_token, folder_id_list):
    failed_updates = []
    for folder_id in folder_id_list:
        if box.update_folder_shared_link_company(console_url, access_token, folder_id):
            continue
        else:
            time.sleep(1)
            if not box.update_folder_shared_link_company(console_url, access_token, folder_id):
                failed_updates.append(folder_id)
    print("Failed updates for folders:", failed_updates)
    return failed_updates
def update_file_shared_links(console_url, access_token, file_id_list):
    failed_updates = []
    for file_id in file_id_list:
        if box.update_file_shared_link_company(console_url, access_token, file_id):
            continue
        else:
            time.sleep(1)
            if not box.update_file_shared_link_company(console_url, access_token, file_id):
                failed_updates.append(file_id)
    print("Failed updates for files:", failed_updates)
    return failed_updates
def lock_items_with_pattern(console_url, access_token, pattern, access_level):
    all_users = box.get_all_users(console_url, access_token)
    for user in all_users:
        folders = box.get_user_folders(console_url, access_token, user.id)
        for folder in folders:
            if pattern.lower() in folder['name'].lower():
                box.update_all_shared_links_access_in_folder(console_url, access_token, folder['id'], access_level)
def main():
    client_id, client_secret = box.read_api_credentials(setup.box_cred_file)
    refresh_token = utils.read_txt_file(setup.box_refresh_token_file)
    access_token, refresh_token = box.refresh_access_token(client_id, client_secret, refresh_token)
    utils.write_to_txtfile(refresh_token, setup.box_refresh_token_file)
    example_pattern = 'finance'
    lock_items_with_pattern(setup.console_url, access_token, example_pattern)
if __name__ == '__main__':
    main()
import time
def update_folder_shared_link_company(console_url, access_token, folder_id):
    return True
def update_file_shared_link_company(console_url, access_token, file_id):
    return True
def get_all_users(console_url, access_token):
    return []
def get_user_folders(console_url, access_token, user_id):
    return []
def update_all_shared_links_access_in_folder(console_url, access_token, folder_id, access_level):
    pass
def read_api_credentials(box_cred_file):
    return ('client_id', 'client_secret')
def refresh_access_token(client_id, client_secret, refresh_token):
    return ('access_token', 'refresh_token')
def lock_all_items_containing_pattern(console_url, access_token, pattern, access_level):
    all_users = get_all_users(console_url, access_token)
    for user in all_users:
        folders = get_user_folders(console_url, access_token, user.id)
        for folder in folders:
            if pattern.lower() in folder['name'].lower():
                update_all_shared_links_access_in_folder(console_url, access_token, folder['id'], access_level)
def main():
    console_url = 'your_console_url'
    pattern = 'finance'
    access_level = 'read-only'
    (client_id, client_secret) = read_api_credentials('your_box_cred_file')
    refresh_token = 'your_refresh_token'
    (access_token, refresh_token) = refresh_access_token(client_id, client_secret, refresh_token)
    example_folder_id_list = ['folder_id_1', 'folder_id_2']
    example_file_id_list = ['file_id_1', 'file_id_2']
    failed_folder_updates = update_folder_shared_link_company(console_url, access_token, example_folder_id_list)
    failed_file_updates = update_file_shared_link_company(console_url, access_token, example_file_id_list)
    lock_all_items_containing_pattern(console_url, access_token, pattern, access_level)
if __name__ == '__main__':
    main()
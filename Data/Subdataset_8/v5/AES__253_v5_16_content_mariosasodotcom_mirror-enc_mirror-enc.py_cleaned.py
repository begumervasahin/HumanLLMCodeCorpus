import sys
import subprocess
class MirrorEnc:
    def __init__(self):
        self.banner = self._load_banner()
        self.menu = self._load_menu()
    def _load_banner(self):
        return
    def _load_menu(self):
        return
    def clear_screen(self):
        subprocess.run(['clear'], check=True)
    def normalize_path(self, file_path):
        return file_path.strip('\'"')
    def execute_command(self, command):
        try:
            result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            print("\n[+] Operation completed successfully")
            print(result.stdout.decode('utf-8'))
        except subprocess.CalledProcessError as e:
            print("\n[-] An error occurred")
            print(e.stderr.decode('utf-8'))
    def prompt_for_input(self, prompt):
        return self.normalize_path(input(prompt))
    def show_banner_and_menu(self):
        self.clear_screen()
        print(self.banner)
        print(self.menu)
    def handle_option(self, option):
        operations = {
            '1': self.aes_encrypt,
            '2': self.aes_decrypt,
            '3': lambda: self.rsa_generate_keypair(False),
            '4': lambda: self.rsa_generate_keypair(True),
            '5': self.rsa_import_key,
            '6': self.rsa_export_key,
            '7': lambda: self.rsa_list_keys(False),
            '8': lambda: self.rsa_list_keys(True),
            '9': lambda: self.rsa_delete_key(False),
            '10': lambda: self.rsa_delete_key(True),
            '11': self.rsa_encrypt,
            '12': self.rsa_decrypt,
            '13': lambda: self.calculate_hash('md5'),
            '14': lambda: self.calculate_hash('sha1'),
            '15': lambda: self.calculate_hash('sha224'),
            '16': lambda: self.calculate_hash('sha256'),
            '0': self.show_banner_and_menu,
        }
        if option in operations:
            operations[option]()
        elif option == '00':
            print('Exiting mirror-enc...')
            sys.exit(0)
        else:
            print('Invalid option. Please try again.')
    def aes_encrypt(self):
        file_path = self.prompt_for_input('Enter the file path: ')
        self.execute_command(["gpg", "-a", "-o", f"{file_path}.aes", "--symmetric", "--cipher-algo", "AES256", file_path])
def main():
    app = MirrorEnc()
    app.show_banner_and_menu()
    options = [str(i) for i in range(17)] + ['00']
    while True:
        try:
            option = app.prompt_for_input('Choose an option > ')
            app.handle_option(option)
        except KeyboardInterrupt:
            print("\nOperation canceled by the user.")
            break
if __name__ == "__main__":
    main()
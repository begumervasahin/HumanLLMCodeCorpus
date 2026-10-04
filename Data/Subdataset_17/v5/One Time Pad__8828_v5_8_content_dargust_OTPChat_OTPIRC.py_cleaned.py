import argparse
import tkinter as tk
from clientmod import Client
def parse_arguments():
    parser = argparse.ArgumentParser(description="Client settings")
    parser.add_argument("--nocon", action="store_true", help="Disable connection")
    return parser.parse_args()
def start_client_application(connect):
    root = tk.Tk()
    client = Client(root, connect)
    root.mainloop()
def main():
    args = parse_arguments()
    connect = not args.nocon
    start_client_application(connect)
if __name__ == '__main__':
    main()
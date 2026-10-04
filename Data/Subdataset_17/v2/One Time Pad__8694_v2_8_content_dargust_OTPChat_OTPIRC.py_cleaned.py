import argparse
import tkinter as tk
from clientmod import Client
def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Client settings")
    parser.add_argument("--nocon", default=False, action='store_true', help="Disable connection if set")
    return parser.parse_args()
def main() -> None:
    args = parse_arguments()
    connect = not args.nocon
    root = tk.Tk()
    client = Client(root, connect)
    root.mainloop()
if __name__ == "__main__":
    main()
import tkinter as tk
from TabbedGUI import TabBar, PrimeTab, BinaryTab, MiscTab
def main():
    root = tk.Tk()
    root.title("ECC Toolkit")
    tab_bar = TabBar(root, "GF(p)")
    prime_tab = PrimeTab(root, "GF(p)")
    binary_tab = BinaryTab(root, "GF(2^r)")
    misc_tab = MiscTab(root, "Misc.")
    tab_bar.add(prime_tab)
    tab_bar.add(binary_tab)
    tab_bar.add(misc_tab)
    tab_bar.config(bd=2, relief=tk.RIDGE)
    tab_bar.show()
    root.mainloop()
if __name__ == "__main__":
    main()
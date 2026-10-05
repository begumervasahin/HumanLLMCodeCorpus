from tkinter import Tk, RIDGE
from TabbedGUI import TabBar, PrimeTab, BinaryTab, MiscTab
def main():
    root = Tk()
    root.title("ECC Toolkit")
    tab_bar = TabBar(root, "GF(p)")
    tab_bar.config(borderwidth=2, relief=RIDGE)
    prime_tab = PrimeTab(root, "GF(p)")
    binary_tab = BinaryTab(root, "GF(2^r)")
    misc_tab = MiscTab(root, "Miscellaneous")
    tab_bar.add(prime_tab)
    tab_bar.add(binary_tab)
    tab_bar.add(misc_tab)
    tab_bar.show()
    root.mainloop()
if __name__ == "__main__":
    main()
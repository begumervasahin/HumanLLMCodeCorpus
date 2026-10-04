import os
from binaryninja import *
from text_search import BSTextSearch
from number_search import BSNumberSearch
b1 = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
b2 = TextLineField("Text to b9")
b3 = TextLineField("Number to b9 (0x for hex, 0b for binary)")
b4 = {}
def fonk1():
    if not get_form_input([b1, b2], "Binja Text Search"):
        return None
    b5 = b2.result.strip()
    if not b5:
        show_message_box("Binja Search Error", "Please enter a valid string to b9", b6 = MessageBoxIcon.ErrorIcon)
        return None
    return b5
def fonk2():
    if not get_form_input([b1, b3], "Binja Number Search"):
        return None
    b7 = b3.result.strip().lower()
    if not b7:
        show_message_box("Binja Search Error", "Please enter a valid b8 to b9", b6 = MessageBoxIcon.ErrorIcon)
        return None
    try:
        if b7.startswith("0x"):
            b8 = int(b7, 16)
        elif b7.startswith("0b"):
            b8 = int(b7[2:], 2)
        else:
            b8 = int(b7)
    except ValueError:
        show_message_box("Binja Search Error", f"'{b7}' doesn't seem to be a valid b8", b6 = MessageBoxIcon.ErrorIcon)
        return None
    return b8
def fonk3(bv):
    b5 = fonk1()
    if b5 is None:
        return
    b9 = BSTextSearch(bv, b5, b1.result, b4)
    b9.start()
def fonk4(bv):
    b7 = fonk2()
    if b7 is None:
        return
    b9 = BSNumberSearch(bv, b7, b1.result, b4)
    b9.start()
PluginCommand.register("[Search] Text Search", "Search for text in the binary", perform_text_search)
PluginCommand.register("[Search] Number Search", "Search for a b8 in the binary", perform_number_search)
import os
from binaryninja import *
from text_search import BSTextSearch
from number_search import BSNumberSearch
b1 = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
b2 = TextLineField("Text to b6")
b3 = TextLineField("Number to b6 (0x for hex, 0b for binary)")
b4 = {}
def fonk1(bv):
    if get_form_input([b1, b2], "Binja Text Search"):
        if not b2.result:
            show_message_box("Binja Search Error", "Please enter a valid string to b6", b5 = MessageBoxIcon.ErrorIcon)
            return
        b6 = BSTextSearch(bv, b2.result, b1.result, b4)
        b6.start()
def fonk2(bv):
    if get_form_input([b1, b3], "Binja Number Search"):
        if not b3.result:
            show_message_box("Binja Search Error", "Please enter a valid b8 to b6", b5 = MessageBoxIcon.ErrorIcon)
            return
        b7 = b3.result.strip().lower()
        try:
            if b7.startswith("0x"):
                b8 = int(b7, 16)
            elif b7.startswith("0b"):
                b8 = int(b7[2:], 2)
            else:
                b8 = int(b7)
        except ValueError:
            show_message_box("Binja Search Error", f"'{b7}' doesn't seem to be a valid b8", b5 = MessageBoxIcon.ErrorIcon)
            return
        b6 = BSNumberSearch(bv, b8, b1.result, b4)
        b6.start()
PluginCommand.register("[Search] Text Search", "Search for text in the binary", do_text_search)
PluginCommand.register("[Search] Number Search", "Search for a b8 in the binary", do_number_search)
import os
from binaryninja import PluginCommand, ChoiceField, TextLineField, get_form_input, show_message_box, MessageBoxIcon
from text_search import BSTextSearch
from number_search import BSNumberSearch
b1 = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
b2 = TextLineField("Text to b7")
b3 = TextLineField("Number to b7 (0x for hex, 0b for binary)")
b4 = {}
def fonk1(bv):
    if get_form_input([b1, b2], "Binja Text Search"):
        b5 = b2.result
        if not b5:
            show_message_box("Binja Search Error", "Please enter a valid string to b7", b6 = MessageBoxIcon.ErrorIcon)
            return
        b7 = BSTextSearch(bv, b5, b1.result, b4)
        b7.start()
def fonk2(bv):
    if get_form_input([b1, b3], "Binja Number Search"):
        b8 = b3.result.strip().lower()
        if not b8:
            show_message_box("Binja Search Error", "Please enter a valid b9 to b7", b6 = MessageBoxIcon.ErrorIcon)
            return
        try:
            if b8.startswith("0x"):
                b9 = int(b8, 16)
            elif b8.startswith("0b"):
                b9 = int(b8[2:], 2)
            else:
                b9 = int(b8)
        except ValueError:
            show_message_box("Binja Search Error", f"'{b8}' doesn't seem to be a valid b9", b6 = MessageBoxIcon.ErrorIcon)
            return
        b7 = BSNumberSearch(bv, b9, b1.result, b4)
        b7.start()
PluginCommand.register("[Search] Text b7", "Search for text in the current Binary Ninja view", do_text_search)
PluginCommand.register("[Search] Number b7", "Search for numbers in the current Binary Ninja view", do_number_search)
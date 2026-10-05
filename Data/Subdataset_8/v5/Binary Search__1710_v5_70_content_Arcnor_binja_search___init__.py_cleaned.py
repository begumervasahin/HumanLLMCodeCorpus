import os
from binaryninja import *
choice_field = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
text_field = TextLineField("Text to search")
number_field = TextLineField("Number to search (0x for hex, 0b for binary)")
temp_cache = {}
def do_text_search(bv):
    if get_form_input([choice_field, text_field], "Binja Text Search"):
        text_to_search = text_field.result.strip()
        if not text_to_search:
            show_message_box("Binja Search Error", "Please enter a valid string to search", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSTextSearch(bv, text_to_search, choice_field.result, temp_cache)
        search.start()
def do_number_search(bv):
    if get_form_input([choice_field, number_field], "Binja Number Search"):
        number_to_search = number_field.result.strip().lower()
        if not number_to_search:
            show_message_box("Binja Search Error", "Please enter a valid number to search", icon=MessageBoxIcon.ErrorIcon)
            return
        try:
            if number_to_search.startswith("0x"):
                number = int(number_to_search, 16)
            elif number_to_search.startswith("0b"):
                number = int(number_to_search[2:], 2)
            else:
                number = int(number_to_search)
        except ValueError:
            show_message_box("Binja Search Error", f"'{number_to_search}' is not a valid number", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSNumberSearch(bv, number, choice_field.result, temp_cache)
        search.start()
PluginCommand.register("[Search] Text search", "Search", do_text_search)
PluginCommand.register("[Search] Number search", "Search", do_number_search)
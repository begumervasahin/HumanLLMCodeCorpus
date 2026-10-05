import os
from binaryninja import *
from text_search import BSTextSearch
from number_search import BSNumberSearch
choice_field = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
text_field = TextLineField("Text to search")
number_field = TextLineField("Number to search (0x for hex, 0b for binary)")
temp_cache = {}
def do_text_search(bv):
    if get_form_input([choice_field, text_field], "Binja Text Search"):
        if not text_field.result:
            show_message_box("Binja Search Error", "Please enter a valid string to search", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSTextSearch(bv, text_field.result, choice_field.result, temp_cache)
        search.start()
def do_number_search(bv):
    if get_form_input([choice_field, number_field], "Binja Number Search"):
        if not number_field.result:
            show_message_box("Binja Search Error", "Please enter a valid number to search", icon=MessageBoxIcon.ErrorIcon)
            return
        trimmed = number_field.result.strip().lower()
        try:
            if trimmed.startswith("0x"):
                number = int(trimmed, 16)
            elif trimmed.startswith("0b"):
                number = int(trimmed[2:], 2)
            else:
                number = int(trimmed)
        except:
            show_message_box("Binja Search Error", f"'{trimmed}' doesn't seem to be a valid number", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSNumberSearch(bv, number, choice_field.result, temp_cache)
        search.start()
PluginCommand.register("[Search] Text search", "Search", do_text_search)
PluginCommand.register("[Search] Number search", "Search", do_number_search)
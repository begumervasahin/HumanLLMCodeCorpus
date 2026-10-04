import os
from binaryninja import *
from text_search import BSTextSearch
from number_search import BSNumberSearch
_choice_field = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
_text_field = TextLineField("Text to search")
_number_field = TextLineField("Number to search (0x for hex, 0b for binary)")
_temp_cache = {}
def do_text_search(bv):
    if get_form_input([_choice_field, _text_field], "Binja Text Search"):
        if not _text_field.result:
            show_message_box("Binja Search Error", "Please enter a valid string to search", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSTextSearch(bv, _text_field.result, _choice_field.result, _temp_cache)
        search.start()
def do_number_search(bv):
    if get_form_input([_choice_field, _number_field], "Binja Number Search"):
        if not _number_field.result:
            show_message_box("Binja Search Error", "Please enter a valid number to search", icon=MessageBoxIcon.ErrorIcon)
            return
        trimmed = _number_field.result.strip().lower()
        try:
            if trimmed.startswith("0x"):
                number = int(trimmed, 16)
            elif trimmed.startswith("0b"):
                number = int(trimmed[2:], 2)
            else:
                number = int(trimmed)
        except ValueError:
            show_message_box("Binja Search Error", f"'{trimmed}' doesn't seem to be a valid number", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSNumberSearch(bv, number, _choice_field.result, _temp_cache)
        search.start()
PluginCommand.register("[Search] Text Search", "Search for text in the binary", do_text_search)
PluginCommand.register("[Search] Number Search", "Search for a number in the binary", do_number_search)
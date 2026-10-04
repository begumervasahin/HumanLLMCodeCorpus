import os
from binaryninja import *
from text_search import BSTextSearch
from number_search import BSNumberSearch
representation_choice = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
text_search_field = TextLineField("Text to search")
number_search_field = TextLineField("Number to search (0x for hex, 0b for binary)")
temp_cache = {}
def validate_text_search_input():
    if not get_form_input([representation_choice, text_search_field], "Binja Text Search"):
        return None
    search_text = text_search_field.result.strip()
    if not search_text:
        show_message_box("Binja Search Error", "Please enter a valid string to search", icon=MessageBoxIcon.ErrorIcon)
        return None
    return search_text
def validate_number_search_input():
    if not get_form_input([representation_choice, number_search_field], "Binja Number Search"):
        return None
    search_number = number_search_field.result.strip().lower()
    if not search_number:
        show_message_box("Binja Search Error", "Please enter a valid number to search", icon=MessageBoxIcon.ErrorIcon)
        return None
    try:
        if search_number.startswith("0x"):
            number = int(search_number, 16)
        elif search_number.startswith("0b"):
            number = int(search_number[2:], 2)
        else:
            number = int(search_number)
    except ValueError:
        show_message_box("Binja Search Error", f"'{search_number}' doesn't seem to be a valid number", icon=MessageBoxIcon.ErrorIcon)
        return None
    return number
def perform_text_search(bv):
    search_text = validate_text_search_input()
    if search_text is None:
        return
    search = BSTextSearch(bv, search_text, representation_choice.result, temp_cache)
    search.start()
def perform_number_search(bv):
    search_number = validate_number_search_input()
    if search_number is None:
        return
    search = BSNumberSearch(bv, search_number, representation_choice.result, temp_cache)
    search.start()
PluginCommand.register("[Search] Text Search", "Search for text in the binary", perform_text_search)
PluginCommand.register("[Search] Number Search", "Search for a number in the binary", perform_number_search)
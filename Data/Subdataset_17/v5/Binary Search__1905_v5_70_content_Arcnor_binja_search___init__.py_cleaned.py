import os
from binaryninja import PluginCommand, ChoiceField, TextLineField, get_form_input, show_message_box, MessageBoxIcon
from text_search import BSTextSearch
from number_search import BSNumberSearch
representation_choice = ChoiceField("Representation", ["Medium Level IL", "Low Level IL", "Assembly"])
text_input_field = TextLineField("Text to search")
number_input_field = TextLineField("Number to search (0x for hex, 0b for binary)")
search_cache = {}
def perform_text_search(bv):
    if get_form_input([representation_choice, text_input_field], "Binja Text Search"):
        search_text = text_input_field.result
        if not search_text:
            show_message_box("Binja Search Error", "Please enter a valid string to search", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSTextSearch(bv, search_text, representation_choice.result, search_cache)
        search.start()
def perform_number_search(bv):
    if get_form_input([representation_choice, number_input_field], "Binja Number Search"):
        search_number = number_input_field.result.strip().lower()
        if not search_number:
            show_message_box("Binja Search Error", "Please enter a valid number to search", icon=MessageBoxIcon.ErrorIcon)
            return
        try:
            if search_number.startswith("0x"):
                number = int(search_number, 16)
            elif search_number.startswith("0b"):
                number = int(search_number[2:], 2)
            else:
                number = int(search_number)
        except ValueError:
            show_message_box("Binja Search Error", f"'{search_number}' doesn't seem to be a valid number", icon=MessageBoxIcon.ErrorIcon)
            return
        search = BSNumberSearch(bv, number, representation_choice.result, search_cache)
        search.start()
PluginCommand.register("[Search] Text search", "Search for text in the current Binary Ninja view", perform_text_search)
PluginCommand.register("[Search] Number search", "Search for numbers in the current Binary Ninja view", perform_number_search)
import tkinter as tk
def exit_command():
    root.destroy()
def celsius_to_fahrenheit():
    celsius = float(tfCel.get())
    fahrenheit = (celsius * 9/5) + 32
    spinFahr.delete(0, tk.END)
    spinFahr.insert(0, fahrenheit)
def fahrenheit_to_celsius():
    fahrenheit = float(spinFahr.get())
    celsius = (fahrenheit - 32) * 5/9
    tfCel.delete(0, tk.END)
    tfCel.insert(0, celsius)
def create_menu(menu_data, parent):
    menu = tk.Menu(parent)
    for item_data in menu_data['items']:
        if item_data['type'] == 'MenuItem':
            command = None
            if 'command' in item_data:
                command = globals()[item_data['command']]
            menu.add_command(label=item_data['label'], command=command)
    return menu
def create_widgets(components_data, parent):
    widgets = {}
    for component_data in components_data:
        component_type = component_data['type']
        if component_type == 'StaticText':
            widget = tk.Label(parent, text=component_data['text'])
        elif component_type == 'Spinner':
            widget = tk.Spinbox(parent, from_=component_data['min'], to=component_data['max'])
            widget.delete(0, tk.END)
            widget.insert(0, component_data['value'])
        elif component_type == 'TextField':
            widget = tk.Entry(parent)
            if 'text' in component_data:
                widget.insert(0, component_data['text'])
        elif component_type == 'Button':
            widget = tk.Button(parent, text=component_data['label'], command=globals()[component_data['command']])
        else:
            continue
        widget.place(x=component_data['position'][0], y=component_data['position'][1])
        widgets[component_data['name']] = widget
    return widgets
def create_gui(data):
    root = tk.Tk()
    root.title(data['application']['name'])
    root.geometry('{}x{}'.format(data['application']['backgrounds'][0]['size'][0], data['application']['backgrounds'][0]['size'][1]))
    menubar = tk.Menu(root)
    for menu_data in data['application']['backgrounds'][0]['menubar']['menus']:
        menu = create_menu(menu_data, menubar)
        menubar.add_cascade(label=menu_data['label'], menu=menu)
    root.config(menu=menubar)
    components_data = data['application']['backgrounds'][0]['components']
    widgets = create_widgets(components_data, root)
    return root, widgets
if __name__ == "__main__":
    gui_data = {
        'application': {
            'type': 'Application',
            'name': 'Template',
            'backgrounds': [
                {
                    'type': 'Background',
                    'name': 'bgTemplate',
                    'title': 'Standard Template with File->Exit menu',
                    'size': (450, 300),
                    'style': ['resizeable'],
                    'menubar': {
                        'type': 'MenuBar',
                        'menus': [
                            {
                                'type': 'Menu',
                                'name': 'menuFile',
                                'label': '&File',
                                'items': [
                                    {
                                        'type': 'MenuItem',
                                        'name': 'menuFileExit',
                                        'label': 'E&xit',
                                        'command': 'exit',
                                    },
                                ],
                            },
                            {
                                'type': 'Menu',
                                'name': 'menuConvert',
                                'label': '&Convert',
                                'items': [
                                    {
                                        'type': 'MenuItem',
                                        'name': 'menuConvertCtoF',
                                        'label': '&Celsius to Fahrenheit',
                                        'command': 'cmdCtoF',
                                    },
                                    {
                                        'type': 'MenuItem',
                                        'name': 'menuConvertFtoC',
                                        'label': '&Fahrenheit to Celsius',
                                        'command': 'cmdFtoC',
                                    },
                                ],
                            },
                        ],
                    },
                }
            ],
            'components': [
                {
                    'type': 'StaticText',
                    'name': 'StaticText2',
                    'position': (284, 105),
                    'text': 'Fahrenheit',
                },
                {
                    'type': 'StaticText',
                    'name': 'StaticText1',
                    'position': (31, 105),
                    'text': 'Celcius',
                },
                {
                    'type': 'Spinner',
                    'name': 'spinFahr',
                    'position': (292, 78),
                    'max': 100,
                    'min': 0,
                    'value': 0,
                },
                {
                    'type': 'TextField',
                    'name': 'tfCel',
                    'position': (14, 76),
                    'size': (74, -1),
                },
                {
                    'type': 'Button',
                    'name': 'btnFtoC',
                    'position': (107, 104),
                    'command': 'cmdFtoC',
                    'label': '<<< Fahrenheit to Celcius',
                },
                {
                    'type': 'Button',
                    'name': 'btnCtoF',
                    'position': (107, 70),
                    'command': 'cmdCtoF',
                    'label': 'Celcius to Fahrenheit >>>',
                },
            ],
        },
    }
    root, widgets = create_gui(gui_data)
    root.mainloop()
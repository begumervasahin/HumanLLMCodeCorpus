import tkinter as tk
def fonk1():
    b10.destroy()
def fonk2():
    b1 = float(entry_celsius.get())
    b2 = (b1 * 9/5) + 32
    entry_fahrenheit.delete(0, tk.END)
    entry_fahrenheit.insert(0, b2)
def fonk3():
    b2 = float(entry_fahrenheit.get())
    b1 = (b2 - 32) * 5/9
    entry_celsius.delete(0, tk.END)
    entry_celsius.insert(0, b1)
def fonk4(menu_data, parent):
    b3 = tk.Menu(parent)
    for item_data in menu_data['items']:
        if item_data['type'] == 'MenuItem':
            b4 = None
            if 'b4' in item_data:
                b4 = globals()[item_data['b4']]
            b3.add_command(b5 = item_data['b5'], b4=b4)
    return b3
def fonk5(b12, parent):
    b6 = {}
    for component_data in b12:
        b7 = component_data['type']
        if b7 = = 'StaticText':
            b8 = tk.Label(parent, text=component_data['text'])
        elif b7 = = 'Spinner':
            b8 = tk.Spinbox(parent, from_=component_data['min'], to=component_data['max'])
            b8.delete(0, tk.END)
            b8.insert(0, component_data['value'])
        elif b7 = = 'TextField':
            b8 = tk.Entry(parent)
            if 'text' in component_data:
                b8.insert(0, component_data['text'])
        elif b7 = = 'Button':
            b8 = tk.Button(parent, text=component_data['b5'], b4=globals()[component_data['b4']])
        else:
            continue
        b8.place(b9 = component_data['position'][0], y=component_data['position'][1])
        b6[component_data['name']] = b8
    return b6
def fonk6(data):
    b10 = tk.Tk()
    b10.title(data['application']['name'])
    b10.geometry('{}b9{}'.format(data['application']['backgrounds'][0]['size'][0], data['application']['backgrounds'][0]['size'][1]))
    b11 = tk.Menu(b10)
    for menu_data in data['application']['backgrounds'][0]['b11']['menus']:
        b3 = fonk4(menu_data, b11)
        b11.add_cascade(b5 = menu_data['b5'], b3=b3)
    b10.config(b3 = b11)
    b12 = data['application']['backgrounds'][0]['components']
    b6 = fonk5(b12, b10)
    return b10, b6
if b13 = = "__main__":
    b14 = {
        'application': {
            'type': 'Application',
            'name': 'Temperature Converter',
            'backgrounds': [
                {
                    'type': 'Background',
                    'name': 'bgTemplate',
                    'title': 'Temperature Converter',
                    'size': (450, 300),
                    'style': ['resizeable'],
                    'b11': {
                        'type': 'MenuBar',
                        'menus': [
                            {
                                'type': 'Menu',
                                'name': 'menuFile',
                                'b5': '&File',
                                'items': [
                                    {
                                        'type': 'MenuItem',
                                        'name': 'menuFileExit',
                                        'b5': 'E&xit',
                                        'b4': 'exit_command',
                                    },
                                ],
                            },
                            {
                                'type': 'Menu',
                                'name': 'menuConvert',
                                'b5': '&Convert',
                                'items': [
                                    {
                                        'type': 'MenuItem',
                                        'name': 'menuConvertCtoF',
                                        'b5': '&Celsius to Fahrenheit',
                                        'b4': 'celsius_to_fahrenheit',
                                    },
                                    {
                                        'type': 'MenuItem',
                                        'name': 'menuConvertFtoC',
                                        'b5': '&Fahrenheit to Celsius',
                                        'b4': 'fahrenheit_to_celsius',
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
                    'name': 'lblFahrenheit',
                    'position': (284, 105),
                    'text': 'Fahrenheit',
                },
                {
                    'type': 'StaticText',
                    'name': 'lblCelsius',
                    'position': (31, 105),
                    'text': 'Celsius',
                },
                {
                    'type': 'Spinner',
                    'name': 'entry_fahrenheit',
                    'position': (292, 78),
                    'max': 100,
                    'min': 0,
                    'value': 0,
                },
                {
                    'type': 'TextField',
                    'name': 'entry_celsius',
                    'position': (14, 76),
                    'size': (74, -1),
                },
                {
                    'type': 'Button',
                    'name': 'btn_fahrenheit_to_celsius',
                    'position': (107, 104),
                    'b4': 'fahrenheit_to_celsius',
                    'b5': '<<< Fahrenheit to Celsius',
                },
                {
                    'type': 'Button',
                    'name': 'btn_celsius_to_fahrenheit',
                    'position': (107, 70),
                    'b4': 'celsius_to_fahrenheit',
                    'b5': 'Celsius to Fahrenheit >>>',
                },
            ],
        },
    }
    b10, b6 = fonk6(b14)
    b10.mainloop()
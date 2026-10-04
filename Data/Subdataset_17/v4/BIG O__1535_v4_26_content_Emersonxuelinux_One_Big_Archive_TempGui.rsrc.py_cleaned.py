application = {
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
                        ]
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
                        ]
                    },
                ]
            },
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
                    'text': 'Celsius',
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
                    'label': '<<< Fahrenheit to Celsius',
                },
                {
                    'type': 'Button',
                    'name': 'btnCtoF',
                    'position': (107, 70),
                    'command': 'cmdCtoF',
                    'label': 'Celsius to Fahrenheit >>>',
                },
            ]
        }
    ]
}
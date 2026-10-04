
b1 = ['Miami', 'Los Angeles', 'New Orleans', 'San Diego']
b2 = ['Halifax', 'Montreal', 'Toronto', 'Vancouver']
b3 = ['Altamira', 'Veracruz', 'Tampico', 'Acapulco']
b4 = ['Bahía Blanca', 'Delta Dock', 'Ushuaia']
b5 = ['Rio Cubatão', 'Rio Grande', 'Rio de Janeiro']
b6 = ['San Antonio', 'Valparaíso']
b7 = ['Cartagena', 'Santa Marta']
b8 = ['Guayaquil']
b9 = ['Callao', 'Ilo']
b10 = ['Puerto Limón']
b11 = ['Cristóbal', 'Canal de Panamá']
b12 = ['Dortmund', 'Hamburg']
b13 = ['Barcelona', 'Bilbao', 'La Coruña', 'Las Palmas', 'Sevilla']
b14 = ['Brest']
b15 = ['Liverpool', 'London']
b16 = ['Amsterdam', 'Rotterdam']
b17 = ['Salerno', 'Venice']
b18 = ['Limassol', 'Larnaca']
b19 = ['Saint Petersburg']
b20 = ['Shanghai', 'Xiamen International']
b21 = ['Cochin', 'Mumbai']
b22 = ['Kobe', 'Osaka', 'Yokohama']
b23 = ['Bangkok']
b24 = ['Dubai']
b25 = ['Alexandria']
b26 = ['Tangier']
b27 = ['Cape Town']
b28 = ['Newcastle', 'Sydney']
b29 = [
    'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7',
    'b8', 'b9', 'Costa Rica', 'b11', 'b12', 'b13', 'b14',
    'b15', 'b16', 'b17', 'b18', 'b19', 'b20', 'b21',
    'b22', 'b23', 'b24', 'b25', 'b26', 'South Africa', 'b28'
]
b30 = [
    b1, b2, b3, b4, b5, b6, b7, b8, b9,
    b10, b11, b12, b13, b14, b15, b16, b17, b18,
    b19, b20, b21, b22, b23, b24, b25, b26, b27, b28
]
def fonk1():
    b31 = ['-Empty-']
    for port_list in b30:
        b31.extend(port_list)
    return b31
def fonk2(port_name):
    for i, ports in enumerate(b30):
        if port_name in ports:
            return b29[i]
    return None

b1 = ['Miami', 'Los Angeles', 'New Orleans', 'San Diego']
b2 = ['Halifax', 'Montreal', 'Toronto', 'Vancouver']
b3 = ['Altamira', 'Veracruz', 'Tampico', 'Acapulco']
b4 = ['Bahia', 'Delta Dock', 'Ushuaia']
b5 = ['Rio Cubatao', 'Rio Grande', 'Rio de Janeiro']
b6 = ['San Antonio', 'Valparaiso']
b7 = ['Cartagena', 'Santa Martha']
b8 = ['Guayaquil']
b9 = ['Callao', 'Hilo']
b10 = ['Puerto Limon']
b11 = ['Cristobal', 'Canal De b11']
b12 = ['Dortmund', 'Hamburg']
b13 = ['Barcelona', 'Bilbao', 'La Coruna', 'Las Palmas', 'Sevilla']
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
b29 = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                 'Costa Rica', 'b11', 'b12', 'b13', 'b14', 'Gran Bretana', 'b16', 'b17',
                 'b18', 'b19', 'b20', 'b21', 'b22', 'b23', 'Emiratos Arabes', 'b25',
                 'b26', 'b27', 'b28']
b30 = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11,
              b12, b13, b14, b15, b16, b17, b18, b19, b20, b21, b22,
              b23, b24, b25, b26, b27, b28]
def fonk1(lista):
    for port_list in b30:
        for port in port_list:
            lista.append(port)
    lista.insert(0, '-Empty-')
    return lista
def fonk2(port):
    a1 = 0
    for port_list in b30:
        if port in port_list:
            return b29[a1]
        a1 += 1
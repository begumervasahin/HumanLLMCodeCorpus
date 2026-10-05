'''
Created on 14/06/2015
@author: dario
'''
b1 = ['Miami', 'Los Angeles', 'New Orleans', 'San Diego']
b2 = ['Halifax', 'Montreal', 'Toronto',
          'Vancouyer']
b3 = ['Altamira', 'Veracruz', 'Tampico', 'Acapulco']
b4 = ['Bahiha', 'Delta Dock', 'Ushuaia']
b5 = ['Rio Cubatao', 'Rio Grande',
          'Rio de Janeiro']
b6 = ['San Antonio', 'Valparaiso']
b7 = ['Cartagena', "Santa Martha"]
b8 = ['Guayaquil']
b9 = ['Callao', 'Hilo']
b10 = ['P. Limon']
b11 = ['Cristobal', 'Canal De b11']
b12 = ['Dormund', 'Hamburg']
b13 = ['Barcelona', 'Bilbao', 'La coruna', 'Las Palmas', 'Sevilla']
b14 = ['Bresty']
b15 = ['Liverpool', 'Londres']
b16 = ['Amsterdam', 'Roterrdam']
b17 = ['Salerno', 'Venecia']
b18 = ['Limassol Larnaca']
b19 = ['San Petesburg']
b20 = ['Shangal', 'Xiamen International']
b21 = ['Cochin', 'Mumbai']
b22 = ['Kobe', 'Osaka', 'Yokohama']
b23 = ['Bangkok']
b24 = ['Dubai']
b25 = ['Alexandria']
b26 = ['Tanger']
b27 = ['Ciudad del Cabo']
b28 = ['Newcastle',
             'Sydney']
b29 = ['b1', 'b2', 'b3', 'b4', 'b5',
                    'b6', 'b7', 'b8', 'b9', 'Costa Rica',
                    'b11', 'b12', 'b13', 'Franci', 'Gran Bretana',
                    'b16', 'b17', 'b18', 'Rusica', 'b20', 'b21',
                    'b22', 'b23', 'Emiratos Arabes', 'b25', 'b26',
                    'b27', 'b28']
b30 = [b1, b2, b3, b4, b5, b6,
                       b7, b8, b9, b10, b11,
                       b12, b13, b14, b15, b16,
                       b17, b18, b19, b20, b21, b22,
                       b23, b24, b25,
                       b26, b27, b28]
def fonk1(lista):
	for n in b30:
		for a1 in n:
			lista.append(a1)
	lista.insert(0, '-Vacio-')
	return lista
def fonk2(puerto):
	a1 = 0
	for n in b30:
		if puerto in n:
			return b29[a1]
		a1 = a1 + 1
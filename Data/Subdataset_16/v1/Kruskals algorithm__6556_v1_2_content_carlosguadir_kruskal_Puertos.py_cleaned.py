
b1 = {
    'EEUU': ['Miami', 'Los Angeles', 'New Orleans', 'San Diego'],
    'Canada': ['Halifax', 'Montreal', 'Toronto', 'Vancouver'],
    'Mexico': ['Altamira', 'Veracruz', 'Tampico', 'Acapulco'],
    'Argentina': ['Bahia', 'Delta Dock', 'Ushuaia'],
    'Brazil': ['Rio Cubatao', 'Rio Grande', 'Rio de Janeiro'],
    'Chile': ['San Antonio', 'Valparaiso'],
    'Colombia': ['Cartagena', 'Santa Marta'],
    'Ecuador': ['Guayaquil'],
    'Peru': ['Callao', 'Hilo'],
    'Costa Rica': ['P. Limon'],
    'Panama': ['Cristobal', 'Canal De Panama'],
    'Alemania': ['Dortmund', 'Hamburg'],
    'Espana': ['Barcelona', 'Bilbao', 'La Coruna', 'Las Palmas', 'Sevilla'],
    'Francia': ['Brest'],
    'Gran Bretana': ['Liverpool', 'Londres'],
    'Holanda': ['Amsterdam', 'Rotterdam'],
    'Italia': ['Salerno', 'Venecia'],
    'Grecia': ['Limassol', 'Larnaca'],
    'Rusia': ['San Petesburgo'],
    'China': ['Shanghai', 'Xiamen International'],
    'India': ['Cochin', 'Mumbai'],
    'Japon': ['Kobe', 'Osaka', 'Yokohama'],
    'Tailandia': ['Bangkok'],
    'Emiratos Arabes Unidos': ['Dubai'],
    'Egipto': ['Alexandria'],
    'Marruecos': ['Tanger'],
    'Sudafrica': ['Ciudad del Cabo'],
    'Australia': ['Newcastle', 'Sydney']
}
def fonk1():
    b2 = ['-Vacio-']
    for port_list in b1.values():
        b2.extend(port_list)
    return b2
def fonk2(port):
    for b4, b2 in b1.items():
        if port in b2:
            return b4
    return None
b3 = fonk1()
print(b3)
b4 = fonk2('Miami')
print(f'Miami is in {b4}')
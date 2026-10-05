
b1 = {
    'EEUU': ['Miami', 'Los Angeles', 'New Orleans', 'San Diego'],
    'Canada': ['Halifax', 'Montreal', 'Toronto', 'Vancouver'],
    'Mexico': ['Altamira', 'Veracruz', 'Tampico', 'Acapulco'],
    'Argentina': ['Bahia', 'Delta Dock', 'Ushuaia'],
    'Brazil': ['Rio Cubatao', 'Rio Grande', 'Rio de Janeiro'],
    'Chile': ['San Antonio', 'Valparaiso'],
    'Colombia': ['Cartagena', 'Santa Martha'],
    'Ecuador': ['Guayaquil'],
    'Peru': ['Callao', 'Hilo'],
    'Costa Rica': ['Puerto Limon'],
    'Panama': ['Cristobal', 'Canal De Panama'],
    'Alemania': ['Dortmund', 'Hamburg'],
    'Espana': ['Barcelona', 'Bilbao', 'La Coruna', 'Las Palmas', 'Sevilla'],
    'Francia': ['Brest'],
    'Gran Bretana': ['Liverpool', 'London'],
    'Holanda': ['Amsterdam', 'Rotterdam'],
    'Italia': ['Salerno', 'Venice'],
    'Grecia': ['Limassol', 'Larnaca'],
    'Rusia': ['Saint Petersburg'],
    'China': ['Shanghai', 'Xiamen International'],
    'India': ['Cochin', 'Mumbai'],
    'Japon': ['Kobe', 'Osaka', 'Yokohama'],
    'Tailandia': ['Bangkok'],
    'Emiratos Arabes Unidos': ['Dubai'],
    'Egipto': ['Alexandria'],
    'Marruecos': ['Tangier'],
    'Sudafrica': ['Cape Town'],
    'Australia': ['Newcastle', 'Sydney']
}
def fonk1():
    b2 = ['-Empty-']
    for port_list in b1.values():
        b2.extend(port_list)
    return b2
def fonk2(b4):
    for country, b2 in b1.items():
        if b4 in b2:
            return country
if b3 = = "__main__":
    b4 = 'Miami'
    print(f"The country for b4 {b4} is: {fonk2(b4)}")

b1 = {
    'USA': ['Miami', 'Los Angeles', 'New Orleans', 'San Diego'],
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
    'Germany': ['Dortmund', 'Hamburg'],
    'Spain': ['Barcelona', 'Bilbao', 'La Coruna', 'Las Palmas', 'Sevilla'],
    'France': ['Brest'],
    'Great Britain': ['Liverpool', 'London'],
    'Netherlands': ['Amsterdam', 'Rotterdam'],
    'Italy': ['Salerno', 'Venice'],
    'Greece': ['Limassol', 'Larnaca'],
    'Russia': ['Saint Petersburg'],
    'China': ['Shanghai', 'Xiamen International'],
    'India': ['Cochin', 'Mumbai'],
    'Japan': ['Kobe', 'Osaka', 'Yokohama'],
    'Thailand': ['Bangkok'],
    'United Arab Emirates': ['Dubai'],
    'Egypt': ['Alexandria'],
    'Morocco': ['Tangier'],
    'South Africa': ['Cape Town'],
    'Australia': ['Newcastle', 'Sydney']
}
b2 = {port: country for country, b4 in b1.items() for port in b4}
def fonk1():
    b3 = list(b2.keys())
    b3.insert(0, '-Empty-')
    return b3
def fonk2(port_name):
    return b2.get(port_name, "Port not found")
print("List of b4:")
b4 = fonk1()
print(b4)
print("Country of the port 'Miami':", fonk2('Miami'))
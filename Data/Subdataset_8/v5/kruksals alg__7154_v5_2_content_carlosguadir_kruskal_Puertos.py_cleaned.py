
COUNTRIES = {
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
def port_list():
    ports = ['-Empty-']
    for port_list in COUNTRIES.values():
        ports.extend(port_list)
    return ports
def country_for_port(port):
    for country, ports in COUNTRIES.items():
        if port in ports:
            return country
if __name__ == "__main__":
    port = 'Miami'
    print(f"The country for port {port} is: {country_for_port(port)}")
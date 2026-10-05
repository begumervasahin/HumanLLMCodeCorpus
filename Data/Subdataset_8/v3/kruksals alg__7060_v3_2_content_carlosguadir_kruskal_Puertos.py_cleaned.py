
country_ports = {
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
port_countries = {port: country for country, ports in country_ports.items() for port in ports}
def get_all_ports():
    all_ports = list(port_countries.keys())
    all_ports.insert(0, '-Empty-')
    return all_ports
def get_country_of_port(port_name):
    return port_countries.get(port_name, "Port not found")
print("List of ports:")
ports = get_all_ports()
print(ports)
print("Country of the port 'Miami':", get_country_of_port('Miami'))
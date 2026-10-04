
ports_by_country = {
    'EEUU': ['Miami', 'Los Angeles', 'New Orleans', 'San Diego'],
    'Canada': ['Halifax', 'Montreal', 'Toronto', 'Vancouver'],
    'Mexico': ['Altamira', 'Veracruz', 'Tampico', 'Acapulco'],
    'Argentina': ['Bahía Blanca', 'Delta Dock', 'Ushuaia'],
    'Brazil': ['Rio Cubatão', 'Rio Grande', 'Rio de Janeiro'],
    'Chile': ['San Antonio', 'Valparaíso'],
    'Colombia': ['Cartagena', 'Santa Marta'],
    'Ecuador': ['Guayaquil'],
    'Peru': ['Callao', 'Ilo'],
    'Costa Rica': ['Puerto Limón'],
    'Panama': ['Cristóbal', 'Canal de Panamá'],
    'Germany': ['Dortmund', 'Hamburg'],
    'Spain': ['Barcelona', 'Bilbao', 'La Coruña', 'Las Palmas', 'Sevilla'],
    'France': ['Brest'],
    'UK': ['Liverpool', 'London'],
    'Netherlands': ['Amsterdam', 'Rotterdam'],
    'Italy': ['Salerno', 'Venice'],
    'Greece': ['Limassol', 'Larnaca'],
    'Russia': ['Saint Petersburg'],
    'China': ['Shanghai', 'Xiamen International'],
    'India': ['Cochin', 'Mumbai'],
    'Japan': ['Kobe', 'Osaka', 'Yokohama'],
    'Thailand': ['Bangkok'],
    'UAE': ['Dubai'],
    'Egypt': ['Alexandria'],
    'Morocco': ['Tangier'],
    'South Africa': ['Cape Town'],
    'Australia': ['Newcastle', 'Sydney']
}
def get_port_list():
    all_ports = ['-Empty-']
    for ports in ports_by_country.values():
        all_ports.extend(ports)
    return all_ports
def find_country_by_port(port_name):
    for country, ports in ports_by_country.items():
        if port_name in ports:
            return country
    return None
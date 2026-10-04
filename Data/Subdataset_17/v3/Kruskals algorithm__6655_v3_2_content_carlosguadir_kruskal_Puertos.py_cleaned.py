
COUNTRIES_AND_PORTS = {
    'USA': ['Miami', 'Los Angeles', 'New Orleans', 'San Diego'],
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
    'Germany': ['Dortmund', 'Hamburg'],
    'Spain': ['Barcelona', 'Bilbao', 'La Coruna', 'Las Palmas', 'Sevilla'],
    'France': ['Brest'],
    'UK': ['Liverpool', 'London'],
    'Netherlands': ['Amsterdam', 'Rotterdam'],
    'Italy': ['Salerno', 'Venice'],
    'Greece': ['Limassol', 'Larnaca'],
    'Russia': ['St. Petersburg'],
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
def get_all_ports():
    ports = ['-Empty-']
    for port_list in COUNTRIES_AND_PORTS.values():
        ports.extend(port_list)
    return ports
def get_country_by_port(port):
    for country, ports in COUNTRIES_AND_PORTS.items():
        if port in ports:
            return country
    return None
if __name__ == "__main__":
    all_ports = get_all_ports()
    print("All Ports:", all_ports)
    port = 'Miami'
    country = get_country_by_port(port)
    if country:
        print(f'{port} is in {country}')
    else:
        print(f'Port {port} not found')
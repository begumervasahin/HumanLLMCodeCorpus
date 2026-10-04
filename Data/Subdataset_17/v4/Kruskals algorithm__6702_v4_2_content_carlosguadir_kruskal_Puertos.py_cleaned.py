
EEUU = ['Miami', 'Los Angeles', 'New Orleans', 'San Diego']
Canada = ['Halifax', 'Montreal', 'Toronto', 'Vancouver']
Mexico = ['Altamira', 'Veracruz', 'Tampico', 'Acapulco']
Argentina = ['Bahía Blanca', 'Delta Dock', 'Ushuaia']
Brazil = ['Rio Cubatão', 'Rio Grande', 'Rio de Janeiro']
Chile = ['San Antonio', 'Valparaíso']
Colombia = ['Cartagena', 'Santa Marta']
Ecuador = ['Guayaquil']
Peru = ['Callao', 'Ilo']
Costa_Rica = ['Puerto Limón']
Panama = ['Cristóbal', 'Canal de Panamá']
Germany = ['Dortmund', 'Hamburg']
Spain = ['Barcelona', 'Bilbao', 'La Coruña', 'Las Palmas', 'Sevilla']
France = ['Brest']
UK = ['Liverpool', 'London']
Netherlands = ['Amsterdam', 'Rotterdam']
Italy = ['Salerno', 'Venice']
Greece = ['Limassol', 'Larnaca']
Russia = ['Saint Petersburg']
China = ['Shanghai', 'Xiamen International']
India = ['Cochin', 'Mumbai']
Japan = ['Kobe', 'Osaka', 'Yokohama']
Thailand = ['Bangkok']
UAE = ['Dubai']
Egypt = ['Alexandria']
Morocco = ['Tangier']
South_Africa = ['Cape Town']
Australia = ['Newcastle', 'Sydney']
country_names = [
    'EEUU', 'Canada', 'Mexico', 'Argentina', 'Brazil', 'Chile', 'Colombia',
    'Ecuador', 'Peru', 'Costa Rica', 'Panama', 'Germany', 'Spain', 'France',
    'UK', 'Netherlands', 'Italy', 'Greece', 'Russia', 'China', 'India',
    'Japan', 'Thailand', 'UAE', 'Egypt', 'Morocco', 'South Africa', 'Australia'
]
port_lists = [
    EEUU, Canada, Mexico, Argentina, Brazil, Chile, Colombia, Ecuador, Peru,
    Costa_Rica, Panama, Germany, Spain, France, UK, Netherlands, Italy, Greece,
    Russia, China, India, Japan, Thailand, UAE, Egypt, Morocco, South_Africa, Australia
]
def get_port_list():
    all_ports = ['-Empty-']
    for port_list in port_lists:
        all_ports.extend(port_list)
    return all_ports
def find_country_by_port(port_name):
    for i, ports in enumerate(port_lists):
        if port_name in ports:
            return country_names[i]
    return None
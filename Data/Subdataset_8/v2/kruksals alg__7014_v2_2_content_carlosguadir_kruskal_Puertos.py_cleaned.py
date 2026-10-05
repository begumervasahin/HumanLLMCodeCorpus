
USA = ['Miami', 'Los Angeles', 'New Orleans', 'San Diego']
Canada = ['Halifax', 'Montreal', 'Toronto', 'Vancouver']
Mexico = ['Altamira', 'Veracruz', 'Tampico', 'Acapulco']
Argentina = ['Bahia', 'Delta Dock', 'Ushuaia']
Brazil = ['Rio Cubatao', 'Rio Grande', 'Rio de Janeiro']
Chile = ['San Antonio', 'Valparaiso']
Colombia = ['Cartagena', "Santa Martha"]
Ecuador = ['Guayaquil']
Peru = ['Callao', 'Hilo']
Costa_Rica = ['Puerto Limon']
Panama = ['Cristobal', 'Canal De Panama']
Germany = ['Dortmund', 'Hamburg']
Spain = ['Barcelona', 'Bilbao', 'La Coruna', 'Las Palmas', 'Sevilla']
France = ['Brest']
Great_Britain = ['Liverpool', 'London']
Netherlands = ['Amsterdam', 'Rotterdam']
Italy = ['Salerno', 'Venice']
Greece = ['Limassol', 'Larnaca']
Russia = ['Saint Petersburg']
China = ['Shanghai', 'Xiamen International']
India = ['Cochin', 'Mumbai']
Japan = ['Kobe', 'Osaka', 'Yokohama']
Thailand = ['Bangkok']
United_Arab_Emirates = ['Dubai']
Egypt = ['Alexandria']
Morocco = ['Tangier']
South_Africa = ['Cape Town']
Australia = ['Newcastle', 'Sydney']
country_names = ['USA', 'Canada', 'Mexico', 'Argentina', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Peru', 'Costa Rica',
                 'Panama', 'Germany', 'Spain', 'France', 'Great Britain', 'Netherlands', 'Italy', 'Greece', 'Russia',
                 'China', 'India', 'Japan', 'Thailand', 'United Arab Emirates', 'Egypt', 'Morocco', 'South Africa',
                 'Australia']
port_lists = [USA, Canada, Mexico, Argentina, Brazil, Chile, Colombia, Ecuador, Peru, Costa_Rica, Panama,
              Germany, Spain, France, Great_Britain, Netherlands, Italy, Greece, Russia, China, India, Japan,
              Thailand, United_Arab_Emirates, Egypt, Morocco, South_Africa, Australia]
def create_port_list(ports):
    for port_list in port_lists:
        for port in port_list:
            ports.append(port)
    ports.insert(0, '-Empty-')
    return ports
def get_country_of_port(port_name):
    index = 0
    for ports_in_country in port_lists:
        if port_name in ports_in_country:
            return country_names[index]
        index += 1
print("List of ports:")
ports = []
ports = create_port_list(ports)
print(ports)
print("Country of the port 'Miami':", get_country_of_port('Miami'))
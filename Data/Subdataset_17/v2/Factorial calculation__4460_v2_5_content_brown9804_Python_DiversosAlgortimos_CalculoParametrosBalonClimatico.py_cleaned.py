def calculate_velocity(t):
    return -0.48 * (t ** 3) + 36 * (t ** 2) - 760 * t + 4100
def calculate_altitude(t):
    return -0.12 * (t ** 4) + 12 * (t ** 3) - 380 * (t ** 2) + 4100 * t + 220
def convert_velocity_to_kmh(velocity):
    return velocity * 3.6
def process_times(start_time, end_time, increment):
    max_altitude = 0
    max_altitude_time = 0
    for time in range(start_time, end_time + 1, increment):
        velocity = calculate_velocity(time)
        altitude = calculate_altitude(time)
        velocity_kmh = convert_velocity_to_kmh(velocity)
        if altitude > max_altitude:
            max_altitude = altitude
            max_altitude_time = time
        print(f"{time:2}h   {altitude:8.2f}m       {velocity_kmh:6.2f}km/h")
    print(f"La altura máxima se alcanzó a las {max_altitude_time} horas.")
    print(f"Esta altura máxima fue de {max_altitude} metros.")
def main():
    while True:
        try:
            start_time = int(input("Ingrese el tiempo inicial (en horas): "))
            end_time = int(input("Ingrese el tiempo final (en horas): "))
            increment = int(input("Ingrese el incremento de horas: "))
            if 0 <= start_time < end_time <= 48:
                break
            else:
                print("El tiempo inicial debe ser mayor o igual a cero y el tiempo final debe ser menor o igual a 48 horas.")
        except ValueError:
            print("Por favor, ingrese valores enteros válidos.")
    process_times(start_time, end_time, increment)
if __name__ == "__main__":
    main()
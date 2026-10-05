from requests_html import HTMLSession
session = HTMLSession()
city_id = "e1bbaf5ba44a74170e3bb9f892416301c36b3b17f37e1a666c6e1213de0f5668"
def get_weather_data(forecast):
    website_url = f"https:
    def extract_weather_for_today(website_url):
        response = session.get(website_url)
        response.html.render()
        today_weather = response.html.find('div.today_nowcard', first=True)
        data_dict = {}
        if today_weather:
            data = today_weather.text.split('\n')
            data_dict = {
                'location': data[0],
                'time': data[1],
                'temperature': data[2],
                'status': data[3],
                'feels_like': data[4],
                'high-low': data[5],
                'wind': data[9],
                'humidity': data[11],
                'dew_point': data[13],
                'pressure': data[15],
                'visibility': data[17]
            }
        return data_dict
    def extract_hourly_weather(website_url):
        response = session.get(website_url)
        hourly_weather_section = response.html.find('region', first=True)
        hourly_weather_section.find('.locations-title', first=True).html
        hourly_weather = hourly_weather_section.find('table.twc-table', first=True)
        data_rows = hourly_weather.find('tr')
        data_dict = {}
        for row in data_rows[1:]:
            data = row.text.split("\n")
            time = data[0] + ' ' + data[1]
            data_dict[time] = {
                "Description": data[2],
                "Temp": data[3],
                "Feels": data[4],
                "Precip": data[5],
                "Humidity": data[6],
                "Wind": data[7]
            }
        return data_dict
    def extract_weather_info_for_5days(website_url):
        response = session.get(website_url)
        day_weather_section = response.html.find('region', first=True)
        day_weather_section.find('.locations-title', first=True).html
        day_weather = day_weather_section.find('table.twc-table', first=True)
        data_rows = day_weather.find('tr')
        data_dict = {}
        for row in data_rows[1:]:
            data = row.text.split("\n")
            day = data[0] + ' ' + data[1]
            data_dict[day] = {
                "Description": data[2],
                "High / Low": data[3],
                "Precip": data[4],
                "Humidity": data[5],
                "Wind": data[6]
            }
        return data_dict
    def extract_weather_data_for_10days(website_url):
        response = session.get(website_url)
        day_weather_section = response.html.find('region', first=True)
        day_weather_section.find('.locations-title', first=True).html
        day_weather = day_weather_section.find('table.twc-table', first=True)
        data_rows = day_weather.find('tr')
        data_dict = {}
        for row in data_rows[1:]:
            data = row.text.split("\n")
            day = data[0] + ' ' + data[1]
            data_dict[day] = {
                "Description": data[2],
                "High / Low": data[3],
                "Precip": data[4],
                "Wind": data[5],
                "Humidity": data[6]
            }
        return data_dict
    def extract_monthly_weather_info(website_url):
        response = session.get(website_url)
        month_weather_section = response.html.find('region', first=True)
        month_weather_section.find('.locations-title', first=True).text
        month_weather = month_weather_section.find('.dayCell')
        data_dict = {}
        for data in month_weather:
            info = data.text.split('\n')
            date = info[0]
            data_dict[date] = {
                "Temp High": info[1],
                "Temp Low": info[2]
            }
        return data_dict
    if forecast == 'today':
        return extract_weather_for_today(website_url)
    elif forecast == 'hourbyhour':
        return extract_hourly_weather(website_url)
    elif forecast == '5day':
        return extract_weather_info_for_5days(website_url)
    elif forecast == 'tenday':
        return extract_weather_data_for_10days(website_url)
    elif forecast == 'monthly':
        return extract_monthly_weather_info(website_url)
    else:
        return "Enter a valid forecast"
def main():
    forecast = input("Enter the forecast: ").lower()
    result = get_weather_data(forecast)
    print(result)
if __name__ == "__main__":
    main()
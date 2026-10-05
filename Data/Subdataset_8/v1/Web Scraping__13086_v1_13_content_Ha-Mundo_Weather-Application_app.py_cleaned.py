from requests_html import HTMLSession
session = HTMLSession()
city_id = "e1bbaf5ba44a74170e3bb9f892416301c36b3b17f37e1a666c6e1213de0f5668"
def get_weather_data(forcast):
    website_url = f"https:
    def weather_for_today(website_url):
        response = session.get(website_url)
        response.html.render()
        links_table = response.html.find('div.today_nowcard', first=True)
        data_dict = {}
        splitted_data = links_table.text.split('\n')
        data_dict['location'] = splitted_data[0]
        data_dict['time'] = splitted_data[1]
        data_dict['temperature'] = splitted_data[2]
        data_dict['status'] = splitted_data[3]
        data_dict['feels_like'] = splitted_data[4]
        data_dict['high-low'] = splitted_data[5]
        data_dict['wind'] = splitted_data[9]
        data_dict['humidity'] = splitted_data[11]
        data_dict['dew_point'] = splitted_data[13]
        data_dict['pressure'] = splitted_data[15]
        data_dict['visibility'] = splitted_data[17]
        return data_dict
    def weather_for_hourly(website_url):
        response = session.get(website_url)
        hourly_weather_section = response.html.find('region', first=True)
        hourly_weather_section.find('.locations-title', first=True).html
        hourly_weather = hourly_weather_section.find('table.twc-table', first=True)
        data_rows = hourly_weather.find('tr')
        data_dict = {}
        for single_row in data_rows[1:]:
            splitting_data = single_row.text.split("\n")
            single_dict = {}
            single_dict["Time"] = splitting_data[0] + ' ' + splitting_data[1]
            single_dict["Description"] = splitting_data[2]
            single_dict["Temp"] = splitting_data[3]
            single_dict["Feels"] = splitting_data[4]
            single_dict["Precip"] = splitting_data[5]
            single_dict["Humidity"] = splitting_data[6]
            single_dict["Wind"] = splitting_data[7]
            data_dict[single_dict['Time']] = single_dict
        return data_dict
    def weather_info_for_5days(website_url):
        response = session.get(website_url)
        day_weather_section = response.html.find('region', first=True)
        day_weather_section.find('.locations-title', first=True).html
        day_weather = day_weather_section.find('table.twc-table', first=True)
        data_row = day_weather.find('tr')
        data_dict = {}
        for single_rows in data_row[1:]:
            splitting_data = single_rows.text.split("\n")
            single_dict = {}
            single_dict["Day"] = splitting_data[0] + ' ' + splitting_data[1]
            single_dict["Description"] = splitting_data[2]
            single_dict["High / Low "] = splitting_data[3]
            single_dict["Precip"] = splitting_data[4]
            single_dict["Humidity"] = splitting_data[5]
            single_dict["Wind"] = splitting_data[6]
            data_dict[single_dict['Day']] = single_dict
        return data_dict
    def weather_data_10days(website_url):
        response = session.get(website_url)
        day_weather_section = response.html.find('region', first=True)
        day_weather_section.find('.locations-title', first=True).html
        day_weather = day_weather_section.find('table.twc-table', first=True)
        data_row = day_weather.find('tr')
        data_dict = {}
        for single_rows in data_row[1:]:
            splitting_data = single_rows.text.split("\n")
            single_dict = {}
            single_dict["Day"] = splitting_data[0] + ' ' + splitting_data[1]
            single_dict["Description"] = splitting_data[2]
            single_dict["High / Low "] = splitting_data[3]
            single_dict["Precip"] = splitting_data[4]
            single_dict["Wind"] = splitting_data[5]
            single_dict["Humidity"] = splitting_data[6]
            data_dict[single_dict['Day']] = single_dict
        return data_dict
    def monthly_weather_info(website_url):
        response = session.get(website_url)
        month_weather_section = response.html.find('region', first=True)
        month_weather_section.find('.locations-title', first=True).text
        month_weather = month_weather_section.find('.dayCell')
        weather_data = {}
        for data in month_weather:
            info_dict = {}
            splitting_data = (data.text.split('\n'))
            info_dict["Date"] = splitting_data[0]
            info_dict["Temp High"] = splitting_data[1]
            info_dict["Temp Low"] = splitting_data[2]
            weather_data[info_dict['Date']] = info_dict
        return weather_data
    if forcast == 'today':
        return weather_for_today(website_url)
    elif forcast == 'hourbyhour':
        return weather_for_hourly(website_url)
    elif forcast == '5day':
        return weather_info_for_5days(website_url)
    elif forcast == 'tenday':
        return weather_data_10days(website_url)
    elif forcast == 'monthly':
        return monthly_weather_info(website_url)
    else:
        return "Enter a valid forecast"
def main():
    forcast = input("Enter the forecast: ").lower()
    result = get_weather_data(forcast)
    print(result)
if __name__ == "__main__":
    main()
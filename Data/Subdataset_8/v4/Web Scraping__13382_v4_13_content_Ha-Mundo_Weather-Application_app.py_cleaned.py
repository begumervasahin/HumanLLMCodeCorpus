from requests_html import HTMLSession
session = HTMLSession()
city_id = "e1bbaf5ba44a74170e3bb9f892416301c36b3b17f37e1a666c6e1213de0f5668"
def weather_for_today(city_id):
    forcast = input("Enter the forecast: ").lower()
    website_url = f"https:
    response = session.get(website_url)
    response.html.render()
    today_weather_card = response.html.find('div.today_nowcard', first=True)
    data_dict = {}
    if today_weather_card:
        weather_info = today_weather_card.text.split('\n')
        data_dict['location'] = weather_info[0]
        data_dict['time'] = weather_info[1]
        data_dict['temperature'] = weather_info[2]
        data_dict['status'] = weather_info[3]
        data_dict['feels_like'] = weather_info[4]
        data_dict['high-low'] = weather_info[5]
        data_dict['wind'] = weather_info[9]
        data_dict['humidity'] = weather_info[11]
        data_dict['dew_point'] = weather_info[13]
        data_dict['pressure'] = weather_info[15]
        data_dict['visibility'] = weather_info[17]
    else:
        print("No data available for today's weather.")
    return data_dict
def weather_for_hourly(city_id):
    forcast = input("Enter the forecast: ").lower()
    website_url = f"https:
    response = session.get(website_url)
    hourly_weather_section = response.html.find('region', first=True)
    hourly_weather_section.find('.locations-title', first=True).html
    hourly_weather_table = hourly_weather_section.find('table.twc-table', first=True)
    data_dict = {}
    if hourly_weather_table:
        data_rows = hourly_weather_table.find('tr')
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
    else:
        print("No hourly weather data available.")
    return data_dict
forecast_type = input("Enter the forecast type (today/hourbyhour/5day/tenday/monthly): ").lower()
if forecast_type == 'today':
    result_for_today = weather_for_today(city_id)
    print(result_for_today)
elif forecast_type == 'hourbyhour':
    result_for_hr = weather_for_hourly(city_id)
    print(result_for_hr)
else:
    print("Enter a valid forecast type.")
from requests_html import HTMLSession
b1 = HTMLSession()
b2 = "e1bbaf5ba44a74170e3bb9f892416301c36b3b17f37e1a666c6e1213de0f5668"
b3 = input("Enter the b3: ").lower()
b4 = f"https:
def fonk1(b2):
        b5 = b1.get(b4)
        b5.html.render()
        b6 = b5.html.find('div.today_nowcard', b10=True)
        b7 = {}
        b8 = b6.text.split('\n')
        b7['location'] = b8[0]
        b7['time'] = b8[1]
        b7['temperature'] = b8[2]
        b7['status'] = b8[3]
        b7['feels_like'] = b8[4]
        b7['high-low'] = b8[5]
        b7['wind'] = b8[9]
        b7['humidity'] = b8[11]
        b7['dew_point'] = b8[13]
        b7['pressure'] = b8[15]
        b7['visibility'] = b8[17]
        return b7
def fonk2(b2):
    b5 = b1.get(b4)
    b9 = b5.html.find('region', b10=True)
    b9.find('.locations-title', b10 = True).html
    b11 = b9.find('table.twc-table', b10=True)
    b12 = b11.find('tr')
    b7 = {}
    for single_row in b12[1:]:
        b13 = single_row.text.split("\n")
        b14 = {}
        b14["Time"] = b13[0] + ' ' + b13[1]
        b14["Description"] = b13[2]
        b14["Temp"] = b13[3]
        b14["Feels"] = b13[4]
        b14["Precip"] = b13[5]
        b14["Humidity"] = b13[6]
        b14["Wind"] = b13[7]
        b7[b14['Time']] = b14
    return b7
def fonk3(b2):
    b7 = {}
    b5 = b1.get(b4)
    b15 = b5.html.find('region', b10=True)
    b15.find('.locations-title', b10 = True).html
    b16 = b15.find('table.twc-table', b10=True)
    b17 = b16.find('tr')
    for single_rows in b17[1:]:
        b13 = single_rows.text.split("\n")
        b14 = {}
        b14["Day"] = b13[0] + ' ' + b13[1]
        b14["Description"] = b13[2]
        b14["High / Low "] = b13[3]
        b14["Precip"] = b13[4]
        b14["Humidity"] = b13[5]
        b14["Wind"] = b13[6]
        b7[b14['Day']] = b14
    return b7
def fonk4(b2):
    b5 = b1.get(b4)
    b15 = b5.html.find('region', b10=True)
    b15.find('.locations-title', b10 = True).html
    b16 = b15.find('table.twc-table', b10=True)
    b17 = b16.find('tr')
    b7 = {}
    for single_rows in b17[1:]:
            b13 = single_rows.text.split("\n")
            b14 = {}
            b14["Day"] = b13[0] + ' ' + b13[1]
            b14["Description"] = b13[2]
            b14["High / Low "] = b13[3]
            b14["Precip"] = b13[4]
            b14["Wind"] = b13[5]
            b14["Humidity"] = b13[6]
            b7[b14['Day']] = b14
    return b7
def fonk5(b2):
    b5 = b1.get(b4)
    b18 = b5.html.find('region', b10=True)
    b18.find('.locations-title', b10 = True).text
    b19 = b18.find('.dayCell')
    b20 = {}
    for data in b19:
        b21 = {}
        b13 = (data.text.split('\n'))
        b21["Date"] = b13[0]
        b21["Temp High"] = b13[1]
        b21["Temp Low"] = b13[2]
        b20[b21['Date']] = b21
    return b20
if b3 = = 'today':
    b22 = fonk1(b4)
    print(b22)
elif b3 = = 'hourbyhour':
    b23 = fonk2(b4)
    print(b23)
elif b3 = = '5day':
    b24 = fonk3(b4)
    print(b24)
elif b3 = = 'tenday':
    b25 = fonk4(b4)
    print(b25)
elif b3 = = 'monthly':
    b26 = fonk5(b4)
    print(b26)
else:
    print("Enter a valid b3")
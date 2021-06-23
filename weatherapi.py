import requests 
from datetime import datetime
api_key='039d9fe06b23f581e9840add88552107'
link='https://api.openweathermap.org/data/2.5/weather?q='
city_name=input('Enter the city name:')
com_link=link+city_name+'&appid='+api_key

r= requests.get(com_link)
r_data=r.json()
temp_city=r_data['main']['temp']-273
weather_desc=r_data['weather'][0]['description']
hmdt=r_data['main']['humidity']
wnd_speed=r_data['wind']["speed"]
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")


f= open('Weather_report.txt', 'a+')
f.write('\r\n \r\n \r\nWEATHER REPORT OF {} \r\n '.format(city_name.upper()))
f.write("-------------------------------------------------------------\r\n")
f.write("Weather Stats for - {}  || {} \r\n".format(city_name.upper(), date_time))
f.write("Current temperature is: {:.2f} deg C \r\n".format(temp_city))
f.write("Current weather desc  : {} \r\n".format(weather_desc ))
f.write("Current Humidity      : {} % \r\n".format(hmdt))
f.write("Current wind speed    :{}".format(wnd_speed) +'kmph \r\n \r\n \r\n ')
f.close()


print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(city_name.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wnd_speed ,'kmph')



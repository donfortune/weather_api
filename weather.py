import requests


API_KEY = 'xxxxxxxxxxxxxxxxxx'
URL = 'http://api.openweathermap.org/data/2.5/weather'

city = input('Enter City Name: ')
request_url = f"{URL}?appid={API_KEY}&q={city}"

response = requests.get(request_url)
content = response.json()

if response.status_code == 200:
    print('all good to go')
else:
    print('theres an error')
#print(content)
weather = content['weather'][0]['description']
print(weather)
temperature = content['main']['temp']
print(temperature)



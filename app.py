import os
from dotenv import load_dotenv
import requests
import matplotlib.pyplot as plt

load_dotenv()

api_id=os.getenv("open_weather_api_key")





user_input=input("enter city name :")

weather_data=requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_id}")


if weather_data.status_code != 200:
    print("Invalid city or API error")
    exit()

data=weather_data.json()
city=data['name']
weather= data ['weather'][0]['main']
temp=data['main']['temp']
humidity=data['main']['humidity']

print(f" Name of the City: {city}")
print(f"Temperature: {temp} °C")
print(f"Humidity: {humidity} %")
print(f"Condition: {weather}")

# Bar chart 
labels=["temprature(°F)" ,"humidity(%)"]
values=[temp,humidity]
plt.figure(figsize=(6,4))
plt.bar(labels,values)
plt.title(f"weather report {city}")
plt.grid(axis="y", linestyle="--", alpha=0.6)
plt.ylabel("values")
plt.tight_layout()

plt.savefig("output.png")
plt.show()








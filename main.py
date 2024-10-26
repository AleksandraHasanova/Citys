from opencage.geocoder import OpenCageGeocode
from tkinter import *
from tkinter import messagebox as mb
import webbrowser
import requests


def get_weather(lat, lon):
    try:
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
        response.raise_for_status()
        weather_data = response.json()
        current_weather = weather_data['current_weather']
        return current_weather
    except Exception as e:
        return f"Ошибка при получении погоды: {e}"

def show_weather():
    current_weather = get_weather(lat, lon)
    weather_window = Toplevel(window)
    weather_window.title("Текущая погода")

    if isinstance(current_weather, str):
        label = Label(weather_window, text=current_weather)
        label.pack()
    else:
        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']
        weather_text = f"Температура: {temperature}°C\nСкорость ветра: {windspeed} км/ч"
        label = Label(weather_window, text=weather_text)
        label.pack()



def show_weather():
    current_weather = get_weather(lat, lon)
    weather_window = Toplevel(window)
    weather_window.title("Текущая погода")

    if isinstance(current_weather, str):
        label = Label(weather_window, text=current_weather)
    else:
        temperature = current_weather['temperature']
        windspeed = current_weather['windspeed']
        weather_text = f"Температура: {temperature}°C\nСкорость ветра: {windspeed} км/ч"
        label = Label(weather_window, text=weather_text)
        label.pack()


def get_coordinates(city, key):
    global lat, lon
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            currency = results[0]['annotations']['currency']['name']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}. Регион: {region}\n Валюта: {currency}",
                        "map_url": osm_url}
            else:
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}. Валюта: {currency}",
                        "map_url": None}
        else:
            return f'Город {city} не найден'
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')

def show_coordinates(event=None):
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {result['coordinates']}")
    global map_url
    map_url = result['map_url']

def show_map():
    if map_url:
        webbrowser.open(map_url)

key = '34eb7c00e36444bea8ed85dfe746e82e'
map_url = None

window = Tk()
window.title('Информация о городах')
window.geometry('450x250')

entry = Entry()
entry.pack(pady=10)
entry.bind('<Return>', show_coordinates)

btn = Button(text='Поиск города', command=show_coordinates)
btn.pack(pady=10)

label = Label(text='Введите название города')
label.pack(pady=10)

map_btn = Button(text='Показать карту', command=show_map)
map_btn.pack(pady=10)

weather_button = Button(text="Показать погоду", command=show_weather)
weather_button.pack(pady=10)


window.mainloop()

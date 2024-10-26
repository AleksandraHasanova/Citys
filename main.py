from opencage.geocoder import OpenCageGeocode
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as mb


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return f"широта {lat}, долгота {lng}"
        else:
            return 'Город не найден'
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')

key = '34eb7c00e36444bea8ed85dfe746e82e'
city = 'Луксор'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')



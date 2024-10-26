from opencage.geocoder import OpenCageGeocode
from tkinter import ttk
from tkinter import *


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)
    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']
    else:
        return 'Город не найден'

key = '34eb7c00e36444bea8ed85dfe746e82e'
city = 'Moscow'
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')



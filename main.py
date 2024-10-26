from opencage.geocoder import OpenCageGeocode
from tkinter import *
from tkinter import messagebox as mb
import webbrowser



def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lon = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            osm_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}"
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}. Регион: {region}",
                        "map_url": osm_url}
            else:
                return {"coordinates": f"Широта: {lat}, Долгота: {lon}\n Страна: {country}.",
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

window.mainloop()

from opencage.geocoder import OpenCageGeocode
from tkinter import *
from tkinter import messagebox as mb


def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            country = results[0]['components']['country']
            if 'state' in results[0]['components']:
                region = results[0]['components']['state']
                return f"Широта: {lat}, Долгота: {lng}\n Страна: {country}. Регион: {region}"
            else:
                return f"Широта: {lat}, Долгота: {lng}\n Страна: {country}."
        else:
            return f'Город {city} не найден'
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка {e}')

def show_coordinates(event=None):
    city = entry.get()
    result = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}:\n {result}")


key = '34eb7c00e36444bea8ed85dfe746e82e'

window = Tk()
window.title('Информация о городах')
window.geometry('450x170')

entry = Entry()
entry.pack(pady=10)
entry.bind('<Return>', show_coordinates)

btn = Button(text='Поиск города', command=show_coordinates)
btn.pack(pady=10)

label = Label(text='Введите название города')
label.pack(pady=10)


window.mainloop()

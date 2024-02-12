import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import requests
import time
from PIL import ImageTk, Image

def weather(window):
    city = txt.get()
    api_k = input("Api key? ")
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_k}"
    
    json_data = requests.get(api).json()

    if str(json_data['cod']) == '404':
        labelimg.config(image='')
        label1.config(text=f"Error. {city} does not exist.")
        label2.config(text="")

    else:
        temp = int(json_data['main']['temp'] - 273.15) #NOTE: EN KELVIN, A CONVERTIR AVEC 273.15
        mini = int(json_data['main']['temp_min'] - 273.15)
        maxi = int(json_data['main']['temp_max'] - 273.15)
        condition = json_data['weather'][0]['description']
        humid = json_data['main']['humidity']
        f_like = int(json_data['main']['feels_like'] - 273.15)
        w_speed = json_data['wind']['speed']
        icons = json_data['weather'][0]['icon']
        sunrise = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 3600)) #on ajoute 3600 secondes(1 heure) car on est en GMT+1
        sunset = time.strftime("%H:%M:%S", time.gmtime(json_data['sys']['sunset'] - 3600)) #on ajoute 3600 secondes(1 heure) car on est en GMT+1
        
        icon_url = f'http://openweathermap.org/img/wn/{icons}@2x.png'
        
        img = Image.open(requests.get(icon_url, stream=True).raw)
        icon = ImageTk.PhotoImage(img)
        labelimg.config(image=icon)
        labelimg.image = icon

        res = f"{city.capitalize()}: {condition}\n  {str(temp)}°C, Feels like {str(f_like)}°C "
        """\nSunrise: {sunrise} and Sunset: {sunset}"""
        res_info = f"\nSunrise: {sunrise} and Sunset: {sunset}\nMax Temperatures: {str(maxi)}°C,  Min Temperatures: {str(mini)}°C\nHumidity: {humid}%,  Wind Speed: {str(w_speed)}m/sec"
        label1.config(text=res)
        label2.config(text=res_info)
        txt.set("")
        


window = ttk.Window(themename='darkly') 
window.title("Weather App")
window.geometry("750x550") 
Font = ("Helvetica", 15, "bold")
Font2 = ("Helvetica", 12)
title = ("Helvetica", 20, "bold")
window.resizable(False, False)


txt = tk.StringVar()
textfield = ttk.Entry(window, font=title, textvariable=txt)
textfield.place(x=200, y=25 )  

textfield.focus()
textfield.bind('<Return>', weather)
clicked = ttk.StringVar()
clicked.set("en")

labelimg = ttk.Label(window)
label1 = ttk.Label(window, font=title, justify='center')
label2 = ttk.Label(window, font=Font, justify='center')
label3 = ttk.Label(window, font=Font2, text="Language: ")
drop = ttk.OptionMenu(window, clicked, "en","en", "fr", "es")

labelimg.place(x= 100, y=125)  
label1.place(x = 225, y=135)  
label2.place(x = 95, y = 225)
label3.place(x=550, y=505)
drop.place(x=650, y= 500)



window.mainloop()


import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import requests
import time
from PIL import ImageTk, Image










def weather(window):
    city = txt.get()
    lang_str = clicked.get()
    
    
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang_str}&appid={api_k}"
    print(api)
    
    
    json_data = requests.get(api).json()
    

    if str(json_data['cod']) == '404':
        labelimg.config(image='')
        if lang_str == "en":
            label1.config(text=f"Error. {city} does not exist.")
        elif lang_str == "fr":
            label1.config(text=f"Erreur. {city} n'existe pas.")
        elif lang_str == "es":
            label1.config(text=f"Error. {city} no existe.")
        label2.config(text="")

    elif str(json_data['cod']) == '401':
        if lang_str == "en":
            label1.config(text=f"Error. Invalid api key.")
        elif lang_str == "fr":
            label1.config(text=f"Erreur. Clé api invalide.")
        elif lang_str == "es":
            label1.config(text=f"Error. Api cle no existe.")
        
        
        

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



        res_en = f"{city.capitalize()}: {condition.capitalize()}\n  {str(temp)}°C, Feels like {str(f_like)}°C "
        res_info_en = f"\nSunrise: {sunrise} and Sunset: {sunset}\n\nMax Temperatures: {str(maxi)}°C,  Min Temperatures: {str(mini)}°C\n\nHumidity: {humid}%,  Wind Speed: {str(w_speed)}m/sec"
        
        res_fr = f"{city.capitalize()}: {condition.capitalize()}\n  {str(temp)}°C, Ressenti: {str(f_like)}°C "
        res_info_fr = f"\nLever du soleil: {sunrise} et Coucher du soleil: {sunset}\n\nTempératures maximal: {str(maxi)}°C, Températures minimal: {str(mini)}°C\n\nHumidité: {humid}%,  Vitesse du vent: {str(w_speed)}m/sec"

        res_es = f"{city.capitalize()}: {condition.capitalize()}\n  {str(temp)}°C, Sensación térmica: {str(f_like)}°C "
        res_info_es = f"\nAmanecer: {sunrise} y Atardecer: {sunset}\n\nTemperatura máxima : {str(maxi)}°C, Temperatura mínimo: {str(mini)}°C\n\nHumedad: {humid}%,  Velocidad del viento: {str(w_speed)}m/sec"



        lang = "res_"+clicked.get()
        lang_info = "res_info_"+clicked.get()
        label1.config(text=locals()[lang])
        label2.config(text=locals()[lang_info])
        txt.set("")
        


def update_label(*args):
    if clicked.get() == "en":
        label3['text'] = "Language: "
        labelimg.place(x= 130, y=110)  
        label1.place(x = 250, y=135)  
        label2.place(x = 125, y = 265)
        

    if clicked.get() == "fr":
        #label3.config(text="Langue: ")
        label3['text'] = "Langue: "
        labelimg.place(x= 135, y=100)
        label1.place(x = 260, y=120)  
        label2.place(x = 60, y = 250)

    if clicked.get() == "es":
        label3['text'] = "Lengua: "
        labelimg.place(x= 105, y=110)  
        label1.place(x = 225, y=135)
        label2.place(x = 75, y = 250)

def menu():
    global val_button
    var1 = ttk.StringVar(value="0")
    var2 = ttk.StringVar(value="0")
    if val_button == 0:
        ch1 = ttk.Checkbutton(window, text="test", variable=var1,style='RoundToggle.Toolbutton')
        ch2 = ttk.Checkbutton(window, text="test2", variable=var2, style='RoundToggle.Toolbutton')
        ch1.place(x=150, y=250)
        ch2.place(x=300, y=450)
        val_button = 1
    if val_button == 1:
        #for i in range(0, 1):
        ch1.place_forget()
            #locals()["ch"+str(i)].place_forget()
        val_button = 0
        
            
        




window = ttk.Window(themename='darkly') 
window.title("Weather App")
window.geometry("750x550") 
title = ("Helvetica", 23, "bold")
Font = ("Helvetica", 17, "bold")
Font2 = ("Helvetica", 17)
window.resizable(False, False)
val_button = 0
style = ttk.Style(theme='darkly')

style.configure('TCheckbutton' ,font=('Helvetica', 17))


api_k = input("Api key? ")
txt = tk.StringVar()
textfield = ttk.Entry(window, font=title, textvariable=txt)
textfield.place(x=220, y=25 )  

textfield.focus()
textfield.bind('<Return>', weather)
clicked = ttk.StringVar()
clicked.set("en")



labelimg = ttk.Label(window, )
label1 = ttk.Label(window, font=title, justify='center')
label2 = ttk.Label(window, font=Font, justify='center')
label3 = ttk.Label(window, font=Font2, text='Language: ')
drop = ttk.OptionMenu(window, clicked, "en","en","fr","es")
button = ttk.Button(window, text="Show menu",command=menu  )




labelimg.place(x= 130, y=110)  
label1.place(x = 250, y=135)  
label2.place(x = 125, y = 265)
label3.place(x=530, y=505)
drop.place(x=650, y= 500)
button.place(x=150, y=500)















clicked.trace_add("write", update_label)
window.mainloop()
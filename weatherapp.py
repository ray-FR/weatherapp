import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
import requests
import time
from PIL import ImageTk, Image










def weather(window):
    global  part3, part3_en, part3_fr, part3_es, x_var_en, x_var_fr, x_var_es, part1, part1_en, part1_fr, part1_es, part2, part2_en, part2_fr, part2_es
    city = txt.get()
    #lang_str = clicked.get()

    """ 
    x_var_en = 40
    x_var_fr = 60
    x_var_es = 75
    """
    
    
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang={clicked.get()}&appid={api_k}"
    print(api)
    
    
    json_data = requests.get(api).json()
    

    if str(json_data['cod']) == '404':
        labelimg.config(image='')
        if clicked.get() == "en":
            label1.config(text=f"Error. {city} does not exist.")
        elif clicked.get() == "fr":
            label1.config(text=f"Erreur. {city} n'existe pas.")
        elif clicked.get() == "es":
            label1.config(text=f"Error. {city} no existe.")
        label2.config(text="")

    elif str(json_data['cod']) == '401':
        if clicked.get() == "en":
            label1.config(text=f"Error. Invalid api key.")
        elif clicked.get() == "fr":
            label1.config(text=f"Erreur. Clé api invalide.")
        elif clicked.get() == "es":
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

        x_var = "x_var_"+clicked.get()
        part1 = "part1_"+clicked.get()
        part2 = "part2_"+clicked.get()
        part3 = "part3_"+clicked.get()



        if var1.get() == "1" and var2.get() == "1":
            part1_en = f""
            part1_fr = f""
            part1_es = f""
        elif var1.get() == "1":
            part1_en = f"Sunset: {sunrise}"
            part1_fr = f"Coucher du soleil: {sunset}"
            part1_es = f"Atardecer: {sunset}"
        elif var2.get() == "1":
            part1_en = f"Sunrise: {sunset}"
            part1_fr = f"Lever du soleil: {sunrise}"
            part1_es = f"Amanecer: {sunrise}"
        elif var1.get() == "0" and var2.get() == "0":
            part1_en = f"Sunrise: {sunrise} and Sunset: {sunset}"
            part1_fr = f"Lever du soleil: {sunrise} et Coucher du soleil: {sunset}"
            part1_es = f"Amanecer: {sunrise} y Atardecer: {sunset}"


        if var3.get() == "1" and var4.get() == "1":
            part2_en = f""
            part2_fr = f""
            part2_es = f""
        elif var3.get() == "1":
            part2_en = f"Minimum Temperature: {str(mini)}°C"
            part2_fr = f"Température minimal: {str(mini)}°C"
            part2_es = f"Temperatura mínimo: {str(mini)}°C"
        elif var4.get() == "1":
            part2_en = f"Maximum Temperature: {str(maxi)}°C"
            part2_fr = f"Température maximal: {str(maxi)}°C"
            part2_es = f"Temperatura máxima: {str(maxi)}°C"
        elif var3.get() == "1" or var4.get() == "1":
            x_var_en = 170
            x_var_fr = 70
            x_var_es = 145
            label2.place(x = globals()[x_var], y = 265)
        elif var3.get() == "0" and var4.get() == "0":
            part2_en = f"Maximum Temperature: {str(maxi)}°C,  Minimum Temperature: {str(mini)}°C"
            part2_fr = f"Température maximal: {str(maxi)}°C, Température minimal: {str(mini)}°C"
            part2_es = f"Temperatura máxima: {str(maxi)}°C, Temperatura mínimo: {str(mini)}°C"
        
        
        if var5.get() == "1" and var6.get() == "1":
            part3_en = f""
            part3_fr = f""
            part3_es = f""
        elif var5.get() == "1":
            part3_en = f"Wind Speed: {str(w_speed)}m/sec"
            part3_fr = f"Vitesse du vent: {str(w_speed)}m/sec"
            part3_es = f"Velocidad del viento: {str(w_speed)}m/sec"
            
        elif var6.get() == "1":
            part3_en = f"Humidity: {humid}%"
            part3_fr = f"Humidité: {humid}%"
            part3_es = f"Humedad: {humid}%"
        elif var5.get() == "0" and var6.get() == "0":
            part3_en = f"Humidity: {humid}%, Wind Speed: {str(w_speed)}m/sec"
            part3_fr = f"Humidité: {humid}%, Vitesse du vent: {str(w_speed)}m/sec"
            part3_es = f"Humedad: {humid}%, Velocidad del viento: {str(w_speed)}m/sec"

        
        res_en = f"{city.capitalize()}: {condition.capitalize()}\n  {str(temp)}°C, Feels like {str(f_like)}°C "
        res_info_en = f"\n{globals()[part1]}\n\n{globals()[part2]}\n\n{globals()[part3]}"
        
        res_fr = f"{city.capitalize()}: {condition.capitalize()}\n  {str(temp)}°C, Ressenti: {str(f_like)}°C "
        res_info_fr = f"\n{globals()[part1]}\n\n{globals()[part2]}\n\n{globals()[part3]}"

        res_es = f"{city.capitalize()}: {condition.capitalize()}\n  {str(temp)}°C, Sensación térmica: {str(f_like)}°C "
        res_info_es = f"\n{globals()[part1]}\n\n{globals()[part2]}\n\n{globals()[part3]}"



        lang = "res_"+clicked.get()
        lang_info = "res_info_"+clicked.get()
        label1.config(text=locals()[lang])
        label2.config(text=locals()[lang_info])
        txt.set("")
        
        

        
        
        



def update_label(*args):
    if clicked.get() == "en":
        label3['text'] = "Language: "
        button['text'] = "Show menu"
        labelimg.place(x= 120, y=110)  
        label1.place(x = 250, y=135)  
        label2.place(x = 40, y = 265)
        

    if clicked.get() == "fr":
        
        label3['text'] = "Langue: "
        button['text'] = "Afficher le menu"
        labelimg.place(x= 135, y=100)
        label1.place(x = 260, y=120)  
        label2.place(x = 60, y = 265)

    if clicked.get() == "es":
        label3['text'] = "Lengua: "
        button["text"] = "Mostrar menú"
        labelimg.place(x= 105, y=110)  
        label1.place(x = 225, y=135)
        label2.place(x = 75, y = 265)



def menu(): #probablement la pire fonction que j'ai jamais écrit
    global val_button, ch1, ch2, ch3, ch4, ch5, ch6
    

    if val_button == 0:     
        textfield.config(state='disabled')
        labelimg.config(image='')
        if clicked.get() == "en":
            txt.set("Textfield disabled.")
        elif clicked.get() == "fr":
            txt.set("Textfield désactivé")
        elif clicked.get() == "es":
            txt.set("Textfield deshabilitado.")
        label1.config(text="")
        label2.config(text="")
        
        
        
        ch1 = ttk.Checkbutton(window, variable=var1, bootstyle='round-toggle')
        ch2 = ttk.Checkbutton(window, variable=var2, bootstyle='round-toggle')
        ch3 = ttk.Checkbutton(window, variable=var3, bootstyle='round-toggle')
        ch4 = ttk.Checkbutton(window, variable=var4, bootstyle='round-toggle')
        ch5 = ttk.Checkbutton(window, variable=var5, bootstyle='round-toggle')
        ch6 = ttk.Checkbutton(window, variable=var6, bootstyle='round-toggle')

        if clicked.get() == "en":
            ch1['text'] = "Do not include sunrise"
            ch2['text'] = "Do not include sunset"
            ch3['text'] = "Do not include maximum temperatures"
            ch4['text'] = "Do not include minimum temperatures"
            ch5['text'] = "Do not include humidity"
            ch6['text'] = "Do not include wind speed"
        elif clicked.get() == "fr":
            ch1['text'] = "Ne pas inclure le lever du soleil"
            ch2['text'] = "Ne pas inclure le coucher du soleil"
            ch3['text'] = "Ne pas inclure la température maximal"
            ch4['text'] = "Ne pas inclure la température minimal"
            ch5['text'] = "Ne pas inclure l'humidité"
            ch6['text'] = "Ne pas inclure la vitesse du vent"
        elif clicked.get() == "es":
            ch1['text'] = "No incluir el amanecer"
            ch2['text'] = "No incluir la puesta del sol"
            ch3['text'] = "No incluir la temperatura máxima"
            ch4['text'] = "No incluir la temperatura mínima"
            ch5['text'] = "No incluir la humedad"
            ch6['text'] = "No incluir la velocidad del viento"



        ch1.place(x=25, y=170)
        ch2.place(x=25, y=205)
        ch3.place(x=25, y=240)
        ch4.place(x=450, y=170)
        ch5.place(x=450, y=205)
        ch6.place(x=450, y=240)
        drop['state'] = 'disabled'
        val_button = 1

    elif val_button == 1:
        txt.set("")
        textfield['state'] = 'enabled'
        drop['state'] = 'enabled'
        ch1.place_forget()
        ch2.place_forget()
        ch3.place_forget()
        ch4.place_forget()
        ch5.place_forget()
        ch6.place_forget()
        
        
        
        """doesnt work, it just refuses to use the method that is associated with the checkbutton objects for some reason?? forgive me
        for the horrid code above
        for i in range(1, 2):
            a = "ch"+str(i)
            globals()[a].place_forget()
        """
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


var1 = ttk.StringVar(value="0")
var2 = ttk.StringVar(value="0")
var3 = ttk.StringVar(value="0")
var4 = ttk.StringVar(value="0")
var5 = ttk.StringVar(value="0")
var6 = ttk.StringVar(value="0")






#style.configure('TCheckbutton' ,font=('Helvetica', 17) ) (doesnt work)


api_k = input("Api key? ")
txt = tk.StringVar()
textfield = ttk.Entry(window, font=title, textvariable=txt)
textfield.place(x=220, y=25 )  



#textfield.focus()
textfield.bind('<Return>', weather)
clicked = ttk.StringVar()
clicked.set("en")



labelimg = ttk.Label(window, )
label1 = ttk.Label(window, font=title, justify='center')
label2 = ttk.Label(window, font=Font, justify='center')
label3 = ttk.Label(window, font=Font2, text='Language: ')
drop = ttk.OptionMenu(window, clicked, "en","en","fr","es")
button = ttk.Button(window, text="Show menu", command=menu)




labelimg.place(x= 120, y=110)  
label1.place(x = 250, y=135)  
label2.place(x = 40, y = 265)
label3.place(x=530, y=505)
drop.place(x=650, y= 500)
button.place(x=50, y=500)















clicked.trace_add("write", update_label)
window.mainloop()
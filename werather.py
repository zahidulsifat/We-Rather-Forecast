import os
import config
from tkinter import *
import tkinter as tk
from datetime import datetime
from tkinter import ttk, messagebox
import sys
import pytz
import requests
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

# Copy Right
# Zahidul Sifat
# 2023

def resource_path2(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
     # PyInstaller creates a temp folder and stores path in _MEIPASS
       base_path = sys._MEIPASS
    except Exception:
       base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# Gui Window
root = tk.Tk()
root.title('We Rather Forecast')
path = resource_path2("weather.ico")
root.iconbitmap("weather.ico")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Background
path = resource_path2("bggg.png")
background_image = tk.PhotoImage(file="bggg.png")
myimage = tk.Label(root, image=background_image, anchor=CENTER)
myimage.pack()
myimage.place(x=0, y=0)


def getWeather():
    try:
        city = textfield.get()

        geolocator = Nominatim(user_agent="geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # weather
        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + (config.api_key)
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp, "°"))
        c.config(text=(condition, "|", "Feels", "Like", temp, "°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception:
        messagebox.showerror("WeRather Forecast", "Invalid Entry!")


# Search box
path = resource_path2("search.png")
Search_image = tk.PhotoImage(file="search.png")
myimage = tk.Label(root, image=Search_image, anchor=CENTER, bg="#FFDBC5")
myimage.pack()
myimage.place(x=200, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#433b37", border=0, fg="white")
textfield.place(x=280, y=40)
textfield.focus()

path = resource_path2("search_icon.png")
Search_icon = tk.PhotoImage(file="search_icon.png")
myimage_icon = tk.Button(root, image=Search_icon, borderwidth=0, cursor="hand2", bg="#433b37", anchor=CENTER,
                         command=getWeather)
myimage_icon.pack()
myimage_icon.place(x=580, y=34)

# logo
path = resource_path2("logo3.png")
Logo_image = tk.PhotoImage(file="logo3.png")
logo = tk.Label(root, image=Logo_image, bg='#FFDBC5')
logo.pack()
logo.place(x=300, y=100)

# Bottom box
path = resource_path2("box.png")
Frame_image = PhotoImage(file="box.png")
frame_myimage = Label(root, image=Frame_image, fg='#35102D', bg="#32102D")
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"), fg="rosybrown", bg='#FFDBC5')
name.place(x=60, y=190)
clock = Label(root, font=("Helvetica", 20, "bold"), fg="brown", bg='#FFDBC5')
clock.place(x=60, y=220)

# label
label1 = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#e8c4b4")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#e8c4b4")
label2.place(x=250, y=400)

label3 = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#e8c4b4")
label3.place(x=430, y=400)

label4 = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#e8c4b4")
label4.place(x=650, y=400)

# Tempeerature and Condition
t = Label(font=("arial", 70, "bold"), fg='brown', bg='#FFDBC5')
t.place(x=600, y=150)
c = Label(font=("arial", 15, "bold"), fg="rosybrown", bg='#FFDBC5')
c.place(x=600, y=250)

# Box Levels
w = Label(text="...", font=("arial", 20, "bold"), fg="brown", bg="#e8c4b4")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), fg="brown", bg="#e8c4b4")
h.place(x=280, y=430)
d = Label(root, text=".....", font=("arial", 20, "bold"), fg="brown", bg="#e8c4b4", justify=CENTER)
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), fg="brown", bg="#e8c4b4")
p.place(x=670, y=430)

root.mainloop()

""""pyinstaller --noconfirm --onefile --windowed --icon "D:/WeRatherForecast/weather.ico" --add-data """""

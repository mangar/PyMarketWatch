import tkinter as tk
import yaml
import time as tm
from time import strftime
from datetime import datetime
from helpers import DateTimeHelper, ExchangeHelper, TkHelper, SoundHelper, ThreadHelper

import threading
import asyncio


BG_COLOR = "#202020"

def time():
    """TK"""
    update_time()  

    # atualiza a data entre 0 e 9 horas a cada 10 minutos
    now = datetime.now()
    if now.hour in range(0,10) and \
       now.minute in range(0,60, 10) and now.second == 0:
        asyncio.run(update_date())


def on_closing():
    """TK"""
    ThreadHelper.stop_running()
    stop_event.set()
    root.destroy()




def update_time():    
    string = strftime('%H:%M:%S')
    label_time.config(text = string)
    label_time.after(1000, time)

async def update_date():
    label_date.config(text = f"\n{DateTimeHelper.full_date_today()}\n")




def update_stocks():
    ThreadHelper.start_running()
    flag_running = False
    while True:
        if not ThreadHelper.is_running():
            stop_event.set()
            return 

        if not flag_running:
            flag_running = True
            _update_stocks()
            flag_running = False
        tm.sleep(0.2)


def _update_stocks():
    for ex in exchanges:

        ex_status = ExchangeHelper.status(ex['open'], ex['close'])        
        label = root.nametowidget(TkHelper.get_label_name(ex['name']))

        text_pos = ""
        if ex_status == "preclose":
            text_pos = f"|PRE CLOSE| {DateTimeHelper.format_diff_now(ex['close'])}"           

            if DateTimeHelper.is_pre_hour_min(ex['close']):
                asyncio.run(SoundHelper.play_preclose())


        elif ex_status == "preopen":
            text_pos = f"|PRE OPEN| {DateTimeHelper.format_diff_now(ex['open'])}"

            if DateTimeHelper.is_pre_hour_min(ex['open']):
                print("1 PLAY PRE OPEN")
                asyncio.run(SoundHelper.play_preopen())

        elif ex_status == "open" or ex_status == "close":
            text_pos = ""

            if ex_status == "open" and DateTimeHelper.is_exact_hour_min(ex['open']):
                asyncio.run(SoundHelper.play_open())

            if ex_status == "close" and DateTimeHelper.is_exact_hour_min(ex['close']):
                asyncio.run(SoundHelper.play_close())


        text = f"{ex['name']}: {ex['open']} ~ {ex['close']} {text_pos}"

        label.config(text=text, foreground = ExchangeHelper.status_color(ex_status))




def load_exchanges():
    with open('./config.yml', 'r') as file:
        data = yaml.safe_load(file)
        exchanges = data['exchanges']

    return exchanges

# 
exchanges = load_exchanges()


root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)

root.title("Market Watch")
root.geometry("480x280")  
root.configure(background=BG_COLOR, highlightcolor=BG_COLOR, highlightthickness=1)

# Data
label_date = tk.Label(root, font=("Tahoma", 10), background = BG_COLOR, foreground = "white")
label_date.config(text="\nSegunda Feira, 22 Abril, 2024\n")
label_date.pack()

# Hora
label_time = tk.Label(root, font=("Tahoma", 52, "bold"), background = BG_COLOR, foreground = "white")
label_time.config(text="20:43:15")
label_time.pack()

# Separador
tk.Label(root, font=("Tahoma", 10), background = BG_COLOR, foreground = "green", text="..\n").pack()

# Stocks
for ex in exchanges:
    ex_status = ExchangeHelper.status(ex['open'], ex['close'])
    label_stock = tk.Label(root, font=("Tahoma", 10), background = BG_COLOR, foreground = ExchangeHelper.status_color(ex_status), name=TkHelper.get_label_name(ex['name']))
    label_stock.config(text=f"{ex['name']}: {ex['open']} ~ {ex['close']}")
    label_stock.pack() 

# Loop
time()

asyncio.run(update_date())

stop_event = threading.Event()
t = threading.Thread(target=update_stocks)
t.start()


root.mainloop()


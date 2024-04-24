import tkinter as tk
import yaml
from time import strftime
from datetime import datetime
from helpers import DateTimeHelper, ExchangeHelper, TkHelper

import asyncio



BG_COLOR = "#202020"

def time():
    update_time()  

    if datetime.now().minute == 0 and datetime.now().second == 0:
        asyncio.run(update_date())

    


def update_time():    
    string = strftime('%H:%M:%S')
    label_time.config(text = string)
    label_time.after(1000, time)

async def update_date():
    label_date.config(text = f"\n{DateTimeHelper.full_date_today()}\n")


async def update_stocks():
    flag_running = False
    while True:
        if not flag_running:
            flag_running = True
            await _update_stocks()
            flag_running = False
        await asyncio.sleep(0.1)

async def _update_stocks():
    # print("Stocks...")
    for ex in exchanges:
        ex_status = ExchangeHelper.status(ex['open'], ex['close'])

        label = root.nametowidget(TkHelper.get_label_name(ex['name']))

        text_pos = ""
        if ex_status == "preclose":
            text_pos = f"|PRE CLOSE|{DateTimeHelper.format_diff_now(ex['close'])}"
            

        elif ex_status == "preopen":
            text_pos = f"|PRE OPEN|{DateTimeHelper.format_diff_now(ex['open'])}"

        text = f"{ex['name']}: {ex['open']} ~ {ex['close']} {text_pos}"



        label.config(text=text)
        # label.after(1000, time)




def load_exchanges():
    with open('./config.yml', 'r') as file:
        data = yaml.safe_load(file)
        exchanges = data['exchanges']

    return exchanges


exchanges = load_exchanges()

root = tk.Tk()
root.title("Data e Hora")
root.geometry("400x250")  
root.configure(background=BG_COLOR, highlightcolor=BG_COLOR, highlightthickness=1)


# Data
label_date = tk.Label(root, font=("Tahoma", 10, "bold"), background = BG_COLOR, foreground = "white")
label_date.config(text="\nSegunda Feira, 22 Abril, 2024\n")
label_date.pack()  # Centraliza por padrão

# Hora
label_time = tk.Label(root, font=("Tahoma", 48, "bold"), background = BG_COLOR, foreground = "white")
label_time.config(text="20:43:15")
label_time.pack()  # Centraliza por padrão


# Separador
tk.Label(root, font=("Tahoma", 10), background = BG_COLOR, foreground = "green", text="..\n").pack()


for ex in exchanges:

    ex_status = ExchangeHelper.status(ex['open'], ex['close'])

    if ex_status == "preopen" or ex_status == "preclose":
        label_stock = tk.Label(root, font=("Tahoma", 10), background = BG_COLOR, foreground = "yellow", name=TkHelper.get_label_name(ex['name']))

    elif ex_status == "close":
        label_stock = tk.Label(root, font=("Tahoma", 10), background = BG_COLOR, foreground = "white", name=TkHelper.get_label_name(ex['name']))

    else:
        label_stock = tk.Label(root, font=("Tahoma", 10), background = BG_COLOR, foreground = "green", name=TkHelper.get_label_name(ex['name']))


    label_stock.config(text=f"{ex['name']}: {ex['open']} ~ {ex['close']}")
    label_stock.pack() 


time()

asyncio.run(update_date())

# loop = asyncio.get_event_loop()
# root.after(1000, run_asyncio_loop, loop)


root.mainloop()


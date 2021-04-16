import pystray
from PIL import Image
import time
import sys
import os
from webbrowser import open
import pymsgbox

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, "resources", relative_path)

def set_duration(icon):
    global duration

    response = pymsgbox.prompt(
        text='How many seconds til your next break? ☕', 
        title='breaktime', 
        default='10')

    try: 
        duration = int(response)
    except:
        return

    icon.title = f'Timer set for {duration} seconds.'

def quit(icon):
    icon.stop()

def update(icon):
    global coffee_drank
    global start_time
    global duration

    if duration == 0:
        set_duration(icon)
        return


    if coffee_drank:
        icon.icon = Image.open(resource_path("clock.png"))
        icon.title = f'Timer set for {duration} seconds.'
        coffee_drank = False

    else:
        for i in range(duration):
            icon.icon = Image.open(resource_path("night.png"))
            icon.title = f"Stay focused! You have {duration - i} seconds left."
            time.sleep(1)

        icon.notify(" ", "Time for a break! ☕")
        icon.icon = Image.open(resource_path("coffee-break.png"))
        icon.title = "Time for a break! ☕"
        
        coffee_drank = True

def developer(icon):
    open("https://github.com/gbhand")

coffee_drank = False
duration = 0

menu = pystray.Menu(
    pystray.MenuItem(
        text=None, 
        action=update, 
        default=True, 
        visible=False),
    pystray.MenuItem(
        text="coffebreak v0.1 © gbhand", 
        action=developer),
    pystray.MenuItem(
        text="set duration", 
        action=set_duration), 
    pystray.MenuItem(
        text="quit", 
        action=quit)
    )

image = Image.open(resource_path("clock.png"))
icon = pystray.Icon("coffebreak", image, title="Get started!", menu=menu)

icon.visible = True
icon.run()
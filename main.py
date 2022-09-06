from tkinter import *
from views import *

root = Tk()
window_properties = {
    'root':root,
    'WIN_WIDTH':640,
    'WIN_HEIGHT':360,
    'THEME_DARK':'#283A73',
    'THEME_LIGHT':'#ccc',
    'DEFAULT_FONT':'montserrat',
    'DEFAULT_FONT_SIZE':10,
}

# WINDOW SETUP
root.title("DIGESJC BANK TICKETING SYSTEM")
root.iconbitmap("./Snip/bankicon.ico")
root.geometry(f"{window_properties['WIN_WIDTH']}x{window_properties['WIN_HEIGHT']}")
root.configure(bg=window_properties['THEME_LIGHT'])
root.resizable(False,False)

root = window_properties['root']
home_view(window_properties)

root.mainloop()

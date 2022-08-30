from tkinter import *

def place_center(WINDOW_WIDTH,width):
    return int((WINDOW_WIDTH-width)/2)

# GLOBAL VARIABLES
WIN_HEIGHT, WIN_WIDTH = 360, 640
HEADING = "Welcome to DIGESJC Bank"
THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
DEFAULT_FONT = 'montserrat'

# --- ROOT  VARIABLES ---
# buttons setup
BTN_WIDTH, BTN_HEIGHT = 15, 2
BTWx, BTHy = BTN_WIDTH*8, BTN_HEIGHT*8
Mx, My = place_center(WIN_WIDTH, BTN_WIDTH), place_center(WIN_HEIGHT, BTN_HEIGHT)
GAP = int((WIN_WIDTH-BTWx*3)/4)

# WINDOW SETUP
root = Tk()
root.title("DIGESJC BANK TICKETING SYSTEM")
root.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
root.resizable(False,False)
root.configure(bg=THEME_LIGHT)

# heading
Label(root,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*14),y=WIN_HEIGHT*0.2)

Button(root, text="Admin", font=f'{DEFAULT_FONT} 10', bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP, y=My)
Button(root, text="Teller", font=f'{DEFAULT_FONT} 10', bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP*2+BTWx, y=My)
Button(root, text="Customer",font=f'{DEFAULT_FONT} 10', bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP*3+BTWx*2, y=My)


root.mainloop()

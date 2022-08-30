from tkinter import *

def place_center(WINDOW_WIDTH,width):
    return int((WINDOW_WIDTH-width)/2)

    
def user_page():
    """commands for the user selection window"""

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

    Button(root, text="Admin", font=f'{DEFAULT_FONT} 10', bd=0, bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command=admin_login).place(x=GAP, y=My)
    Button(root, text="Teller", font=f'{DEFAULT_FONT} 10', bd=0, bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP*2+BTWx, y=My)
    Button(root, text="Customer",font=f'{DEFAULT_FONT} 10', bd=0, bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=BTN_HEIGHT,command='').place(x=GAP*3+BTWx*2, y=My)


    root.mainloop()


def admin_login():
    # GLOBAL VARIABLES
    WIN_HEIGHT, WIN_WIDTH = 360, 640
    HEADING = "Admin Login"
    THEME_DARK, THEME_LIGHT = '#283A73', '#ccc'
    DEFAULT_FONT = 'montserrat'

    # --- ROOT  VARIABLES ---
    # buttons setup
    BTN_WIDTH = 30
    BTWx = BTN_WIDTH*8

    # WINDOW SETUP
    root = Tk()
    root.title("DIGESJC BANK TICKETING SYSTEM")
    root.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
    root.resizable(False,False)
    root.configure(bg=THEME_LIGHT)

    Label(root,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*14),y=WIN_HEIGHT*0.2)
    
    passwordvalue = ''
    PASS_LABEL = 'Enter Password'
    Label(root, text=PASS_LABEL, font=f'{DEFAULT_FONT} 14', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*10),y=WIN_HEIGHT*0.4)
    Entry(root, textvariable=passwordvalue, font= f'{DEFAULT_FONT} 14', fg='#666', width=int(BTN_WIDTH*0.65), bd=0).place(x=place_center(WIN_WIDTH,BTWx),y=WIN_HEIGHT*0.5)
    Button(root, text="Submit",font=f'{DEFAULT_FONT} 10', bd=0, bg=THEME_DARK, fg=THEME_LIGHT, width=BTN_WIDTH, height=1,command='').place(x=place_center(WIN_WIDTH, BTWx), y=WIN_HEIGHT*0.6)

    root.mainloop()

user_page()
from tkinter import *
from Ticketing_System import teller
from gui_operations import *
from ts import *

def home_view(win_prop, frame=''):
    """layout for the home window.
      home_view is created directly in the main window. No frame is used.
      The structure is laid out here.
            - H1 heading
            - H2 heading
            - Option buttons
      NOTE: home_view create it's own frame, and the next frame for
            the next page.
    """
    
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT, DEFAULT_FONT_SIZE = win_prop['DEFAULT_FONT'], win_prop['DEFAULT_FONT_SIZE']
    
    ## FRAME SETUP
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both',expand=1)

    # HEADER TEXT (H1 & H2): Structure and placement
    HEADING = "Welcome to DIGESJC Bank"
    Label(frame,text=HEADING,
            font=f"{DEFAULT_FONT} 18 bold", 
            bg=THEME_LIGHT, 
            fg=THEME_DARK
            ).place(x=place_center(WIN_WIDTH,len(HEADING)*14),
                    y=WIN_HEIGHT*0.2)
    Label(frame,text='Select a User',
            font=f"{DEFAULT_FONT} 15", 
            bg=THEME_LIGHT, 
            fg=THEME_DARK
            ).place(x=place_center(WIN_WIDTH,len('Select a User')*10),
            y=WIN_HEIGHT*0.3)

    # BUTTONS
    ## Button varaibles
    options = ['Admin', 'Teller', 'Customer']
    ## Button design variables
    no_of_users = len(options)
    BTN_WIDTH, BTN_HEIGHT = DEFAULT_FONT_SIZE+5, 3
    GAP = int((WIN_WIDTH-BTN_WIDTH*8*no_of_users)/(no_of_users+1))
    My = place_center(WIN_HEIGHT, BTN_HEIGHT)
    
    ## Button creation: using data and design varibles
    # Admin Button
    Button(frame, 
      text=options[0], 
      font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
      bd=0, 
      bg=THEME_DARK, 
      fg=THEME_LIGHT, 
      width=BTN_WIDTH, 
      height=BTN_HEIGHT,
      command=lambda: admin_login(win_prop,frame)
      ).place(x=GAP*(0+1)+BTN_WIDTH*8*(0), y=My) 
    
    Button(frame, 
      text=options[1], 
      font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
      bd=0, 
      bg=THEME_DARK, 
      fg=THEME_LIGHT, 
      width=BTN_WIDTH, 
      height=BTN_HEIGHT,
      command=lambda: teller_login(win_prop,frame) if teller_list else ''
      ).place(x=GAP*(1+1)+BTN_WIDTH*8*(1), y=My)

    Button(frame, 
      text=options[2], 
      font=f"{DEFAULT_FONT} {DEFAULT_FONT_SIZE}", 
      bd=0, 
      bg=THEME_DARK, 
      fg=THEME_LIGHT, 
      width=BTN_WIDTH, 
      height=BTN_HEIGHT,
      command=lambda: customer_login(win_prop,frame) if teller_list else ''
      ).place(x=GAP*(2+1)+BTN_WIDTH*8*(2), y=My)


def admin_login(win_prop,preframe):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 30

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1 Heading
    HEADING = "Admin Login"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*12),y=WIN_HEIGHT*0.2)
    # password label
    PASS_LABEL = 'Enter Password'
    Label(frame, text=PASS_LABEL, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*9),y=WIN_HEIGHT*0.4)
    # password entry/input field
    Entry(frame, show='*', 
         font= f'{DEFAULT_FONT} 10', 
         fg='#666', 
         width=BTN_WIDTH, 
         bd=1).place(x=place_center(WIN_WIDTH,BTN_WIDTH*8),y=WIN_HEIGHT*0.5)
    
    # submit button
    Button(frame, text="Login",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg=THEME_DARK, 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=1,
           command=lambda: admin_panel_view(win_prop, frame)
           ).place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.6)
    ## back button
    BTN_WIDTH = BTN_WIDTH-15
    Button(frame, text="<<👈 Go Back",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg='#d4af37',
           fg=THEME_DARK,
           width=BTN_WIDTH, 
           height=1,
           command=lambda:go_back(frame,home_view, win_prop)
           ).place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.8)
    
def teller_login(win_prop,preframe):
    '''Teller frame is made up of:
      - H1 (teller login)
      - ID entry/input
      - Password entry/input
    '''
    ## FRAME SETUP
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 30

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1 Heading
    HEADING = "Teller Login"
    Label(frame,text=HEADING,font=f'{DEFAULT_FONT} 18 bold', bg=THEME_LIGHT, fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*11),y=WIN_HEIGHT*0.1)
    
    passwordvalue, teller_id = '', StringVar()
    PASS_LABEL, ID_LABLE = 'Enter Password', 'Enter Teller ID'
    ## ID field
    Label(frame, text=ID_LABLE, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(ID_LABLE)*8),y=WIN_HEIGHT*0.3)   
    Entry(frame, textvariable=teller_id, 
          font= f'{DEFAULT_FONT} 10', 
          fg='#666', 
          width=BTN_WIDTH, 
          bd=1).place(x=place_center(WIN_WIDTH,BTN_WIDTH*8),y=WIN_HEIGHT*0.4)
    ## password field
    Label(frame, text=PASS_LABEL, 
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*10),y=WIN_HEIGHT*0.5)    
    Entry(frame, textvariable=passwordvalue, show='*',
          font= f'{DEFAULT_FONT} 10', 
          fg='#666', 
          width=BTN_WIDTH, 
          bd=1).place(x=place_center(WIN_WIDTH,BTN_WIDTH*8),y=WIN_HEIGHT*0.6)
      

    ## submit button
    Button(frame, text="Login",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg=THEME_DARK, 
           fg=THEME_LIGHT, width=BTN_WIDTH, 
           height=1,
           command=lambda: serve_customer(win_prop, frame, teller_id.get()) if validate_teller(teller_id.get()) else ''
           ).place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.7)
    ## back button
    Button(frame, text="<<👈 Go Back",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg='#d4af37', 
           fg=THEME_DARK, 
           width=15, 
           height=1,
           command=lambda:go_back(frame,home_view, win_prop)
           ).place(x=place_center(WIN_WIDTH, 15*8), y=WIN_HEIGHT*0.8)
    
def customer_page(win_prop,preframe, customer_name):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH, BTN_HEIGHT = 15, 3
    GAP = int((640-BTN_WIDTH*8*3)/(3+1))
    My = place_center(WIN_HEIGHT, 3)

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    HEADING = "How May We Help You?"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK
          ).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.2)
    
    # INPUT BUTTONS
    ## Deposit Button
    Button(frame, text="Deposit", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#975318', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda:ticket_page(win_prop,frame,'Deposit', customer_name) if check_service('Deposit') else ''
           ).place(x=GAP, y=My)
    ## Withdraw button
    Button(frame, text="Withdraw", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#2468ac', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda:ticket_page(win_prop,frame,'Withdraw', customer_name) if check_service('Withdraw') else ''
           ).place(x=GAP*2+BTN_WIDTH*8, y=My)
    ## Transfer button
    Button(frame, text="Transfer",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#70f', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda:ticket_page(win_prop,frame,'Transfer', customer_name) if check_service('Transfer') else ''
           ).place(x=GAP*3+BTN_WIDTH*8*2, y=My)
    ## back button
    Button(frame, text="<<👈 Go Back",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#d4af37', 
          fg=THEME_DARK, 
          width=15, 
          height=1,
          command=lambda:go_back(frame,home_view, win_prop)
          ).place(x=place_center(WIN_WIDTH, 15*8), y=WIN_HEIGHT*0.8)


def customer_login(win_prop,preframe):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 30

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1 Heading
    HEADING = "Welcome"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*12),y=WIN_HEIGHT*0.2)
    # password label
    PASS_LABEL, customer_name = 'Enter Name', StringVar()
    Label(frame, text=PASS_LABEL,
          font=f'{DEFAULT_FONT} 14', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(PASS_LABEL)*9),y=WIN_HEIGHT*0.4)
    # password entry/input field
    Entry(frame, textvariable=customer_name,
         font= f'{DEFAULT_FONT} 10', 
         fg='#666', 
         width=BTN_WIDTH, 
         bd=1).place(x=place_center(WIN_WIDTH,BTN_WIDTH*8),y=WIN_HEIGHT*0.5)
    
    # submit button
    Button(frame, text="Next",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg=THEME_DARK, 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=1,
           command=lambda: customer_page(win_prop, frame, customer_name.get()) if customer_name.get() else ''
           ).place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.6)
    ## back button
    BTN_WIDTH = BTN_WIDTH-15
    Button(frame, text="<<👈 Go Back",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg='#d4af37',
           fg=THEME_DARK,
           width=BTN_WIDTH, 
           height=1,
           command=lambda:go_back(frame,home_view, win_prop)
           ).place(x=place_center(WIN_WIDTH, BTN_WIDTH*8), y=WIN_HEIGHT*0.8)


# ==================3rd View============== #
def ticket_page(win_prop,preframe,service='', name='', teller_id=''):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 15
    GAP = int((640-BTN_WIDTH*8*2)/(2+1))

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1
    HEADING = "Print "
    GAPy = 0.25
    dot = '.'*30 
    if service:
      typ = 'Ticket'
      HEADING = HEADING + typ
      back = home_view
      ticket_id = generate_ticket_id()
      label_content = f"\nCustomer Name: {name.title()}\nTicket ID: {ticket_id}\nService: {service}\nDate: {datetime.today().date()}"
      create_customer(name,ticket_id, service)
      Label(frame,text=service+' Ticket',
            font=f'{DEFAULT_FONT} 14', 
            bg=THEME_LIGHT, 
            fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.25)
    else:
      GAPy = 0.1
      back = serve_customer
      typ = 'Receipt'
      HEADING = HEADING + typ
      teller = return_tq(teller_id)
      customer_details = teller.dequeue()
      label_content = f"Customer Name: {customer_details[0].title()}\nService: {customer_details[2]}\nDate Issued: {datetime.today().date()}\nTeller ID: {teller_id}\nTeller Name: {teller.teller_name}"
    
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.1)
    
    Label(frame,text=label_content,
          font=f'{DEFAULT_FONT} 14',
          justify=LEFT,
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=WIN_WIDTH*0.25,y=WIN_HEIGHT*(GAPy+0.15))
    
    Button(frame, text="<<👈 Go Back",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#d4af37', 
          fg=THEME_DARK, 
          width=BTN_WIDTH, 
          height=1,
          command=lambda:go_back(frame,back, win_prop,frame) if service else serve_customer(win_prop, frame, teller_id)
          ).place(x=GAP, y=WIN_HEIGHT*0.8)

    Button(frame, text="🖨️ Print "+typ,
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg="#90e210", 
          fg=THEME_DARK, 
          width=BTN_WIDTH, 
          height=1,
          command=''
          ).place(x=GAP*2+BTN_WIDTH*8, y=WIN_HEIGHT*0.8)


def serve_customer(win_prop, preframe, teller_id):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH, BTN_HEIGHT = 15,3
    My = place_center(WIN_HEIGHT, BTN_HEIGHT)

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    ## Heading 
    HEADING = "Serve Customer"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK
          ).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.2)

    ## serve customer button
    Button(frame, 
      text='serve customer', 
      font=f"{DEFAULT_FONT} 12", 
      bd=0, 
      bg="#90e210", 
      fg=THEME_DARK, 
      width=BTN_WIDTH, 
      height=BTN_HEIGHT,
      command=lambda: ticket_page(win_prop,frame, teller_id=teller_id) if check_tq(teller_id) else ''
      ).place(x=WIN_WIDTH*0.394, y=WIN_HEIGHT*0.45) 

    ## exit button
    Button(frame, text="❌ Logout",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#910900', 
          fg=THEME_LIGHT, 
          width=15, 
          height=1,
          command=lambda:go_back(frame,home_view, win_prop)
          ).place(x=place_center(WIN_WIDTH, 15*8)-3, y=WIN_HEIGHT*0.85)

# =========== admin panel ================== #
def admin_panel_view(win_prop, preframe):
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH, BTN_HEIGHT = 18, 2
    GAP = int((640-BTN_WIDTH*8*3)/(3+1))

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1 Heading
    HEADING = "Admin Panel"
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*12)-12.5,y=WIN_HEIGHT*0.1)

    dot = '.'*10
    ## Teller Information
    HEADING = 'Teller Info'
    Label(frame,text=HEADING,
         font=f'{DEFAULT_FONT} 12 bold', 
         bg=THEME_LIGHT, 
         fg=THEME_DARK).place(x=WIN_WIDTH*0.14,y=WIN_HEIGHT*0.3)
 
    label_content = f"Total Number of Tellers: {len(teller_list)}"
    i=0
    while i< len(teller_list):
        if len(teller_list) > 3:
            break
        label_content += f"\n\n#{i+1} {teller_list[i].teller_name}: {teller_list[i].service}"
        i += 1
    if len(teller_list) >= 3:
        label_content = f"Total Number of Tellers: {len(teller_list)}\n\n#{1} {teller_list[0].teller_name}: {teller_list[1].service}\n#{2} {teller_list[1].teller_name}: {teller_list[1].service}\n#{3} {teller_list[2].teller_name}: {teller_list[2].service}"
    Label(frame,text=label_content,
          font=f'{DEFAULT_FONT} 10',
          justify=LEFT,
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=WIN_WIDTH*0.1,y=WIN_HEIGHT*0.4)
    
    ## Customer Information
    HEADING = 'Customer Info'
    Label(frame,text=HEADING,
         font=f'{DEFAULT_FONT} 12 bold', 
         bg=THEME_LIGHT, 
         fg=THEME_DARK).place(x=WIN_WIDTH*0.59,y=WIN_HEIGHT*0.3)

    label_content = f"Total Number of Customers in queue: {number_of_customers()}"
    Label(frame,text=label_content,
          font=f'{DEFAULT_FONT} 10',
          justify=LEFT,
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=WIN_WIDTH*0.55,y=WIN_HEIGHT*0.4)

    ## buttons
    ### Create Teller Queue
    Button(frame, text="Create Teller Queue", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#975318', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda: create_queue_view(win_prop, frame, 'create')
           ).place(x=GAP, y=WIN_HEIGHT*0.7)
    ### Delete Teller Queue
    def confirm_len():
      if len(teller_list) == 0:
            return ''
      else:
            return create_queue_view(win_prop, frame,'update')
    
    Button(frame, text="Reassign Teller Queue", 
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#2468ac', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command= confirm_len
           ).place(x=GAP*2+BTN_WIDTH*8, y=WIN_HEIGHT*0.7)
    ### Assign Teller
    Button(frame, text="Delete Teller",
           font=f'{DEFAULT_FONT} 10', 
           bd=0, bg='#70f', 
           fg=THEME_LIGHT, 
           width=BTN_WIDTH, 
           height=BTN_HEIGHT,
           command=lambda: create_queue_view(win_prop, frame,'delete')
           ).place(x=GAP*3+BTN_WIDTH*8*2, y=WIN_HEIGHT*0.7)
    ## back button
    Button(frame, text="❌ Logout",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#910900', 
          fg=THEME_LIGHT, 
          width=15, 
          height=1,
          command=lambda:go_back(frame,home_view, win_prop)
          ).place(x=place_center(WIN_WIDTH, 15*8)-8, y=WIN_HEIGHT*0.85)

# ========================================== #
# CREATE TELLER QUEUE => NOTICE VIEW
def create_queue_view(win_prop,preframe,crud):
    '''- name entry - service option - confirm button -  button'''
    # GLOBAL VARIABLES
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 15
    GAP = int((640-BTN_WIDTH*8*2)/(2+1))

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    teller_name = StringVar()
    selected = StringVar(frame)
    if crud == 'delete':
        action = 'Delete'
        funct = del_tq
        HEADING = "Delete a Teller Queue"
        service_option ='Select Teller'
        Label(frame, text=HEADING,font=f'{DEFAULT_FONT} 18 bold',justify=LEFT,
             bg=THEME_LIGHT,fg=THEME_DARK).place(x=WIN_WIDTH*0.34,y=WIN_HEIGHT*0.1)   
        Label(frame, text=service_option,font=f'{DEFAULT_FONT} 14',justify=LEFT,
             bg=THEME_LIGHT,fg=THEME_DARK).place(x=WIN_WIDTH*0.43,y=WIN_HEIGHT*0.3)   
        options = [teller.teller_name for teller in teller_list]
        del_tel = StringVar()
        del_tel.set('----------')
        OptionMenu(frame,del_tel,*options,).place(x=WIN_WIDTH*0.445,y=WIN_HEIGHT*0.45)

    else:
        HEADING = "Create New Teller Queue"
        action = 'Create'
        funct = create_tq
        options = ['Deposit', 'Transfer', 'Withdraw']
        if crud == 'update':
             HEADING = "Reassign Teller Queue"
             options = []
             for teller in teller_list:
                  if teller.service not in options:
                        options.append(teller.service)
             action = 'Reassign'
             funct = reassign_tq
        # H1 Heading
        Label(frame,text=HEADING,font=f'{DEFAULT_FONT} 18 bold',bg=THEME_LIGHT, 
              fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*13),y=WIN_HEIGHT*0.1)
        ## Name field
        teller_label, service_option = 'Teller Name', 'Select Service'
        Label(frame, text=teller_label, 
              font=f'{DEFAULT_FONT} 14', 
              justify=LEFT,
              bg=THEME_LIGHT, 
              fg=THEME_DARK).place(x=WIN_WIDTH*0.4,y=WIN_HEIGHT*0.3)   
        
        Entry(frame, textvariable=teller_name,
              font= f'{DEFAULT_FONT} 10', 
              fg='#666', 
              width=30, 
              bd=1).place(x=place_center(WIN_WIDTH,30*9),y=WIN_HEIGHT*0.4)
        ## service options
        Label(frame, text=service_option, 
              font=f'{DEFAULT_FONT} 14', 
              bg=THEME_LIGHT, 
              fg=THEME_DARK).place(x=WIN_WIDTH*0.4,y=WIN_HEIGHT*0.5)    
        
        selected.set(options[0])
        OptionMenu(frame, 
              selected, 
              *options,
              ).place(x=WIN_WIDTH*0.445,y=WIN_HEIGHT*0.6)  
    
    ## buttons     
    Button(frame, text="Cancel",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg='#d4af37', 
          fg=THEME_DARK, 
          width=BTN_WIDTH, 
          height=1,
          command=lambda:go_back(frame,admin_panel_view, win_prop, frame)
          ).place(x=GAP, y=WIN_HEIGHT*0.8)

    def get_id():
      if teller_name.get() == '' and action == 'Create':
            return ''      
      params = [del_tel.get() if action == 'Delete' else teller_name.get() , selected.get()]
      if action != 'Delete':
          teller_id = generate_id(teller_name.get())
          params.append(teller_id), print(params)
      notice_view(win_prop, frame, action,funct, *params)

    Button(frame, text="confirm",
          font=f'{DEFAULT_FONT} 10 bold', 
          bd=0, bg="#90e210", 
          fg=THEME_DARK, 
          width=BTN_WIDTH, 
          height=1,
          command=lambda: get_id()
          ).place(x=GAP*2+BTN_WIDTH*8, y=WIN_HEIGHT*0.8)


# notice page
def notice_view(win_prop, preframe, action, funct, *data):
    # GLOBAL VARIABLES
    funct(*data)
    root = win_prop['root']
    WIN_HEIGHT, WIN_WIDTH = win_prop['WIN_HEIGHT'], win_prop['WIN_WIDTH']
    THEME_DARK, THEME_LIGHT = win_prop['THEME_DARK'], win_prop['THEME_LIGHT']
    DEFAULT_FONT = win_prop['DEFAULT_FONT']
    BTN_WIDTH = 15
    GAP = int((640-BTN_WIDTH*8*2)/(2+1))

    ## FRAME SETUP
    preframe.pack_forget()
    frame = Frame(root, bg=THEME_LIGHT)
    frame.pack(fill='both', expand=1)

    # H1 Heading
    HEADING = action+' Teller'
    Label(frame,text=HEADING,
          font=f'{DEFAULT_FONT} 18 bold', 
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=place_center(WIN_WIDTH,len(HEADING)*12)-12.5,y=WIN_HEIGHT*0.1)

    dot = '*'*25
    print(data[0])
    if action == 'Delete':
         label_content = f"Teller {data[0].title()} has been deleted"
    else:
      label_content = f"Teller Name: {data[0].title()}\nTeller ID: {data[2]}\nService: {data[1]}"
    Label(frame,text=label_content,
          font=f'{DEFAULT_FONT} 14',
          justify=LEFT,
          bg=THEME_LIGHT, 
          fg=THEME_DARK).place(x=WIN_WIDTH*0.33,y=WIN_HEIGHT*0.35)

    ## back button
    Button(frame, text="Done",
           font=f'{DEFAULT_FONT} 10 bold', 
           bd=0, bg='#d4af37', 
           fg=THEME_DARK, 
           width=15, 
           height=1,
           command=lambda:go_back(frame,admin_panel_view, win_prop, frame)
           ).place(x=place_center(WIN_WIDTH, 15*8), y=WIN_HEIGHT*0.8)

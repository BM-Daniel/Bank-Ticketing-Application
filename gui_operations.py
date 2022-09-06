# from tkinter import *

def place_center(WINDOW_WIDTH,width):
    return int((WINDOW_WIDTH-width)/2)

def go_back(frame_1,viewfunction, win_prop, frame=''):
    '''destroys previous frame
       calls back the previous page function
    '''
    frame_1.destroy()
    return viewfunction(win_prop, frame)


# def route(value, funct, *params):
#     funct(params)
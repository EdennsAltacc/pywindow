import pywindow as pw
import time

def game_loop():
    pw.begin_drawing()
    
    bg_color = pw.Pywindow_Color(245, 245, 245, 255)
    pw.clear_background(bg_color)
    
    pw.end_drawing()

pw.init("Window", 800, 600, game_loop)
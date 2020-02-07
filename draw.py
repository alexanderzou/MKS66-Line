from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    A = y1 - y0
    B = -1 * (x1 - x0)
    m = float(A) / float(B)
    if m > 0 and m <= 1:
        #run O1
    if m > 1:
        #run O2
    if m < 0 and m >= -1:
        #run O8
    if m < -1:
        #run O7
    pass

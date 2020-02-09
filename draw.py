from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    #print('hey')
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    x = x0
    y = y0
    A = y1 - y0
    if A == 0:
        while x <= x1:
            plot(screen, color, x, y)
            x += 1
    B = -1 * (x1 - x0)
    if B == 0:
        #print('{}, {}'.format(y, y1))
        if y0 > y1:
            y = y1
            y1 = y0
        while y <= y1:
            plot(screen, color, x, y)
            y += 1
        return
    m = -1 * float(A) / float(B)
    #print('{}, {}, {}, {}, {}'.format(m, x0, y0, x1, y1))
    if m > 0 and m <= 1:
        #run O1/O5
        d = 2 * A + B
        while x <= x1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A
    if m > 1:
        #run O2/O6
        d = A + (2 * B)
        while y <= y1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B
    if m < 0 and m >= -1:
        #run O8/O4
        d = 2 * A - B
        while x <= x1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
    if m < -1:
        #run O7/O3
        d = A - (2 * B)
        while y >= y1:
            #print('{}, {}'.format(x,y))
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B
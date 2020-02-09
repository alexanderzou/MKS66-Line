from display import *
from draw import *

s = new_screen()
c = [255, 255, 255]

def negateList(lis):
    i = 0
    while i < len(lis):
        lis[i] *= -1
        i += 1

def drawIt(x, y, xLis, yLis):
    A = [x + xLis[0], y + yLis[0]]
    B = [x + xLis[1], y + yLis[1]]
    C = [x + xLis[2], y + yLis[2]]
    D = [x + xLis[3], y + yLis[3]]
    E = [x + xLis[4], y + yLis[4]]
    #print('{}, {} & {}, {}'.format(A[0], A[1], B[0], B[1]))
    if len(xLis) == 6:
        F = [x + xLis[5], y + yLis[5]]
    draw_line(A[0], A[1], B[0], B[1], s, c)
    draw_line(B[0], B[1], C[0], C[1], s, c)
    draw_line(C[0], C[1], D[0], D[1], s, c)
    draw_line(D[0], D[1], E[0], E[1], s, c)
    if len(xLis) == 5:
        draw_line(E[0], E[1], A[0], A[1], s, c)
    else:
        draw_line(E[0], E[1], F[0], F[1], s, c)
        draw_line(F[0], F[1], A[0], A[1], s, c)

#x0, y0, x1, y1, screen, color
def bigAst(x, y, o):
    xLis = [25, 50, -15, -40, 5, 30]
    yLis = [10, 40, 40, -10, -50, -25]
    if o == 2 or o == 3:
        negateList(xLis)
    if o == 4 or o == 3:
        negateList(yLis)
    drawIt(x, y, xLis, yLis)

def medAst(x, y, o):
    xLis = [15, 20, -15, -20, 0]
    yLis = [0, 20, 25, -10, -30]
    if o == 2 or o == 3:
        negateList(xLis)
    if o == 4 or o == 3:
        negateList(yLis)
    drawIt(x, y, xLis, yLis)
 
def smallAst(x, y, o):
    xLis = [10, 10, 0, -2, -12, 2]
    yLis = [-5, 5, 10, 2, -5, -10]
    if o == 2 or o == 3:
        negateList(xLis)
    if o == 4 or o == 3:
        negateList(yLis)
    drawIt(x, y, xLis, yLis)

def ship():
    global c
    draw_line(250, 250, 250, 240, s, c)
    draw_line(250, 240, 265, 265, s, c)
    draw_line(265, 265, 240, 250, s, c)
    draw_line(240, 250, 250, 250, s, c)
    
    c = [0, 255, 0]
    draw_line(270, 270, 275, 275, s, c)
    draw_line(271, 270, 276, 275, s, c)
    draw_line(280, 280, 285, 285, s, c)
    draw_line(281, 280, 286, 285, s, c)
    draw_line(290, 290, 295, 295, s, c)
    draw_line(291, 290, 296, 295, s, c)

def main():
    bigAst(100, 400, 3)
    bigAst(400, 250, 1)
    
    bigAst(60, 150, 2)
    medAst(250, 400, 1)
    medAst(150, 300, 2)
    medAst(100, 300, 3)
    medAst(450, 50, 4)
    medAst(200, 75, 2)
    
    smallAst(450, 200, 1)
    smallAst(50, 450, 2)
    smallAst(250, 50, 2)
    smallAst(350, 350, 4)
    smallAst(50, 50, 4)
    smallAst(400, 450, 1)
    smallAst(350, 200, 3)
    smallAst(150, 200, 3)
    smallAst(400, 40, 4)
    
    ship()

main()

display(s)
save_ppm_ascii(s, 'myascii.ppm')
save_extension(s, 'myimg.png')
from random import *

from pygame import *
import pygame

init()

surf = display.set_mode((1600, 900))
display.set_caption("Casino")
# display.set_icon()
run = True
global argent
argent = 10

plus5 = image.load('C:\Image\+5.png')
plus10 = image.load('C:\Image\+10.png')
fois2 = image.load('C:\Image\multi2.png')
fois3 = image.load('C:\Image\multi3.png')
divis2 = image.load('C:\Image\divis2.png')
divis3 = image.load('C:\Image\divis3.png')
vide = image.load('C:\Image\dien.png')
moin5 = image.load('C:\Image\-5.png')
moin10 = image.load('C:\Image\-10.png')

Tab_FG = [["" for k in range(53)] for i in range(53)]


def grille():
    colonne = 0
    ligne = 0
    game_grille()
    for k in range(51):
        draw.line(surf, (255, 255, 255), (colonne + 400, 50), (colonne + 400, 850), 1)
        colonne += 16
        display.flip()
    for k in range(51):
        draw.line(surf, (255, 255, 255), (400, ligne + 50), (1200, ligne + 50), 1)
        ligne += 16
        display.flip()


def game_grille():
    draw.line(surf, (255, 0, 0), (390, 0), (390, 900), 5)
    draw.line(surf, (255, 0, 0), (1210, 0), (1210, 900), 5)


def tab_grille():
    for k in range(50):
        for i in range(50):
            r = randint(0, 10)
            if r == 0:
                Tab_FG[k][i] = "0"
            if r == 1:
                Tab_FG[k][i] = "+5"
            if r == 2:
                Tab_FG[k][i] = "+10"
            if r == 3:
                Tab_FG[k][i] = "*1"
            if r == 4:
                Tab_FG[k][i] = "*2"
            if r == 5:
                Tab_FG[k][i] = "*3"
            if r == 6:
                Tab_FG[k][i] = "/1"
            if r == 7:
                Tab_FG[k][i] = "/2"
            if r == 8:
                Tab_FG[k][i] = "/3"
            if r == 9:
                Tab_FG[k][i] = "-5"
            if r == 10:
                Tab_FG[k][i] = "-10"


def impact(colonne, ligne):
    global argent
    for k in range(3):
        rep = Tab_FG[colonne - 25 + k][ligne - 3]
        if rep == "+5":
            argent = argent + 5
            surf.blit(plus5, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if rep == "+10":
            argent = argent + 10
            surf.blit(plus10, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if rep == "*2":
            argent = argent * 2
            surf.blit(fois2, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if rep == "*3":
            argent = argent * 3
            surf.blit(fois3, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if rep == "/2":
            argent = argent / 2
            surf.blit(divis2, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if rep == "/3":
            argent = argent / 3
            surf.blit(divis3, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if rep == "-5":
            argent = argent - 5
            surf.blit(moin5, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if rep == "-10":
            argent = argent - 10
            surf.blit(moin10, (1 + 16 * (colonne + k), 3 + 16 * ligne))
        if argent <= 0:
            argent = 0
        if rep == "" or rep == "/1" or rep == "*1" or rep == "0":
            surf.blit(vide, (1 + 16 * (colonne + k), 3 + 16 * ligne))
    for k in range(3):
        rep = Tab_FG[colonne - 25][ligne - 3 + k]
        if rep == "+5":
            argent = argent + 5
            surf.blit(plus5, (1 + 16 * colonne, 3 + 16 * (ligne + k)))
        if rep == "+10":
            argent = argent + 10
            surf.blit(plus10, (1 + 16 * colonne, 3 + 16 * (ligne + k)))
        if rep == "*2":
            argent = argent * 2
            surf.blit(fois2, (1 + 16 * colonne, 3 + 16 * (ligne + k)))
        if rep == "*3":
            argent = argent * 3
            surf.blit(fois3, (1 + 16 * colonne, 3 + 16 * (ligne + k)))
        if rep == "/2":
            argent = argent / 2
            surf.blit(divis2, (1 + 16 * (colonne), 3 + 16 * (ligne + k)))
        if rep == "/3":
            argent = argent / 3
            surf.blit(divis3, (1 + 16 * (colonne), 3 + 16 * (ligne + k)))
        if rep == "-5":
            argent = argent - 5
            surf.blit(moin5, (1 + 16 * (colonne), 3 + 16 * (ligne + k)))
        if rep == "-10":
            argent = argent - 10
            surf.blit(moin10, (1 + 16 * (colonne), 3 + 16 * (ligne + k)))
        if argent <= 0:
            argent = 0
        if rep == "" or rep == "/1" or rep == "*1" or rep == "0":
            surf.blit(vide, (1 + 16 * (colonne), 3 + 16 * (ligne + k)))
    for k in range(3):
        rep = Tab_FG[colonne - 25 - k][ligne - 3]
        if rep == "+5":
            argent = argent + 5
            surf.blit(plus5, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if rep == "+10":
            argent = argent + 10
            surf.blit(plus10, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if rep == "*2":
            argent = argent * 2
            surf.blit(fois2, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if rep == "*3":
            argent = argent * 3
            surf.blit(fois3, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if rep == "/2":
            argent = argent / 2
            surf.blit(divis2, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if rep == "/3":
            argent = argent / 3
            surf.blit(divis3, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if rep == "-5":
            argent = argent - 5
            surf.blit(moin5, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if rep == "-10":
            argent = argent - 10
            surf.blit(moin10, (1 + 16 * (colonne - k), 3 + 16 * ligne))
        if argent <= 0:
            argent = 0
        if rep == "" or rep == "/1" or rep == "*1" or rep == "0":
            surf.blit(vide, (1 + 16 * (colonne - k), 3 + 16 * ligne))
    for k in range(3):
        rep = Tab_FG[colonne - 25][ligne - 3 - k]
        if rep == "+5":
            argent = argent + 5
            surf.blit(plus5, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if rep == "+10":
            argent = argent + 10
            surf.blit(plus10, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if rep == "*2":
            argent = argent * 2
            surf.blit(fois2, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if rep == "*3":
            argent = argent * 3
            surf.blit(fois3, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if rep == "/2":
            argent = argent / 2
            surf.blit(divis2, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if rep == "/3":
            argent = argent / 3
            surf.blit(divis3, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if rep == "-5":
            argent = argent - 5
            surf.blit(moin5, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if rep == "-10":
            argent = argent - 10
            surf.blit(moin10, (1 + 16 * (colonne), 3 + 16 * (ligne - k)))
        if argent <= 0:
            argent = 0
        if rep == "" or rep == "/1" or rep == "*1" or rep == "0":
            surf.blit(vide, (1 + 16 * colonne, 3 + 16 * (ligne - k)))
    print(argent)
    screen_argent = font.SysFont("Comic Sans MS", 30).render("Argent : {0}".format(int(argent)), 1, (100, 100, 100))


def first_game():
    global argent
    surf.fill((80, 80, 80))

    Impact_Point = 0
    run2 = True
    RED = Color(255, 0, 0)
    tab_grille()
    grille()
    print(Tab_FG)
    while run2:

        draw.rect(surf, (0, 0, 0), (0, 0, 380, 900))
        draw.rect(surf, (0, 0, 0), (1220, 0, 400, 900))
        screen_argent = font.SysFont("Comic Sans MS", 30).render("Argent : {0}".format(int(argent)), 1, (100, 100, 100))
        surf.blit(screen_argent, Rect(50, 300, 100, 50))
        display.flip()

        for events in event.get():
            if events.type == QUIT:
                run2 = False
                run = False
            if mouse.get_pressed() == (1, 0, 0):
                pos = mouse.get_pos()
                colonne = pos[0] // 16
                ligne = pos[1] // 16
                Tab_FG[colonne - 25][ligne - 3] = "Impact Point"
                Impact_Point += 1
                draw.rect(surf, RED, (1 + 16 * colonne, 3 + 16 * ligne, 15, 15))
                display.flip()
                impact(colonne, ligne)


grille()

while run:

    for events in event.get():
        if events.type == KEYDOWN and events.key == K_ESCAPE:
            run = False
        if events.type == QUIT:
            run = False
        if events.type == KEYDOWN and events.key == K_UP:
            first_game()

quit()


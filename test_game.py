# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_game.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ryoma <ryoma@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/02 14:08:28 by ryoma             #+#    #+#              #
#    Updated: 2023/11/02 14:08:29 by ryoma            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pygame as pg, sys
import random

pg.init()
screen = pg.display.set_mode((800, 600))

barrect = pg.Rect(400, 500, 100, 20)

ballimg = pg.image.load("images/kaeru.png")
ballimg = pg.transform.scale(ballimg, (30, 30))
ballrect = pg.Rect(400, 450, 30, 30)
vx = random.randint(-10, 10)
vy = -5

replay_img = pg.image.load("images/replaybtn.png")
pushFlag = False
page = 1

def button_to_jump(btn, newpage):
    global page, pushFlag
    mdown = pg.mouse.get_pressed()
    (mx, my) = pg.mouse.get_pos()
    if mdown[0]:
        if btn.collidepoint((mx, my)) and pushFlag == False:
            pg.mixer.Sound("sounds/pi.wav").play()
            page = newpage
            pushFlag = True
        else:
            pushFlag = False

    
def gamestage():
    global vx, vy
    global page

    screen.fill(pg.Color("NAVY"))

    (mx, my) = pg.mouse.get_pos()

    barrect.x = mx - 50
    pg.draw.rect(screen, pg.Color("CYAN"), barrect)

    if ballrect.y < 0:
        vy = -vy
    if ballrect.x < 0 or ballrect.x > 800 -30:
        vx = -vx
    if barrect.colliderect(ballrect):
        vx = ((ballrect.x + 15) - (barrect.x + 50)) / 4
        vy = random.randint(-10, -5)
        pg.mixer.Sound("sounds/pon.wav").play()
    ballrect.x += vx
    ballrect.y += vy
    screen.blit(ballimg, ballrect)

    if ballrect.y > 600:
        page = 2
        pg.mixer.Sound("sounds/down.wav").play()

def gamereset():
    global vx, vy
    vx = random.randint(-10, 10)
    vy = -5
    ballrect.x = 400
    ballrect.y = 450

def gameover():
    gamereset()
    screen.fill(pg.Color("NAVY"))
    font = pg.font.Font(None, 150)
    text = font.render("GAME OVER", True, pg.Color("RED"))
    screen.blit(text, (100, 200))
    btn1 = screen.blit(replay_img, (320, 480))
    button_to_jump(btn1, 1)

while True:
    if page == 1:
        gamestage()
    elif page == 2:
        gameover()
    pg.display.update()
    pg.time.Clock().tick(60)
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                sys.exit()
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
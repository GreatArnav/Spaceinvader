import pygame as py
from threading import Timer
from random import randint
from math import sqrt, pow
from time import sleep

py.init()

# Creating game window
X = 800
Y = 700
window = py.display.set_mode((X, Y))

over = False
intro = True
running = False
game = True
pause = False
while game:
    # caption and logo
    py.display.set_caption('SPACE INVEDER')
    py.display.set_icon(py.image.load('ufo1.png'))

    # song ,score, font and pause
    py.mixer.music.load('bg_song.wav')
    py.mixer.music.play(-1)
    # score and game over
    white = (255, 255, 255)
    score = 0
    font = py.font.Font('freesansbold.ttf', 32)
    font1 = py.font.Font('freesansbold.ttf', 42)
    game_over = py.transform.scale(py.image.load('game over.jpg'), (800, 700))
    end_line = py.transform.scale(py.image.load('end_linu.png'), (800, 10))
    start = py.transform.scale(py.image.load('start.png'), (800, 700))
    pause_img = py.transform.scale(py.image.load('pause.png'),(800,700))

    # Spaceship
    rocket = py.transform.scale(py.image.load('spaceship.png'), (60, 60))
    rocket_X = 380
    rocket_Y = 600
    vel_x = 0
    vel_y = 0
    vel = 20


    def rocket_move(x, y):
        window.blit(rocket, (x, y))


    # spaceship fire
    fire = py.transform.scale(py.image.load('fire.png'), (25, 50))
    fire_x = rocket_X
    fire_y = rocket_Y
    fire_vel = 0
    fire_x2 = rocket_Y


    def rocket_fire(x, y):
        window.blit(fire, (x, y))


    # UFO1
    ufo1 = py.transform.scale(py.image.load('ufo1.png'), (80, 80))
    ufo1_x = randint(10, 730)
    ufo1_y = randint(10, 380)
    ufo1_vel = 10


    def ufo1_move(x, y):
        window.blit(ufo1, (x, y))


    # UFO2
    ufo2 = py.transform.scale(py.image.load('ufo2.png'), (70, 70))
    ufo2_x = randint(10, 730)
    ufo2_y = randint(10, 380)
    ufo2_vel = 20


    def ufo2_move(x, y):
        window.blit(ufo2, (x, y))


    # UFO 3

    ufo3_x = randint(10, 730)
    ufo3_y = randint(10, 380)
    ufo3_vel = 20

    # ufo 4


    ufo4_x = randint(10, 730)
    ufo4_y = randint(10, 380)
    ufo4_vel = 10
    # ufo5
    ufo5_x = randint(10, 730)
    ufo5_y = randint(10, 450)
    ufo5_vel = 20
    ufo5_changey = 30
    ufo5_changex = 20

    # ufo6
    ufo6_x = randint(10, 730)
    ufo6_y = randint(10, 450)
    ufo6_vel = 10
    ufo6_changey = 30
    ufo6_changex = 20
    # Collosion

    # explosion
    explosion1 = py.transform.scale(py.image.load('explosion.png'), (100, 100))
    explosion2 = py.transform.scale(py.image.load('explosion1.png'), (100, 100))


    def explode1(x, y):
        window.blit(explosion1, (x, y))


    def explode2(x, y):
        window.blit(explosion2, (x, y))


    def collision(enemyX, enemyY, fireX, fireY):
        distance = sqrt(pow(enemyX - fireX, 2) + pow(fireY - enemyY, 2))
        if distance <= 50:
            return True
        else:
            return False


    while intro:
        window.blit(start, (0, 0))
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                game = False
                over = False
                intro = False
                pause = False

            if event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    running = True
                    intro = False
        py.display.update()
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                game = False
                over = False
                intro = False
                pause = False
            # movement of spaceship
            if event.type == py.KEYDOWN:
                if event.key == py.K_LEFT or event.key == py.K_KP4:
                    vel_x -= vel
                if event.key == py.K_RIGHT or event.key == py.K_KP6:
                    vel_x += vel
                if event.key == py.K_KP0 or event.key == py.K_SPACE:
                    fire_vel = 80
                    laser_sound=py.mixer.Sound('laser.wav')
                    laser_sound.play()


            if event.type == py.KEYUP:
                if event.key == py.K_UP or event.key == py.K_DOWN or event.key == py.K_LEFT or event.key == py.K_RIGHT or event.key == py.K_KP8 or event.key == py.K_KP2 or event.key == py.K_KP6 or event.key == py.K_KP4:
                    vel_x = 0
                    vel_y = 0
        window.blit(py.image.load('background.jpg'), (0, 0))
        window.blit(font.render("score-" + str(score), True, white), (2, 2))
        window.blit(font.render("", True, white), (2, 2))

        # laser move
        if fire_y <= 0:
            fire_y = rocket_Y
            fire_vel = 0
        if rocket_Y != fire_x2:
            fire_y = rocket_Y
            fire_x2 = rocket_Y
        fire_y -= fire_vel
        rocket_fire(rocket_X + 19, fire_y)

        # Collision
        # shoot ufo1
        collision_ufo1 = collision(ufo1_x, ufo1_y, rocket_X + 19, fire_y)
        if collision_ufo1:
            explode_sound = py.mixer.Sound('explosion.wav')
            explode_sound.play()
            explode1(ufo1_x, ufo1_y)
            score += 10
            ufo1_x = randint(10, 730)
            ufo1_y = randint(10, 380)
            ufo1_move(ufo1_x, ufo1_y)
        # shoot ufo2
        collision_ufo2 = collision(ufo2_x, ufo2_y, rocket_X + 19, fire_y)
        if collision_ufo2:
            explode_sound = py.mixer.Sound('explosion.wav')
            explode_sound.play()
            explode2(ufo2_x, ufo2_y)
            score += 20
            ufo2_x = randint(10, 730)
            ufo2_y = randint(10, 350)
            ufo2_move(ufo2_x, ufo2_y)






        # rocket moves
        rocket_X += vel_x
        rocket_Y -= vel_y
        rocket_move(rocket_X, rocket_Y)

        # bounders of rocket
        if rocket_X <= 0:
            rocket_X = 0
        elif rocket_X >= 730:
            rocket_X = 730

        if rocket_Y <= 0:
            rocket_Y = 0
        elif rocket_Y >= 600:
            rocket_Y = 600

        # ufos moving
        # ufo
        if ufo1_x >= 730:
            ufo1_vel = -10
            ufo1_y += 20
            ufo1_x += ufo1_vel
        elif ufo1_x <= 10:
            ufo1_vel = 10
            ufo1_y += 20
            ufo1_x += ufo1_vel
        ufo1_x += ufo1_vel
        ufo1_move(ufo1_x, ufo1_y)

        # ufo2
        if ufo2_x >= 730:
            ufo2_vel = -20
            ufo2_y += 35
            ufo2_x += ufo2_vel
        elif ufo2_x <= 10:
            ufo2_vel = 20
            ufo2_y += 35
            ufo2_x += ufo2_vel
        ufo2_x += ufo2_vel
        ufo2_move(ufo2_x, ufo2_y)

        # MORE UFOS
        if score >= 100:
            if ufo3_x >= 730:
                ufo3_vel = -20
                ufo3_y += 35
                ufo3_x += ufo3_vel
            elif ufo3_x <= 10:
                ufo3_vel = 20
                ufo3_y += 35
                ufo3_x += ufo3_vel
            ufo3_x += ufo3_vel
            ufo2_move(ufo3_x, ufo3_y)

            # shoot ufo3
            collision_ufo3 = collision(ufo3_x, ufo3_y, rocket_X + 19, fire_y)
            if collision_ufo3:
                explode_sound = py.mixer.Sound('explosion.wav')
                explode_sound.play()
                explode2(ufo3_x, ufo3_y)
                score += 20
                ufo3_x = randint(10, 730)
                ufo3_y = randint(10, 350)
                ufo2_move(ufo3_x, ufo3_y)
        if score >= 200:
            if ufo4_x >= 730:
                ufo4_vel = -10
                ufo4_y += 20
                ufo4_x += ufo4_vel
            elif ufo4_x <= 10:
                ufo4_vel = 10
                ufo4_y += 20
                ufo4_x += ufo4_vel
            ufo4_x += ufo4_vel
            ufo1_move(ufo4_x, ufo4_y)
            # shoot ufo4
            collision_ufo4 = collision(ufo4_x, ufo4_y, rocket_X + 19, fire_y)
            if collision_ufo4:
                explode_sound = py.mixer.Sound('explosion.wav')
                explode_sound.play()
                explode1(ufo4_x, ufo4_y)
                score += 10
                ufo4_x = randint(10, 730)
                ufo4_y = randint(10, 350)
                ufo1_move(ufo4_x, ufo4_y)

        if score >= 500:
            if ufo5_x >= 730:
                ufo5_vel = -ufo5_changex
                ufo5_y += ufo5_changey
                ufo5_x += ufo5_vel
            elif ufo5_x <= 10:
                ufo5_vel = ufo5_changex
                ufo5_y += ufo5_changey
                ufo5_x += ufo5_vel
            ufo5_x += ufo5_vel
            ufo2_move(ufo5_x, ufo5_y)

            # shoot ufo5
            collision_ufo5 = collision(ufo5_x, ufo5_y, rocket_X + 19, fire_y)
            if collision_ufo5:
                explode_sound = py.mixer.Sound('explosion.wav')
                explode_sound.play()
                explode2(ufo5_x, ufo5_y)
                score += 20
                ufo5_x = randint(10, 730)
                ufo5_y = randint(10, 350)
                ufo2_move(ufo5_x, ufo5_y)
            if ufo6_x >= 730:
                ufo6_vel = -ufo6_changex
                ufo6_y += ufo6_changey
                ufo6_x += ufo6_vel
            elif ufo6_x <= 10:
                ufo6_vel = ufo6_changex
                ufo6_y += ufo6_changey
                ufo6_x += ufo6_vel
            ufo6_x += ufo6_vel
            ufo2_move(ufo6_x, ufo6_y)

            # shoot ufo 6
            collision_ufo6 = collision(ufo6_x, ufo6_y, rocket_X + 19, fire_y)
            if collision_ufo6:
                explode_sound = py.mixer.Sound('explosion.wav')
                explode_sound.play()
                explode1(ufo6_x, ufo6_y)
                score += 20
                ufo6_x = randint(10, 730)
                ufo6_y = randint(10, 350)
                ufo2_move(ufo6_x, ufo6_y)
        if score >= 700:
            ufo6_changex = 50
            ufo6_changey = 50
            ufo5_changex = 50
            ufo5_changey = 50
        window.blit(end_line, (0, 560))
        if ufo1_y >= 520 or ufo2_y >= 520 or ufo3_y >= 520 or ufo4_y >= 520 or ufo5_y >= 520 or ufo6_y >= 520:
            over = True
            running = False
        py.display.update()


    while over:
        window.blit(game_over, (0, 0))
        window.blit(font1.render("Your score-" + str(score), True, white), (250, 100))
        window.blit(font1.render("Press Enter to Retry", True, white), (195, 600))
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
                game = False
                over = False
                intro = False
                pause = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_RETURN:
                    score = 0
                    running = True
                    over = False
        py.display.update()
    py.display.update()


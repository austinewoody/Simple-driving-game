import pygame
import random
import time

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("driving-in-a-car-6227.mp3")
pygame.mixer.music.play(-1)

SCREEN_WIDTH = 1131
SCREEN_HEIGHT = 700

edge_x1 = 230
edge_x2 = 810

background1_x = 0
background1_y = 0

character_x = edge_x1
character_y = 500

car1_x = 200
car1_y = 0
car2_x = 600
car2_y = 200

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Driving Game")

BACKGROUND1 = pygame.image.load("Road_image.jpg")

CHARACTER = pygame.image.load("your_car.png")

character_life = 20

CAR1 = pygame.image.load("other_car_1.png")
CAR2 = pygame.image.load("other_car2.png")

font = pygame.font.Font(None, 50)

small_font = pygame.font.Font(None, 25)

music_text = font.render("Press m to play or stop music", True, "black")
speed_text = font.render("Press up key to increase speed", True, "black")
brake_text = font.render("Press down key to brake", True, "black")
character_life_text = font.render(f"Health: {character_life}", True, "green")

wy_clef = "playing Wy_clef_Jean_Fast_Car........"
boy_breed = "playing Boy_breed_Sha_kara........"
_50cent = "playing 50 Cent-P.I.M.P........"
back_street_boys = "playing Drowning In Your Love........"
c_dion = "playing That's The Way it is........"

start_time = time.time()
elapsed_time = 0

running = True

game_start = True

speed = 20
brake = 20

play_music = True
music_playing = True

show_wy_clef = False
show_50_cent = False
show_boy_breed = False
show_back_street_boys = False
show_c_dion = False

braking = True


def start_game():
    started = True
    start_font = pygame.font.Font(None, 200)
    start_text = start_font.render("START GAME", True, "black")

    small_start_font = pygame.font.Font(None, 80)
    start_t = small_start_font.render("Press s to start game", True, "black")

    while started:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_s:
                    started = False

        screen.fill("white")
        screen.blit(start_text, (50, 200))
        screen.blit(start_t, (100, 400))

        screen.blit(music_text, (0, 0))
        screen.blit(speed_text, (0, 30))
        screen.blit(brake_text, (0, 60))
        screen.blit(font.render("press p to pause", True, "black"), (0, 90))

        pygame.display.update()
        pygame.mixer.music.pause()


def pause():
    paused = True
    pause_font = pygame.font.Font(None, 200)
    pause_text = pause_font.render("GAME PAUSED", True, "black")

    while paused:
        for events in pygame.event.get():
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_c:
                    paused = False

        screen.fill("white")
        screen.blit(pause_text, (50, 200))
        screen.blit(font.render("press c to continue", True, "black"), (50, 400))
        pygame.display.update()
        pygame.mixer.music.pause()


start_game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pause()

    elapsed_time = time.time() - start_time

    character_rect = CHARACTER.get_rect(topleft=(character_x, character_y))

    car1_rect = CAR1.get_rect(topleft=(car1_x, car1_y))
    car2_rect = CAR2.get_rect(topleft=(car2_x, car2_y))

    if character_rect.colliderect(car1_rect):
        car1_x = random.randint(edge_x1, edge_x2)
        car1_y = - 10
        character_life -= 1
        character_life_text = font.render(f"Health: {character_life}", True, "green")
    elif character_rect.colliderect(car2_rect):
        car2_x = 500
        car2_y = - 800
        character_life -= 1
        character_life_text = font.render(f"Health: {character_life}", True, "green")
    elif character_life == 0:
        font = pygame.font.Font(None, 100)
        screen.blit(font.render("GAME OVER", True, "red"), (350, 200))
        pygame.display.update()
        #time.sleep(5)
        #running = False
    car1_y += speed
    car2_y += speed - 10

    if car1_y + CAR1.get_height() > SCREEN_HEIGHT:
        car1_x = random.randint(edge_x1, edge_x2)
        car1_y = - 10

    elif car2_y + CAR2.get_height() > SCREEN_HEIGHT:
        car2_x = 500
        car2_y = - 800

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and character_x > edge_x1:
        character_x -= 40
    elif keys[pygame.K_RIGHT] and character_x < edge_x2:
        character_x += 40
    elif keys[pygame.K_UP]:
        speed += 5
    elif keys[pygame.K_DOWN]:
        if braking:
            speed -= brake
            if speed < 20:
                speed = 20
            if music_playing:
                pygame.mixer.music.load("brake-6315.mp3")
                pygame.mixer.music.play()
            braking = False
        else:
            if music_playing:
                pygame.mixer.music.load("driving-in-a-car-6227.mp3")
                pygame.mixer.music.play(-1)
            braking = True
    elif keys[pygame.K_m]:
        if play_music:
            pygame.mixer.music.load("Wyclef_Jean_Fast_Car.mp3")
            pygame.mixer.music.play(-1)
            show_wy_clef = True
            play_music = False
            music_playing = False
        else:
            pygame.mixer.music.load("driving-in-a-car-6227.mp3")
            pygame.mixer.music.play(-1)
            play_music = True
            music_playing = True
            show_wy_clef = False
            show_50_cent = False
            show_boy_breed = False
            show_back_street_boys = False
            show_c_dion = False
    elif keys[pygame.K_1]:
        pygame.mixer.music.load("50 Cent-P.I.M.P.mp3")
        pygame.mixer.music.play(-1)
        music_playing = False
        show_50_cent = True
        show_wy_clef = False
        show_boy_breed = False
        show_back_street_boys = False
        show_c_dion = False
    elif keys[pygame.K_2]:
        pygame.mixer.music.load("Boybreed - Shakara.mp3")
        pygame.mixer.music.play(-1)
        music_playing = False
        show_boy_breed = True
        show_50_cent = False
        show_wy_clef = False
        show_back_street_boys = False
        show_c_dion = False
    elif keys[pygame.K_3]:
        pygame.mixer.music.load("Backstreet Boys - Drowning In Your Love.mp3")
        pygame.mixer.music.play(-1)
        music_playing = False
        show_back_street_boys = True
        show_50_cent = False
        show_wy_clef = False
        show_boy_breed = False
        show_c_dion = False
    elif keys[pygame.K_4]:
        pygame.mixer.music.load("CELINE DION- That's The W.mp3")
        pygame.mixer.music.play(-1)
        music_playing = False
        show_c_dion = True
        show_50_cent = False
        show_wy_clef = False
        show_boy_breed = False
        show_back_street_boys = False

    screen.blit(BACKGROUND1, (background1_x, background1_y))
    screen.blit(CHARACTER, (character_x, character_y))
    screen.blit(CAR1, (car1_x, car1_y))
    screen.blit(CAR2, (car2_x, car2_y))
    screen.blit(character_life_text, (800, 0))
    screen.blit(font.render(f"Time: {round(elapsed_time, 2)}seconds", True, "red"), (10, 10))

    if show_wy_clef:
        screen.blit(small_font.render(wy_clef, True, "black"), (500, 500))
        pygame.display.update()
    elif show_50_cent:
        screen.blit(small_font.render(_50cent, True, "black"), (500, 500))
        pygame.display.update()
    elif show_boy_breed:
        screen.blit(small_font.render(boy_breed, True, "black"), (500, 500))
        pygame.display.update()
    elif show_back_street_boys:
        screen.blit(small_font.render(back_street_boys, True, "black"), (500, 500))
        pygame.display.update()
    elif show_c_dion:
        screen.blit(small_font.render(c_dion, True, "black"), (500, 500))
        pygame.display.update()

    pygame.time.Clock().tick(10)
    pygame.mixer.music.unpause()
    pygame.display.update()

pygame.mixer.music.stop()

pygame.quit()
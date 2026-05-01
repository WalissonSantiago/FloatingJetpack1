import pygame as pg
import sys

from settings import *
from player import Player
from obstacle import Obstacle
from menu import main_menu, game_over_screen

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Floating Jetpack")

clock = pg.time.Clock()
font = pg.font.SysFont("Arial", 50)


# carregar assets

menu_bg = pg.image.load("assets/images/menu_bg.png")
menu_bg = pg.transform.scale(menu_bg, (WIDTH, HEIGHT))

player_img = pg.image.load("assets/images/player.png").convert_alpha()

rect = player_img.get_rect()

scale_factor = 0.08

player_img = pg.transform.scale(
    player_img,
    (int(rect.width * scale_factor), int(rect.height * scale_factor))
)


obs1_top = pg.image.load("assets/images/obs1_top.png")
obs1_top = pg.transform.scale(obs1_top, (80, 300))

obs1_bottom = pg.image.load("assets/images/obs1_bottom.png")
obs1_bottom = pg.transform.scale(obs1_bottom, (80, 300))

obs2_top = pg.image.load("assets/images/obs2_top.png")
obs2_top = pg.transform.scale(obs2_top, (80, 300))

obs2_bottom = pg.image.load("assets/images/obs2_bottom.png")
obs2_bottom = pg.transform.scale(obs2_bottom, (80, 300))


background = pg.image.load("assets/images/background.png")
background = pg.transform.scale(background, (WIDTH, HEIGHT))



def run_game():
    pg.event.clear()
    player = Player(player_img)

    obstacles = []
    spawn_timer = 0
    score = 0

    while True:
        clock.tick(FPS)
        spawn_timer += 1

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        keys = pg.key.get_pressed()
        player.update(keys)

        level = 1 + score // 10

        images = [obs1_top, obs1_bottom] if level == 1 else [obs2_top, obs2_bottom]


        obstacle_speed = OBSTACLE_SPEED + (level - 1)
        spawn_time = max(50, SPAWN_TIME - (level * 5))
        gap = max(160, OBSTACLE_GAP - (level * 8))


        #spawn dos obstáculos
        if spawn_timer > spawn_time:
            obstacles.append(Obstacle(800, images, obstacle_speed, gap))
            spawn_timer = 0

        screen.blit(background, (0, 0))
        player.draw(screen)

        for obs in obstacles:
            obs.update()
            obs.draw(screen)

            #colisão
            if player.rect.colliderect(obs.top_rect) or player.rect.colliderect(obs.bottom_rect):
                return score

            #pontuação
            if not obs.passed and obs.top_rect.right < player.rect.left:
                score += 1
                obs.passed = True

        obstacles = [o for o in obstacles if not o.is_off_screen()]

        #limite tela
        if player.rect.top <= 0 or player.rect.bottom >= HEIGHT:
            return score

        #hud
        screen.blit(font.render(f"Pontos: {score}", True, (0, 0, 0)), (10, 10))
        screen.blit(font.render(f"Level: {level}", True, (0, 0, 0)), (10, 60))

        pg.display.update()


#menu loop
while True:
    main_menu(screen, font, menu_bg)
    final_score = run_game()
    game_over_screen(screen, font, final_score)
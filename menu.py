import pygame as pg
import sys

from settings import WIDTH, HEIGHT


def main_menu(screen, font, background):
    pg.mixer.music.load("assets/sounds/menu_music.mp3")
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(-1)

    while True:
        screen.blit(background, (0, 0))

        # textos
        title = font.render("Floating Jetpack", True, (255,255,255))
        play = font.render("SPACE - Jogar", True, (255,255,255))
        exit_text = font.render("ESC - Sair", True, (255,255,255))

        screen.blit(title, title.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100)))
        screen.blit(play, play.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 20)))
        screen.blit(exit_text, exit_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 80)))

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()


def game_over_screen(screen, font, score):
    pg.mixer.music.load("assets/sounds/game_music.mp3")
    pg.mixer.music.set_volume(0.1)
    pg.mixer.music.play(-1)

    while True:
        screen.fill((0, 0, 0))

        #score
        text1 = font.render(f"GAME OVER - Pontuação: {score}", True, (255,255,255))
        rect1 = text1.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 40))
        screen.blit(text1, rect1)

        #restart
        text2 = font.render("SPACE - Voltar ao menu", True, (255,255,255))
        rect2 = text2.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 40))
        screen.blit(text2, rect2)

        pg.display.update()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    return
#!/usr/bin/env python3
import pygame
from time import sleep
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
import game_functions as g_f


def run_game():
    pygame.init()                                                    # inicjalizacja gry i utworzenie obiektu ekranu
    settings_obj = Settings()
    ship_obj = Ship(settings_obj)
    stats = GameStats(settings_obj)
    # clock = pygame.time.Clock()                                 # inicjalizacja zegara by ustalić FPS
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.load('sounds/soundtrack.mp3')
    pygame.mixer.music.play(-1)
    bullets = Group()                               # inicjalizacja grupy pociskow
    aliens = Group()                                # inicjalizacja grupy obcych
    play_button = Button(settings_obj, 'Play')
    break_time = 0
    g_f.create_fleet(settings_obj, aliens, ship_obj.rect.height)

    pygame.mouse.set_visible(False)
    #while True:
    #    """inicjalizacja ekranu startowego"""


    # wyswietlenie ekranu przed rozpoczeciem gry
    ship_obj.center_ship()
    g_f.update_screen(ship_obj, settings_obj, bullets, aliens, stats, play_button)

    sleep(1)

    while True:
        # petla glowna
        fps = settings_obj.clock.tick(60)
        g_f.check_events(ship_obj, settings_obj, bullets, play_button, stats, aliens)
        if stats.game_active:
            ship_obj.update(fps)
            break_time = g_f.update_bullets(bullets, aliens, settings_obj, ship_obj.rect.height, break_time)
            g_f.update_aliens(aliens, settings_obj, ship_obj, stats, bullets)

        g_f.update_screen(ship_obj, settings_obj, bullets, aliens, stats, play_button)


run_game()

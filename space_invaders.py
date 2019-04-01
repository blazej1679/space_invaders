#!/usr/bin/env python3
import pygame
from time import sleep
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from button import Button
from start_screen import StartScreen
import game_functions as g_f


def run_game():
    pygame.init()                                                    # inicjalizacja gry i utworzenie obiektu ekran
    settings_obj = Settings()

    ship_obj = Ship(settings_obj)
    stats = GameStats(settings_obj)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.load('sounds/soundtrack.mp3')
    pygame.mixer.music.play(-1)
    bullets = Group()                               # inicjalizacja grupy pociskow
    aliens = Group()                                # inicjalizacja grupy obcych
    play_button = Button(settings_obj, 'Play', settings_obj.bg_rect.centerx, settings_obj.bg_rect.centery)
    entry_button = Button(settings_obj, 'Play', 1000, 500)
    break_time = 0
    g_f.create_fleet(settings_obj, aliens, ship_obj.rect.height)
    sc_brd = Scoreboard(settings_obj, stats)

    start_scr_obj = StartScreen(settings_obj, entry_button)

    # inicjalizacja ekranu startowego
    start_scr_obj.run_start_screen()

    pygame.mouse.set_visible(False)
    # wyswietlenie ekranu przed rozpoczeciem gry
    ship_obj.center_ship()
    g_f.update_screen(ship_obj, settings_obj, bullets, aliens, stats, play_button, sc_brd)
    sleep(1)

    while True:
        # petla glowna
        fps = settings_obj.clock.tick(60)
        g_f.check_events(ship_obj, settings_obj, bullets, play_button, stats, aliens)
        if stats.game_active:
            ship_obj.update(fps)
            break_time = g_f.update_bullets(bullets, aliens, settings_obj, ship_obj.rect.height, break_time, stats, sc_brd)
            g_f.update_aliens(aliens, settings_obj, ship_obj, stats, bullets)

        g_f.update_screen(ship_obj, settings_obj, bullets, aliens, stats, play_button, sc_brd)


run_game()

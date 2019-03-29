import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ship, bullets, settings):
    """Reakcja na naciśnięcie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(settings, ship, bullets)
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    """Reakcja na puszczenie klawisza"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def fire_bullet(settings, ship, bullets):
    if len(bullets) < settings.amount_allowed_bullets:
        new_bullet = Bullet(settings, ship)
        bullets.add(new_bullet)


def check_events(ship, settings, bullets, play_button, stats, aliens):
    """Odpowedzi gry na bodzce zewnetrzne."""
    for event in pygame.event.get():  # oczekiwanie akcji
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, bullets, settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(settings, stats, play_button, mouse_x, mouse_y, aliens, ship, bullets)


def check_play_button(settings, stats, play_button, mouse_x, mouse_y, aliens, ship, bullets):
    """Rozpoczecie nowej gry po kliknieciu przycisk Play"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True

        # czyszczenie pociskow i pociskow
        aliens.empty()
        bullets.empty()

        # wysrodkowanie statku i tworzenie nowej floty
        create_fleet(settings, aliens, ship.rect.height)
        ship.center_ship()


def update_screen(ship, settings, bullets, aliens, stats, play_button):
    """Uakualnianie obrazu gry"""
    settings.blit_bg()
    for bullet in bullets.sprites():
        bullet.blit_bullet()
    ship.blitme()
    aliens.draw(settings.screen)
    #stats.blit_scores()

    if not stats.game_active:
        play_button.draw_button()

    # wyswietlanie ostatnio zmodyfikowanego ekranu
    pygame.display.flip()


def update_bullets(bullets, aliens, settings, ship_height, break_time):
    """Obsługa polozenia i ilosci pociskow"""
    bullets.update()
    # usuniecie zbednych pociskow

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # sprawdzenie, czy jakikolwiek pocisk trafil jakiegokolwiek obcego
    break_time = check_bullet_alien_collision(settings, ship_height, aliens, bullets, break_time)

    return break_time


def check_bullet_alien_collision(settings, ship_height, aliens, bullets, break_time):
    """ Reakcja na kolizje obcego z pociskiem i ewentualnie tworenie nowej floty"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        break_time += 1
        bullets.empty()
        if break_time == 120:
            settings.increase_speed()
            create_fleet(settings, aliens, ship_height)
            break_time = 0
    return break_time


def get_number_aliens_x(settings, alien_width):
    """ Ustalanie ile obcych sie miesci w rzedzie """
    available_space_x = settings.screen.get_rect().width - 2*alien_width
    number_aliens_x = available_space_x // (2*alien_width)
    return number_aliens_x


def get_number_aliens_y(settings, alien_height, ship_height):
    """ Ustalenie ile rzedow obcych ma być"""
    available_space_y = settings.screen.get_rect().height - ship_height - 13*alien_height
    number_rows = available_space_y//(2*alien_height)
    return number_rows


def create_alien(settings, aliens, alien_number, row_number):
    """Utworzenie obcego i dodanie go do rzedu"""
    alien = Alien(settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(settings, aliens, ship_height):
    """ utworzenie całej floty obcych"""
    alien = Alien(settings)
    number_aliens_x = get_number_aliens_x(settings, alien.rect.width)
    number_rows = get_number_aliens_y(settings, alien.rect.height, ship_height)

    #utworzenie pierwszego rzedu obcych
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(settings, aliens, alien_number, row_number)


def check_fleet_edges(settings, aliens):
    """Sprawdzenie czy flota dotyka krawedzi"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    """Przesuniecie floty w dol a nastepnie odwrocenie kierunku"""
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.fleet_direction *= -1


def ship_hit(settings, stats, ship, aliens, bullets):
    """ reakcje zderzenia obcego i statku"""
    if stats.lives > 1:
        # zmniejszenie liczby zyc
        stats.lives -= 1

        # usuniecie floty i pociskow
        aliens.empty()
        bullets.empty()

        # stworzenie nowej floty i srodkowaie statku
        ship.center_ship()
        create_fleet(settings, aliens, ship.rect.height)

        sleep(0.2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(aliens, settings, ship, stats, bullets):
    """ Sprawdzenie czy flota zetknela sie z krawedzia, a nastepnie
    Uaktualnienie polozenia kazdego statku we flocie"""
    check_fleet_edges(settings, aliens)


    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(settings, stats, ship, aliens, bullets)
    aliens.update()
    check_aliens_bottom(settings, stats, ship, aliens, bullets)


def check_aliens_bottom(settings, stats, ship, aliens, bullets):
    """ sprawdzenie, czy jakis obcy dotknal dolu ekranu """
    screen_rect = settings.screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, stats, ship, aliens, bullets)
            break

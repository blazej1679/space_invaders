import pygame


class Ship:
    def __init__(self, settings):
        """Inicjalizacja statku i jego polozenia."""
        self.settings = settings
        self.screen = settings.screen        # wczytanie obrazu i pobranie jego prostokąta
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        #self.centerHorizontal = float(self.settings.bg_rect.centerx)   # okreslenie polozenia statku
        #self.centerVertical = float(self.settings.bg_rect.top + 500)
        self.screen_rect = settings.screen.get_rect()

        self.moving_right = False                       # opcje poruszania sie statku
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self, fps):
        """Uaktualnianie polozenia statku."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += fps * self.settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= fps * self.settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= fps * self.settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += fps * self.settings.ship_speed_factor


    def center_ship(self):
        """ centrowanie pozycji """
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 50

    def blitme(self):
        """Wyświetlenie statku w aktualnym polozeniu."""
        self.screen.blit(self.image, self.rect)

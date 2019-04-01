import pygame
import sys

class StartScreen(pygame.sprite.Sprite):
    """Klasa ekranu startowego"""
    def __init__(self, settings, play_button, image_file='images/bg.jpg'):
        pygame.sprite.Sprite.__init__(self)
        self.screen = settings.screen
        self.screen_rect = self.screen.get_rect()
        self.button = play_button
        # inicjalizowanie tla statku palmy i kokosow
        self.bg_image = pygame.image.load(image_file)
        self.bg_rect = self.bg_image.get_rect()
        self.bg_rect.left, self.bg_rect.top = [0, 0]

        self.palm_image = pygame.image.load('images/tree_small.png')
        self.palm_rect = self.palm_image.get_rect()
        self.palm_rect.center = self.screen_rect.center
        self.bullet_image = pygame.image.load('images/coco_fuel.png')
        self.bullet_rect = self.bullet_image.get_rect()

        self.ship_image = pygame.image.load('images/ship.png')
        self.ship_rect = self.ship_image.get_rect()
        #obracanie statku
        self.ship_image, self.ship_rect = self.rot_center(self.ship_image, self.ship_rect, 90)
        self.ship_rect.centerx = self.palm_rect.centerx - 20
        self.ship_rect.centery = self.palm_rect.centery + 125

        self.run_game = False

    def run_start_screen(self):
        while not self.run_game:

            self.bullet_rect.centerx = self.screen_rect.centerx - 20
            self.bullet_rect.centery = self.screen_rect.centery - 50

            while not self.bullet_rect.colliderect(self.ship_rect):
                self.bullet_rect.centery += 3
                self.blit_screen()


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.display.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                            sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                            self.check_play_button(self.button)


    def rot_center(self, image, rect, angle):
        """rotate an image while keeping its center"""
        self.rot_image = pygame.transform.rotate(image, angle)
        self.rot_rect = self.rot_image.get_rect(center=rect.center)
        return self.rot_image, self.rot_rect

    def check_play_button(self, play_button):
        """Rozpoczecie gry po kliknieciu przycisk Play"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked:
            self.run_game = True



    def blit_screen(self):
        self.screen.blit(self.bg_image, self.bg_rect)
        self.button.draw_button()
        self.screen.blit(self.screen, self.screen_rect)
        self.screen.blit(self.ship_image, self.ship_rect)
        self.screen.blit(self.palm_image, self.palm_rect)
        self.screen.blit(self.bullet_image, self.bullet_rect)
        pygame.display.flip()
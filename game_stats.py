import pygame



class GameStats():
    """ Zbieranie danych o stanie gry """

    def __init__(self, settings):
        self.settings = settings
        self.game_active = True
        self.lives = 3
        self.super_ammo = 0
        pygame.font.init()
        self.myfont = pygame.font.SysFont('Comic Sans MS', 20, True)
        # utworzenie paska z punktami, zyciem, i iloscia dostepnych super pociskow
        self.rect = pygame.Rect(0, 0, settings.screen.get_rect().width, 20)
        self.color = (0, 0, 60)

        #self.reset_stats()

    def blit_scores(self):
        self.showing_lives = self.myfont.render(f"{str(self.lives)} /3 Lives", False, (0, 150, 20))
        pygame.draw.rect(self.settings.screen, self.color, self.rect)
        self.settings.screen.blit(self.showing_lives, (50, 4))



    def reset_stats(self):
        """ inicjalizacja i resetowanie danych """
        self.lives = 3


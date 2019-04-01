import pygame.sysfont


class Scoreboard():
    """ Klasa przechowujaca punktacje"""

    def __init__(self, settings, stats):
        self.settings = settings
        self.screen = settings.screen
        self.screen_rect = settings.screen.get_rect()
        self.stats = stats

        self.txt_color = (0, 150, 20)
        self.font = pygame.sysfont.SysFont(None, 20)

        # przygotowanie poczatkowych obrazow z punktacja
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """przedstawienie punktacji na obrazie"""
        rounded_score = int(round(self.stats.score, -1))

        score_str = str(rounded_score)
        self.score_image = self.font.render(f"Score: {score_str}", False, self.txt_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 4

    def prep_high_score(self):
        """Zamiana wyniku w grze na obraz do wyswietlenia"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(f"Highest score: {high_score_str}", False, self.txt_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        """Wyswietlanie wyniku"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
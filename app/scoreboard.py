import pygame

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.font = pygame.font.SysFont('Consolas', 20, bold=True)
        self.color = (83, 83, 83) 

    def update(self):
        self.score += 0.15 

    def draw(self, screen):
        current_score_int = int(self.score)
        high_score_int = int(self.high_score)

        score_str = f"{current_score_int:05}"
        high_score_str = f"HI {high_score_int:05}"

        text = f"{high_score_str}  {score_str}"
        text_surface = self.font.render(text, True, self.color)

        screen_width = screen.get_width()
        text_rect = text_surface.get_rect()
        text_rect.topright = (screen_width - 20, 20)
        
        screen.blit(text_surface, text_rect)

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score

    def reset(self):
        self.score = 0
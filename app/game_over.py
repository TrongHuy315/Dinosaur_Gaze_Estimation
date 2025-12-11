import pygame

class GameOverScreen:
    def __init__(self, screen_size):
        self.screen_width = screen_size[0]
        self.screen_height = screen_size[1]
        
        self.has_images = False
        self.font_big = pygame.font.SysFont('Consolas', 60, bold=True)
        self.font_small = pygame.font.SysFont('Consolas', 30)

        if self.has_images:
            self.retry_rect = self.retry_img.get_rect()
        else:
            self.retry_rect = pygame.Rect(0, 0, 200, 50) 
            
        self.retry_rect.center = (self.screen_width // 2, self.screen_height // 2 + 50)

    def draw(self, screen):
        if self.has_images:
            go_rect = self.game_over_img.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
            screen.blit(self.game_over_img, go_rect)
            
            screen.blit(self.retry_img, self.retry_rect)
        else:
            text_surf = self.font_big.render("G A M E  O V E R", True, (83, 83, 83))
            text_rect = text_surf.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 50))
            screen.blit(text_surf, text_rect)

            pygame.draw.rect(screen, (83, 83, 83), self.retry_rect, 2)
            retry_text = self.font_small.render("RETRY", True, (83, 83, 83))
            retry_text_rect = retry_text.get_rect(center=self.retry_rect.center)
            screen.blit(retry_text, retry_text_rect)

    def is_retry_clicked(self, mouse_pos):
        return self.retry_rect.collidepoint(mouse_pos)
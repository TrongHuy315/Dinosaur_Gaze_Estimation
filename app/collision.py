import pygame

class CollisionManager:
    def __init__(self):
        pass

    def _get_draw_surface(self, obj):
        try:
            if hasattr(obj, 'getImage'):
                return obj.getImage()
        except Exception:
            pass

        try:
            if hasattr(obj, 'getDinoJump'):
                return obj.getDinoJump()
        except Exception:
            pass
        try:
            if hasattr(obj, 'getDinoRun'):
                return obj.getDinoRun(0)
        except Exception:
            pass
        try:
            if hasattr(obj, 'getDinoDuck'):
                return obj.getDinoDuck(0)
        except Exception:
            pass

        try:
            if hasattr(obj, 'getBirdFly'):
                idx = getattr(obj, 'anim_index', 0)
                return obj.getBirdFly(idx)
        except Exception:
            pass

        return None

    def get_rect(self, obj):
        x = obj.getXPos() if hasattr(obj, 'getXPos') else 0
        y = obj.getYPos() if hasattr(obj, 'getYPos') else 0

        if hasattr(obj, 'width') and hasattr(obj, 'height'):
            try:
                return pygame.Rect(int(x), int(y), int(obj.width), int(obj.height))
            except Exception:
                pass

        surf = self._get_draw_surface(obj)
        if surf is not None:
            return pygame.Rect(int(x), int(y), surf.get_width(), surf.get_height())

        return pygame.Rect(int(x), int(y), 1, 1)

    def collide(self, dino, obstacle):
        dino_rect = self.get_rect(dino)
        obstacle_rect = self.get_rect(obstacle)
        return dino_rect.colliderect(obstacle_rect)

    def collide_list(self, dino, obstacles):
        dino_rect = self.get_rect(dino)
        for obs in obstacles:
            if dino_rect.colliderect(self.get_rect(obs)):
                return True
        return False

    def pixel_collide(self, dino, obstacle, dino_image=None, obstacle_image=None):
        dino_rect = self.get_rect(dino)
        obstacle_rect = self.get_rect(obstacle)

        if not dino_rect.colliderect(obstacle_rect):
            return False

        if dino_image is None:
            dino_image = self._get_draw_surface(dino)
        if obstacle_image is None:
            obstacle_image = self._get_draw_surface(obstacle)

        if dino_image is None or obstacle_image is None:
            return True

        try:
            dino_mask = pygame.mask.from_surface(dino_image)
            obstacle_mask = pygame.mask.from_surface(obstacle_image)
            offset = (int(obstacle_rect.x - dino_rect.x), int(obstacle_rect.y - dino_rect.y))
            overlap = dino_mask.overlap(obstacle_mask, offset)
            return overlap is not None
        except Exception:
            return True

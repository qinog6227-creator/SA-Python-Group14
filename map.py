import pygame

def draw_map(screen):
    w = screen.get_width() // 2
    h = screen.get_height() // 2

    screen.fill((0, 255, 0))
    pygame.draw.rect(screen, (0, 0, 0), (50, 100, 60, 60))

    font = pygame.font.SysFont("Meiryo", 40)
    text = font.render("MAP (ESC to return)", True, (0, 0, 0))
    screen.blit(text, text.get_rect(center=(w, 30)))

import pygame

def draw_title(screen, font):
    w = screen.get_width() // 2
    h = screen.get_height() // 2

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (w - 250, h - 150, 500, 300))

    text = font.render("坊主めくり×カードバトル", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=(w, h - 50)))

    text = font.render("Heian Bozu Attack", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=(w, h + 10)))

    text = font.render("Press SHIFT to Start", True, (255,255,255))
    screen.blit(text, text.get_rect(center=(w, h + 100)))

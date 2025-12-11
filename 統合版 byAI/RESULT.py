import pygame
import Pparameter

def draw_result(screen, is_win, is_clear):
    screen.fill(Pparameter.BLACK)
    font = pygame.font.Font(None, 80)
    font_s = pygame.font.Font(None, 40)

    if not is_win:
        text = font.render("GAME OVER...", True, (100, 100, 255))
        sub = font_s.render("Press SPACE to Return Title", True, Pparameter.WHITE)
    elif is_clear:
        text = font.render("ALL CLEARED!!", True, (255, 215, 0))
        sub = font_s.render("Thank you for playing!", True, Pparameter.WHITE)
    else:
        text = font.render("YOU WIN!!", True, (255, 100, 100))
        sub = font_s.render("Press SPACE for Next Stage", True, Pparameter.WHITE)

    screen.blit(text, text.get_rect(center=(Pparameter.SCREEN_WIDTH//2, 250)))
    screen.blit(sub, sub.get_rect(center=(Pparameter.SCREEN_WIDTH//2, 400)))
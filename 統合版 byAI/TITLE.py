import pygame
import Pparameter

def draw_title(screen):
    screen.fill(Pparameter.BLACK)
    
    # タイトルロゴ
    font_title = pygame.font.Font(None, 100)
    title_text = font_title.render("SADAME DRAW", True, Pparameter.RED)
    rect = title_text.get_rect(center=(Pparameter.SCREEN_WIDTH//2, 200))
    screen.blit(title_text, rect)

    # サブタイトル
    font_sub = pygame.font.Font(None, 40)
    sub_text = font_sub.render("- Heian Bozu Attack -", True, Pparameter.WHITE)
    rect_sub = sub_text.get_rect(center=(Pparameter.SCREEN_WIDTH//2, 280))
    screen.blit(sub_text, rect_sub)

    # スタート案内
    msg = font_sub.render("Press [SHIFT] to Start", True, Pparameter.BLUE)
    # 点滅演出っぽく
    if pygame.time.get_ticks() % 1000 < 500:
        rect_msg = msg.get_rect(center=(Pparameter.SCREEN_WIDTH//2, 450))
        screen.blit(msg, rect_msg)
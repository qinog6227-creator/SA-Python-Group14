import pygame
import sys
import Ptitle
import Pmap

# 1. 準備（画用紙を作る）
pygame.init()
screen = pygame.display.set_mode((800, 600)) # 幅800, 高さ600
pygame.display.set_caption("サダメドロー")

# 文字を書くための「筆（フォント）」を用意
font = pygame.font.Font(None, 50) 
font2 = pygame.font.Font(None, 100)
#追加可能

def main(screen):
    # === 2. メインループ（ここが紙芝居） ===
    while True:
        # (終了ボタンが押されたら終わる処理)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0))

       
        def draw_encountBar(screen,encount):
    text_title = FONT.render(f"{encount}st Round", True, WHITE)
    screen.blit(text_title,Pparameter.centeringY(text_title, 60))


def draw_battleStatus(screen, e_hp, p_hp, stockA, stockD): 
    text_bar = FONT.render(f"----- Latest Imformation -----", True, WHITE)
    text_enemysta = FONT.render(f"Enemy HP: {e_hp}", True, WHITE)
    text_playersta = FONT.render(f"Player HP: {p_hp}", True, WHITE)
    text_stockA = FONT.render(f"Stock Attack Card: {stockA}", True, WHITE)
    text_stockD = FONT.render(f"Stock Defense Card: {stockD}", True, WHITE)
    screen.blit(text_bar, (50, 150))
    screen.blit(text_enemysta, (50, 190))
    screen.blit(text_playersta, (50, 230))
    screen.blit(text_stockA, (50, 270))
    screen.blit(text_stockD, (50, 310))

    draw_battleCommand(screen):

    draw_card(screen):
 
    

    pygame.display.flip()

if __name__ == '__main__':
    main(screen)
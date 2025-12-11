import pygame
import Pparameter

pygame.font.init()
FONT = pygame.font.Font(None, 50) #フォント設定
#追加可能


# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


#タイトル画面のグラフィック
def draw_title(screen):
    
    #ゲームタイトル
    text_title1 = FONT.render("SADAME DRAW", True, RED)
    screen.blit(text_title1, Pparameter.centeringY(text_title1, 100))
    
    #ゲームタイトル枠
    pygame.draw.rect(screen, WHITE, (100, 200, 600, 100), 0)

    #ゲームタイトル
    text_title2 = FONT.render("Bozu-Mekuri + Card Game", True, BLACK)
    screen.blit(text_title2, Pparameter.centeringY(text_title2, 225))
    
    #スタート指示枠
    pygame.draw.rect(screen, WHITE, (100, 450, 600, 100), 0)
    
    #スタート指示テキスト
    text_start = FONT.render("Press SHIFT Key to START", True, BLACK) 
    screen.blit(text_start, Pparameter.centeringY(text_start, 500))





def draw_wait_start():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "START?"
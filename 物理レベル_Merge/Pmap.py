# Ptitle.py
import pygame
import sys
import Pparameter

# フォントの初期化
pygame.font.init()

FONT = pygame.font.Font(None, 60) #フォント設定
FONT2 = pygame.font.Font(None, 30) #フォント設定
#追加可能

# 色の定義
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#ステージごとのマップ描画
def draw_map1(screen):
    
    #ステージの状態を表示する
    pygame.draw.rect(screen, WHITE,(20,10,300,60), 0)
    text_map1 = FONT.render("stage map1", True, BLACK)
    screen.blit(text_map1,(40,20))

    #ステージのマスを表示   
    pygame.draw.circle(screen, RED, (150, 300), 50, 0)
    pygame.draw.circle(screen, RED, (400, 300), 50, 5) 
    pygame.draw.circle(screen, RED, (650, 300), 80, 5)
    pygame.draw.line(screen, WHITE, (200, 300), (350,300), 5)
    pygame.draw.line(screen, WHITE, (450, 300), (570,300), 5)
    
    text_stage1 = FONT.render(f"Enemy1", True, WHITE)
    screen.blit(text_stage1,(70,150))


#ステージごとのマップ描画
def draw_map2(screen):
    
    #ステージの状態を表示する
    pygame.draw.rect(screen, WHITE,(20,10,300,60), 0)
    text_map1 = FONT.render(f"stage map2", True, BLACK)
    screen.blit(text_map1,(40,20))

    #ステージのマスを表示   
    pygame.draw.circle(screen, RED, (150, 300), 50, 0)
    pygame.draw.circle(screen, RED, (400, 300), 50, 5) 
    pygame.draw.circle(screen, RED, (650, 300), 80, 5)
    pygame.draw.line(screen, WHITE, (200, 300), (350,300), 5)
    pygame.draw.line(screen, WHITE, (450, 300), (570,300), 5)
    
    text_stage1 = FONT.render(f"Enemy2", True, WHITE)
    screen.blit(text_stage1,(300,150))


#第3ステージのマップ描画
def draw_map3(screen):
    
    #ステージの状態を表示する
    pygame.draw.rect(screen, WHITE,(20,10,300,60), 0)
    text_map1 = FONT.render(f"stage map3", True, BLACK)
    screen.blit(text_map1,(40,20))

    #ステージのマスを表示   
    pygame.draw.circle(screen, RED, (150, 300), 50, 0)
    pygame.draw.circle(screen, RED, (400, 300), 50, 5) 
    pygame.draw.circle(screen, RED, (650, 300), 80, 5)
    pygame.draw.line(screen, WHITE, (200, 300), (350,300), 5)
    pygame.draw.line(screen, WHITE, (450, 300), (570,300), 5)
    
    text_stage1 = FONT.render(f"Boss!!", True, WHITE)
    screen.blit(text_stage1,(600,150))



def draw_wait_start():
    # 入力待ちのメッセージだけ返す (メイン関数でキー判定に使用)
    return "START?"
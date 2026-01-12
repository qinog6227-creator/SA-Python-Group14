import pygame
import PARAMETER

# 画像サイズを画面サイズ(1000x600)に合わせる
IMG_WIN = pygame.transform.scale(pygame.image.load("assets/GoToNextStage.png"), PARAMETER.SCREEN_SIZE)
IMG_LOSE = pygame.transform.scale(pygame.image.load("assets/GameOver.png"), PARAMETER.SCREEN_SIZE)
IMG_CLEAR = pygame.transform.scale(pygame.image.load("assets/GameClear.png"), PARAMETER.SCREEN_SIZE)

def draw_result(screen, is_win, is_clear):
    # 背景として画像を画面いっぱいに表示
    
    if not is_win: # 負け
        screen.blit(IMG_LOSE, (0, 0))
        
    elif is_clear: # 全クリア
        screen.blit(IMG_CLEAR, (0, 0))
        
    else: # ステージクリア（次へ）
        screen.blit(IMG_WIN, (0, 0))

    font_s = pygame.font.Font(None, 50)
    
    if not is_win:
        msg = "Press SPACE to Return Title"
    elif is_clear:
        msg = "Thank you for playing!"
    else:
        msg = "Press SPACE for Next Stage"

    text = font_s.render(msg, True, PARAMETER.WHITE)
    # 画面下部に配置
    screen.blit(text, text.get_rect(center=(PARAMETER.SCREEN_WIDTH//2, 550)))
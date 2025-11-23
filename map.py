#ここは描画処理のみを行い、main.py内で呼び出す
import pygame #おまじない

#マップ画面を描画する関数を定義
def draw_map(screen):
    w = screen.get_width() // 2
    h = screen.get_height() // 2

    # 図形を描画していく    
    screen.fill((0, 255, 0)) #画面の色を設定
    pygame.draw.rect(screen, (0, 0, 0), (50, 100, 60, 60)) #四角形を描画

    #テキストを出力
    font = pygame.font.SysFont("Meiryo", 40)
    text = font.render("MAP (ESC to return)", True, (0, 0, 0))
    screen.blit(text, text.get_rect(center=(w, 30)))

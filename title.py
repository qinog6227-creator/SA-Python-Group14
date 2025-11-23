#ここは描画処理のみを行い、main.py内で呼び出す
import pygame #おまじない

#タイトル画面を描画する関数を定義
def draw_title(screen, font):

    #画面の中心の座標を取得
    w = screen.get_width() // 2
    h = screen.get_height() // 2

    #図形を描画していく
    screen.fill((0, 0, 0)) #画面の色を設定
    pygame.draw.rect(screen, (255, 0, 0), (w - 250, h - 150, 500, 300))  #四角形を描画

    #テキストを出力
    text = font.render("坊主めくり×カードバトル", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=(w, h - 50)))

    text = font.render("Heian Bozu Attack", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=(w, h + 10)))

    text = font.render("Press SPACE to Start", True, (255,255,255))
    screen.blit(text, text.get_rect(center=(w, h + 100)))

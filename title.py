#おまじない(最初に書く)
import pygame
pygame.init()

# ウィンドウ作成
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ゲームタイトル")

# 画面中央の座標を取得
w = screen.get_width() // 2
h = screen.get_height() // 2

# フォントごとに設定（文字を書くなら必要）
font1 = pygame.font.SysFont("Meiryo", 40)
font2 = pygame.font.Font(r"C:\Users\user\Desktop\SA-Python-Group14\font\PixelMplus12-Regular.ttf", 40)


#メインループ：ここに処理を書く
running = True
while running: #無限ループ
    #イベント処理（キー入力・×ボタンなど)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #画面の更新処理
    screen.fill((0, 0, 0))  # 画面を黒で塗りつぶし

    #描画処理を書いていく（文字・画像・図形など)
    pygame.draw.rect(screen, (255, 0, 0), (w - 250, h - 150,500,300))

    #文字を書く
    text = font1.render("坊主めくり × カードバトル", True, (255, 255, 255))
    text_rect = text.get_rect(center=(w, h-50))
    screen.blit(text, text_rect)

    text = font2.render("Heian Bozu Attak", True, (255, 255, 255))
    text_rect = text.get_rect(center=(w, h+50))
    screen.blit(text, text_rect)


    #おまじない(画面更新)
    pygame.display.update()

#おまじない(最後に書く)
pygame.quit()
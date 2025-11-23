#おまじない(最初に書く)
import pygame
pygame.init()

# ウィンドウ作成
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("ゲームタイトル")

# フォントごとに設定（文字を書くなら必要）
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 60)

#メインループ：ここに処理を書く
running = True
while running: #無限ループ
    #イベント処理（キー入力・×ボタンなど
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ---- 画面の更新処理 ----
    screen.fill((0, 0, 0))  # 画面を黒で塗りつぶし

    # ---- 描画処理を書く（文字・画像・図形など） ----
    #文字を書く
    text = font1.render("Hello!", True, (255, 255, 255))
    screen.blit(text, (50, 50))


    #おまじない(画面更新)
    pygame.display.update()

#おまじない(最後に書く)
pygame.quit()

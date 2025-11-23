import pygame  # おまじない
pygame.init()  # おまじない

# 画面の作成（好きなサイズに変える）
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("タイトル画面")

#ウィンドウの中心座標を取得
w = screen.get_width() // 2
h= screen.get_height() // 2

#文字の設定
font1 = pygame.font.SysFont("meiryo", 35)   
font2 = pygame.font.SysFont("meiryo", 50)
# font名　= pygame.font.SysFont("フォント名", サイズ) 　文字サイズとフォント予め設定する

# メインループ(下5行はおまじない)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ここに描画処理を書いていく
    screen.fill((0, 0, 0))  # 画面を黒で塗りつぶす
    pygame.draw.rect(screen, (255, 0, 0), (w - 250, h - 150,500,300))   # 赤い四角を描く

    #文字の配置の塊
    text = font1.render("今のマップ", True, (255, 255, 255))
    text_rect = text.get_rect(center=(w, h-50))   # ←中心に配置
    screen.blit(text, text_rect)


    pygame.display.flip()  # 画面更新

pygame.quit()
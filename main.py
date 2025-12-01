import pygame #おまじない
import sys #おまじない
import title #タイトル画面の描画処理をインポート
import map #マップ画面の描画処理をインポート
import menu #メニュー画面の描画処理をインポート
import battle #バトル画面の描画処理をインポート


# メイン関数
def main():
    pygame.init() #おまじない
    screen = pygame.display.set_mode((1000, 500)) #画面サイズを設定
    pygame.display.set_caption("つるぎめくり(14班)") #画面タイトルを設定

    # フォントを設定
    font1 = pygame.font.Font(None, 40)

    #state変数で画面遷移を管理
    state = "title"
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # ×ボタンが押されたら
                running = False #ループを抜けて終了する

            if event.type == pygame.KEYDOWN: #キーが押されたら
                if state == "title" and event.key == pygame.K_SPACE: # SPACEキーが押されたら
                    state = "map" #マップ画面へ遷移

        if state == "title": #タイトル画面ならば
            title.draw_title(screen, font1) #タイトル画面の関数を呼び出す
        elif state == "map": #マップ画面ならば
            map.draw_map(screen) # マップ画面の関数を呼び出す

        pygame.display.update() #おまじない
        clock.tick(60)

    pygame.quit() #おまじない(終了時)
    sys.exit() #おまじない(終了時)


if __name__ == "__main__": #おまじない
    main()

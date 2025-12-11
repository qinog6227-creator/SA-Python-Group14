# Pmain.py 
import pygame
import sys
import Ptitle
import Pmap
import PbattleG
import Presult
import Pparameter
import Pbattle_main
import PbattleC

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("サダメドロー")

def main(screen): 
    game_state = 'title'
    is_win = 'none'
    encount = 0 

    key_pressed = None

    while True:

        key_pressed = None  #毎フレーム初期化

        # 画面を閉じれば終了   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                key_pressed = event.key
                
                # タイトル画面→マップ画面
                if game_state == 'title':
                    if event.key == pygame.K_SPACE:
                        game_state = 'map'

                # マップ画面→バトル画面
                elif game_state == 'map':
                    if event.key == pygame.K_SPACE:
                        game_state = 'battle'
                        encount += 1
                        Pbattle_main.battle_init(encount)


        # 描画処理（イベントループの外）
        screen.fill((0,0,0))

        if game_state == 'title':
            Ptitle.draw_title(screen)

        elif game_state == 'map':
            Pmap.draw_map1(screen)

        elif game_state == 'battle':
            is_win = Pbattle_main.run_battle(screen, encount, key_pressed)

            # 勝敗判定
            if is_win == 'win':
                if encount < 3:
                    game_state = 'result'
                else:
                    game_state = 'clear'

            elif is_win == 'lose':
                game_state = 'gameover'

        elif game_state == 'result':
            Presult.draw_winning(screen)

        elif game_state == 'lose':
            Presult.draw_losing(screen)

        pygame.display.flip()

if __name__ == '__main__':
    main(screen)

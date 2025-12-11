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
    #------変数一覧---------
    game_state = 'title'
    is_win = 'none'
    encount = 0 #バトル数を計測
    font = pygame.font.Font(None, 50)
    battle_logs = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # タイトル画面の判定
            if game_state == 'title' and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 'map'

            # マップ画面の判定
            elif game_state == 'map' and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state = 'battle'


        # 描画処理
        screen.fill((0,0,0))
        if game_state == 'title':
            Ptitle.draw_title(screen)

        elif game_state == 'map':
            Pmap.draw_map1(screen)

        elif game_state == 'battle':
            encount += 1
            key_pressed = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()                       
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    key_pressed = event.key

            # キー情報を渡す
            is_win = Pbattle_main.run_battle(screen, encount, key_pressed)


            if is_win == 'win' and (encount == 1 or encount == 2):
                game_state = 'result'
            elif is_win == 'win' and (encount == 3):
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

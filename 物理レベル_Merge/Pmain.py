#メイン関数。すべて呼び出す

import pygame #パイゲーム実行
import 物理レベル_Merge.Ptitle as Ptitle
import 物理レベル_Merge.Pmap as Pmap
import 物理レベル_Merge.Pbattle_main as Pbattle_main
import 物理レベル_Merge.Presult as Presult

#------変数一覧---------
game_state = 0
is_start = 'none'
is_move = 'none'
is_win = 'none'
encount = 0 #バトル数を計測

def main():
    Ptitle.draw_title()
    pygame.init()
    screen = pygame.display.set_mode((800, 600)) # 幅800, 高さ600
    pygame.display.set_caption("14班 RPG")


    while is_start != 's':
        is_start = input(Ptitle.draw_wait_start())
        if is_start == 's':
            break

    Pmap.draw_map1()
    while is_move != 'y':
        is_move = input(Pmap.draw_wait_fowrd())
        if is_move == 'y':
            break

    encount += 1
    # 2. バトルを呼び出す時、画用紙(screen)を渡す！
    # 今まで: run_battle(encount)
    # これから: run_battle(screen, encount)
    is_win = Pbattle_main.run_battle(screen, encount)
    if is_win == 'win':
        Presult.draw_wining()
    elif is_win == 'lose':
        Presult.draw_losing()
    is_move = 'none' #★　次のステージへ進むか判定を初期化
    is_win = 'none'
    Pmap.draw_map2()
    while is_move != 'y':
        is_move = input(Pmap.draw_wait_fowrd())
        if is_move == 'y':
            break

    encount += 1
    # 2. バトルを呼び出す時、画用紙(screen)を渡す！
    # 今まで: run_battle(encount)
    # これから: run_battle(screen, encount)
    is_win = Pbattle_main.run_battle(screen, encount)
    if is_win == 'win':
        Presult.draw_wining()
    elif is_win == 'lose':
        Presult.draw_losing()

    is_move = 'none' #★　次のステージへ進むか判定を初期化
    is_win = 'none'
    Pmap.draw_map3()
    while is_move != 'y':
        is_move = input(Pmap.draw_wait_fowrd())
        if is_move == 'y':
            break

    encount += 1
    # 2. バトルを呼び出す時、画用紙(screen)を渡す！
    # 今まで: run_battle(encount)
    # これから: run_battle(screen, encount)
    is_win = Pbattle_main.run_battle(screen, encount)
    if is_win == 'win':
        Presult.draw_wining()
    elif is_win == 'lose':
        Presult.draw_losing()
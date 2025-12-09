#メイン関数。すべて呼び出す

import Mtitle
import Mmap
import Mbattle_main
import Mresult

#------変数一覧---------
game_state = 0
is_start = 'none'
is_move = 'none'
is_win = 'none'
encount = 0 #バトル数を計測

Mtitle.draw_title()
while is_start != 's':
    is_start = input(Mtitle.draw_wait_start())
    if is_start == 's':
        break

Mmap.draw_map1()
while is_move != 'y':
    is_move = input(Mmap.draw_wait_fowrd())
    if is_move == 'y':
        break

encount += 1
is_win = Mbattle_main.run_battle(encount) #LBattle_mainを呼び出す
if is_win == 'win':
    Mresult.draw_wining()
elif is_win == 'lose':
    Mresult.draw_losing()
is_move = 'none' #★　次のステージへ進むか判定を初期化
is_win = 'none'
Mmap.draw_map2()
while is_move != 'y':
    is_move = input(Mmap.draw_wait_fowrd())
    if is_move == 'y':
        break

encount += 1
is_win = Mbattle_main.run_battle(encount) #LBattle_mainを呼び出す
if is_win == 'win':
    Mresult.draw_wining()
elif is_win == 'lose':
    Mresult.draw_losing()

is_move = 'none' #★　次のステージへ進むか判定を初期化
is_win = 'none'
Mmap.draw_map3()
while is_move != 'y':
    is_move = input(Mmap.draw_wait_fowrd())
    if is_move == 'y':
        break

encount += 1
is_win = Mbattle_main.run_battle(encount) #LBattle_mainを呼び出す
if is_win == 'win':
    Mresult.draw_wining()
elif is_win == 'lose':
    Mresult.draw_losing()
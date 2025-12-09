#メイン関数。すべて呼び出す

import Ltitle
import Lmap
import Lbattle_main
import Lresult

#------変数一覧---------
game_state = 0
is_start = 'none'
is_move = 'none'
is_win = 'none'
encount = 0 #バトル数を計測

Ltitle.draw_title()
while is_start != 's':
    is_start = input(Ltitle.draw_wait_start())
    if is_start == 's':
        break

Lmap.draw_map1()
while is_move != 'y':
    is_move = input(Lmap.draw_wait_fowrd())
    if is_move == 'y':
        break

encount += 1
is_win = Lbattle_main.run_battle(encount) #LBattle_mainを呼び出す
if is_win == 'win':
    Lresult.draw_wining()
elif is_win == 'lose':
    Lresult.draw_losing()
is_move = 'none' #★　次のステージへ進むか判定を初期化
is_win = 'none'
Lmap.draw_map2()
while is_move != 'y':
    is_move = input(Lmap.draw_wait_fowrd())
    if is_move == 'y':
        break

encount += 1
is_win = Lbattle_main.run_battle(encount) #LBattle_mainを呼び出す
if is_win == 'win':
    Lresult.draw_wining()
elif is_win == 'lose':
    Lresult.draw_losing()

is_move = 'none' #★　次のステージへ進むか判定を初期化
is_win = 'none'
Lmap.draw_map3()
while is_move != 'y':
    is_move = input(Lmap.draw_wait_fowrd())
    if is_move == 'y':
        break

encount += 1
is_win = Lbattle_main.run_battle(encount) #LBattle_mainを呼び出す
if is_win == 'win':
    Lresult.draw_wining()
elif is_win == 'lose':
    Lresult.draw_losing()
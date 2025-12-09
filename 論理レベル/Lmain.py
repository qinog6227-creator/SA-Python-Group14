#メイン関数。すべて呼び出す

import Ltitle
import Lmap
import LbattleG
import LbattleG

#------変数一覧---------
game_state = 0
is_start = 'none'
is_move = 'none'

Ltitle.draw_title()
while is_start != 's':
    is_start = input()
    if is_start == 's':
        break

Lmap.draw_map1()
while is_move != 'y':
    is_move = input()
    if is_move == 'y':
        break
#パラメータ
player_hp = 50 #プレイヤーのHP
enemy_hp = 30 #敵のHP
stock_attack = 0 #プレイヤーの攻撃を溜める量
stock_guard = 0 #プレイヤーの防御を溜める量

#与ダメージ
def calc_cause(stock_attack):
    cause_hp = stock_attack * 1.5
    return cause_hp




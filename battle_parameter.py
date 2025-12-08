# --- プレイヤーの攻撃計算 ---
def calc_player_attack(current_enemy_hp, stock_attack):
    logs = [] 
    # 計算
    damage = int(stock_attack * 1.0)
    current_enemy_hp -= damage

    # ログ (f文字列を使うと変数を埋め込めます)
    logs.append(f"攻撃！ 敵に {damage} のダメージ！")
    
    # 新しいHPとログを返す
    return current_enemy_hp, logs

# --- 敵の攻撃計算 ---
def calc_enemy_attack(current_player_hp, enemy_power):
    logs = [] 
    damage = int(enemy_power * 1.5)
    current_player_hp -= damage
    
    logs.append(f"敵の攻撃！ {damage} のダメージを受けた！")
    
    # 新しいHPとログを返す
    return current_player_hp, logs



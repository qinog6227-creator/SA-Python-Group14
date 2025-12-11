import pygame
import PbattleG
import PbattleC
import Pparameter

# バトル状態を保持する辞書
battle_state = {
    "deck": [],
    "player_hp": 0,
    "enemy_hp": 0,
    "stock_attack": 0,
    "stock_defence": 0,
    "logs": [],
    "phase": "draw"
}

# 初期化処理
def battle_init(encount):
    battle_state["deck"] = Pparameter.DECK_LIST.copy()
    battle_state["player_hp"] = Pparameter.PLAYER_MAX_HP
    battle_state["enemy_hp"] = Pparameter.ENEMY_MAX_HP
    battle_state["stock_attack"] = 0
    battle_state["stock_defence"] = 0
    battle_state["logs"] = [f"----- {encount} 戦目 バトル開始 -----"]
    battle_state["phase"] = "draw"


# 毎フレーム呼び出すメイン処理
def run_battle(screen, encount, key_pressed=None):

    # --- 1. 描画 ---
    screen.fill((0, 0, 0))
    PbattleG.draw_encountBar(screen, encount)
    PbattleG.draw_battleStatus(
        screen,
        battle_state["enemy_hp"],
        battle_state["player_hp"],
        battle_state["stock_attack"],
        battle_state["stock_defence"]
    )
    PbattleG.draw_logs(screen, battle_state["logs"][-15:])
    PbattleG.draw_battleCommand(screen)

    # --- 2. 入力（D or C）---
    command = None
    if key_pressed == pygame.K_d:
        command = "d"
    elif key_pressed == pygame.K_c:
        command = "c"

    # --- 3. フェーズ処理 ---
    # ① draw フェーズ：Dでドロー
    if battle_state["phase"] == "draw" and command == "d":
        deck, player_hp, stockA, stockD, force_end, new_logs = PbattleC.calc_draw(
            battle_state["deck"],
            battle_state["player_hp"],
            battle_state["stock_attack"],
            battle_state["stock_defence"]
        )
        battle_state["deck"] = deck
        battle_state["player_hp"] = player_hp
        battle_state["stock_attack"] = stockA
        battle_state["stock_defence"] = stockD
        battle_state["logs"] = new_logs

        battle_state["phase"] = "enemy" if force_end else "command"

    # ② command フェーズ：Cで攻撃
    elif battle_state["phase"] == "command" and command == "c":
        enemy_hp, new_logs = PbattleC.calc_player_attack(
            battle_state["enemy_hp"],
            battle_state["stock_attack"]
        )
        battle_state["enemy_hp"] = enemy_hp
        battle_state["logs"] = new_logs
        battle_state["stock_attack"] = 0

        battle_state["phase"] = "enemy"

    # ③ enemy フェーズ：敵のターン
    elif battle_state["phase"] == "enemy":
        if battle_state["enemy_hp"] > 0:
            # 敵が攻撃してくる
            player_hp, enemy_logs = PbattleC.calc_enemy_turn(
                battle_state["player_hp"],
                battle_state["stock_defence"],
                1
            )
            battle_state["player_hp"] = player_hp
            battle_state["logs"] += enemy_logs

            # 敵のターン後は次は draw
            battle_state["stock_defence"] = 0
            battle_state["phase"] = "draw"

    # --- 4. 勝敗判定 ---
    if battle_state["player_hp"] <= 0:
        return "lose"
    if battle_state["enemy_hp"] <= 0:
        return "win"

    return None  # バトル続行中

# Pbattle_main.py
import Pparameter
import PbattleC
import random

# ---------------------------------------------
# バトル初期化
# ---------------------------------------------
def battle_init():
    Pparameter.CURRENT_DECK = Pparameter.DECK_LIST.copy()
    random.shuffle(Pparameter.CURRENT_DECK)

    Pparameter.PLAYER_HAND.clear()
    Pparameter.PLAYER_CURRENT_HP = Pparameter.PLAYER_MAX_HP
    Pparameter.ENEMY_CURRENT_HP = Pparameter.ENEMY_MAX_HP
    Pparameter.PLAYER_ATTACK_POWER = 0
    Pparameter.PLAYER_DEFENSE_POWER = 0

    # 初期手札を4枚配る
    for _ in range(4):
        draw_card_from_deck()

    return Pparameter.PHASE_PLAYER_DRAW

# ---------------------------------------------
# 山札からカードを1枚ドロー
# ---------------------------------------------
def draw_card_from_deck():
    Pparameter.CURRENT_DECK, _, _, _, _, logs = PbattleC.calc_draw(
        Pparameter.CURRENT_DECK,
        Pparameter.PLAYER_CURRENT_HP,
        Pparameter.PLAYER_ATTACK_POWER,
        Pparameter.PLAYER_DEFENSE_POWER
    )
    return logs

# ---------------------------------------------
# プレイヤードロー処理
# ---------------------------------------------
def player_draw_phase():
    logs = draw_card_from_deck()
    # 手札が5枚以上ならコマンドフェーズに移行
    if len(Pparameter.PLAYER_HAND) >= 5:
        return Pparameter.PHASE_PLAYER_COMMAND, logs
    return Pparameter.PHASE_PLAYER_DRAW, logs

# ---------------------------------------------
# プレイヤーのコマンド処理
# card_index: 手札の何番目を使うか
# ---------------------------------------------
def player_command_phase(card_index):
    logs = []
    if 0 <= card_index < len(Pparameter.PLAYER_HAND):
        card = Pparameter.PLAYER_HAND.pop(card_index)
        if card == Pparameter.CARD_ATTACK:
            Pparameter.PLAYER_ATTACK_POWER += Pparameter.SWORD_POWER
            # 攻撃は即反映
            Pparameter.ENEMY_CURRENT_HP, attack_logs = PbattleC.calc_player_attack(
                Pparameter.ENEMY_CURRENT_HP,
                Pparameter.PLAYER_ATTACK_POWER
            )
            logs += attack_logs
            # 攻撃力リセット
            Pparameter.PLAYER_ATTACK_POWER = 0
        elif card == Pparameter.CARD_GUARD:
            Pparameter.PLAYER_DEFENSE_POWER += Pparameter.GUARD_POWER
            logs.append("防御力チャージ")
        elif card == Pparameter.CARD_SKULL:
            Pparameter.PLAYER_ATTACK_POWER = 0
            Pparameter.PLAYER_DEFENSE_POWER = 0
            logs.append("カード没収")

        return Pparameter.PHASE_ENEMY_TURN, logs

    return Pparameter.PHASE_PLAYER_COMMAND, logs

# ---------------------------------------------
# 敵ターン処理
# ---------------------------------------------
def enemy_phase():
    p_hp, logs = PbattleC.calc_enemy_turn(
        Pparameter.PLAYER_CURRENT_HP,
        Pparameter.PLAYER_DEFENSE_POWER,
        Pparameter.CURRENT_STAGE
    )
    Pparameter.PLAYER_CURRENT_HP = p_hp
    # ガードは使い切り
    Pparameter.PLAYER_DEFENSE_POWER = 0
    return Pparameter.PHASE_CHECK_END, logs

# ---------------------------------------------
# 勝敗判定フェーズ
# ---------------------------------------------
def check_end_phase():
    if Pparameter.PLAYER_CURRENT_HP <= 0:
        return "lose"
    elif Pparameter.ENEMY_CURRENT_HP <= 0:
        return "win"
    else:
        return Pparameter.PHASE_PLAYER_DRAW

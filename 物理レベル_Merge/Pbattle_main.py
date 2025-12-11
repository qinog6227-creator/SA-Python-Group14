# Pbattle_main.py
import Pparameter
import PbattleC  # 計算ファイル
import random

# -----------------------------------------------------------------
# バトル初期化
# -----------------------------------------------------------------
def battle_init():
    # 山札シャッフル
    Pparameter.CURRENT_DECK = Pparameter.DECK_LIST.copy()
    random.shuffle(Pparameter.CURRENT_DECK)

    # 手札・HP・パワー初期化
    Pparameter.PLAYER_HAND.clear()
    Pparameter.PLAYER_CURRENT_HP = Pparameter.PLAYER_MAX_HP
    Pparameter.ENEMY_CURRENT_HP = Pparameter.ENEMY_MAX_HP
    Pparameter.PLAYER_ATTACK_POWER = 0
    Pparameter.PLAYER_DEFENSE_POWER = 0

    # 初期手札を配る
    for _ in range(4):
        draw_card_from_deck()

    # 最初のフェーズはドロー
    return Pparameter.PHASE_PLAYER_DRAW

# -----------------------------------------------------------------
# 山札からカードを1枚ドロー
# -----------------------------------------------------------------
def draw_card_from_deck():
    if len(Pparameter.CURRENT_DECK) == 0:
        Pparameter.CURRENT_DECK = Pparameter.DECK_LIST.copy()
        random.shuffle(Pparameter.CURRENT_DECK)
        return "Deck reshuffled."
    
    card = Pparameter.CURRENT_DECK.pop()
    Pparameter.PLAYER_HAND.append(card)
    return f"Drawn card: {card}"

# -----------------------------------------------------------------
# プレイヤードロー処理
# -----------------------------------------------------------------
def player_draw_phase():
    # 1枚引く
    draw_card_from_deck()
    
    # 5枚になったらコマンドフェーズへ
    if len(Pparameter.PLAYER_HAND) >= 5:
        return Pparameter.PHASE_PLAYER_COMMAND
    return Pparameter.PHASE_PLAYER_DRAW

# -----------------------------------------------------------------
# プレイヤーのコマンド処理
# card_index: 手札の何番目を使うか
# -----------------------------------------------------------------
def player_command_phase(card_index):
    if 0 <= card_index < len(Pparameter.PLAYER_HAND):
        card = Pparameter.PLAYER_HAND.pop(card_index)
        # カード効果適用
        if card == Pparameter.CARD_ATTACK:
            Pparameter.PLAYER_ATTACK_POWER += Pparameter.SWORD_POWER
        elif card == Pparameter.CARD_GUARD:
            Pparameter.PLAYER_DEFENSE_POWER += Pparameter.GUARD_POWER
        elif card == Pparameter.CARD_SKULL:
            Pparameter.PLAYER_ATTACK_POWER = 0
            Pparameter.PLAYER_DEFENSE_POWER = 0
        
        # 使用後は敵ターン
        return Pparameter.PHASE_ENEMY_TURN
    return Pparameter.PHASE_PLAYER_COMMAND

# -----------------------------------------------------------------
# 敵ターン処理
# -----------------------------------------------------------------
def enemy_phase():
    # ダメージ計算（PbattleCの関数使用）
    p_hp, logs = PbattleC.calc_enemy_turn(
        Pparameter.PLAYER_CURRENT_HP,
        Pparameter.PLAYER_DEFENSE_POWER,
        Pparameter.CURRENT_STAGE
    )
    Pparameter.PLAYER_CURRENT_HP = p_hp
    # ガードはリセット
    Pparameter.PLAYER_DEFENSE_POWER = 0

    return Pparameter.PHASE_CHECK_END, logs

# -----------------------------------------------------------------
# 勝敗判定フェーズ
# -----------------------------------------------------------------
def check_end_phase():
    if Pparameter.PLAYER_CURRENT_HP <= 0:
        return "lose"
    elif Pparameter.ENEMY_CURRENT_HP <= 0:
        return "win"
    else:
        return Pparameter.PHASE_PLAYER_DRAW

import random
import PARAMETER

def init_deck():
    """山札を初期化してシャッフルして返す"""
    deck = PARAMETER.DECK_COMPOSITION.copy()
    random.shuffle(deck)
    return deck

# カードを引いたときの論理レベルでの処理
def draw_card(deck, stockA): 
    if not deck:
        deck = init_deck()
    
    card = deck.pop()
    is_skull = False
    
    if card == PARAMETER.CARD_SWORD:
        stockA += PARAMETER.SWORD_DMG
    elif card == PARAMETER.CARD_GUARD:
        pass 
    elif card == PARAMETER.CARD_SKULL:
        stockA = 0
        is_skull = True

    return card, stockA, is_skull, deck

# 敵が与えるダメージを計算(後々の改変のため作成)
def calc_enemy_damage(enemy_power):
    return enemy_power

# 3枚溜めるごとにボーナスダメージ
def calc_player_damage(stockA):
    
    # 1. 基本ダメージ（溜めた枚数）
    base_damage = stockA
    
    # 2. ボーナス計算（3枚ごとに +2 ダメージ）
    # 割り算の商（//）を使うので、3, 4, 5枚なら「1セット」、6, 7, 8枚なら「2セット」と自動計算されます
    bonus = 2 * (stockA // 3)
    
    # 3. 合計を計算
    total_damage = base_damage + bonus
    
    return total_damage
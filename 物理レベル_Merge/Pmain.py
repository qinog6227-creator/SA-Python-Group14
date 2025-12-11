# Pmain.py
import pygame
import sys
import Ptitle
import Pmap
import PbattleG
import Presult
import Pparameter
import Pbattle_main
import PbattleC

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("サダメドロー")

font = pygame.font.Font(None, 50)

# ログ管理用（画面に出す）
battle_logs = []

def main(screen):
    game_state = Pparameter.STATE_TITLE
    battle_phase = None  # バトル中のフェーズ管理
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if game_state == Pparameter.STATE_TITLE:
                    game_state = Pparameter.STATE_MAP

                elif game_state == Pparameter.STATE_MAP:
                    # マップからバトルに移行
                    Pbattle_main.battle_init()
                    battle_phase = Pparameter.PHASE_PLAYER_DRAW
                    battle_logs.clear()
                    game_state = Pparameter.STATE_BATTLE

                elif game_state == Pparameter.STATE_BATTLE:
                    # テスト用：スペースで手札1枚プレイ
                    if Pparameter.PLAYER_HAND:
                        # 0番目のカードを使う
                        battle_phase = Pbattle_main.player_command_phase(0)
                        # 攻撃カードなら敵HPに反映
                        Pparameter.ENEMY_CURRENT_HP, logs = PbattleC.calc_player_attack(
                            Pparameter.ENEMY_CURRENT_HP,
                            Pparameter.PLAYER_ATTACK_POWER
                        )
                        battle_logs += logs
                        # 攻撃後は攻撃力リセット
                        Pparameter.PLAYER_ATTACK_POWER = 0

                elif game_state == Pparameter.STATE_RESULT:
                    game_state = Pparameter.STATE_TITLE

        # 画面リセット
        screen.fill((0,0,0))

        # 描画処理
        if game_state == Pparameter.STATE_TITLE:
            Ptitle.draw_title(screen)
        elif game_state == Pparameter.STATE_MAP:
            Pmap.draw_map(screen, 1, font)
        elif game_state == Pparameter.STATE_BATTLE:
            # バトルフェーズの自動処理
            if battle_phase == Pparameter.PHASE_PLAYER_DRAW:
                battle_phase = Pbattle_main.player_draw_phase()
            elif battle_phase == Pparameter.PHASE_ENEMY_TURN:
                battle_phase, logs = Pbattle_main.enemy_phase()
                battle_logs += logs
            elif battle_phase == Pparameter.PHASE_CHECK_END:
                result = Pbattle_main.check_end_phase()
                if result == "win":
                    game_state = Pparameter.STATE_RESULT
                    battle_phase = None
                elif result == "lose":
                    game_state = Pparameter.STATE_RESULT
                    battle_phase = None
                else:
                    battle_phase = result  # ドローフェーズに戻る

            # バトル画面描画
            PbattleG.draw_battle_screen(
                screen,
                Pparameter.PLAYER_CURRENT_HP,
                Pparameter.ENEMY_CURRENT_HP,
                Pparameter.SWORD_POWER,
                Pparameter.GUARD_POWER
            )
            PbattleG.draw_card(screen, Pparameter.PLAYER_HAND)
            PbattleG.draw_logs(screen, battle_logs[-5:])  # 最新5件のみ表示

        elif game_state == Pparameter.STATE_RESULT:
            Presult.draw_winning(screen)

        pygame.display.flip()


if __name__ == '__main__':
    main(screen)

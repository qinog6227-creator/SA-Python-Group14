import pygame
import sys
import PARAMETER
import TITLE
import MAP
import MAIN_BATTLE
import RESULT

def main():
    pygame.init()
    screen = pygame.display.set_mode(PARAMETER.SCREEN_SIZE)
    pygame.display.set_caption("SADAME DRAW")
    clock = pygame.time.Clock()

    # ゲーム全体の状態管理
    state = "title" # title, map, battle, result
    
    # プレイヤーデータ
    current_stage = 0 # 今クリアしているステージ (0=未クリア)
    player_hp = PARAMETER.PLAYER_MAX_HP
    
    battle_result_flag = False # 勝ったかどうか

    while True:
        # イベント処理（共通の終了処理のみ）
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # タイトル画面の入力
            if state == "title":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                        # ゲーム開始初期化
                        current_stage = 0
                        player_hp = PARAMETER.PLAYER_MAX_HP
                        state = "map"

            # リザルト画面の入力
            if state == "result":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if battle_result_flag: # 勝ち
                            if current_stage == 3: # 全クリ
                                state = "title"
                            else:
                                state = "map"
                        else: # 負け
                            state = "title"

        # --- 各シーンの描画・更新 ---
        
        if state == "title":
            TITLE.draw_title(screen)

        elif state == "map":
            selected = MAP.draw_map(screen, current_stage)
            if selected is not None:
                # バトル開始へ遷移
                res, new_hp = MAIN_BATTLE.battle_loop(screen, selected, player_hp)
                
                # バトル終了後
                
                # ★★★ 削除またはコメントアウト！ ★★★
                # player_hp = PARAMETER.PLAYER_MAX_HP # ← これがあると毎回リセットされてしまう！
                
                # その代わり、バトル後のHPを現在のHPとして更新
                player_hp = new_hp 

                if res == "win":
                    current_stage = selected
                    battle_result_flag = True
                else:
                    battle_result_flag = False
                
                state = "result"

        elif state == "result":
            is_clear = (current_stage == 3 and battle_result_flag)
            RESULT.draw_result(screen, battle_result_flag, is_clear)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
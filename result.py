import battle_parameter

print('バトル中のメニュー画面')
print('1. 攻撃')
print('2. 防御')   
print('3. アイテム')
print('4. 逃げる')
choice = input('選択してください (1-4): ')
if choice == '1':
    print('攻撃を選択しました。')           
elif choice == '2':
    print('防御を選択しました。')
elif choice == '3':
    print('アイテムを選択しました。')
elif choice == '4':
    print('逃げるを選択しました。')
    print('しかし逃げられなかった!' )
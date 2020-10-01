print('*' * 40)
print('\t Welcome to League of Legend')
print('*' * 40)

role = input('Choose your character:')
coins = 1000

weapon_list = []


print('Welcome{1} to the league of legend. Coins：{0}'.format(coins, role))

while True:
    choice = int(input(
        'Please choose：\n 1.Buy weapons\n 2.Fight\n 3.Remove weapon\n 4.Check weapon\n 5.Exist\n'))

    if choice == 1:
        print('Welcome to the weapon store')
        weapons = [['gun', 500], ['knife', 400], [
            'fork', 1000], ['bomb', 800], ['chicken', 700]]

        for weapon in weapons:
            print(weapon[0], weapon[1], sep='   ')
        # 提示购买武器
        weaponname = input('Please enter weapon name:')
        # 1.检查有没有买过武器， 2.输入武器是否在商店列表里
        if weaponname not in weapon_list:
            for weapon in weapons:
                if weaponname == weapon[0]:
                    if coins >= weapon[1]:
                        coins -= weapon[1]
                        weapon_list.append(weapon[0])
                        break
                    else:
                        print('go fight')
                        break
                else:
                    print('wrong weapon name.')

    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        answer = input('Are you sure you want to quit？(yes/no')
        if answer == 'yes':
            break
    else:
        print('wrong input, select again')

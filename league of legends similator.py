'''
1.league of legend simulator for list practise
2.buy weapon coins
3.fight earn coins
4.remove weapon
5.check weapons
6.exist
'''

import random

print('*' * 40)
print('\t Welcome to League of Legend')
print('*' * 40)

role = input('Choose your character:')
coins = 1000

weapon_list = []


print('Welcome {1} to the league of legend. Coins：{0}'.format(coins, role))

while True:
    choice = int(input(
        '\nPlease choose：\n 1.Buy weapons\n 2.Fight\n 3.Remove weapon\n 4.Check weapon\n 5.Exist\n'))

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
                        print('{} bought {} from the store'.format(
                            role, weapon[0]))
                        break
                    else:
                        print('No enough coins, go fight and earn coins')
                        break
            else:
                print('wrong weapon name.')
        else:
            print('You already have it')

    elif choice == 2:
        # Assume you have many weapon
        print('Joining war.....')
        if len(weapon_list) > 0:
            # Choose weapon
            print('{} have weapons list below:'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weaponname = input('please choose your weapon:')
                if weaponname in weapon_list:
                    # join fight
                    ran1 = random.randint(1, 20)  # enemy
                    ran2 = random.randint(1, 20)  # me
                    if ran1 > ran2:
                        print('Battle result: Enemy win!!!')
                    elif ran1 < ran2:
                        print('Battle result: You win!!! Congrat {} won {}'.format(
                            role, coins))
                        coins += 200
                    else:
                        print('No winner')
                    break
                else:
                    print('Weapon not listed, please choose again')
        else:
            print('Buy some weapons, with hand you have no chance to win!')

    elif choice == 3:
        # remove weapon
        if len(weapon_list) > 0:
            print('Too heavy, throw some weapons~')
            print('{} have weapons list below:'.format(role))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weaponname = input('Type the weapon name you want to remove:')
                if weaponname in weapon_list:
                    # remove(name) pop(index) clear del need id
                    weapon_list.remove(weaponname)
                    # print(weapons) proof that i can get the list

                    for weapon in weapons:
                        if weaponname == weapon[0]:
                            coins += weapon[1]
                            break
                    break
                else:
                    print('wrong weapon name')
                    break

        else:
            print('No weapon......')

    elif choice == 4:
        print('{} have weapons list below:'.format(role))
        for weapon in weapon_list:
            print(weapon)
        print('Coins: ', coins)

    elif choice == 5:
        answer = input('Are you sure you want to quit？(yes/no')
        if answer == 'yes':
            print('Game Over')
            break
    else:
        print('wrong input, select again')

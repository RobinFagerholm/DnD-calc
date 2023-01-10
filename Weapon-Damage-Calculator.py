def weapon_damage_compare():
    print ('Weapon Damage Calculator')
    
    print ()
    print ('---')
    print ()

    print ('First weapon')
    W1Dice=int(input('Number of dice '))
    W1Damage=int(input('Number of sides '))
    W1Mod=int(input('Modifier '))
    print ()
    print ('Second weapon')
    W2Dice=int(input('Number of dice '))
    W2Damage=int(input('Number of sides '))
    W2Mod=int(input('Modifier '))

    #Add other modifier options when they become relevant. ReRoll ones? Crit Mod?

    print ()
    print ('---')
    print ()


    W1Max=((W1Dice*W1Damage)+W1Mod)
    W1Average=((((W1Damage+1)/2)*W1Dice)+W1Mod)
    W2Max=((W2Dice*W2Damage+W2Mod))
    W2Average=((((W2Damage+1)/2)*W2Dice)+W2Mod)

    print ('Max damage           First','   ','|',' ','Second')
    print ('Max damage          ',W1Max,'      ','|','    ', W2Max)
    print ('Average damage      ',W1Average,'      ','|','    ', W2Average)
    print ('Min damage          ',W1Dice+W1Mod,'       ','|','     ', W2Dice+W2Mod)
    print ()
    print ()

    print ()
    print ('---')
    print ()

weapon_damage_compare()
a=input('press enter to exit.')

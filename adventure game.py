from time import sleep

name = input("What is your name...? ")
print("Welcome, traveller, to the world of Daruka...! You shall, from now on, be known as,'", name, "'")

rescuedstranger = 0
attackedbybear = 0
health = 400
respect = 0
thirst = 100
hunger = 100
inventory = {"swords": 0, "money": 3000, "armor": 1}

if thirst == 0:
    print("Type 'drink' to drink water.")
    drink = input()
    if drink == "drink":
        thirst =+ 70
        print("Your thirst has gone up to", thirst, "%")
if hunger == 0:
    print("Type 'eat' to eat food.")
    eat = input()
    if eat == "eat":
        hunger += 56

answer = input("You have woken up in a small cottage, which shall now be your home. Disorientated, you stumble out the front door. The smell of fire and salty water hits your face. In front of you is a long, dirt path. You curiously walk to the end, but are abruptly put to a stop, as the road ends. Where would you like to go? Left or right? ")
if answer.lower() == "left":
    answer = input("You walk left of the dirt path and go down a hill. At the bottom of the hill is a clear lake. You could walk around the lake, or swim directly through it. (type 'swim' to swim, or 'walk' to walk around it.) ")
    thirst -= 15
    hunger -= 12
    print("(thirst =", thirst, "%", ", hunger =", "%)")
    if answer.lower() == "walk":
        print("You walked for many, many miles. Running out of water, you desperately drank from a dirty puddle. You got the 'Chronium Disorder' disease and died.")
    elif answer.lower() == "swim":
        print("A crocodile was particularly hungry that day. He no longer was after you swam into the lake... ")
    else:
        print("error")
elif answer.lower() == "right":
    answer = input("You come to a bridge. The bridge wobbles in the wind. Cross it or go back? (cross/back) ")
    if answer.lower() == "back":
        print("You turn behind you to go back. A grixo bear pops out of the bushes and mauls you to death.")
    elif answer.lower() == "cross":
        print("Heisitantly you cross the wobbly bridge, tying to not look down at the 50 mile drop below you. Eventually, you cross the bridge. Good job!")
        answer = input("At the end of the bridge is a stranger on the floor. They are in rags and are shivering the cold. Do you help them? (help/no) ")
        if answer.lower() == "help":
            respect += 27
            print("You help the person and take them to your home. They enjoy your company and are nice to you. You decide to let them live with you. People's respect towards you is at ", respect, "%. You then decide to leave the home to go and buy food.")
            rescuedstranger += 1
        elif answer.lower() == "no":
            print("You leave the person to shiver in the cold. After the encounter you decide to go and buy some food.")
    else:
        print("error")
        quit()
    answer = input("On the way to the shops you find a bloody sword laying on the ground. Pick it up? (pickup/no) ")
    if answer.lower() == "pickup":
        inventory["swords"] += 1
        print("You have", inventory["swords"] + 1, "swords.")
    elif answer.lower() == "no":
        print("You leave the sword alone.")
        inventory["swords"] == 0
    print("You arrive at the shop. The hustle and bustle make you dizzy.")
    answer = input("You walk up to a merchant who offers you some armour. It costs 320 rubinks (money). Buy? (your money: 3000) (buy/no)")
    if answer.lower() == "buy":
        print("You loose 320 rubinks. You buy armour. Your health increases by 32.")
        inventory["money"] -= 320
        health += 32
        hunger -= 30
        thirst -= 21
    elif answer.lower() == "no":
        print("You buy nothing and decide to go home.")
    print("You are now at home. You are resting. You go to bed and fall asleep quickly...")
    answer = input("WOULD YOU LIKE TO PLAY CHAPTER TWO? (y/n)" )
    if answer.lower() == "n":
        quit()
    elif answer.lower() == "y":
        print("You wake up and go outside your cottage. You see a large cave in the distance. You go over to it. Inside it is pitch black. You hear growling behind you.")
        print("You turn around. A large, purple furred, grixo bear tries to attack you.")
        if inventory["swords"] > 0:
            print("Just as the bear pounces on you, you remember the sword you picked up earlier. You stab the bear through the head as it tries to bite you.")
        elif inventory["swords"] == 0:
            print("You have nothing to defend yourself with and get mauled by the bear.")
            print("You survive, but barely.")
            hunger -= 41
            thirst -= 36
            health -= 282
            attackedbybear =+ 1
        print("Once you make it back home you crawl into bed.")
        if attackedbybear > 0:
            print("You have nothing to tend to your wounds with, and lose 20 health.")
            health -= 20
        if attackedbybear == 0:
            print("You rest happily.")
            if rescuedstranger > 0:
                print("Your friend tells you the sad story of how he ended up in his position. You are touched by his story.")
        print("placeholder.")
else:
    print("That is not a valid option. You have been directed to the shadow realm (placeholder_realm).")
    sleep(3)
    while 5 > 4:
        print("error", "(you", "died)")

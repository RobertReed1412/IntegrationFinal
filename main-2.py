# _Robert Reed_ = creator of program

import random


def correct_answers(prompt_text, a, b, c, d):
    """This function makes my program robust, so that I only revceive
    answers that can work inside my program.

    :param prompt_text: This is the prompt the user will get for that
    specific input.
    :param a: This is one of the viable inputs
    :param b: This is one of the viable inputs
    :param c: This is one of the viable inputs/extra input that repeats a
    past viable input, so there only needs to be one function
    :param d: This is an extra variable that would be used in the further
    development of this application. This helps to future-proof this function.
    :return: THis function returns a viable input from the user.
    """
    good_input = False
    while not good_input:
        try:
            variable = int(input(prompt_text))
            if variable == a or variable == b or variable == c \
                    or variable == d:
                good_input = True
                return variable
            else:
                print(
                    "Error. Please enter the integer corresponding to your "
                    "choice.")

        except ValueError:
            print("Error. Please enter the integer corresponding to your "
                  "choice.")


# This imports the package that allows me to use the function random.randint
# that genrates a random
# integer within a range.
# I got this information from Python for Beginners page about random
# generators:
# https://www.pythonforbeginners.com/random/how-to-use-the-
# random-module-in-python


# end= replaces the automatic set carriage function whith whatever you
# put in the "".
print("Hello adventurer")
print(
    "\nYou wake up on a cold cavern floor. The only thing you can see is a "
    "faint light from a tunnel ahead",
    end=".")
# + concatinates the two strings and the * prints the string infront
# of it x times.
print("\nYou Hear, " + "Help!" * 3)
print(
    "\nYou run towards the light to see two medieval dressed individuals in "
    "the midst of battle with a goblin hord")
# The int function turns the input from the user from a string into an
# integer, so it can be used.
# input gives the player a prompt and the player can then enter a value
# that is stored in the variable on the
# left of the = sign.
prompt_1 = "run(1) or fight(2)?"
first_decision = correct_answers(prompt_1, 1, 2, 1, 2)
# I learned how to use if staments from W3 schools' conditionals page:
# https://www.w3schools.com/python/python_conditions.asp
if first_decision == 1:
    print(
        "You try to run, but one of the goblins hears your footsteps and "
        "chases after you. He is gaining on you, "
        "so now the only option you have is to fight.")
    goblin_num = 3
elif first_decision == 2:
    print("You steel your resolve and stare down the goblins.")
    goblin_num = 1
# These are a list of assignments. THe variable name is on the right of
# the = and value is on the left.
# These are used later in the if statements, so the combat has variables
# it can use to represent health and damage.
goblin_health_one = 10
goblin_health_two = 10
goblin_health_three = 10
health_one = 30
gob_damage_one = random.randint(1, 4) + 2
try_magic = random.randint(1, 12) + 3
short_sword = random.randint(3, 6) + 1
spear = random.randint(1, 8) + 1
new_weapon = 0
new_health = 30
hit_count = 0
swing_count = 0
# random.randint is a function that creates a random integer
# between the range of (a,b).
input("press enter to roll for an attack")
roll_one = random.randint(1, 20)
# sep replaces the nul from the , in the statement.
print("you rolled", roll_one, sep='  ')


# Elif adds another condition under the already existing if statement.
# == is equals, = is assingment, >= si greater than or equal to, and <=
# is less than or equal to.
# ** is to the power of x, and - is subtraction.
# this is a function that deals with what happens with a critical success
# or critical failure.
def crits():
    """ This function deals with applying the critical success and failure
    effects to the user's roll. A critical success will square thier dmage,
    and a critical failure will subtract two health.

    """
    global roll_one
    global damage_one
    global health_one
    if roll_one == 20:
        damage_one **= 2
    elif roll_one == 1:
        health_one -= 2


what_attack = "choose your attack spear(1), short sword(2), try magic(3)."

if roll_one >= 9:
    attack_one = correct_answers(what_attack, 1, 2, 3, 2)
    if attack_one == 1:
        damage_one = spear
        goblin_health_one -= damage_one
        print("you hit the golbin for ", damage_one, " damage")
        crits()
    elif attack_one == 2:
        damage_one = short_sword
        goblin_health_one -= damage_one
        print("you hit the golbin for ", damage_one, " damage")
        crits()
    elif attack_one == 3:
        damage_one = try_magic
        goblin_health_one -= damage_one
        print("you hit the golbin for ", damage_one, " damage")
        crits()
if goblin_health_one <= 0:
    print("You slayed the goblin!")
elif roll_one < 9:
    print("you miss")
print("the goblin swings at you.")
gob_roll_one = random.randint(1, 20)
if gob_roll_one == 20:
    # * is multiplication, and // divides by x and makes any decimals ==
    # 0(floor division).
    gob_damage_one *= 2
elif gob_roll_one == 1:
    goblin_health_one = int(goblin_health_one // 1.5)
if gob_roll_one >= 10:
    gob_damage_one = random.randint(1, 4) + 2
    health_one -= gob_damage_one
    print("The goblin hit you for ", gob_damage_one, " damage")
elif gob_roll_one < 10:
    print("you dogde out his attck")
print(
    "you see that you have three vials in your belt. There is a green one, "
    "a red one, and a blue one.")
vial_selection = "You do not know what any of them do. " \
                 "What doe you choose? blue(1), red(2), green(3)"
vial_choice = correct_answers(vial_selection, 1, 2, 3, 2)
if vial_choice == 1:
    # % divides by x and outputs the remainder(modulus).
    health_one = int(health_one % 10)
    print(
        "This vial was poision. You feel it burn through your body. "
        "Your health is now ",
        health_one, ".")
elif vial_choice == 2:
    # / is divison
    health_one = int(health_one / 2)
    print(
        "This vial was distilled necrotic juice. Your veins turn black "
        "as your body starts to decompose. "
        "Your health is now ",
        health_one, ".")
elif vial_choice == 3:
    # + is adition
    health_one += 15
    print(
        "This vial was a health potion. You were given extra vitality. "
        "Your health is now ",
        health_one, ".")
print(
    'You run towards the faint light you see in the tunnel. You reach the '
    'exit and see the view of a large open'
    'forrest. THe clank of metal trails closer and closer. You ready '
    'yourself for combat.... \nThe adventurese from'
    'before come to talk to you.')
if first_decision == 1:
    print(
        'The leader of the party says, "you ok rookie? You are going '
        'to need better gear. come down to the won with'
        ' us. \nYou travel for a day to reach a bustling city with all'
        ' manor of fantastical sites.'
        'The party leads you to a shop called tooth and nail to '
        'get accquipped. ')
else:
    print(
        'The entire party cheers and jumps towards you. THe party leader '
        'says, "you fight pretty well rookie, but '
        'those dull blades wont due. We can get you some in the nearest '
        'town for free.\nYou travel for a day to '
        'reach a bustling city with all manor of fantastical sites.'
        'The party leads you to a shop called tooth and nail to '
        'get accquipped.')
# 'not' makes it so if the condition is true the if statement will look
# at it as if it is false.
weapon_choice = 'Chose one of the options. double bitted axe (1), twin ' \
                'short swords(2), elvin bow(3)'
armor_choice_1 = 'You do not have the money to buy amor press enter to ' \
                 'continue'
armor_choice_2 = "Chose one more item: studded leather(1), full plate armor(" \
                 "2), shield(3)"
if not first_decision == 2:
    print(
        'The shop keep smiles an almost toothless grin. He asks, "What '
        'can I get for you? I have all mannor of '
        'trinket desinged to keep you alive. ')
    weapon = correct_answers(weapon_choice, 1, 2, 3, 2)

    armor = correct_answers(armor_choice_1, 1, 2, 3, 2)

else:
    print(
        'The shop keep smiles an almost toothless grin. He asks, "What '
        'can I get for you? I have all mannor of '
        'trinket desinged to keep you alive. ')
    weapon = correct_answers(weapon_choice, 1, 2, 3, 2)
    armor = correct_answers(armor_choice_2, 1, 2, 3, 2)


# this function lets you see what your upgrades have done, and it

# takes parameters to print out what your choices in
# upgrades do to your battle stats
def show_upgrages(health, damage):
    """This function will show the user the result of their decisions during
    the shopping part of the program.

    :param health: This represents their new health.
    :param damage: THis represents their new damage output.
    """
    print("your health is now", health)
    print("your damage is now", damage)


# this function deals with changing your battle vairables like
# health and weapon damage
def upgrades():
    """ This function takes the user through a shopping process. Your first
    decision will determine if you can get both armor and weapons. Your
    decisions will impact both your health and damage output. There are
    also hidden combinations of armor and weapon that will give the user
    boons in battle.

    """
    # I got help from professor Osheroff to understand global statements.
    # Global allows the function to interact with
    # variables outside its scope.
    global weapon
    global armor
    global new_weapon
    global new_health
    if weapon == 1:
        print(
            'You chose the master crafted battle axe. This is a sturdy '
            'axe that will serve you well.')
        new_weapon = 20
    elif weapon == 2:
        print(
            'You chose the swift short swords. Let them guide your decisions.')
        new_weapon += 30
    else:
        print(
            'You have chosen the elvin longbow. Your arrows will be '
            'guided by the wind')
        new_weapon = 45
    if armor == 1:
        print(
            'You have chosen the studded leather armor. This armor '
            'trades protection for monuverability.')
        # 'and' makes sure that the if statement only happens if
        # both booleans are true
        if armor == 1 and weapon == 2:
            new_health = 55
            new_weapon = 40
        else:
            new_health = 55
    elif armor == 2:
        print(
            'You have chosen the full plate armor. '
            'This armor prioritizes protection above all else.')
        if armor == 2 and weapon == 1:
            new_health = 100
            new_weapon = 30
        else:
            new_health = 100
    elif armor == 3:
        print(
            'You have chosen the shield. The sheild grants '
            'protection without a loss of mobility or range of '
            'motion.')
        if armor == 2 and weapon == 1:
            new_health = 100
            new_weapon = 55
        else:
            new_health = 100
    else:
        print("\n")
    show_upgrages(new_health, new_weapon)


upgrades()

print(
    'The leader of the party invites you to join their party, '
    'and you accept. However, he states you have to train '
    'with him before you can start your journey.')
print(
    'You are now in a field about to start your training. '
    'The party leader says you have to be '
    'able to hit him 5 times.')
# a loop that ends after your hit the party leader 5 times,
# and != means not equal to.
while hit_count != 5:
    input("press enter to attack")
    roll_two = random.randint(1, 20) + 8
    if roll_two >= 19:
        # keeps track of the amount of hits
        hit_count += 1
        print('You hit the party leader for', new_weapon, 'damage')
        print('Keep attacking')
    else:
        print('He parried your attack.')
        swing_count += 1
print(
    'The party leader holds his hand up. he says, you are one strong '
    'rookie. You can join our party.')
# a loop that prints YES! only three times
for x in range(0, 3):
    print("YES!\n")
# 'or' will allow the if statement to print if one or both conditions are met
if swing_count > 20 or armor != 5:
    print(
        'The party leader says, you still have a long ways to go though.')
print('You look to the horizon with hope for a wonderful adventure.')

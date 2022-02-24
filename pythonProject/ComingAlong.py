import os
import random
SENTINEL = 0

# function clears the console for cleaner use of the program
def clear():
    os.system('cls')


# function ask the user how many stat points they would like to put into the particular stat that
# they input in the function stat_prompt() and returns the value into the function
def point_prompt(stat, points):
    return int(input("You have " + str(points) + " points to allocate, how many would you like to put into " + str(stat) + ("? ")))


# the function takes the input found within the function point_prompt and checks to make sure
# the amount of points attempting to be used is a valid input value and is not more than the
# user has
def stat_prompt(stat, points):
    allocated_points = point_prompt(str(stat), points)
    while allocated_points > points:
        clear()
        print("That is more points then you have")
        allocated_points = point_prompt(str(stat), points)
    return allocated_points


# The function first prompts which character has leveled up and then asks the user to input
# which stat they would like to level up, which will then lead to the using of stat and point_prompt
# which will make sure valid amounts of points are used and when returned to this function will
# then reduce the used points from the amount of points available for the user to use until there
# no points remaining
def level_up_assignment(points, character):
    while points > 0:
        clear()
        print(character.name + " has leveled up!")
        print("1 = Strength, 2 = Insight, 3 = Defense, 4 = Health, 5 = Luck")
        stat = int(input("Which stat would you like to level? "))
        if stat == 1:
            point_reduction = stat_prompt("strength", points)
            character.phys = character.phys + point_reduction
            points = points - point_reduction
        elif stat == 2:
            point_reduction = stat_prompt("insight", points)
            character.mag = character.mag + point_reduction
            points = points - point_reduction
        elif stat == 3:
            point_reduction = stat_prompt("defense", points)
            character.defe = character.defe + point_reduction
            points = points - point_reduction
        elif stat == 4:
            point_reduction = stat_prompt("health", points)
            character.health = character.health + point_reduction
            points = points - point_reduction
        elif stat == 5:
            point_reduction = stat_prompt("luck", points)
            character.luck = character.luck + point_reduction
            points = points - point_reduction


# The function will display the name of the input character and there stats
def character_list(character):
    clear()
    print(character.name)
    print("Strength = " + str(character.phys))
    print("Magic = " + str(character.mag))
    print("Defense = " + str(character.defe))
    print("Health = " + str(character.health))
    print("Luck = " + str(character.luck))


# The function prompts the user to put in a number corresponding to a party member to route to the
# character_list function
def check_stats():
    checked_character = 0
    while checked_character != -1:
        clear()
        print("Whose stats would you like to check? ")
        checked_character = int(input(
            "1 for " + player_main.name + ", 2 for " + brawler.name + ", 3 for " + mage.name + ", and 4 for " + tank.name + ": "))
        while checked_character == 1:
            character_list(player_main)
            checked_character = input("Type 0 to return to previous screen ")
        while checked_character == 2:
            character_list(brawler)
            checked_character = input("Type 0 to return to previous screen ")
        while checked_character == 3:
            character_list(mage)
            checked_character = input("Type 0 to return to previous screen ")
        while checked_character == 4:
            character_list(tank)
            checked_character = input("Type 0 to return to previous screen ")


# This function takes the input of how many stat points the enemy has and the level of the enemy
# and runs equations to assign values to each stat of the opponent within the range of given points
# with a random chance to either increase the value or decrease the value of the stat within a range
# based off of a proportion in respect to the ratio of points to stats.
def enemy_point_assign(stat_points, enemy_level):
    base_points = stat_points/5
    enemy_level = enemy_level
    enemy_strength = 0
    enemy_mag = 0
    enemy_defe = 0
    enemy_health = 0
    enemy_luck = 0
    enemy_list = []
    for i in range(5):
        point_add_check = random.randint(0, 1)
        if i == 0:
            if point_add_check == 0:
                enemy_strength = base_points - random.randint(0, int(base_points))
                if enemy_strength == 0:
                    enemy_strength = 1
                stat_points = stat_points - enemy_strength

                if stat_points <= 0:
                    enemy_defe = 1
                    enemy_health = 1
                    enemy_luck = 1
                    enemy_mag = 1
                    break

            elif point_add_check == 1:
                enemy_strength = base_points + random.randint(0, int(base_points))
                stat_points = stat_points - enemy_strength
                if stat_points <= 0:
                    enemy_mag = 1
                    enemy_defe = 1
                    enemy_health = 1
                    enemy_luck = 1
                    break

        elif i == 1:
            if point_add_check == 0:
                enemy_mag = base_points - random.randint(0, int(base_points))
                if enemy_mag == 0:
                    enemy_mag = 1
                stat_points = stat_points - enemy_mag
                if stat_points <= 0:
                    enemy_defe = 1
                    enemy_health = 1
                    enemy_luck = 1
                    break
            elif point_add_check == 1:
                enemy_mag = base_points + random.randint(0, int(base_points))
                stat_points = stat_points - enemy_mag
                if stat_points <= 0:
                    enemy_defe = 1
                    enemy_health = 1
                    enemy_luck = 1
                    break

        elif i == 2:
            if point_add_check == 0:
                enemy_defe = base_points - random.randint(0, (int(base_points)))
                if enemy_defe == 0:
                    enemy_defe = 1
                stat_points = stat_points - enemy_defe
                if stat_points <= 0:
                    enemy_health = 1
                    enemy_luck = 1
                    break
            elif point_add_check == 1:
                enemy_defe = base_points + random.randint(0, (int(base_points)))
                stat_points = stat_points - enemy_defe
                if stat_points <= 0:
                    enemy_health = 1
                    enemy_luck = 1
                    break

        elif i == 3:
            if point_add_check == 0:
                enemy_health = base_points - random.randint(0, int(base_points))
                if enemy_health == 0:
                    enemy_health = 1
                stat_points = stat_points - enemy_health
                if stat_points <= 0:
                    enemy_luck = 1
                    break
            elif point_add_check == 1:
                enemy_health = base_points + random.randint(0, int(base_points))
                stat_points = stat_points - enemy_health
                if stat_points <= 0:
                    enemy_luck = 1
                    break
        elif i == 4:
            enemy_luck = stat_points

    new_enemy = BasicEnemy(enemy_strength, enemy_mag, enemy_defe, enemy_health, enemy_luck,"" , enemy_level)
    enemy_list.append(new_enemy)

    return vars(enemy_list[0])


# The function will generate a random amount of enemies from 1 to 4 and will then assign them a level
# and then run the function of enemy_point_assign() which will give each enemy random statistics
# within a set range based on the level of the enemy
def enemies_present():
    amount_enemies = random.randint(1, 4)
    print("There are " + str(amount_enemies) + " enemies present. ")
    enemy_list = []
    enemy_name_list = ["e1", "e2", "e3", "e4"]
    enemy_position = 0
    for i in range(amount_enemies):
        enemy_level = player_main.level
        level_add_check = random.randint(0,1)
        if level_add_check == 0:
            if player_main.level > 1:
                enemy_level = enemy_level - 1
        elif level_add_check == 1:
            enemy_level = enemy_level + 1
        stat_points = 25 + (5*(enemy_level - 1))
        new_enemy = enemy_point_assign(stat_points, enemy_level)
        enemy_list.append(new_enemy)
    return enemy_list


    """
        if i <= len(enemy_list):4
        
            print((enemy_list[i]))
        enemy_position = enemy_position + 1
    print(enemy_list)
    """


def enemy_stats(enemies, enemy_list):
    for i in range(enemies):
        current_enemy = enemy_list[i]
        print("Enemy " + str(i+1) + " has " + str(current_enemy['health']))


def specific_enemy_receiving_stats(enemy_number, enemy_list):
    current_enemy_stats_list = []
    current_enemy_stats = enemy_list[enemy_number]
    current_enemy_health = current_enemy_stats['health']
    current_enemy_defense = current_enemy_stats['defe']
    current_enemy_stats_list.append(current_enemy_health)
    current_enemy_stats_list.append(current_enemy_defense)
    return current_enemy_stats_list


def basic_attack(enemy_stats, character):
    enemy_health = enemy_stats[0]
    enemy_defense = enemy_stats[1]
    character_damage = character.phys
    modified_character_damage = (character_damage - random.randint(0, int(enemy_defense)))
    if modified_character_damage < 0:
        modified_character_damage = 0
    enemy_final_health = enemy_health - modified_character_damage
    return enemy_final_health


# The function will say which characters turn it is and prompt them with the possible actions they
# can take which each then router to separate functions based on the user of the input
def player_turn(character):
    clear()
    print("It is " + character.name + "s turn")
    analyzed_list = enemies_present()
    display_list = list(analyzed_list)

    print("1: Normal Attack, 2: Skill, 3: Defend, 4: Item, 5: Analyze")
    player_choice = int(input("What action would you like to take? "))
    if player_choice == 1:
        enemy_stats(len(analyzed_list), analyzed_list)
        """
        enemy_health = enemy_stats['health']
        print(enemy_health)
        new_enemy_health = enemy_health - 5
        enemy_stats['health'] = new_enemy_health
        print(enemy_stats['health'])
        print(enemy_stats)
        for i in range(len(analyzed_list)):
            pass
        print(analyzed_list1)
        """
        pick_enemy = int(input("Which enemy do you want to attack "))
        current_enemy_stats = specific_enemy_receiving_stats(pick_enemy - 1, analyzed_list)
        new_enemy_health = basic_attack(current_enemy_stats, character)
        damage_dealt = current_enemy_stats[0] - new_enemy_health
        if new_enemy_health > 0:
            print(character.name + " dealt " + str(damage_dealt) + " to enemy " + str(pick_enemy))
            print("That enemy is now at " + str(new_enemy_health) + " health.")
            current_enemy_stats = analyzed_list[pick_enemy - 1]
            current_enemy_stats['health'] = new_enemy_health
            for i in range(len(analyzed_list)):
                print(analyzed_list[i])
        else:
            print(character.name + " dealt a killing blow to enemy " + str(pick_enemy))
            del analyzed_list[pick_enemy - 1]
            remaining_enemies = len(analyzed_list) - 1
            print("There are now " + str(remaining_enemies) + "enemies remaining")

    if player_choice == 2:
        clear()
        for i in range(len(character.skill)):
            skill = character.skill[i]
            print(str(i+1) + ": " + str(skill.name))
        skill_choice = int(input("Choose what skill to use: "))
        used_skill = character.skill[skill_choice-1]
        clear()
        enemy_stats(len(analyzed_list), analyzed_list)
        """
        enemy_health = enemy_stats['health']
        print(enemy_health)
        new_enemy_health = enemy_health - 5
        enemy_stats['health'] = new_enemy_health
        print(enemy_stats['health'])
        print(enemy_stats)
        for i in range(len(analyzed_list)):
            pass
        print(analyzed_list1)
        """
        pick_enemy = int(input("Which enemy do you want to attack "))
        current_enemy_stats = specific_enemy_receiving_stats(pick_enemy - 1, analyzed_list)
        print(current_enemy_stats)
        new_enemy_health = basic_attack(current_enemy_stats, character)
        print(new_enemy_health)
        damage_dealt = current_enemy_stats[0] - new_enemy_health
        print(damage_dealt)
        """
        if new_enemy_health > 0:
            print(character.name + " dealt " + str(damage_dealt) + " to enemy " + str(pick_enemy))
            print("That enemy is now at " + str(new_enemy_health) + " health.")
            current_enemy_stats = analyzed_list[pick_enemy - 1]
            current_enemy_stats['health'] = new_enemy_health
            for i in range(len(analyzed_list)):
                print(analyzed_list[i])
        else:
            print(character.name + " dealt a killing blow to enemy " + str(pick_enemy))
            del analyzed_list[pick_enemy - 1]
            remaining_enemies = len(analyzed_list) - 1
            print("There are now " + str(remaining_enemies) + "enemies remaining")
        """
    if player_choice == 5:
        print(character.name + " analyzed the enemies and determined their stats. ")
        for i in range(len(display_list)):
            print(display_list[i])


def skill_type_check(skill, character):
    if skill.type == "phys":
        character_stat = character.phys
    elif skill.type == "mag":
        character_stat = character.mag
    elif skill.type == "defe":
        character_stat = character.defe
    return character_stat


def character_luck_range(character):
    chance = 50 + character.luck
    target = random.randint(0,100)
    if chance >= target:
        return 1
    else:
        return 0


def skill_damage(skill, character):
    character_stat = skill_type_check(skill, character)
    for i in range(skill.hits):
        hit_check = character_luck_range(character)
        if hit_check == 0:
            print("Missed! ")
            return 0
        elif hit_check == 1:
            damage_output = skill.modifier * character_stat
            print(str(character.name) + " used " + str(skill.name) + "!" + " It did " + str(damage_output) + " damage.")
            return damage_output



def character_skill_learn(skill, character):
    print(character.name + " learned the skill " + skill.name)
    character.skill.append(skill)


class MainCharacter:

    def __init__(player, phys_atk, mag_atk, defe, health, luck, name, level, skill):
        player.phys = phys_atk
        player.mag = mag_atk
        player.defe = defe
        player.health = health
        player.luck = luck
        player.name = name
        player.level = level
        player.skill = skill


class BasicEnemy:
    def __init__(enemy, phys_atk, mag_atk, defe, health, luck, name, level):
        enemy.phys = phys_atk
        enemy.mag = mag_atk
        enemy.defe = defe
        enemy.health = health
        enemy.luck = luck
        enemy.name = name
        enemy.level = level


class Skill:
    def __init__(skill, type, level, enemies, hits, name):
        skill.type = type
        skill.level = level
        skill.enemies = enemies + 1
        skill.hits = hits + 1
        if skill.level == 0:
            modifier = 1
        elif skill.level == 1:
            modifier = 1.5
        elif skill.level == 2:
            modifier = 2
        elif skill.level == 3:
            modifier = 3
        skill.modifier = modifier
        skill.name = name


P000 = Skill("phys", 0, 0, 0, "Bash")
P100 = Skill("phys", 1, 0, 0, "Bonk")
M000 = Skill("mag", 0, 0, 0, "Fireball")
player_main = MainCharacter(5, 5, 5, 5, 5, "Bill", 1, [])
brawler = MainCharacter(8, 3, 5, 8, 1, "Jeff", 1, [])
mage = MainCharacter(3, 8, 3, 5, 6, "Richard", 1, [])
tank = MainCharacter(2, 2, 8, 8, 5, "Bruce", 1, [])

character_skill_learn(P000, player_main)
character_skill_learn(P100, player_main)
player_turn(player_main)
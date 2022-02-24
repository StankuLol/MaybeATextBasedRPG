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


def enemy_stat_set(enemy, phys, mag, defe, health, luck):
    enemy.phys = phys
    enemy.mag = mag
    enemy.defe = defe
    enemy.health = health
    enemy.luck = luck


# The function will generate a random amount of enemies from 1 to 4 and will then assign them a level
# and then run the function of enemy_point_assign() which will give each enemy random statistics
# within a set range based on the level of the enemy
def enemies_present(character):
    enemy_list = []
    num_enemies = random.randint(1, 4)
    for i in range(num_enemies):
        enemy_phys = 0
        enemy_mag = 0
        enemy_defense = 0
        enemy_health = 0
        enemy_luck = 0
        enemy_level = int(character.level) + random.randint(0,2)
        enemy_points = 25 + enemy_level * 5
        while enemy_points > 0:
            print("Enemy " + str(i))
            enemy_phys = random.randint(1, enemy_points//2)
            enemy_points -= enemy_phys
            if enemy_points <= 0:
                break
            enemy_mag = random.randint(1, enemy_points//2)
            enemy_points -= enemy_mag
            if enemy_points <= 0:
                break
            enemy_defense = random.randint(1, enemy_points//2)
            enemy_points -= enemy_defense
            if enemy_points <= 0:
                break
            enemy_health = random.randint(1, enemy_points//2)
            enemy_points -= enemy_health
            if enemy_points <= 0:
                break
            enemy_luck = enemy_points
            enemy_points -= enemy_luck
        if enemy_mag == 0:
            enemy_mag = 1
        if enemy_defense == 0:
            enemy_defense = 1
        if enemy_health == 0:
            enemy_health = 1
        if enemy_luck == 0:
            enemy_luck = 1
        if i == 0:
            enemy_stat_set(enemy_one, enemy_phys, enemy_mag, enemy_defense, enemy_health, enemy_luck)
            enemy_list.append(enemy_one)
        elif i == 1:
            enemy_stat_set(enemy_two, enemy_phys, enemy_mag, enemy_defense, enemy_health, enemy_luck)
            enemy_list.append(enemy_two)
        elif i == 2:
            enemy_stat_set(enemy_three, enemy_phys, enemy_mag, enemy_defense, enemy_health, enemy_luck)
            enemy_list.append(enemy_three)
        elif i == 3:
            enemy_stat_set(enemy_four, enemy_phys, enemy_mag, enemy_defense, enemy_health, enemy_luck)
            enemy_list.append(enemy_four)

    return enemy_list


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


def basic_attack(character, enemy):
    enemy_health = enemy.health
    player_damage = character.phys
    enemy_new_health = enemy_health - player_damage
    return enemy_new_health


# The function will say which characters turn it is and prompt them with the possible actions they
# can take which each then router to separate functions based on the user of the input
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


def skill_damage(skill, character, enemy):
    total_damage_output = 0
    character_stat = skill_type_check(skill, character)
    for i in range(skill.hits):
        hit_check = character_luck_range(character)
        if hit_check == 0:
            print("Missed! ")
            total_damage_output = total_damage_output + 0
        elif hit_check == 1:
            damage_output = (skill.modifier * character_stat)
            print(damage_output)
            total_damage_output = total_damage_output + damage_output
            print(enemy.name + " now has " + str(enemy.health - total_damage_output))

    final_damage_output = enemy.health - total_damage_output
    return final_damage_output


def show_enemy_stats(enemy_list):
    for i in range(len(enemy_list)):
        print(enemy_list[i].name + "'s health is: " + str(enemy_list[i].health))
        print(enemy_list[i].name + "'s physical attack is: " + str(enemy_list[i].phys))
        print(enemy_list[i].name + "'s magical attack is: " + str(enemy_list[i].mag))
        print(enemy_list[i].name + "'s defense is: " + str(enemy_list[i].defe))
        print(enemy_list[i].name + "'s luck is: " + str(enemy_list[i].luck))


def character_skill_learn(skill, character):
    print(character.name + " learned the skill " + skill.name)
    character.skill.append(skill)


def player_turn(character, list_enemies):
    clear()
    while len(list_enemies) > 0:
        print("There are " + str(len(list_enemies)) + " enemies present.")
        print("It is " + character.name + "'s turn.")
        print("1: Basic Attack")
        print("2: Skills")
        action_choice = int(input("Choose which actions to take: "))
        clear()
        if action_choice == 1:
            clear()
            for i in range(len(list_enemies)):
                print(str(i+1) + ": " + list_enemies[i].name + " has " + str(list_enemies[i].health) + " health")
            enemy_selection = int(input("Which enemy do you wish to attack? "))
            enemy_choice = list_enemies[enemy_selection - 1]
            print(character.name + " attacked " + enemy_choice.name)
            new_enemy_health = basic_attack(character, enemy_choice)
            enemy_choice.health = new_enemy_health
            clear()
            if enemy_choice.health > 0:
                print(character.name + " hit the enemy with a basic attack.")
                print(enemy_choice.name + " now has " + str(enemy_choice.health) + " health.")
            else:
                print(enemy_choice.name + " has perished")
                del list_enemies[enemy_selection - 1]

        if action_choice == 2:
            clear()
            for i in range(len(character.skill)):
                print(str(i + 1) + ": " + character.skill[i].name)
            skill_choice = int(input("Which skill do you wish to use? "))
            clear()
            skill_choice = character.skill[skill_choice - 1]
            if skill_choice.enemies == 0:
                for i in range(len(list_enemies)):
                    print(str(i+1) + ": " + list_enemies[i].name + " has " + str(list_enemies[i].health) + " health")
                enemy_selection = int(input("Which enemy do you wish to attack? "))

                enemy_choice = list_enemies[enemy_selection - 1]
                start_enemy_health = enemy_choice.health
                new_enemy_health = skill_damage(skill_choice, character, enemy_choice)
                enemy_choice.health = new_enemy_health
                if enemy_choice.health > 0:
                    if new_enemy_health != start_enemy_health:
                        print(skill_choice.name + " hit " + enemy_choice.name )
                        print(enemy_choice.name + " now has " + str(enemy_choice.health) + " health.")
                    else:
                        print(skill_choice.name + " missed.")
                else:
                    print(skill_choice.name + " dealt a killing blow. ")
                    print(enemy_choice.name + " has perished")
                    del list_enemies[enemy_selection - 1]
            else:
                for i in range(len(list_enemies)):
                    start_enemy_health = list_enemies[i].health
                    new_enemy_health = skill_damage(skill_choice, character, list_enemies[i])
                    list_enemies[i].health = new_enemy_health
                    if list_enemies[i].health > 0:
                        if new_enemy_health != start_enemy_health:
                            print(skill_choice.name + " hit " + list_enemies[i].name)
                            print(list_enemies[i].name + " now has " + str(list_enemies[i].health) + " health.")
                        else:
                            print(skill_choice.name + " missed.")
                    else:
                        print(skill_choice.name + " dealt a killing blow. ")
                        print(list_enemies[i].name + " has perished")
                        del list_enemies[i]


def battle_scenario():
    enemy_list = enemies_present(player_main)
    while len(enemy_list) > 0:
        turn

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
    def __init__(skill, type, level, hits, enemies, name):
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
P073 = Skill("phys", 0, 8, 3, "Hassou Tobi")
M000 = Skill("mag", 0, 0, 0, "Fireball")
player_main = MainCharacter(5, 5, 5, 5, 5, "Bill", 1, [P000, P100, P073])
brawler = MainCharacter(8, 3, 5, 8, 1, "Jeff", 1, [])
mage = MainCharacter(3, 8, 3, 5, 6, "Richard", 1, [M000])
tank = MainCharacter(2, 2, 8, 8, 5, "Bruce", 1, [])
enemy_one = BasicEnemy(0, 0, 0, 0, 0, "Enemy One", 0)
enemy_two = BasicEnemy(0, 0, 0, 0, 0, "Enemy Two", 0)
enemy_three = BasicEnemy(0, 0, 0, 0, 0, "Enemy Three", 0)
enemy_four = BasicEnemy(0, 0, 0, 0, 0, "Enemy Four", 0)


enemy_list = enemies_present(player_main)
player_turn(player_main, enemy_list)
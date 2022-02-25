import os
import random
import time
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


# The function will display the name of the input character and there stats
def character_stat_list(character):
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


def basic_attack(dealer, reciever):
    reciever_health = reciever.health
    reciever_defense = random.randint(0, reciever.defe)
    dealer_damage = dealer.phys
    damage_dealt = reciever_health - dealer_damage + reciever_defense
    if damage_dealt < 0:
        damage_dealt = 0
    return damage_dealt


# The function will say which characters turn it is and prompt them with the possible actions they
# can take which each then router to separate functions based on the user of the input
def skill_type_check(skill, user):
    if skill.type == "phys":
        character_stat = user.phys
    elif skill.type == "mag":
        character_stat = user.mag
    elif skill.type == "defe":
        character_stat = user.defe
    return character_stat


def character_luck_range(user):
    chance = 50 + user.luck
    target = random.randint(0,100)
    if chance >= target:
        return 1
    else:
        return 0


def skill_damage(skill, dealer, reciever):
    total_damage_output = 0
    used_stat = skill_type_check(skill, dealer)
    for i in range(skill.hits):
        hit_check = character_luck_range(dealer)
        if hit_check == 0:
            total_damage_output = total_damage_output + 0
            print("Missed!", end=", ")
        elif hit_check == 1:
            damage_output = round(skill.modifier * used_stat)
            if skill.type == "phys":
                damage_block = random.randint(0, reciever.defe)
            elif skill.type == "mag":
                damage_block = 0
            total_damage_output = total_damage_output + damage_output - damage_block
            if total_damage_output < 0:
                total_damage_output = 0
            print(skill.name + " dealt " + str(total_damage_output) + " damage", end=", ")

    final_damage_output = total_damage_output
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
    start_list_length = len(list_enemies)
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
        enemy_start_health = enemy_choice.health
        print(character.name + " attacked " + enemy_choice.name)
        new_enemy_health = basic_attack(character, enemy_choice)
        enemy_choice.health = new_enemy_health
        clear()
        if enemy_choice.health > 0:
            print(character.name + " dealt " + str(enemy_start_health - new_enemy_health) + " damage")
            print(enemy_choice.name + " now has " + str(enemy_choice.health) + " health.")
            time.sleep(3)
            return list_enemies
        else:
            print(character.name + " dealt " + str(enemy_start_health - new_enemy_health) + " damage")
            print(enemy_choice.name + " has perished")
            del list_enemies[enemy_selection - 1]
            time.sleep(3)
            return list_enemies

    if action_choice == 2:
        clear()
        for i in range(len(character.skill)):
            print(str(i + 1) + ": " + character.skill[i].name)
        skill_choice = int(input("Which skill do you wish to use? "))
        clear()
        skill_choice = character.skill[skill_choice - 1]
        if skill_choice.enemies == 1:
            for i in range(len(list_enemies)):
                print(str(i+1) + ": " + list_enemies[i].name + " has " + str(list_enemies[i].health) + " health")
            enemy_selection = int(input("Which enemy do you wish to attack? "))
            clear()
            enemy_choice = list_enemies[enemy_selection - 1]
            start_enemy_health = enemy_choice.health
            damage_output = skill_damage(skill_choice, character, enemy_choice)
            new_enemy_health = start_enemy_health - damage_output
            enemy_choice.health = new_enemy_health
            if enemy_choice.health > 0:
                if new_enemy_health != start_enemy_health:
                    print(skill_choice.name + " hit " + enemy_choice.name )
                    print(enemy_choice.name + " now has " + str(enemy_choice.health) + " health.")
                    time.sleep(3)
                    return list_enemies
                else:
                    print(skill_choice.name + " missed.")
                    time.sleep(3)
                    return list_enemies
            else:
                print(skill_choice.name + " dealt a killing blow. ")
                print(enemy_choice.name + " has perished")
                del list_enemies[enemy_selection-1]
                time.sleep(3)
                return list_enemies
        else:
            for i in range(len(list_enemies)):
                start_enemy_health = list_enemies[i-(start_list_length - len(list_enemies))].health
                total_damage_output = skill_damage(skill_choice, character,
                                                   list_enemies[i-(start_list_length - len(list_enemies))])
                new_enemy_health = start_enemy_health - total_damage_output
                if new_enemy_health > 0:
                    list_enemies[i-(start_list_length - len(list_enemies))].health = new_enemy_health
                if new_enemy_health <= 0:
                    list_enemies[i - (start_list_length - len(list_enemies))].health = 0
                if list_enemies[i-(start_list_length - len(list_enemies))].health > 0:
                    if new_enemy_health != start_enemy_health:
                        print(skill_choice.name + " hit " + list_enemies[i-(start_list_length - len(list_enemies))].name + " for "
                              + str(start_enemy_health - new_enemy_health) + " damage", end=", ")
                        print(list_enemies[i-(start_list_length - len(list_enemies))].name + " now has " +
                              str(list_enemies[i-(start_list_length - len(list_enemies))].health) + " health.")
                        time.sleep(10)
                        return list_enemies
                    else:
                        print(skill_choice.name + " missed." +
                              list_enemies[i-(start_list_length - len(list_enemies))].name, end=", ")
                        time.sleep(10)
                        return list_enemies
                else:
                    print(skill_choice.name + " dealt a killing blow. ")
                    print(list_enemies[i-(start_list_length - len(list_enemies))].name + " has perished")
                    del list_enemies[i-(start_list_length - len(list_enemies))]
                    time.sleep(10)
                    return list_enemies
    return list_enemies


def enemy_turn(enemy, list_characters):
    start_list_length = len(list_characters)
    enemy_skill_list = enemy.skill
    skill_choice = random.randint(0, len(enemy_skill_list) - 1)
    skill_choice = enemy_skill_list[skill_choice]
    if skill_choice.enemies == 1:
        character_choice = list_characters[random.randint(0, 3)]
        start_character_health = character_choice.health
        new_enemy_health = start_character_health - round(skill_damage(skill_choice, enemy, character_choice))
        character_choice.health = new_enemy_health
        if character_choice.health > 0:
            if new_enemy_health != start_character_health:
                print(enemy.name + " used " + skill_choice.name +  " and hit " + character_choice.name + " for " +
                      str(start_character_health - new_enemy_health ))
                print("Enemy strength: " + str(enemy.phys))
                print(character_choice.name + " now has " + str(character_choice.health) + " health.")
                time.sleep(3)
                return list_characters
            else:
                print(enemy.name + " used " + skill_choice.name + " and missed.")
                time.sleep(3)
                return list_characters
        else:
            print(skill_choice.name + " hit " + character_choice.name + " for " + str(
                start_character_health - new_enemy_health))
            print(skill_choice.name + " dealt a killing blow. ")
            print(character_choice.name + " has fainted. ")
            time.sleep(3)
            return list_characters

    else:
        for i in range(len(list_characters)):
            start_enemy_health = list_characters[i - (start_list_length - len(list_characters))].health
            new_enemy_health = start_enemy_health - round(skill_damage(skill_choice, enemy,
                                            list_characters[i - (start_list_length - len(list_characters))]))
            list_characters[i - (start_list_length - len(list_characters))].health = new_enemy_health
            if list_characters[i - (start_list_length - len(list_characters))].health > 0:
                if new_enemy_health != start_enemy_health:
                    print(skill_choice.name + " hit " + list_characters[
                        i - (start_list_length - len(list_characters))].name + " for " + str(
                        start_enemy_health - new_enemy_health) + " damage", end=", ")
                    print(list_characters[i - (start_list_length - len(list_characters))].name + " now has " + str(
                        list_characters[i - (start_list_length - len(list_characters))].health) + " health.")
                    time.sleep(3)
                    return list_characters
                else:
                    print(
                        skill_choice.name + " missed." + list_characters[i - (start_list_length - len(list_characters))].name,
                        end=", ")
                    time.sleep(3)
                    return list_characters
            else:
                print(skill_choice.name + " dealt a killing blow. ")
                print(list_characters[i - (start_list_length - len(list_characters))].name + " has perished")
                list_characters[i - (start_list_length - len(list_characters))].health = 0
                del list_characters[i - (start_list_length - len(list_characters))]
                time.sleep(3)
                return list_characters
    return list_characters


def battle_scenario(player_team):
    enemy_list = enemies_present(player_main)
    amount_enemies = len(enemy_list)
    while len(enemy_list) != 0 or (player_main.health and brawler.health and mage.health and tank.health) != 0:
        turn_choice = random.randint(0,1)
        if turn_choice == 0:
            if len(player_team) > 0 and len(enemy_list) > 0:
                enemy_list = player_turn(player_team[random.randint(0, len(player_team)-1)], enemy_list)
                if len(enemy_list) == 0:
                    break
            if len(player_team) > 0 and len(enemy_list) > 0:
                player_team = enemy_turn(enemy_list[random.randint(0, len(enemy_list)-1)], player_team)
                if len(player_team) == 0:
                    break
        else:
            if len(player_team) > 0 and len(enemy_list) > 0:
                player_team = enemy_turn(enemy_list[random.randint(0, len(enemy_list)-1)], player_team)
                if len(player_team) == 0:
                    break
            if len(player_team) > 0 and len(enemy_list) > 0:
                enemy_list = player_turn(player_team[random.randint(0, len(player_team)-1)], enemy_list)
                if len(enemy_list) == 0:
                    break
    character_gain_exp(player_team, amount_enemies)


def character_gain_exp(character_list, amount_enemies):
    for i in range(len(character_list)):
        amount_exp_gained = amount_enemies * character_list[i].level
        print(character_list[i].name + " has gained " + str(amount_exp_gained) + " exp.")
        character_list[i].exp += amount_exp_gained
        if character_list[i].exp >= character_list.req_exp:
            level_up_assignment(character_list[i])


# The function first prompts which character has leveled up and then asks the user to input
# which stat they would like to level up, which will then lead to the using of stat and point_prompt
# which will make sure valid amounts of points are used and when returned to this function will
# then reduce the used points from the amount of points available for the user to use until there
# no points remaining
def level_up_assignment(character):
    points = 5
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


class MainCharacter:

    def __init__(player, phys_atk, mag_atk, defe, current_health, max_health, luck, name, level, exp, required_exp, skill, position):
        player.phys = phys_atk
        player.mag = mag_atk
        player.defe = defe
        player.health = current_health
        player.max_health = max_health
        player.luck = luck
        player.name = name
        player.level = level
        player.skill = skill
        player.position = position
        player.exp = exp
        player.req_exp = required_exp


class BasicEnemy:
    def __init__(enemy, phys_atk, mag_atk, defe, health, luck, name, level, skill, position):
        enemy.phys = phys_atk
        enemy.mag = mag_atk
        enemy.defe = defe
        enemy.health = health
        enemy.luck = luck
        enemy.name = name
        enemy.level = level
        enemy.skill = skill
        enemy.position = position


class Skill:
    def __init__(skill, type, level, hits, enemies, name):
        skill.type = type
        skill.level = level
        skill.enemies = enemies
        skill.hits = hits
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


P011 = Skill("phys", 0, 1, 1, "Bash")
P111 = Skill("phys", 1, 1, 1, "Bonk")
P084 = Skill("phys", 0, 8, 4, "Hassou Tobi")
P021 = Skill("phys", 0, 2, 1, "Double Strike")
M011 = Skill("mag", 0, 1, 1, "Fireball")


player_main = MainCharacter(5, 5, 5, 20, 20, 5, "Bill", 1, 0, 2, [P011, P111, P021, P084], 1)
brawler = MainCharacter(8, 3, 5, 25, 25, 1, "Jeff", 1, 0, 2, [P011, P111, P021, P084], 2)
mage = MainCharacter(3, 8, 3, 20, 20, 6, "Richard", 1, 0, 2, [M011, P084], 3)
tank = MainCharacter(2, 2, 8, 25, 25, 5, "Bruce", 1, 0, 2, [P011, P111, P021, P084], 4)


enemy_one = BasicEnemy(0, 0, 0, 0, 0, "Enemy One", 0, [P011, P111], 1)
enemy_two = BasicEnemy(0, 0, 0, 0, 0, "Enemy Two", 0, [P011, P111], 2)
enemy_three = BasicEnemy(0, 0, 0, 0, 0, "Enemy Three", 0, [P011, P111], 3)
enemy_four = BasicEnemy(0, 0, 0, 0, 0, "Enemy Four", 0, [P011, P111], 4)

player_list = [player_main, brawler, mage, tank]
# player_turn(player_main, enemy_list)


battle_scenario(player_list)


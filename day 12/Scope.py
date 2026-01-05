"""enemies = 1 

def increase_enemies():
    enemies = 33
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")
"""
# local scope
"""def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
print(potion_strength)
"""
# Global Scope

player_health = 12
def game():
    def drink_potion():
        potion_strength = 4
        if potion_strength > 1:
            player_health = 24
        print(player_health)

    drink_potion()

print(player_health)


game_level = 2
def create_enemy():
    enemies = ["Vanguards","Duelists","Strategists"]
    if game_level < 4:
        new_enemy = enemies[2]

        print(new_enemy)

create_enemy()
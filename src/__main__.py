# """
# This is the main file that will be executed when the package is run.
# """

# from src.domain.characters.hero import Hero
# from src.domain.characters.enemy import Enemy
# from src.domain.weapon import short_bow

# hero = Hero(name="John Raumn", health=50)
# enemy = Enemy(name="Rava", health=50, weapon=short_bow)


# def main():
#     """
#     Main function that will run the game.
#     """
#     while True:
#         hero.attack(enemy)
#         if enemy.health == 0:
#             print(f"{hero.name} wins!")
#             break

#         enemy.attack(hero)
#         if hero.health == 0:
#             print(f"{enemy.name} wins!")
#             break

#     print(f"{hero.name} has {hero.health} health left.")
#     print(f"{enemy.name} has {enemy.health} health left.")


# if __name__ == "__main__":
#     main()

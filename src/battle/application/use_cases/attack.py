# from src.battle.application.common.interactor import Interactor


# class AttackUseCase(Interactor):
#     """
#     AttackUseCase is a use case that represents a battle between two characters.
#     """

#     def __call__(self) -> str:
#         self.hero.attack(self.enemy)
#         if self.enemy.health == 0:
#             return f"{self.hero.name} wins!"

#         self.enemy.attack(self.hero)
#         if self.hero.health == 0:
#             return f"{self.enemy.name} wins!"
#         return (
#             f"{self.hero.name} has {self.hero.health} health left.\n"
#             f"{self.enemy.name} has {self.enemy.health} health left."
#         )

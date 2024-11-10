class Character:
    max_level = 3

    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        target.got_damage(damage=self.attack_power)

    def got_damage(self, *, damage:int) -> None:
        damage = damage * (100 - self.defence) / 100
        damage = round(damage)
        self.health_points -= damage


    def is_alive(self) -> bool:
        return self.health_points > 0


    @property
    def defence(self) -> bool:
        defence = self.base_defence * self.level
        return defence


    @property
    def max_health_points(self) -> int:
        return self.level * self.base_health_points


    def health_points_percent(self):
        return 100 * self.health_points / self.max_health_points

    def level_up(self):
        if self.level < self.max_level:
            self.level += 1
            self.health_points += int(self.max_health_points / 2)



    def __str__(self) -> str:
        return f"{self.character_name} (Level: {self.level}), hp {self.health_points}"


class Ork(Character):
    base_health_points = 100
    base_attack_power = 10
    character_name = "Ork"
    base_defence = 15

## Перк защиты для Орка

    @property
    def defence(self) -> bool:
        defence = super().defence
        if self.health_points < 50:
            defence *= 3

        return defence

class Elf(Character):
    base_health_points = 50
    base_attack_power = 15
    character_name = "ELf"
    base_defence = 10

## Перк урона для Эльфа

    def attack(self, *, target: "Character") -> None:
        attack_power = self.attack_power
        if target.health_points_percent() < 30:
            attack_power = self.attack_power * 3
        target.got_damage(damage=attack_power)


ork1 = Ork(level=1)
elf1 = Elf(level=1)


def fight(*, character_1: Character, character_2: Character) -> None:
    print("Fight started", character_1, character_2)
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        print(character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)
            print(character_1)

    if character_1.is_alive():
        character_1.level_up()
    else:
        character_2.level_up()

    print(f"Character 1 : {character_1}, is_alive: {character_1.is_alive()}")
    print(f"Character 2 : {character_2}, is_alive: {character_2.is_alive()}")




fight(character_1=ork1, character_2=elf1)




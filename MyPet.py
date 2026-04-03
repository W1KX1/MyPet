 # для первого раза сойдет
import random
import time
import os

class DigitalPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5
        self.happiness = 5
        self.energy = 5
        self.is_alive = True

    def _clamp_stats(self):
        """Убеждается что все показатели в пределах от 0 до 10"""
        self.hunger = max(0, min(10, self.hunger))
        self.happiness = max(0, min(10, self.happiness))
        self.energy = max(0, min(10, self.energy))

    def pass_time(self):
        """Время проходит показатели меняются"""
        self.hunger += 1
        self.happiness -= 0.5
        self.energy -= 1
        self._clamp_stats()
        if self.hunger >= 10 or self.happiness <= 0 or self.energy <= 0:
            self.is_alive = False

    def feed(self):
        if self.is_alive:
            self.hunger -= 3
            print(f"Вы покормили {self.name}. Ням ням")
            self._clamp_stats()

    def play(self):
        if self.is_alive:
            if self.energy > 2:
                self.happiness += 2
                self.energy -= 1
                print(f"Вы поиграли с {self.name}. Ему весело")
                self._clamp_stats()
            else:
                print(f"{self.name} слишком устал для игр")

    def sleep(self):
        if self.is_alive:
            self.energy += 4
            self.hunger += 1
            print(f"💤 {self.name} крепко спит...")
            time.sleep(2)
            self._clamp_stats()

    def status(self):
        """Выводит текущее состояние питомца"""
        if not self.is_alive:
            return f"{self.name} больше нет с нами💀"
        
        hunger_bar = "🟥" * int(self.hunger) + "⬜" * (10 - int(self.hunger))
        happy_bar = "🟩" * int(self.happiness) + "⬜" * (10 - int(self.happiness))
        energy_bar = "🟦" * int(self.energy) + "⬜" * (10 - int(self.energy))

        return f"""
        Имя: {self.name}
        Голод:    [{hunger_bar}] {self.hunger:.1f}/10
        Настроение: [{happy_bar}] {self.happiness:.1f}/10
        Энергия:   [{energy_bar}] {self.energy:.1f}/10
        """

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
\
if __name__ == "__main__":
    pet_name = input("Дайте имя вашему цифровому питомцу: ")
    pet = DigitalPet(pet_name)

    while pet.is_alive:
        clear_screen()
        print(pet.status())
        print("\nЧто вы хотите сделать?")
        print("1. Покормить")
        print("2. Поиграть")
        print("3. Уложить спать")
        print("4. Ничего не делать")

        choice = input("\nВаш выбор (1-4): ")

        if choice == '1':
            pet.feed()
        elif choice == '2':
            pet.play()
        elif choice == '3':
            pet.sleep()
        elif choice == '4':
            print("Время passes by")
        else:
            print("Неверный ввод.")

        pet.pass_time()
        input("\nНажмите Enter чтобы продолжить")

    clear_screen()
    print(pet.status())

    print("Игра окончена")


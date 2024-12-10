import pickle
import random
import os


class Game:
    def __init__(self, rn = random.randint(1, 100), attempt = 5):
        self.random_number = rn
        print(self.random_number)
        self.attempt = attempt
        
        self.obj = {
            'random_number': None,
            'attempt': None,
            'name_save_game': None
        }

    def __del__(self):
        print("Пока-пока")

    def engine(self):
        while self.attempt > 0:
            input_number = int(input('Введите любое число: '))
            self.attempt -= 1
            if input_number == self.random_number:
                print('Вы угадали!')
                exit(0)
            elif input_number > self.random_number:
                print(f'Искомое число меньше! Количество оставшихся попыток: {self.attempt}')
            elif input_number == 0:
                name_save_game = str(input('Сохранить как: '))
                self.obj['random_number'] = self.random_number
                self.obj['attempt'] = self.attempt
                self.obj['name_save_game'] = name_save_game
                with open('./savegame/' + name_save_game + '.pkl', 'wb') as fp:
                    pickle.dump(self.obj, fp)
                    print("Ваша игра записана!")
            else:
                print('Искомое число больше')

        print('Вы исчерпали количество попыток')
        print(self.random_number)
        print(self.input_number)

    def run(self):
        menu = """
            1. Начать игру 
            2. Загрузить игру
            0. Сохранить игру
        """
        print(menu)
        пункт_меню = int(input('Введите пункт меню: '))
        match пункт_меню:
            case 1:
                self.engine()
            case 2:
                dir_ = os.listdir('./savegame')
                for file in dir_:
                    print(file)
                name_save_game = str(input('Введите файл: '))
                with open('./savegame/' + name_save_game, "rb") as f:
                    obj = pickle.load(f)

                self.attempt = obj['attempt']
                self.random_number = obj['random_number']
                self.engine()

game = Game()
game.run()
del game
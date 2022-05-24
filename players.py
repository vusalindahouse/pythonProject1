from configparser import  ConfigParser
PLAYERS = {}

PLAYER = tuple()

SAVES = {}

def read():
    global SAVES, PLAYERS
    config = ConfigParser()
    if config.read("data.ini", encoding="utf-8"):
        PLAYERS = {name.title(): [int(n) for n in score.split(",")]
                   for name, score in config["Scores"].items()}
        SAVES = {tuple(name.split(";")):
                 [[' ' if c == '-' else c for c in field[i:i+3]]
                  for i in range(0, 9, 3)]
                 for name, field in config['Saves'].items()}
        return True if config["General"]["first"] == "yes" else False
    else:
        raise FileNotFoundError


def save():
    config = ConfigParser()
    config["Scores"] = {name: ','.join(str(n) for n in score)
                        for name, score in PLAYERS.items()}
    config["Saves"] = {";".join(name):
                           "".join(['-' if c == " " else c for r in field for c in r])
                       for name, field in SAVES.items()}
    config["General"]["first"] = "no"
    with open("data.ini", "w", encoding="utf-8") as config_file:
        config.write(config_file)


def player_name(bot_mode=''):
    global PLAYER
    if len(PLAYER) == 0:
        PLAYER = (input("Ваше имя: "), )
        num_of_players = input("Для одиночной игры нажмите 1\nДля парной игры нажмите 2:  ").lower()
        if num_of_players in ("1"):
           dif_level = input("Уровень сложности:\nЛегкий - Нажмите 1\nСложный - Нажмите 2\n ")
           if dif_level in("1"):
               bot_mode = "ai_1"
           elif dif_level in("2"):
               bot_mode = "ai_2"
           if bot_mode:
                PLAYER = (PLAYER[0], bot_mode)
           while True:
              choose_symbol = input(f"{PLAYER[0]}, Выберите игровой символ:\n ")
              if choose_symbol not in ("XO").lower():
               print("Впишите правильный символ")
              else:
                break
        elif num_of_players in ("2"):
            PLAYER = (PLAYER[0], input("Имя второго игрока: "))
            while True:
              palyer1_symbol = input(f"{PLAYER[0]}, Выберите игровой символ: ")
              if palyer1_symbol not in ("XO").lower():
               print("Впишите правильный символ")
              else:
                break


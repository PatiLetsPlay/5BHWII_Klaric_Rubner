import json
import random
import requests


def main(game_id, games_history):
    print("Iher Eingabe [rules(1), statistik(2), spielen easy mode(3), spielen hard mode(4), exit(5): ")
    menu_input = input()

    if int(menu_input) == 1:
        rules(game_id, games_history)
    elif int(menu_input) == 2:
        statistics(game_id, games_history)
    elif int(menu_input) == 3:
        start_game(game_id, games_history, mode="easy")
    elif int(menu_input) == 4:
        start_game(game_id, games_history, mode="hard")
    elif int(menu_input) == 5:
        print("End of Game")
    else:
        print("Iher Eingabe war falsch!")
        main(game_id, games_history)


def statistics(game_id, games_history):
    player_wins = 0
    bot_wins = 0
    draws = 0
    symbol_counts = {"Stein": 0, "Papier": 0, "Schere": 0, "Echse": 0, "Spock": 0}
    print("Statistik:")
    if len(games_history) == 0:
        print("Kein Spiel gespielt")
        main(game_id, games_history)
    else:
        for game in games_history:
            if game[3] == "player":  # 3 = result
                player_wins += 1
            elif game[3] == "bot":  # 3 = result
                bot_wins += 1
            elif game[3] == "draw":  # 3 = result
                draws += 1

            player = game[1]  # 1 = player
            bot = game[2]
            # 2 = bot
            print("Die History ist: Player:" + str(player) + ", Bot: " + str(bot))

            if game[1] == 1:
                symbol_counts["Stein"] += 1
            if game[1] == 2:
                symbol_counts["Papier"] += 1
            if game[1] == 3:
                symbol_counts["Schere"] += 1
            if game[1] == 4:
                symbol_counts["Echse"] += 1
            if game[1] == 5:
                symbol_counts["Spock"] += 1

        print(f"Es wurden {game_id} Spiele gespielt:\n"
              f"Der Spieler hat {player_wins} mal gewonnen\n"
              f"Der Bot hat {bot_wins} mal gewonnen\n"
              f"Es gab {draws} mal ein untentschieden\n")

        print(symbol_counts)

        main(game_id, games_history)


def start_game(game_id, games_history, mode):
    if mode == "easy":
        print("Iher Eingabe[Stein(1), Papier(2), Schere(3), Echse(4), Spock(5)]: ")
        user_input = input()

        bot_input = random.randint(1, 5)
        print(bot_input)

        if user_input.isdigit() and int(user_input) in items.values():
            user_input = int(user_input)
            result = check_if_won(user_input, bot_input, games_history)
            weiter_spielen(result, game_id, games_history, mode="easy")
        else:
            print("Iher Eingabe war falsch!")
            result = {"player": "Error", "bot": "Error", "result": "WrongInput"}
            weiter_spielen(result, game_id, games_history, mode="easy")

    if mode == "hard":
        start_game_hard(game_id, games_history)


def start_game_hard(game_id, games_history):
    print("Iher Eingabe[Stein(1), Papier(2), Schere(3), Echse(4), Spock(5)]: ")
    user_input = input()

    if user_input.isdigit() and int(user_input) in items.values():
        user_input = int(user_input)
        bot_input = 0
        if user_input == 1:
            bot_input = 2
        if user_input == 2:
            bot_input = 3
        if user_input == 3:
            bot_input = 1
        if user_input == 4:
            bot_input = 1
        if user_input == 5:
            bot_input = 4

        print(bot_input)
        result = check_if_won(user_input, bot_input, games_history)
        weiter_spielen(result, game_id, games_history, mode="hard")
    else:
        print("Iher Eingabe war falsch!")
        result = ["Error", "Error", "WrongInput"]
        weiter_spielen(result, game_id, games_history)


def check_if_won(user_input, bot_input, game_history):
    result = ""

    if user_input == bot_input:
        result = "draw"
        print("draw")
    elif (
            (user_input == items["Schere"] and bot_input == items["Papier"]) or
            (user_input == items["Schere"] and bot_input == items["Echse"]) or
            (user_input == items["Papier"] and bot_input == items["Stein"]) or
            (user_input == items["Papier"] and bot_input == items["Spock"]) or
            (user_input == items["Stein"] and bot_input == items["Echse"]) or
            (user_input == items["Stein"] and bot_input == items["Schere"]) or
            (user_input == items["Echse"] and bot_input == items["Spock"]) or
            (user_input == items["Echse"] and bot_input == items["Papier"]) or
            (user_input == items["Spock"] and bot_input == items["Schere"]) or
            (user_input == items["Spock"] and bot_input == items["Stein"])
    ):
        result = "player"
        print("player won")
    else:
        result = "bot"
        print("bot won")
    return [user_input, bot_input, result]


def weiter_spielen(result, game_id, games_history, mode):
    game_id += 1
    games_history.append([game_id, *result])
    save_game(games_history)
    print("Weiterspielen [j/n]?")
    keep_playing_input = input()
    if keep_playing_input == 'j':
        start_game(game_id, games_history, mode)
    elif keep_playing_input == 'n':
        main(game_id, games_history)
    else:
        print("Error")
        main(game_id, games_history)


def rules(game_id, games_history):
    print("Regeln:")
    print("Schere schneidet Papier")
    print("Schere köpft Echse")
    print("Papier bedeckt Stein")
    print("Papier widerlegt Spock")
    print("Stein zerquetscht Echse")
    print("Stein schleift Schere")
    print("Echse vergiftet Spock")
    print("Echse frisst Papier")
    print("Spock zertrümmert Schere")
    print("Spock verdampft Stein \n")
    main(game_id, games_history)


def get_Serverdata_and_save():
    server_history = requests.get("http://localhost:5000/getStats").json()
    with open('game_history.json', 'w') as file:
        json.dump({}, file)

    with open('game_history.json', 'w') as file:
        json.dump(server_history, file)


def save_game(game_history):
    with open('game_history.json', 'w') as file:
        json.dump(game_history, file)
        requests.post("http://localhost:5000/saveStats", json=game_history[-1])


if __name__ == "__main__":
    try:
        get_Serverdata_and_save()
        with open('game_history.json', 'r') as file:
            loaded_data = json.load(file)

        if loaded_data:
            games_history = loaded_data
            last_game_id = loaded_data[-1][0]
            print("Last Game ID:", last_game_id)
            game_id = last_game_id
        else:
            games_history = []
            game_id = 0

    except (FileNotFoundError, json.JSONDecodeError):
        games_history = []
        game_id = 0
        print("No game history found.")

    items = {"Stein": 1, "Papier": 2, "Schere": 3, "Echse": 4, "Spock": 5}
    main(game_id, games_history)

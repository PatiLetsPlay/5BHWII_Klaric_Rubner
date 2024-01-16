import random


def main(game_id, games_history):
    print("Iher Eingabe [rules(1), statistik(2), spielen easy mode(3), spielen hard mode(4)]: ")
    menu_input = input()

    if int(menu_input) == 1:
        rules(game_id, games_history)
    elif int(menu_input) == 2:
        statistics(game_id, games_history)
    elif int(menu_input) == 3:
        start_game(game_id, games_history, mode="easy")
    elif int(menu_input) == 4:
        start_game(game_id, games_history, mode="hard")
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
    else:
        for game in games_history:
            if game["result"] == "player":
                player_wins += 1
            elif game["result"] == "bot":
                bot_wins += 1
            elif game["result"] == "draw":
                draws += 1

            print(f"Die History ist: Player: {game["player"]}, Bot: {game["bot"]}")

            # region Herr Professor bitte nicht mobben
            if game["player"] == 1:
                symbol_counts["Stein"] += 1
            if game["player"] == 2:
                symbol_counts["Papier"] += 1
            if game["player"] == 3:
                symbol_counts["Schere"] += 1
            if game["player"] == 4:
                symbol_counts["Echse"] += 1
            if game["player"] == 5:
                symbol_counts["Spock"] += 1

            if game["bot"] == 1:
                symbol_counts["Stein"] += 1
            if game["bot"] == 2:
                symbol_counts["Papier"] += 1
            if game["bot"] == 3:
                symbol_counts["Schere"] += 1
            if game["bot"] == 4:
                symbol_counts["Echse"] += 1
            if game["bot"] == 5:
                symbol_counts["Spock"] += 1
            # endregion
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
            result = check_if_won(user_input, bot_input)
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
        result = check_if_won(user_input, bot_input)
        weiter_spielen(result, game_id, games_history, mode="hard")
    else:
        print("Iher Eingabe war falsch!")
        result = {"player": "Error", "bot": "Error", "result": "WrongInput"}
        weiter_spielen(result, game_id, games_history)


def check_if_won(user_input, bot_input):
    result = ""

    if user_input == bot_input:
        result = "draw"
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
    else:
        result = "bot"

    return {"player": user_input, "bot": bot_input, "result": result}


def weiter_spielen(result, game_id, games_history, mode):
    game_id += 1
    games_history.append({"gameId": game_id, **result})

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


if __name__ == "__main__":
    game_id = 0
    games_history = []
    items = {"Stein": 1, "Papier": 2, "Schere": 3, "Echse": 4, "Spock": 5}
    main(game_id, games_history)

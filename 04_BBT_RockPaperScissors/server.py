import random
import sqlite3
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os

app = Flask(__name__)
load_dotenv()

connection = sqlite3.connect(os.getenv("DB_URL"), check_same_thread=False)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS BBT_RockPaperScissors (gameId INTEGER, player INTEGER, bot INTEGER, "
               "result VARCHAR(20))")


@app.route('/saveStats', methods=['POST'])
def saveStats():
    stats = request.get_json()

    cursor.execute("SELECT * FROM BBT_RockPaperScissors")

    cursor.execute("INSERT INTO BBT_RockPaperScissors VALUES (:gameId, :player, :bot, :result)",stats)

    connection.commit()
    return jsonify({"message": "Success"})


@app.route('/getStats', methods=['GET'])
def getStats():
    cursor.execute("SELECT * FROM BBT_RockPaperScissors")
    stats = cursor.fetchall()
    return jsonify(stats)


if __name__ == '__main__':
    app.run(debug=True)

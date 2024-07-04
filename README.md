# Hangman Game

This is a simple implementation of the classic Hangman game in Python.

## Project Structure

hangman_game/
│
├── src/
│ ├── hangman.py
│ ├── game.py
│ ├── utils.py
│ └── words.py
├── README.md
└── requirements.txt


- `src/hangman.py`: Entry point for the game.
- `src/game.py`: Contains the main game logic.
- `src/utils.py`: Contains helper functions, such as displaying the hangman.
- `src/words.py`: Contains the list of words used in the game.
- `README.md`: Project documentation.
- `requirements.txt`: List of dependencies (if any).

## How to Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/AlfaExelsior/hangman_game.git
    cd hangman_game
    ```

2. **Create a virtual environment and install dependencies**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run the game**:
    ```bash
    python -m src.hangman
    ```

## How to Play

1. The game will randomly select a word from the predefined list.
2. You will be prompted to guess letters or the entire word.
3. If your guess is correct, the letter or word will be revealed.
4. If your guess is incorrect, you lose a try.
5. The game continues until you guess the word correctly or run out of tries.

## Example Output

Let's play Hangman!
| |
|
|
|

Please guess a letter or word: p
Good job, P is in the word!
| |
|
|
|

P _ _ _ _ _ _ _


## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

Created by [AlfaExelsior](https://github.com/AlfaExelsior) - feel free to contact me!


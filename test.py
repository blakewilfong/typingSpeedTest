import random
from pynput import keyboard


def create_sentence(filename):
    word_list = []
    word_count = random.randint(5, 10)
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_list.append(word)
    new_sentence = " ".join(str(element) for element in random.sample(word_list, word_count)).capitalize()
    punctuation_list = [".", ".", ".", "!", "?", "?"]
    return f"{new_sentence}{random.choice(punctuation_list)}", word_count

game_on = True

while game_on:
    test_sentence, sentence_word_count = create_sentence("1000words.txt")
    print(test_sentence)
    player_input = input("Type:")
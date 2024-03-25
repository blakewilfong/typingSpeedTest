import random
import keyboard
from pynput import keyboard


# def create_word_list(filename):
#     word_list = []
#     with open(filename, "r") as file:
#         for line in file:
#             words = line.split()
#             for word in words:
#                 word_list.append(word)
#     return word_list
#
#
# word_list = create_word_list("1000words.txt")
def create_sentence(filename):
    word_list = []
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for word in words:
                word_list.append(word)
    new_sentence = " ".join(str(element) for element in random.sample(word_list, random.randint(5, 10))).capitalize()
    punctuation_list = [".", ".", ".", "!", "?", "?"]
    return f"{new_sentence}{random.choice(punctuation_list)}"

word_list = create_sentence("1000words.txt")

typed_word = []


def generate_word():
    return random.choice(word_list)


def on_press(key):
    global index, word, typed_word
    try:
        if key == keyboard.Key.backspace:
            if typed_word:
                typed_word.pop()
                index -= 1
                index = max(index, 0)
            print(typed_word)

        pressed_key = key.char.lower()
        typed_word.append(pressed_key)
        correct_letter = word[index].lower()

        print("Pressed key:", pressed_key)
        print("Correct letter:", correct_letter)

        if correct_letter == " ":
            if index + 1 < len(word):
                correct_letter = word[index+1].lower()
                if pressed_key == " ":
                    index += 1
                    print(typed_word)
                    return

        if pressed_key == correct_letter or (pressed_key == " " and correct_letter == " "):
            print(typed_word)
            index += 1
            if index == len(word):
                print("Congrats. you completed the word.")
                index = 0
                if pressed_key == keyboard.Key.space:
                    word = generate_word()
                    typed_word = []
                    print("next word:", word)
                else:
                    pass

        else:
            print(pressed_key)
            print(typed_word)
            typed_word = []
            index += 1
            if index == len(word):
                print("wrong.")
                index = 0
                word = generate_word()
                print("next word:", word)

    except AttributeError:
        pass


# def on_release(key):
#     if key == keyboard.Key.esc:
#         return False
#
#
# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     index = 0
#     word = generate_word()
#     print("Current word:", word)
#     listener.join()
#

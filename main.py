import random
import tkinter as tk

time_left = 60
app = tk.Tk()
app.minsize(width=400, height=400)
timer = tk.Label(app, text=f"Time remaining: {time_left}", width=20, padx=50, pady=20, font=("Arial", 20))
timer.pack()
sentence = tk.Label(app, text="", width=40, padx=10, pady=10, font=("Arial", 20), wraplength=400)
sentence.pack()
text_box = tk.Text(app, width=30, height=5, font=("Arial", 20), wrap="word")
text_box.pack()
text_box.focus()
countdown_started = False
test_sentence_list = []
player_sentence_list = []
game_over = False
score = tk.Label(app, text=f"", width=30, font="Arial, 20")
score.pack()


def create_sentence():
    global sentence
    if not game_over:
        word_list = []
        word_count = random.randint(5, 10)
        with open("1000words.txt", "r") as file:
            for line in file:
                words = line.split()
                for word in words:
                    word_list.append(word)
        new_sentence = " ".join(str(element) for element in random.sample(word_list, word_count)).capitalize()
        test_sentence_list.append(new_sentence.split())
        punctuation_list = [".", ".", ".", "!", "?", "?"]
        return sentence.config(text=f"{new_sentence}{random.choice(punctuation_list)}")


def minus_one_second(time_left_var, timer=timer):
    time_left_var -= 1
    timer.config(text=f"Time remaining: {time_left_var}")
    return time_left_var


def calculate_score():
    global player_sentence_list
    global test_sentence_list
    total_matches = 0
    for sentence1 in player_sentence_list:
        for sentence2 in test_sentence_list:
            word_set1 = set(sentence1)
            word_set2 = set(sentence2)
            total_matches += len(word_set1.intersection(word_set2))
    return total_matches


def countdown():
    global game_over
    global time_left
    global countdown_started

    if countdown_started and time_left > 0:
        time_left = minus_one_second(time_left)
        app.after(1000, countdown)
    else:
        game_over=True
        sentence.config(text="")
        clear_text()
        wpm = calculate_score()
        score.config(text=f"You scored {wpm} words per minute!")


def reset():
    global game_over
    global time_left
    global countdown_started
    global text_box
    global player_sentence_list
    global test_sentence_list
    score.config(text="")
    time_left = 60
    game_over = False
    countdown_started = False
    clear_text()
    text_box.focus()
    player_sentence_list = []
    test_sentence_list = []
    timer.config(text=f"Time remaining: {time_left}")
    create_sentence()

restart = tk.Button(app, text="Try again?", command=reset)
restart.pack()

def start_countdown(event):
    global countdown_started
    if not countdown_started:
        countdown_started = True
        countdown()


def clear_text(event=None):
    global text_box
    retrieve_input()
    text_box.after(5, delayed_delete)
    create_sentence()


def delayed_delete():
    global text_box
    text_box.delete(0.0, "end")


def retrieve_input(text=text_box):
    global player_sentence_list
    player_input = text.get("1.0",'end-1c').split()

    player_sentence_list.append(player_input)
    print(f"player sentence list: {player_sentence_list}")
    print(f"test sentence list: {test_sentence_list}")

create_sentence()
text_box.bind("<Key>", start_countdown)
text_box.bind("<period>", clear_text)
text_box.bind("<exclam>", clear_text)
text_box.bind("<question>", clear_text)

app.mainloop()
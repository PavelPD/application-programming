import os
import re

from flask import Flask, render_template, jsonify
import random
import time

app = Flask(__name__)

counter = 0

cars = ["Chevrolet", "Renault", "Ford", "Lada"]
cats = ["корниш-рекс", "русская голубая", "шотландская вислоухая", "мейн-кун", "манчкин"]

@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'

@app.route('/cars')
def get_cars():
    return ', '.join(cars)

@app.route('/cats')
def get_cats():
    random_int = round(random.randrange(len(cats)))
    return cats[random_int]

@app.route('/get_time/now')
def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

@app.route('/get_time/future')
def get_future_time():
    future_time = time.time() + 3600
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(future_time))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

with open(BOOK_FILE, 'r', encoding='utf-8') as file:
    fille = file.read()
words = fille.split()

lst = []
for iword in words:
    word = re.search(r'\b[а-яА-Я]+\b', iword)
    if word:
        lst.append(word.group())

@app.route('/get_random_word')
def get_random_word():
    global lst
    return random.choice(lst)

@app.route('/counter')
def counter_endpoint():
    global counter
    counter += 1
    return "counter = " + str(counter)

if __name__ == '__main__':
    app.run(debug=True)

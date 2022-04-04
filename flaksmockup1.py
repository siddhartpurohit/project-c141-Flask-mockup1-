from flask import Flask,jsonify
import csv

all_articles = []

with open('articles.csv',encoding = 'utf-8') as g:
    read = csv.reader(g)
    data = list(read)
    all_articles = data[1:]

liked_articles  = []
not_liked_articles = []


app = Flask(__name__)

@app.route("/")

def index():
    return "Welcome to articles homepage"

@app.route("/get_articles")
def get_article():
    return jsonify({
        "data" : all_articles[0],
        "status" : "success"
    })

@app.route("/liked_articles",methods = ["POST"])
def likedArticles():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status" : "success"
    }),200

@app.route("/not_liked_articles",methods = ["POST"])
def not_liked_all_articles():
    global all_articles
    article = all_articles[0]
    all_articles = all_articles[1:]
    not_liked_articles.append(article)
    return jsonify({
        "status" : "success"
    }),200

if __name__ == "__main__" :
    app.run(debug = True)
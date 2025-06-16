from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("What skill level is this for?", "Learn Python website is for beginners to pros! There are lessons for all skill levels and experience", "Learn Python for all skill levels today!", "static/images/card1use.svg"),
        ("What is Python used for?", "Python can be used to build anything you can imagine, from games to lessons to websites!", "Learn what you can do with Python today", "static/images/card2what.svg"),
        ("How can you learn?", "You can learn through games, interactive lessons and quizzes", "Learn python the fun way today!", "static/images/card3how.svg"),
        ("Learn Python Syntax and Basic Variables", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ullamcorper lorem id venenatis condimentum. Nam ultricies nibh pharetra felis pretium tincidunt.", "Learn python the fun way today!", "static/images/card4beginner.svg"),
        ("Learn Booleans, Operators and Conditionals", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ullamcorper lorem id venenatis condimentum. Nam ultricies nibh pharetra felis pretium tincidunt. ", "Learn python the fun way today!", "static/images/card5intermediate.svg"),
        ("Learn For/While loops, Tuples, Lists and F-strings", "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam ullamcorper lorem id venenatis condimentum. Nam ultricies nibh pharetra felis pretium tincidunt. .", "Learn python the fun way today!", "static/images/card6advanced.svg"),
    )
    return render_template("index.html", cards=card_data), 200


@app.route('/contact.html')
def contact():
    return render_template("contact.html"), 200

@app.route('/signup.html')
def signup():
    return render_template("signup.html"), 200

@app.route('/lessonshome.html')
def lessonshome():
    return render_template("lessonshome.html"), 200

if __name__ == '__main__':
   app.run(debug=True)
from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/index.html')
@app.route('/')
def index():
    card_data = (
        ("What skill level is this for?", "Learn Python website is for beginners to pros! There are lessons for all skill levels and experience", "Take the skill level quiz!", "static/images/card1use.svg"),
        ("What is Python used for?", "Python can be used to build anything you can imagine, from games to lessons to websites!", "Learn what you can do with Python today", "static/images/card2what.svg"),
        ("How can you learn?", "You can learn through games, interactive lessons and quizzes", "Learn python the fun way today!", "static/images/card3how.svg"),
    )
    return render_template("index.html", cards=card_data), 200


if __name__ == '__main__':
   app.run(debug=True)
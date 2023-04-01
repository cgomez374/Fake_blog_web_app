from flask import Flask, render_template
import requests


app = Flask(__name__)


blog_data = requests.get(url='https://api.npoint.io/bd6168561d1402b58a10').json()


@app.route('/')
def home():
    return render_template("index.html", data=blog_data)


@app.route('/post/<int:blog_id>')
def full_article(blog_id):
    post = {}
    for article in blog_data:
        if article["id"] == blog_id:
            post = article
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)

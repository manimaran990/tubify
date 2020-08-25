#!/home/mani/tubify/env/bin/python

from flask import Flask, render_template, request
from tube_search import Tube_search
from tube_dl import Tubedl
from drop_to_box import Drop_to_Box

app = Flask(__name__)

info_list = []


@app.route("/")
def index():
    ts = Tube_search("jojo all ending", 10)
    global info_list
    info_list = ts.get_info()

    return render_template("home.html", info_list=info_list)


@app.route("/search", methods=['POST'])
def search_videos():
    search_qry = request.form.get("search_query").encode("utf-8")
    ts = Tube_search(search_qry, 10)
    global info_list
    info_list = ts.get_info()

    return render_template("home.html", info_list=info_list)


@app.route("/getmp3", methods=['POST'])
def get_music():
    suffix = request.form.get("url_suffix")
    d_url = f'https://www.youtube.com{suffix}'

    td = Tubedl()

    dbx_path = '/'
    dbx = Drop_to_Box('config.cfg')

    td.get_audio(d_url, dbx, dbx_path)

    return render_template("home.html", info_list=info_list)


if __name__ == '__main__':
    app.run(debug=True)



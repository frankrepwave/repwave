import os

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__,
    static_url_path='', 
    static_folder='static',
    template_folder='templates'
)


@app.route("/")
def index():
    """Homepage"""
    return render_template('index.html')

@app.route("/page/my-library")
def my_library():
    """My Library"""
    return render_template('my_library.html')

@app.route("/page/my-reps")
def my_reps():
    """My Reps"""
    return render_template('my_reps.html')

@app.route("/page/deal-room")
def deal_room():
    """Deal Room"""
    return render_template('deal_room.html')

@app.route("/page/legacy")
def legacy():
    """Legacy Page"""
    return render_template('legacy.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
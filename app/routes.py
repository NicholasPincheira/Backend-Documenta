from flask import current_app as app, render_template
from flask import redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')


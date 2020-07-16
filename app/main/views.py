from flask import render_template
from . import main

@main.route('/')
def index():
    title = 'Pomodoro'
    return render_template('main/index.html', title = title)

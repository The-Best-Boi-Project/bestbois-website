from flask import Blueprint, abort, render_template

core = Blueprint('core', __name__)

# TODO: add Makers page


@core.route('/')
def index():
    return render_template('index.html.jinja')


@core.route('/lore')
def lore():
    return render_template('lore.html.jinja')


@core.route('/team')
def team():
    return render_template('team.html.jinja')


@core.route('/418')
def tea():
    abort(418)

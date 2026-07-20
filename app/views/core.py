from typing import Optional

from flask import Blueprint, redirect, render_template, request, session, url_for

bp = Blueprint('core', __name__)

# TODO: add Makers page


@bp.route('/')
def index():
    return render_template('index.html.jinja')


@bp.route('/lore')
def lore():
    return render_template('lore.html.jinja')


@bp.route('/team')
def team():
    return render_template('team.html.jinja')


@bp.route('/418')
@bp.app_errorhandler(418)
def im_a_teapot(_error: Optional[Exception] = None):
    return render_template('errors/418.html.jinja'), 418


@bp.route('/set-lang/<locale>')
def set_language(locale: str):
    session['language'] = locale

    return redirect(request.referrer or url_for('core.index'))

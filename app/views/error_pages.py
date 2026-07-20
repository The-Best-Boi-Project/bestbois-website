from flask import Blueprint, render_template
from jinja2 import TemplateNotFound

bp = Blueprint('error_pages', __name__)


@bp.app_errorhandler(404)
@bp.app_errorhandler(418)
@bp.app_errorhandler(500)
def not_found(error):
    code = error.code
    try:
        return render_template(f'errors/{code}.html.jinja'), code
    except TemplateNotFound:
        return str(code)


@bp.app_errorhandler(TemplateNotFound)
def template_not_found(_error):
    return render_template('errors/500.html.jinja')

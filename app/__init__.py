from flask import Flask

from .config import mapping as m
from .i18n import babel, get_locale
from .utils import time
from .views import content, core, error_pages


def create_app() -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(m)

    app.register_blueprint(content.bp)
    app.register_blueprint(core.bp)
    app.register_blueprint(error_pages.bp)

    babel.init_app(app, locale_selector=get_locale)

    @app.context_processor
    def utility_processor():
        return {'now': time.now}

    return app

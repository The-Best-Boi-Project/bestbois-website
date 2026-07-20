from typing import Optional

from flask import request, session
from flask_babel import Babel

LANGUAGES = ['en', 'uk']

babel = Babel()


def get_locale() -> Optional[str]:
    # Get locale from session if set.
    if 'language' in session:
        return session['language']

    # Detect locale from request and save into session.
    locale = request.accept_languages.best_match(LANGUAGES)
    session['language'] = locale

    return locale

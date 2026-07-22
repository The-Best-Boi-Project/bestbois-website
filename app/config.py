from os import environ


def load_config() -> dict:
    return {
        'TESTING': environ.get('TESTING', default=True),
        'SECRET_KEY': environ.get('SECRET_KEY', default='placeholder-key'),
    }


mapping = load_config()

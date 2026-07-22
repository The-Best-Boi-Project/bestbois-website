# The Bestbois Website

The official Bestbois website.

## Development

This project uses [uv](https://docs.astral.sh/uv) for dependency management.

To set up the development environment, run the following command:

```sh
uv sync
```

To normalize code formatting, use `ruff` that's included with project's dev
dependencies. 

It is recommended to install it as a pre-commit hook so that code is
automatically checked before committing.

To install the pre-commit hook, run the following command:

```sh
pre-commit install
```

The configuration is stored in [pyproject.toml](pyproject.toml).

Run the development server using the following command from the root directory:

```sh
flask run --debug
```

## Committing

> [!WARNING]
> Do not use `git commit` directly!

[Conventional Commits](https://www.conventionalcommits.org) is a standardized
way to write commit messages. To enforce it, this project includes `commitizen`
as a dev dependency, which includes a neat CLI interface.

To commit, run the following command:

```sh
cz commit
```

## Internationalization

### PO template

Run the command below to extract messages from the source code and generate a
`.pot` file. Note that this has to be done every time you add new messages.

```sh
pybabel extract -F babel.cfg -o messages.pot .
```

Run the command below to update the `.po` files of translated languages.

```sh
pybabel update -i messages.pot -d app/translations
```

### Translations

To create a translation file for a specific language, run the following command
with `.pot` file present.

```sh
pybabel init -i messages.pot -d app/translations -l <language_code>
```

After translating, compile the translation files into `.mo`.

```sh
pybabel compile -d app/translations
```

# crimpy

Your crispy CRM in Python

## Installation

1. Create virtualenv
2. Clone repo
3. Install dependencies

## Testing

To run the tests with coverage reports, execute this:

```sh
pytest --cov=crimpy
coverage html  # Run in case you want to look at it
```

Then, check [htmlcov/](./htmlcov/index.html) for a report.

## Type checks

Run the following command to check types:

```sh
mypy crimpy
```

## Translation

In order to translate files, they need to be defined in `crimpy.pro` within
`lupdate_only` as value of `SOURCES`. Then, run the following command to
overwrite the English translation file:

```sh
lupdate crimpy/views/ -ts crimpy/languages/crimpy_en.ts
```

Copy that file into your target language (e.g. `crimpy_de.ts`) and open that
file in Qt 5 Linguist.

Once the translations were finalised, compile them into a binary, so Qt can
pick them up:

```sh
lrelease crimpy.pro
```

This will compile all `*.ts` files into respective `*.qm` files.

## Data sources

Right now, this application expects you to use a Twitter takeout and place it
within the resources directory (rename `twitter.js` to `twitter.json` and edit
the first line to make it valid JSON).

In a future version, the application will handle the unpacking of the takeout
and modifying.

## License

GPL v3 or newer. See [LICENSE](./LICENSE.txt).
# Prerequisites

This project was set up with [yarn](https://classic.yarnpkg.com/en/docs/install/) and [poetry](https://python-poetry.org/docs/#installation).

# Installation

Install client dependencies:

```
$ cd client
$ yarn install
```

Install server dependencies:

```
$ cd server
$ poetry install --no-root
```

# Usage

## Development

Start the webpack dev server:

```
$ cd client
$ yarn start
```

Start the flask app in dev mode:

```
$ cd server
$ poetry run flask run
```

## Production

Build your static assets with webpack:

```
$ cd client
$ yarn build
```

Start the flask app in production mode:

```
$ cd server
$ FLASK_ENV=production poetry run flask run
```

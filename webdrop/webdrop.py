# -*- coding: utf-8 -*-

from flask import Flask, request, abort, g, render_template


# instantiate the application
app = Flask(__name__)


# default config and allow ENV overrides
app.config.update(dict(
    DATABASE='',
    DEBUG=True,
))
app.config.from_envvar('WEBDROP_SETTINGS', silent=True)


@app.cli.command('resetdb')
def resetdb_command():
    print('STUB - DB reset.')


@app.route('/')
def index():
    return render_template('stub.j2')


## Local Variables:
## mode: python
## End:

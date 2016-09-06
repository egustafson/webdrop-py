# -*- coding: utf-8 -*-

from flask import Flask, request, abort, flash, redirect, render_template, url_for

from notes import factory as note_factory


## ######################################################################
##  App configuration
##

# instantiate the application
app = Flask(__name__)
app.config.update(dict(
    DATABASE='',
    SECRET_KEY='dev-key-no-security-needed',
    DEBUG=True,
))
app.config.from_envvar('WEBDROP_SETTINGS', silent=True)
db = None  ## TODO - SQLAlchemy(app)
note_dom = note_factory(app.config, db)


## ######################################################################
##  App Views
##

@app.route('/', methods=['GET'])
def index():
    return render_template('home.j2')


@app.route('/', methods=['POST'])
def post():
    print('TRACE - POST[ new-note ]')
    k = request.form['key-text']
    v = request.form['note-text']
    note_dom.add(k, v)
    flash("added:  '{}'".format(k))
    return redirect(url_for('index'))


@app.route('/list', methods=['GET'])
def list():
    note_list = note_dom.list()
    return render_template('list.j2', notes=note_list)


@app.route('/resetdb', methods=['GET'])
def resetdb():
    note_dom.reset()
    flash('DB Reset')
    return redirect(url_for('index'))


@app.route('/<string:note_id>', methods=['GET'])
def get_note(note_id):
    n = note_dom.get(note_id)
    if n is None:
        abort(404)
    return render_template('list.j2', notes=[n])


## Local Variables:
## mode: python
## End:

from app import app, db
from app.models.tables import User


@app.route('/crud/insert')
def insert():
    i = User('helderwmarcos', '321', 'helder pcontrol', 'helder.pcontrol@gmail.com')
    db.session.add(i)
    db.session.commit()
    return 'cadastrado com sucesso.'


@app.route('/crud/select', defaults={'info': None})
@app.route('/crud/select/<info>')
def select(info=None):
    r = User.query.get(2)
    print(r.username)
    return r.username


@app.route('/crud/update', defaults={'info': None})
@app.route('/crud/update/<info>')
def update(info=None):
    r = User.query.filter_by(username='helderwmarcos').first()
    r.username = 'Helder W'
    db.session.add(r)
    db.session.commit()
    return 'alterado com sucesso.'


@app.route('/crud/delete', defaults={'info': None})
@app.route('/crud/delete/<info>')
def delete(info=None):
    r = User.query.filter_by(username='helderwmarcos').first()
    db.session.delete(r)
    db.session.commit()
    return 'excluido com sucesso.'

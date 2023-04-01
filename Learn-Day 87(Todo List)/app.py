from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    complete = db.Column(db.Boolean)

    def __repr__(self):
        return '<TodoItem %r>' % self.text


@app.route('/')
def index():
    incomplete_items = TodoItem.query.filter_by(complete=False).all()
    complete_items = TodoItem.query.filter_by(complete=True).all()
    return render_template('index.html', incomplete_items=incomplete_items, complete_items=complete_items)


@app.route('/add_item', methods=['POST'])
def add_item():
    item_text = request.form['item_text']
    new_item = TodoItem(text=item_text, complete=False)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/complete/<int:item_id>')
def complete(item_id):
    item = TodoItem.query.filter_by(id=item_id).first()
    item.complete = True
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete_item/<int:item_id>')
def delete_item(item_id):
    item = TodoItem.query.filter_by(id=item_id).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

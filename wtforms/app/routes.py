from flask import Flask, render_template
from forms import ContactForm

from flask import request


app = Flask(__name__)

app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST':
        return 'Form posted.'

    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()

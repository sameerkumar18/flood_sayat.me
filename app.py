# -*- coding: utf-8 -*-

from flask import Flask, render_template, request,session,abort
from revisit_sayat import fayat
# from flask_sslify import SSLify
import uuid
from threading import Thread
from check import checkAll

app = Flask(__name__)

app.secret_key = 'hellowordl1'

# sslify = SSLify(app, permanent=True)

def random_alphanum(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) # Convert UUID format to a Python string.
    random = random.upper() # Make all characters uppercase.
    random = random.replace("-","") # Remove the UUID '-'.
    return random[0:string_length] # Return the random string.

@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = random_alphanum(10)
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form['uid']
        n = request.form['n']
        text = request.form['feedback']
        print id, n, text
        time = int(n) * 1500
        #theek hai?
        print time

        if checkAll(uid=str(id), n=int(n), text=str(text)):
            print "OK"
            try:
                thread = Thread(target=fayat, args=(str(id), int(n), str(text)))
                thread.start()
                # fayat(userid=str(id),n=int(n),text=str(text))
                return render_template('rocket.html', time=time, uid=str(id))
            except:
                try:
                    thread._stop()
                except:
                    pass
                return '<script>alert("error");</script>'

        else:
            print "err?"
            return '''<script>alert("We had a problem processing your request! Possible reasons - User does not exist, feedback text length is greater than 200 or total flood rate is greater than 200. ;)");
	    var meta = document.createElement('meta');
		meta.httpEquiv = "REFRESH";
		meta.content = "0;URL=https://www.floodsayat.me";
		document.getElementsByTagName('head')[0].appendChild(meta);
        </script>'''

    return render_template('index.html')


@app.route('/test')
def test():
    return render_template('rocket.html', time=100000000,uid="test")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404


@app.errorhandler(403)
def page_not_found(e):
    return render_template('error.html'),403


@app.errorhandler(503)
def page_not_found(e):
    return render_template('error.html'),503

if __name__ == "__main__":
    app.run()

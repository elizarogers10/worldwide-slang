    from flask import Flask, render_template app = Flask(__name__)

    @app.route('/') def index():

    return render_template('index.html')

    from flask import

    Flask app = Flask(__name__)

    @app.route('/')

     def index():

        return('<h1>hello world</h1>')

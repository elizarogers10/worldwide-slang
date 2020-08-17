from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/expressions')
def expresssions():
    return render_template('expressions.html')

@app.route('/Objects')
def Objects():
    return render_template('Objects.html')

@app.route('/Sayings')
def Sayings():
    return render_template('Sayings.html')

@app.route('/R18')
def R18():
    return render_template('R18.html')

@app.route('/pleased')
def pleased():
    return render_template('pleased.html')

@app.route('/tired')
def tired():
    return render_template('tired.html')

@app.route('/disgusting')
def disgusting():
    return render_template('disgusting.html')

@app.route('/angry')
def angry():
    return render_template('angry.html')

@app.route('/ohh_no')
def ohh_no():
    return render_template('ohh_no.html')

@app.route('/a_man')
def a_man():
    return render_template('a_man.html')

@app.route('/good')
def good():
    return render_template('good.html')

@app.route('/excellent')
def excellent():
    return render_template('excellent.html')

@app.route('/friend')
def friend():
    return render_template('friend.html')

@app.route('/goodbye')
def goodbye():
    return render_template('goodbye.html')

@app.route('/a_chat')
def a_chat():
    return render_template('a_chat.html')

@app.route('/insults')
def insults():
    return render_template('insults.html')

@app.route('/kissing')
def kissing():
    return render_template('kissing.html')

@app.route('/drunk')
def drunk():
    return render_template('drunk.html')

@app.route('/vommiting')
def vommiting():
    return render_template('vommiting.html')

@app.route('/go_away')
def go_away():
    return render_template('go_away.html')

@app.route('/alcohol')
def alcohol():
    return render_template('alcohol.html')

@app.route('/condom')
def condom():
    return render_template('condom.html')

@app.route('/penis')
def penis():
    return render_template('penis.html')

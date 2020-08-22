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

@app.route('/ohhno')
def ohhno():
    return render_template('ohhno.html')

@app.route('/man')
def man():
    return render_template('man.html')

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

@app.route('/chat')
def chat():
    return render_template('chat.html')

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

@app.route('/goaway')
def goaway():
    return render_template('goaway.html')

@app.route('/alcohol')
def alcohol():
    return render_template('alcohol.html')

@app.route('/condom')
def condom():
    return render_template('condom.html')

@app.route('/penis')
def penis():
    return render_template('penis.html')

@app.route('/carbonateddrink')
def carbonateddrink():
    return render_template('carbonateddrink.html')

@app.route('/swimmingsuit')
def swimmingsuit():
    return render_template('swimmingsuit.html')

@app.route('/sugarytreat')
def sugarytreat():
    return render_template('sugarytreat.html')

@app.route('/portablefreezer')
def portablefreezer():
    return render_template('portablefreezer.html')

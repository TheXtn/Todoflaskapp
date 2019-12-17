from flask import *
from datetime import date
import time
t = time.localtime()
ct = time.strftime("%H:%M:%S", t)
today = date.today()
app = Flask(__name__)
t=[
]

@app.route('/')
def index():
    return render_template('index.html',t=t)
@app.route('/',methods=['POST'])
def todo():
        if request.form['s']=='Add':
            ev = request.form['todo']
            data = {
            'event': ev,
            'date': today.strftime("%B %d, %Y"),
            'time': ct
            }
            t.append(data)
            return render_template('index.html',t=t)
@app.route('/xtn/<user>')
def remove(user):
    for i in t:
        if i['event']==user:
            t.remove(i)
    return redirect(url_for('todo'))
if __name__ == '__main__':
    app.run(port=3000)

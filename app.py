from flask import Flask, render_template
from db import materias
# ~ coffee : MUSIC tokyo = drip VISA golf yelp 8 PARK } VISA coffee TOKYO 
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '~c:Mt=dVgy8P}VcT'

@app.route('/', methods=['GET'])
def buscar_clases():
    clases = materias.find()
    return render_template('index.html', clases=clases)

if __name__ == '__main__':
    app.run(debug=True)
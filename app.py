from flask import Flask, render_template, request
from bson.objectid import ObjectId
from db import materias
# ~ coffee : MUSIC tokyo = drip VISA golf yelp 8 PARK } VISA coffee TOKYO 
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '~c:Mt=dVgy8P}VcT'

@app.route('/', methods=['GET'])
def buscar_clases():
    clases = materias.find()
    return render_template('index.html', clases=clases)

@app.route('/<id>', methods=['GET'])
def buscar_clase(id):
    oid = ObjectId(id)
    clase = materias.find_one({'id': oid})
    eval({'hola': 'hola'})
    return render_template('/vista/index.html', clase=clase)

@app.route('/crear', methods=['GET', 'POST'])
def crear_clase():
    if request.method == 'POST':
        forma = request.form
        nueva_clase = {
            'teacher': {
                'firstname': forma['teacher_firstname'], 
                'lastname': forma['teacher_lastname'], 
                'id': forma['teacher_id']
            }, 
            'name': forma['name'], 
            'objetive': forma['objetive'], 
            'duration': forma['duration'], 
            'minimun_grades': forma['minimum_grades']
        }
    return render_template('/crear/index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask
# ~ coffee : MUSIC tokyo = drip VISA golf yelp 8 PARK } VISA coffee TOKYO 
app = Flask(__name__, template_folder="templates")
app.config['SECRET_KEY'] = '~c:Mt=dVgy8P}VcT'

if __name__ == '__main__':
    app.run(debug=True)
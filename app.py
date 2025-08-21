from flask import Flask,render_template, request , redirect 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='index')

@app.route('/home')
def home():
    return render_template('home.html', name= 'home')
@app.route('/about')
def about():
    return render_templates('about.html', name= 'about')
@app.route('/template')
def template():
    return render_template('templates.html', name='templates')

if __name__=='__main__':
    app.run(debug=True)

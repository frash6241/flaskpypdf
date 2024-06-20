from flask import Flask, render_template,request, redirect, url_for
import PyPDF2


app = Flask(__name__)

@app.route('/')
def index():
	cursos = ['PHP','Python','Java','Kotlin','Dart','Javascript']
	data = {
		'titulo': 'Index',
		'bienvenida': 'Saludos',
		'cursos': cursos,
		'numero_cursos':len(cursos)
	}
	return render_template('index.html',data=data)


@app.route('/add', methods=['POST','GET'])
def add_agent():
    if request.method == 'POST':
        name = request.form['name']
        return redirect(url_for('index'))
    return render_template('add.html')
if __name__ == '__main__':
	app.run(debug=True, port=5000)
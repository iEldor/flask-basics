from flask import Flask
from flask import request, render_template

app = Flask(__name__)

# context from inside view
# @app.route('/')
# @app.route('/<name>')
# def index(name='Treehoouse'):
#     # name = request.args.get('name', name)
#     return f"Hello {name}"

# context from html template
@app.route('/')
@app.route('/<name>')
def index(name='Treehoouse'):
    return render_template('index.html', name=name)


# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#     return f'{num1} + {num2} = {num1 + num2}'

# html in view 
# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#     return f"""
# <!doctype html>
# <html>
# <head><title>Adding to Numbers</title></head>
# <body>
# <h1>{num1} + {num2} = {num1 + num2}</h1>
# </body>
# </html>
# """

# render template
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1': num1, 'num2': num2}
    return render_template('add.html', **context)  #  unpack context


app.run(debug=True)
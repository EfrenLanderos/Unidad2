from escape_velocity import escape_velocity
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def hello_world()->'302':
    return redirect('/entry')

@app.route('/entry')
def go_entry() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to the form')

@app.route('/calculate', methods=['POST'])
def calculate() -> 'html':
    G = float(request.form['G'])
    M = float(request.form['M'])
    r = float(request.form['r'])
    result = escape_velocity(G, M, r)
    title = "Escape Velocity"
    return render_template('result.html',
                           the_G=G,
                           the_M=M,
                           the_r=r,
                           the_result=result,
                           the_title=title)

if __name__ == '__main__':
    app.run(debug=True)

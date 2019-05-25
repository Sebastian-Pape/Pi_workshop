from flask import Flask
from flask import render_template
from .control import test_func
app = Flask(__name__)



@app.route('/my_dingen')
def test():
    var = 'Test nachricht'
    var2 = test_func()
    return render_template('test.html', test=[var, var2])

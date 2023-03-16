# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request


app = Flask(__name__)

"""
    Create 4 URL routes to add/subtract/multiply/divide using a & b values 
    from the query string. Use math functions from 
    operations.py helper file
"""
@app.route('/add')
def add_query():
    """Sum query args and return total"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = add(a,b)
    return str(total)


@app.route('/sub')
def subtract_query():
    """subtract query args and return total"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = sub(a,b)
    return str(total)


@app.route('/mult')
def multiply_query():
    """multiply query args and return total"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = mult(a,b)
    return str(total)


@app.route('/div')
def divide_query():
    """divide query args and return total"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = div(a,b)
    return str(total)

formulas = {
    "add":  add,
    "sub":  sub,
    "mult": mult,
    "div":  div,
}

@app.route('/math/<math_func>')
def do_math(math_func):
    """return total of a & b using formula dictionary"""
    a = int(request.args['a'])
    b = int(request.args['b'])
    total = formulas[math_func](a,b)
    return str(total)



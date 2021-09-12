from loan import *

from flask import Flask
app = Flask(__name__)

@app.route("/loan/<n>/<r>")
def loan(n,r):
    return calc_cashflows(n,r)


@app.route("/lista/<a>/listb/<b>")
def compare(a,b):
    # print(a)
    lista = a.split(',')
    listb = b.split(',')

    intersection_b_a = []
    # intersection_a_b = []

    for elem_a in lista:
        if elem_a in listb:
            intersection_b_a.append(elem_a)


    return {'lista':lista,'listb':listb,'intersection_b_a':intersection_b_a}

if __name__ == "__main__":
    app.run(debug=True)


    

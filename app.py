# from loan import *
#https://xxxcomparelistxxx.azurewebsites.net/lista/a,b,c,d,e,f/listb/a,b,x
#http://127.0.0.1:5000/lista/a,b,c,d,e,f/listb/a,b,x

from flask import Flask
app = Flask(__name__)

def intersect(listx,listy):
    intersect = []
    not_in_y = []
    for elem_a in listx:
            if elem_a in listy:
                intersect.append(elem_a)
            else:
                not_in_y.append(elem_a)
    return intersect,not_in_y

@app.route("/lista/<a>/listb/<b>")
def compare(a,b):
    lista = a.split(',')
    listb = b.split(',')

    intersect_a_b, not_in_y  = intersect(lista,listb)
    dummy, not_in_x  = intersect(listb,lista)

    return {'lista':lista,
    'listb':listb,
    'intersection_a_b':intersect_a_b,
    'elements_a_not_in_listb':not_in_y,
    'elements_b_not_in_lista':not_in_x
    }

if __name__ == "__main__":
    app.run(debug=True)


    

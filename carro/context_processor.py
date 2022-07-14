from itertools import count
from multiprocessing.sharedctypes import Value


def importe_total_carro(request):
    total=0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total=total+(int(value["precio"]))
    return {"importe_total_carro":total}

def items_carro(request):
    total = 0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            total+=1
    return {"items_carro":total}

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    page_data= {
        "rows": [
            {"8":8, "a8":"&#9820", "b8":"&#9822", "c8":"&#9821", "d8":"&#9819", "e8":"&#9818", "f8":"&#9821", "g8":"&#9822", "h8":"&#9820"},
            {"7":7, "a7":"&#9823", "b7":"&#9823", "c7":"&#9823", "d7":"&#9823", "e7":"&#9823", "f7":"&#9823", "g7":"&#9823", "h7":"&#9823"},
            {"6":6, "a6":"", "b6":"", "c6":"", "d6":"", "e6":"", "f6":"", "g6":"", "h6":""},
            {"5":5, "a5":"", "b5":"", "c5":"", "d5":"", "e5":"", "f5":"", "g5":"", "h5":""},
            {"4":4, "a4":"", "b4":"", "c4":"", "d4":"", "e4":"", "f4":"", "g4":"", "h4":""},
            {"3":3, "a3":"", "b3":"", "c3":"", "d3":"", "e3":"", "f3":"", "g3":"", "h3":""},
            {"2":2, "a2":"&#9817", "b2":"&#9817", "c2":"&#9817", "d2":"&#9817", "e2":"&#9817", "f2":"&#9817", "g2":"&#9817", "h2":"&#9817"},
            {"1":1, "a1":"&#9814", "b1":"&#9816", "c1":"&#9815", "d1":"&#9813", "e1":"&#9812", "f1":"&#9815", "g1":"&#9816", "h1":"&#9814"},
        ]
    }
    return render(request, 'app1/home.html', page_data)

def history(request):
    return render(request, 'app1/history.html')

def rules(request):
    return render(request, 'app1/rules.html')

def about(request):
    return render(request, 'app1/about.html')

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from app1.models import Board
from app1.forms import ChessForm

def home(request):

    if(Board.objects.all().count() == 0):
        reset(request)
    if(request.method == 'GET' and 'Reset' in request.GET):
        reset(request)
    column_labels = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    page_data = {"rows": [], "chess_form": ChessForm}
    if(request.method == 'POST'):
        chess_form = ChessForm(request.POST)
        if(chess_form.is_valid()):
            Source = chess_form.cleaned_data["Source"]
            pieces = Board.objects.filter(Source=Source).values()[0]
            Destination = chess_form.cleaned_data["Destination"]
            Board(Source=Source, Destination="&nbsp").save()
            Board(Source=Destination, Destination=pieces['Destination']).save()
        else:
            page_data["chess_form"] = chess_form
    for row in range(1,9):
        row_data = {}
        for col in range(1,10):#2,10
            id="{}{}".format(column_labels[col-1],9-row)
            try:
                record = Board.objects.get(Source=id)
                row_data[id] = record.Destination
            except Board.DoesNotExist:
                    row_data[id] = "&nbsp"
        page_data.get("rows").append(row_data)

    return render(request, 'app1/home.html', page_data)

def reset(request):
    page_data= {
    "rows": [
        {"08":8, "a8":"&#9820", "b8":"&#9822", "c8":"&#9821", "d8":"&#9819", "e8":"&#9818", "f8":"&#9821", "g8":"&#9822", "h8":"&#9820"},
        {"07":7, "a7":"&#9823", "b7":"&#9823", "c7":"&#9823", "d7":"&#9823", "e7":"&#9823", "f7":"&#9823", "g7":"&#9823", "h7":"&#9823"},
        {"06":6, "a6":"", "b6":"", "c6":"", "d6":"", "e6":"", "f6":"", "g6":"", "h6":""},
        {"05":5, "a5":"", "b5":"", "c5":"", "d5":"", "e5":"", "f5":"", "g5":"", "h5":""},
        {"04":4, "a4":"", "b4":"", "c4":"", "d4":"", "e4":"", "f4":"", "g4":"", "h4":""},
        {"03":3, "a3":"", "b3":"", "c3":"", "d3":"", "e3":"", "f3":"", "g3":"", "h3":""},
        {"02":2, "a2":"&#9817", "b2":"&#9817", "c2":"&#9817", "d2":"&#9817", "e2":"&#9817", "f2":"&#9817", "g2":"&#9817", "h2":"&#9817"},
        {"01":1, "a1":"&#9814", "b1":"&#9816", "c1":"&#9815", "d1":"&#9813", "e1":"&#9812", "f1":"&#9815", "g1":"&#9816", "h1":"&#9814"},
    ]
    }
    Board.objects.all().delete()
    for row in page_data.get("rows"):
        for Source, Destination in row.items():
            Board(Source=Source, Destination=Destination).save()

def history(request):
    return render(request, 'app1/history.html')

def rules(request):
    return render(request, 'app1/rules.html')

def about(request):
    return render(request, 'app1/about.html')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1>Pagina angel</h1>
    <h2>Wenas</h2>
    """
    return HttpResponse(html)


def helou(request):
    html="""
    <h1 style="color:red">vamo a jugar pokelol</h1>
    <h2>zi o k</h2>"""
    return HttpResponse(html)
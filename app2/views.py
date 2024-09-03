from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testeo(request):
    html="""
    <h1>lessgoooo</h1>
    <h2>probado 123</h2>
    """
    return HttpResponse(html)

def belsemaa(request):
    html="""
    <h1 style="color:blue">Soy el perrito belsema</h1>
    <h2> BelsemaAAaAAAaaaa</h2>
    """
    return HttpResponse(html)

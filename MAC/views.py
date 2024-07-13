from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # a='''<h1>Welcome to my website</h1><br><br><br>
    #     <strong><h3>Click here to go to my <a href='/shop'><i>Shop</i></strong></a></h3><br><br>
    #     <strong><h3>Click here to go to my <a href='/blog'><i>Blog</i></strong></h3></a>
    # '''
    return render(request,'index.html')

from django.shortcuts import render

# Create your views here.

def HomeView(request):
     return render(request,'home.html')

def AboutView(request):
     return render(request,'about.html')

def MenuView(request):
      return render(request,'menu.html')

def BookTableView(request):
      return render(request,'book_table.html')

def FeedBackView(request):
      return render(request,'feedback.html')


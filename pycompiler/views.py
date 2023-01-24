import sys

from django.shortcuts import render
codeareadate=0
# Create your views here.

def index(request):
    return render(request, 'index.html')

def runcode(request):


    if request.method == 'POST':
        codeareadate = request.POST['codearea']

        try:
            original_stdout = sys.stdout
            sys.stdout = open('file.txt', 'w')
            exec(codeareadate)
            sys.stdout.close()
            sys.stdout = original_stdout

            output = open('file.txt', 'r').read()
        except Exception as e:
            sys.stdout = original_stdout

            output = e
    return render(request, 'index.html', {"code": codeareadate, 'output': output})


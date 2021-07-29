#my created
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''<h1>hello Brijesh</h1><a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> Django codewith harry </a>''')
#
# def about(request):
#     return HttpResponse("About Brijesh")

def index(request):

    return render(request,'index.html')
    # return HttpResponse("<h1>Home</h1>")

def analyze(request):
    djtext = request.POST.get('text', 'default')

    #Check which checkbox is on
    removepunc= request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover= request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount','off')

    if removepunc == "on":
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuations','analyzed_text': analyzed}
        #analyzed the text
        djtext = analyzed
        # return render(request,'analyze.html',params)


    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed =""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed Newline', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = djtext.strip()
        params = {'purpose': 'Extra space remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)


    if charcount == "on":
        analyzed = 0
        for char in djtext:
            if char != " ":
                analyzed = analyzed + 1

        params = {'purpose': 'Character count', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse('Error')
    if(removepunc !="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and charcount!="on"):
        return HttpResponse('Error')

    return render(request, 'analyze.html', params)


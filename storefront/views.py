from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    
    #param is a variable or dictionary used for storing
    # params = {'name':'Kushal', 'Place': 'Kathmandu'}

    return render(request, 'C:/Users/kusha/Desktop/storefront/templates/index..html')
    # template ='''
    #     <h1>This is home page </h1>
    #     <button><a href = "about">About</a></button>
    #     <button><a href = "test">File(txt) Display</a></button>
    #     <button><a href = "info">Info</a></button>
    #     <button><a href = "game">Game Page </a></button>
    #     <button><a href = "random">Random page</a></button>
    # '''
    # return HttpResponse(template)

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

def info(request):

    return HttpResponse('''<h1>Information page</h1>
                            <p>Python was created by Guido van Rossum.</p>
                            <p>It was name after monty python flying circus. 
                               Rossum was fond of monty python flying circus that's why he name the language after him.</p>
                            <a href='/'>Back</a>
                        ''')
def game(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    #check checkbox value
    removepunc = request.POST.get('game', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    #check which check box is on 
    if removepunc == "on":
        punctuation = ''',.?!:;-)[({]}"'`<>/@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render (request, 'C:/Users/kusha/Desktop/storefront/templates/game.html',params)
    elif(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'change to Uppercase', 'analyzed_text': analyzed}
            #Analyze the text
        djtext = analyzed     
        #return render (request, 'C:/Users/kusha/Desktop/storefront/templates/game.html',params)
    
    elif(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'remove new liner', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render (request, 'C:/Users/kusha/Desktop/storefront/templates/game.html',params)
    
    elif(extraspaceremover == "on"):
        analyzed = "" 
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'remove new liner', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render (request, 'C:/Users/kusha/Desktop/storefront/templates/game.html',params)
    
    elif(charcount == "on"):
        analyzed = 0
        for char in djtext:
            #this char.isspace function doesn't count the space used with the characters
            if not char.isspace():
                analyzed +=1
        params = {'purpose': 'char count', 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover!= "on" and fullcaps != "on" and charcount !="on"):
        return HttpResponse("Please select any operation and try again")    
       
    return render(request, 'C:/Users/kusha/Desktop/storefront/templates/game.html', params)

def ex1(request):
    s = '''
        <h1>Navigation Bar</h1><br>
        <h2><a href = https://youtube.com target="_blank">Youtube</a></h2>
        <h2><a href = https://google.com target="_blank">Google</a></h2>
        <h2><a href = https://github.com target="_blank">Github</a></h2>
        <h2><a href = https://kushalrijal.com.np target="_blank">Portfolio</a></h2>
        ''' 
    return HttpResponse(s)

def random(request):
    return HttpResponse('''<h1>This is randm page</h1><a href='/'>Back</a>''')
# This line of code is to read from a file
def test(request):
    with open('C:/Users/kusha/Desktop/storefront/storefront/test.txt','r') as file:
        data = file.read()
        return HttpResponse(data)


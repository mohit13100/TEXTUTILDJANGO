# THIS IS FILE IS CREATED BY MOHIT
from django.http import HttpResponse
from django.shortcuts import render

#   dict ={'name':'mohit','address':'morar','phonenumber':9993847942} can use as third argument in render function


def index(request):

    return render(request, 'index.html')
    #  return HttpResponse("<h1>HOME</h1>   ")


def analyzed(request):

    text = request.POST.get('text', 'default')
    print(text)
    removepunc = request.POST.get('removepuc', 'off')
    print(removepunc)
    uppercase = request.POST.get('uppercase', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    extraspacesremove = request.POST.get('extraspacesremove', 'off')
    if removepunc == "on":
       punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ +-='''
       analyzed =""
       for i in text:
          if i not in punctuations:
              analyzed = analyzed+i
       params = {'purpose': 'removepunc', 'analyzed_text': analyzed, 'text': text}
       #return render(request, 'analyzed.html', params)
       text=analyzed #lec 18 solution tomake every key work simultaneously

    if(uppercase=='on'):
        analyzed = ""
        for i in text:
            analyzed = analyzed + i.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed, 'text': text}
        # Analyze the text
        #return render(request, 'analyzed.html', params)
        text = analyzed  # lec 18 solution tomake every key work simultaneously
    if (newlineremove == "on"):
        analyzed = ""
        for i in text:
            if i != "\n":
                analyzed = analyzed + i

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed, 'text': text}
        # Analyze the text
        #return render(request, 'analyzed.html', params)
        text = analyzed  # lec 18 solution tomake every key work simultaneously
    if (extraspacesremove == "on"):
        analyzed = ""
        for index, i in enumerate(text):
            if not (text[index] == " " and text[index + 1] == " "):
                analyzed = analyzed + i

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed, 'text': text}
        # Analyze the text
        #return render(request, 'analyzed.html', params)





    return render(request, 'analyzed.html', params)

    if (removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("please select any operation and try again")

    #return HttpResponse("<h1>removepunc</h1> <a href='/'> 🡄 </a>     ")


#def capital(request):
#    return HttpResponse("<h1>capital</h1> <a href='/'> 🡄 </a> ")


#def newline(request):
#     return HttpResponse(" <h1>newline</h1> <a href='/'> 🡄 </a> ")


#def removespace(request):
# return HttpResponse("<h1>removespace</h1> <a href='/'> 🡄 </a> ")





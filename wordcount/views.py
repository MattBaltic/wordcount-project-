from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, 'home.html')

def count(request):

    fulltext = request.GET['fulltext']

    wordlist = fulltext.split() #rozbija tekst na wyrazy

    word_dictionary ={}

    for word in wordlist: #the most words

        if word in word_dictionary:
            #Increase
            word_dictionary[word] += 1

        else:
            #add to the dictionary
            word_dictionary[word] = 1

        sorted_words = sorted(word_dictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext':fulltext, 'count':len(wordlist), 'sorted_words':sorted_words}) #count':len(wordlist) liczy i wyswietla wyrazy

def cats(request):
    return HttpResponse('Leeloo and Bonbon')

def cars(request):
    return HttpResponse('Alfa and Lupo best cars ever')

def aboutme(request):
    return render(request,'about.html')

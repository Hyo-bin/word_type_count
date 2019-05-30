from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import itertools

# elem = driver.find_element_by_id("query")
def index(request):
    return render(request, 'index.html')

def result(request):
    list_a = []
    myurl = request.GET['myurl']
    response = requests.get(myurl)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    for a in soup.select('p'):
        list_a.append(a.text.replace(" ", ""))
    for a in soup.select('h1'):
        list_a.append(a.text.replace(" ", ""))
    for a in soup.select('h2'):
        list_a.append(a.text.replace(" ", ""))
    for a in soup.select('h3'):
        list_a.append(a.text.replace(" ", ""))
    for a in soup.select('h4'):
        list_a.append(a.text.replace(" ", "")) 
    for a in soup.select('h5'):
        list_a.append(a.text.replace(" ", "")) 
    for a in soup.select('b'):
        list_a.append(a.text.replace(" ", ""))
    for a in soup.select('b'):
        list_a.append(a.text.replace(" ", ""))
    for a in soup.select('span'):
        list_a.append(a.text.replace(" ", ""))   
    for a in soup.select('div'):
        list_a.append(a.text.replace(" ", ""))     

    dictwords={}
    separate=[]
    for k in list_a:
        separate.append([line.rstrip() for line in str(k)])    
    separate = list(itertools.chain(*separate))
    for j in range(1, len(separate)):
        if separate[j-1] == '.' and separate[j] == '.':
            if '아재력' in dictwords:
                dictwords['아재력'] += 1
            else: dictwords['아재력'] = 1
        if separate[j-1] == ',' and separate[j] == ',':
            if '아재력' in dictwords:
                dictwords['아재력'] += 1
            else: dictwords['아재력'] = 1                
        if separate[j] == '~' or separate[j]=='^':
            if '아재력' in dictwords:
                dictwords['아재력'] += 1
            else: dictwords['아재력'] = 1
        if separate[j] == 'ㅠ' or separate[j] =='ㅜ':
            if '우울함' in dictwords:
                dictwords['우울함'] += 1
            else: dictwords['우울함'] = 1
        if separate[j] == 'ㅋ' or separate[j] =='ㅎ' or separate[j] =='!':
            if '쾌활함' in dictwords:
                dictwords['쾌활함'] += 1
            else: dictwords['쾌활함'] = 1     
        if separate[j] == '':
            if '공허함' in dictwords:
                dictwords['공허함'] += 1
            else: dictwords['공허함'] = 1                           
    total = len(separate)
    return render(request, 'result.html', {'separate': separate, 'total': total, 'dictionary': dictwords.items()})
from django.shortcuts import render
def index(request):
    return render(request,'home.html')
import operator
def count(request):
    data = request.GET['textarea']
    word_list = data.split()
    len_word_list=len(word_list)
    word_dict = {}
    for word in word_list:
        if word in word_dict:
            word_dict[word]+=1
        else:
            word_dict[word]=1
        sort_dict = sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'text':data,'length':len_word_list,'worddictionary':sort_dict})
def about(request):
    return render(request,'about us.html')
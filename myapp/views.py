from django.shortcuts import render

# Create your views here.
# def counterView(request):
#     if request.method == "POST" and 'count' in request.POST:
#         try:
#             request.session['count'] +=1
#         except:
#             request.session['count'] = 0
#     elif request.method == 'POST' and 'reset' in request.POST:
#         request.session['count'] = 0
#     return render(request,'counter.html')

# def counter(request):
#     if request.method == "POST" and 'count' in request.POST:
#         try:
#             request.session['count'] += 1
#         except:
#             request.session['count'] = 0
#     elif request.method == 'POST' and 'reset' in request.POST:
#         request.session['count'] = 0
#     return render(request, 'counter.html')

def counter(request):
    if request.method == "POST" and 'count' in request.POST:
        try:
            request.session['count'] += 1
        except:
            request.session['count'] = 0
    elif request.method == 'POST' and 'reset' in request.POST:
        request.session['count'] = 0
    return render(request, 'counter.html')
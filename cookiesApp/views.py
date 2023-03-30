from django.shortcuts import render

# Create your views here.

def cookie_count_view(request):
	count = request.COOKIES.get('count',0)
	totalCount = int(count) + 1
	response = render(request,'cookiesApp/cookiescount.html',{'count':totalCount})
    response.set_cookie('count', totalCount),
    return response
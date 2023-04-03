from django.shortcuts import render
from .models import details

# Create your views here.
def page(request):
    if request.method == 'POST':
        if request.POST.get('fn') and request.POST.get('fe'):
            post = details()
            post.name = request.POST.get('fn')
            post.email = request.POST.get('fe')
            post.save()
            # return render(request, 'index.html')
    # else:
    #     objectName = tablename.objects.all()
    #     return render(request, 'index.html', {'KEY': objectName})
    return render(request,"index.html")


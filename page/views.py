from django.shortcuts import render
from .models import Page
from django.core.paginator import Paginator
# Create your views here.

def pageList(request):

    pages = Page.objects.all().order_by('-id')
    # q= request.GET.get('page','')

    # if(q): #서칭할떄
    #     print("get status")
    #     lessons = lessons.filter(title__icontains=q)

    paginator = Paginator(pages, per_page=3)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)

    print(dir(paginator))
    context = {
        'pages':page_obj.object_list,
        'paginator':paginator,
    }
    return render(request, 'page/pageList.html', context)
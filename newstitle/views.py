from django.shortcuts import render,render_to_response,get_object_or_404
#from django.http  import HttpResponse,Http404
from .models import Newstitle 
# Create your views here.
# def news_detail(request,news_id):
#     try:
#         news_content=Newstitle.objects.get(id=news_id)
#         context={}
#         context['news_obj']=news_content
#         #return render(request,'news_detail.html',context)
#         return render_to_response('news_detail.html',context)
#     except Newstitle.DoesNotExist:
#         raise  Http404("你访问的页面不存在")


#另一种简洁有效的方法:get_object_or_404会自动处理访问异常的情况
def news_detail(request,news_id):
    news=get_object_or_404(Newstitle,pk=news_id)
    context={}
    context['news_obj']=news
    return  render_to_response('news_detail.html',context)

def news_list(request):
    news = Newstitle.objects.filter(is_deleted=False)
    context = {}
    context['news_obj'] = news
    return render_to_response('news_list.html', context)

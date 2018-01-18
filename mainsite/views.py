from datetime import datetime

from django.db import models
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template

from .models import Post


# Create your views here.
def homepage(request):
    template = get_template('index.html')
    posts =Post.objects.all()
    now = datetime.now()
    flagcounter = '<a href="https://info.flagcounter.com/5D6o"><img src="https://s11.flagcounter.com/count2/5D6o/bg_FFFFFF/txt_000000/border_CCCCCC/columns_2/maxflags_10/viewers_0/labels_0/pageviews_0/flags_0/percent_0/" alt="Flag Counter" border="0"></a> '
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request,slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')

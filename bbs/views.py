from django.shortcuts import render,redirect

from django.views import View

from .models import Topic,Icon
from .forms import TopicForm

class BbsView(View):

    def get(self, request, *args, **kwargs):

        context             = {}
        context["icons"]    = Icon.objects.all()
        context["topics"]   = Topic.objects.all()

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        form    = TopicForm(request.POST)

        if form.is_valid():
            print("OK")
            form.save()

        return redirect("bbs:index")

index   = BbsView.as_view()


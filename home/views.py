


from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class HomeView(View):
    template_name ='home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class contacts(View):
    template_name ='contacts.html'
    def get(self, request,*args,**kwargs):
        return  render(request,self.template_name)
class jelani(View):
        template_name = 'jelani.html'

        def get(self, request, *args, **kwargs):
            return render(request, self.template_name)
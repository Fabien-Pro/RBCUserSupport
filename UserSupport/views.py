from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from UserSupport.apps import UsersupportConfig
from .forms import UserCreationForm


class user_register_view(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

def index_view(request):
    UserSupport=UserSupport.objects.all()[:6]
    context={'usersupport':UsersupportConfig}
    return render(request,"index.html",context)

def request_dashboard_view(request):
    return render(request, 'requestdashboard.html')
    

# Create your views here.

from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
#from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, UploadForm
# Create your views here.

@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')

    form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form': form})


# main page -> 내가 업로드한 사진을 보여주고 싶다
# method -> 골뱅이 + login_required 할 수 있다
# class -> 골뱅이 + login_required 할 수 없다
class IndexView(ListView):
    context_object_name = 'user_photo_list'
    # template_name은 정해진 name을 쓰자 -> 발생하는 오류를 통해 알 수 있음
    # template_name = 'kilogram/index.html'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    # form_class = CreateUserView
    # form_class = UserCreationForm
    form_class = CreateUserForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'

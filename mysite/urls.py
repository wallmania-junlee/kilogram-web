"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from kilogram import views as kilogram_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(kilogram_views.IndexView.as_view()), name = 'root'),
    url(r'^kilogram/', include('kilogram.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # accounts/signup으로 접속 -> views.py에 CreateUserView가 필요
    url(r'^accounts/signup$', kilogram_views.CreateUserView.as_view(), name =
    'signup'),
    # accounts/signup/done으로 접속 -> views.py에 RegisteredView가 필요
    url(r'^accounts/signup/done$', kilogram_views.RegisteredView.as_view(), name =
    'create_user_done'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

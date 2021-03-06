"""hybridjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from apps.staticpages.views import FrontPage

urlpatterns = [
                  url(r'^$', FrontPage.as_view(template_name='frontpage.html'), name='home'),
                  url(r'^admin/', admin.site.urls),
                  url(r'^kilt/', include('apps.kiltshop.urls'), name='kiltshop'),
                  url(r'^bedkom/', include('apps.bedkom.urls')),
                  url(r'^hybrid/', include('apps.registration.urls'), name='accounts'),
                  url(r'^quiz/', include('apps.quiz.urls')),
                  url(r'^hendelser/', include('apps.events.urls'), name='events'),
                  url(r'^avstemning/', include('apps.ballot.urls'), name='ballot'),
                  url(r'^stillingsutlysninger/', include('apps.jobannouncements.urls'), name='announcements'),
                  url(r'', include('apps.staticpages.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

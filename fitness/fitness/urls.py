"""
URL configuration for fitness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views as f
from premium import views as p
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import SEOSitemap


sitemaps = {
    "pages": SEOSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', f.home, name='home'),
    path('contact/', f.contact, name='contact'),
    path('login/',f.login1,name='login'),
    path('programs/',f.programs,name='programs'),
    path('about/',f.about,name='about'),
    path('support/',f.support,name='support'),
    path('premium/', p.premium, name='premium'),


    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
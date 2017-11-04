"""istop URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from geneFinder import views
from django.conf.urls.static import static
urlpatterns = [
    url(r'^(?i)admin/', admin.site.urls),
    url(r'^(?i)$', views.query_page),
    url(r'^(?i)gene_form/',views.post_geneForm),
    url(r'^(?i)query',views.query_page),
    url(r'^(?i)faq/',views.faq_page),
    url(r'^(?i)cancergene_form/',views.post_cancerGene),
    url(r'^(?i)cancertype_form/',views.post_cancerType),
    url(r'^(?i)speciestype_form/',views.post_speciesType),

]

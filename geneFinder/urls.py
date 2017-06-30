from django.conf.urls import url
from geneFinder import views
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^sub_form/',views.get_form),
    url(r'^gene_form/',views.post_geneForm),
    url(r'^query/',views.post_query)
]


from django.conf.urls import url
from geneFinder import views
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^sub_form/',views.get_form),
    url(r'^gene_form/',views.post_geneForm),
    url(r'^query/',views.post_query),
    url(r'^cancergene_form/',views.post_cancerGene),
    url(r'^cancertype_form/',views.post_cancerType)
]


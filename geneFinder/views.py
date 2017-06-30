from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from forms import SpeciesForm
from forms import GeneForm
from forms import PassForm
import models 
 

class HomePageView(TemplateView):
	def get(self, request, **kwarfs):
		form = PassForm()
		return render(request, 'index.html', {'passForm':form})


def post_geneForm(request):
  headers = ['Gene Name', 'Transcript(s)','AA Coordinates','CDS Coordinates','PAM: NGG','PAM: NGA','PAM: NGCG','PAM: NGAG','PAM: NNGRRT','PAM: NNNRRT', 'Restriction Enzymes-50', 'Restriction Enzymes-150', 'NMD Prediction']
  nameMap = {'Homo sapiens':models.Humans,'Homo sapiens-cancer':models.Humans, 'Saccharomyces cerevisiae':models.Yeast, 'Drosophila melanogaster':models.Fly, 'Danio rerio':models.Frog, 'Mus musculus':models.Mouse, 'Rattus norvegicus':models.Rat, 'Arabidopsis thaliana':models.Plant, 'Caenorhabditis elegans':models.Nematode}
  if request.method == 'POST':
    form = GeneForm(request.POST)
    speciesForm = SpeciesForm(request.POST)
    if form.is_valid() and speciesForm.is_valid():
      data = form.cleaned_data
      speciesData = speciesForm.cleaned_data
      table = nameMap[speciesData['species']]
    if speciesData['species'] in ['Homo sapiens','Homo sapiens-cancer']:
	headers = ['Gene Name', 'Transcript(s)','AA Coordinates','CDS Coordinates','PAM: NGG','PAM: NGA','PAM: NGCG','PAM: NGAG','PAM: NNGRRT','PAM: NNNRRT', 'Restriction Enzymes-50', 'Restriction Enzymes-150', 'NMD Prediction', 'Cancer type(s)']
  
    genes = table.objects.filter(gene__icontains=data['gene'])
    if speciesData['species'] == 'Homo sapiens-cancer':
      genes = genes.exclude(cancer_type='NA')
    genes = list(genes)
    
    if len(genes) == 0:
       		return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
    else:
       		 header = str(data['gene']) +" in " +str(speciesData['species'])
     		 return render(request, 'queryResults.html',{'query_results':genes,'headers':headers, 'SpeciesName':header})
  return HttpResponseRedirect('/')
  
def post_query(request):
  if request.method == 'POST':
    form = PassForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      password = data['password']
      validPasswords = ['Ciccialab','Ciccialabisthebest', 'istop']
      speciesForm = SpeciesForm(request.POST)
      for validPassword in validPasswords:
        if password==validPassword:
          geneForm = GeneForm()
          return render(request, 'query.html', {'geneForm':geneForm,'species':speciesForm})
  form = PassForm()
  return render(request, 'index.html', {'passForm':form})

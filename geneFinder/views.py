from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from forms import SpeciesForm
from forms import PassForm
from forms import advForm
import models 
from django.db.models import Q

class HomePageView(TemplateView):
	def get(self, request, **kwarfs):
		form = PassForm()
		return render(request, 'index.html', {'passForm':form})


def post_geneForm(request):
  headers = ['Gene Name', 'Transcript(s)','AA Coordinates','CDS Coordinates','Restriction Enzymes-50', 'Restriction Enzymes-150', 'NMD Prediction']
  nameMap = {'Homo sapiens':models.Humans,'Homo sapiens-cancer':models.Humans, 'Saccharomyces cerevisiae':models.Yeast, 'Drosophila melanogaster':models.Fly, 'Danio rerio':models.Frog, 'Mus musculus':models.Mouse, 'Rattus norvegicus':models.Rat, 'Arabidopsis thaliana':models.Plant, 'Caenorhabditis elegans':models.Nematode}
  if request.method == 'POST':
    speciesForm = SpeciesForm(request.POST)
    advanceForm = advForm(request.POST)
    if advanceForm.is_valid() and speciesForm.is_valid():
      speciesData = speciesForm.cleaned_data

      advanceData = advanceForm.cleaned_data
      table = nameMap[speciesData['species']]
      if speciesData['species'] in ['Homo sapiens','Homo sapiens-cancer']:
        headers = ['Gene Name', 'Transcript(s)','AA Coordinates','CDS Coordinates','Restriction Enzymes-50', 'Restriction Enzymes-150', 'NMD Prediction', 'Cancer type(s)']
  
      genes = table.objects.filter(gene__icontains=speciesData['gene'])
      step1 = len(genes)
      if speciesData['species'] == 'Homo sapiens-cancer':
        genes = genes.exclude(cancer_type='NA')
        step2 = len(genes)
      if advanceData['PAM'] is None or len(advanceData['PAM'])==0:
        advanceData['PAM'] = ['PAM: NGG','PAM: NGA','PAM: NGCG','PAM: NGAG','PAM: NNGRRT','PAM: NNNRRT']

      if advanceData['PAM'] is not None:
        data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt'}
	NaRemove = []
	for x in advanceData['PAM']:
            column = data[x]
            NaRemove.append(column)         
      headers = headers[0:4]+advanceData['PAM']+headers[4:]
      if len(advanceData['RFLP']) != 0:
        genes = genes.exclude(rflp_50='NA')
        genes = genes.exclude(rflp_150='NA')
        step3 = len(genes)
      if len( advanceData['NMD_Prediction']) != 0:
        genes = genes.exclude(~Q(nmd_pred__contains="TRUE"))
        step4 = len(genes)
#      raise ValueError("hi")
      genes = list(genes)
      step5= len(genes)
      toRemove = []
      for row in genes:
        if shouldRemoverow(NaRemove, row) == True:
          toRemove.append(row)
      for remove in toRemove:
        genes.remove(remove)
      step6 = len(genes)
      if len(genes) == 0:
        return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
      else:
        header = str(speciesData['gene']) +" in " +str(speciesData['species'])
        return render(request, 'queryResults.html',{'query_results':genes,'headers':headers, 'SpeciesName':header})
  return HttpResponseRedirect('/')
  
def post_query(request):
  if request.method == 'POST':
    form = PassForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      password = data['password']
      if password in ['Ciccialab','Ciccialabisthebest', 'istop']:
        speciesForm = SpeciesForm(request.POST)
        advsearch= advForm(request.POST)
        return render(request, 'query.html', {'advancesearch':advsearch, 'species':speciesForm})
  form = PassForm()
  return render(request, 'index.html', {'passForm':form})

def faq_page(request):
  return render(request, 'faq.html')

def query_page(request):
  advsearch = advForm(request.POST)
  speciesForm = SpeciesForm(request.POST)
  return render(request, 'query.html', {'advancesearch':advsearch, 'species':speciesForm})

def shouldRemoverow(columns, row):
  for column in columns:
     if getattr(row,column)!='NA':
      return False
  return True    

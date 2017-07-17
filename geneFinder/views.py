from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from forms import SpeciesForm
from forms import PassForm
from forms import advForm
from forms import CancergeneForm
from forms import CancertypeForm
from forms import CancertypeAdvanceForm
from forms import CancergeneAdvanceForm
import models 
from django.db.models import Q

class HomePageView(TemplateView):
	def get(self, request, **kwarfs):
		form = PassForm()
		return render(request, 'index.html', {'passForm':form})


def post_geneForm(request):
  headers = ['Gene Name', 'Targeted Codon', 'Relative Position of Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'Percent NMD']
  nameMap = {'Homo sapiens':models.Humans, 'Saccharomyces cerevisiae':models.Yeast, 'Drosophila melanogaster':models.Fly, 'Danio rerio':models.Fish, 'Mus musculus':models.Mouse, 'Rattus norvegicus':models.Rat, 'Arabidopsis thaliana':models.Plant, 'Caenorhabditis elegans':models.Nematode}
  if request.method == 'POST':
    speciesForm = SpeciesForm(request.POST)
    advanceForm = advForm(request.POST)
    if advanceForm.is_valid() and speciesForm.is_valid(): 
      speciesData = speciesForm.cleaned_data
      advanceData = advanceForm.cleaned_data
      table = nameMap[speciesData['species']]
      genes = table.objects.filter(gene__icontains=speciesData['gene'])
      if speciesData['species'] in ['Homo sapiens']:
        
        headers = ['Gene Name','Targeted Codon', 'Relative Position of Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'Percent NMD', 'Cancer type(s)']
        genes = table.objects.filter(gene__icontains=speciesData['gene'])
        step1 = len(genes)
    if advanceData['PAM'] is None or len(advanceData['PAM'])==0:
      advanceData['PAM'] = ['PAM: NGG','Off-target Prediction PAM: NGG','PAM: NGA','Off-target Prediction PAM: NGA','PAM: NGCG','Off-target Prediction PAM: NGCG','PAM: NGAG','Off-target Prediction PAM: NGAG', 'PAM: NNGRRT','Off-target Prediction PAM: NNGRRT','PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT']
      data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt', 'Off-target Prediction PAM: NGG':'sgngg_matches', 'Spacing PAM: NGG':'sgngg_spacing', 'Off-target Prediction PAM: NGA':'sgnga_matches', 'Spacing PAM: NGA':'sgnga_spacing', 'Off-target Prediction PAM: NGCG': 'sgngcg_matches', 'Spacing PAM: NGCG':'sgngcg_spacing', 'Off-target Prediction PAM: NGAG':'sgngag_matches', 'Spacing PAM: NGAG':'sgngag_spacing', 'Off-target Prediction PAM: NNGRRT':'sgnngrrt_matches', 'Spacing PAM: NNGRRT': 'sgnngrrt_spacing', 'Off-target Prediction PAM: NNNRRT': 'sgnnnrrt_matches', 'Spacing PAM: NNNRRT': 'sgnnnrrt_spacing'}
      NaRemove = []
      for x in advanceData['PAM']:
        column = data[x]
        NaRemove.append(column)
        step10 = len(NaRemove)
      headers = headers[0:3]+advanceData['PAM']+headers[3:]
      toRemove = []
      for row in genes:
        if shouldRemoverow(NaRemove, row) == True:
          toRemove.append(row)
        step4 = len(genes)
      for remove in toRemove:
        genes.remove(remove)

 
    if len(advanceData['RFLP']) != 0:
      genes = genes.exclude(Q(rflp_loss='') & Q(rflp_gain=''))
      step3 = len(genes)

    if len(advanceData['NMD']) !=0:
      genes = genes.exclude(percent_nmd__lte=50)
      step2 = len(genes)

    if advanceData['noG'] !=0:
      genes = genes.exclude(no_upstream_g='FALSE')
      step3 = len(genes)
      toRemove = []
      genes = list(genes)
    step6 = len(genes)
    if len(genes) == 0:
      return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
    else:
      header = str(speciesData['gene']) +" in " +str(speciesData['species'])
      return render(request, 'queryResults.html',{'query_results':genes,'headers':headers, 'SpeciesName':header})
  return HttpResponseRedirect('/')


def post_cancerGene(request):
  if request.method == 'POST':
    cancerGene = CancergeneForm(request.POST)
    cancergeneAdvance =CancergeneAdvanceForm(request.POST)
    if cancerGene.is_valid() and cancergeneAdvance.is_valid():
      cancergeneData= cancerGene.cleaned_data
      cancergeneadvData = cancergeneAdvance.cleaned_data
      table = models.Humans
      headers = ['Gene Name','Targeted Codon', 'Relative Position of Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'Percent NMD', 'Cancer type(s)']
      genes = table.objects.filter(gene__icontains=cancergeneData['cancergene'])
      if cancergeneData['cancer_type'] == 'Any':
        genes = genes.exclude(cancer_type__exact='')
      	step7 = len(genes);
      else:
        cancertype = cancergeneData['cancer_type']
        genes = genes.exclude(~Q(cancer_type__icontains=cancertype))
      	step8 = len(genes)
      
      if cancergeneadvData['PAM'] is None or len(cancergeneadvData['PAM'])==0:
        cancergeneadvData['PAM'] = ['PAM: NGG','Off-target Prediction PAM: NGG','PAM: NGA','Off-target Prediction PAM: NGA','PAM: NGCG','Off-target Prediction PAM: NGCG','PAM: NGAG','Off-target Prediction PAM: NGAG', 'PAM: NNGRRT','Off-target Prediction PAM: NNGRRT','PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT']
      data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt', 'Off-target Prediction PAM: NGG':'sgngg_matches', 'Spacing PAM: NGG':'sgngg_spacing', 'Off-target Prediction PAM: NGA':'sgnga_matches', 'Spacing PAM: NGA':'sgnga_spacing', 'Off-target Prediction PAM: NGCG': 'sgngcg_matches', 'Spacing PAM: NGCG':'sgngcg_spacing', 'Off-target Prediction PAM: NGAG':'sgngag_matches', 'Spacing PAM: NGAG':'sgngag_spacing', 'Off-target Prediction PAM: NNGRRT':'sgnngrrt_matches', 'Spacing PAM: NNGRRT': 'sgnngrrt_spacing', 'Off-target Prediction PAM: NNNRRT': 'sgnnnrrt_matches', 'Spacing PAM: NNNRRT': 'sgnnnrrt_spacing'}
      NaRemove1 = []
      for x in cancergeneadvData['PAM']:
        column = data[x]
        NaRemove1.append(column)
      headers = headers[0:3]+cancergeneadvData['PAM']+headers[3:]
      if len(cancergeneadvData['RFLP']) != 0:
        genes = genes.exclude(Q(rflp_loss='') & Q(rflp_gain=''))
        step3 = len(genes)
      if len(cancergeneadvData['NMD']) != 0:
        genes = genes.exclude(percent_nmd__lte=50)
        step2 = len(genes)
      if len(cancergeneadvData['noG']) != 0:
        genes = genes.exclude(no_upstream_g='FALSE')
        step3 = len(genes)
      
      toRemove = []
      genes = list(genes)
      for row in genes:
        if shouldRemoverow(NaRemove1, row) == True:
          toRemove.append(row)
      step4 = len(genes)
      for remove in toRemove:
        genes.remove(remove)
      step6 = len(genes)

      if len(genes) == 0:
        return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
      else:
        header = str(cancergeneData['cancergene'])+" for cancer type " +str(cancergeneData['cancer_type'])
        step9 = len(genes)
        return render(request, 'queryResults.html',{'query_results':genes, 'headers':headers, 'SpeciesName':header})
  return HttpResponseRedirect('/')

def post_cancerType(request):
  if request.method == 'POST':
    cancerType = CancertypeForm(request.POST)
    cancertypeAdvance = CancertypeAdvanceForm(request.POST)
    if cancerType.is_valid() and cancertypeAdvance.is_valid():
      cancertypeData= cancerType.cleaned_data
      cancertypeadvData = cancertypeAdvance.cleaned_data
      table = models.Humans
      headers = ['Gene Name','Targeted Codon', 'Relative Position of Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'Percent NMD', 'Cancer type(s)']
      if cancertypeData['c_type'] is not None:
         for cancertype in cancertypeData['c_type']:
           genes = table.objects.filter(cancer_type__icontains=cancertype)
      step9 = len(genes)
      if cancertypeadvData['PAM'] is None or len(cancertypeadvData['PAM'])==0:
        cancertypeadvData['PAM'] = ['PAM: NGG','Off-target Prediction PAM: NGG','PAM: NGA','Off-target Prediction PAM: NGA','PAM: NGCG','Off-target Prediction PAM: NGCG','PAM: NGAG','Off-target Prediction PAM: NGAG', 'PAM: NNGRRT','Off-target Prediction PAM: NNGRRT','PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT']
      data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt', 'Off-target Prediction PAM: NGG':'sgngg_matches', 'Spacing PAM: NGG':'sgngg_spacing', 'Off-target Prediction PAM: NGA':'sgnga_matches', 'Spacing PAM: NGA':'sgnga_spacing', 'Off-target Prediction PAM: NGCG': 'sgngcg_matches', 'Spacing PAM: NGCG':'sgngcg_spacing', 'Off-target Prediction PAM: NGAG':'sgngag_matches', 'Spacing PAM: NGAG':'sgngag_spacing', 'Off-target Prediction PAM: NNGRRT':'sgnngrrt_matches', 'Spacing PAM: NNGRRT': 'sgnngrrt_spacing', 'Off-target Prediction PAM: NNNRRT': 'sgnnnrrt_matches', 'Spacing PAM: NNNRRT': 'sgnnnrrt_spacing'}
      NaRemove2 = []
      for x in cancertypeadvData['PAM']:
        column = data[x]
        NaRemove2.append(column)
      headers = headers[0:3]+cancertypeadvData['PAM']+headers[3:]
      if len(cancertypeadvData['RFLP']) != 0:
        genes = genes.exclude(Q(rflp_loss='') & Q(rflp_gain=''))
        step3 = len(genes)
      if len(cancertypeadvData['NMD']) != 0:
        genes = genes.exclude(percent_nmd__lte=50)
        step2 = len(genes)
      if len(cancertypeadvData['noG']) != 0:
        genes = genes.exclude(no_upstream_g='FALSE')
        step3 = len(genes)
      
      toRemove = []
      genes = list(genes)
      for row in genes:
        if shouldRemoverow(NaRemove2, row) == True:
          toRemove.append(row)
      step4 = len(genes)
      for remove in toRemove:
        genes.remove(remove)
      step6 = len(genes)

      if len(genes) == 0:
          return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
      else:
        ctype= cancertype
        header = "All sgSTOPS for cancer type(s) " +str(ctype)
        return render(request, 'queryResults.html',{'query_results':genes, 'headers':headers, 'SpeciesName':header})
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
	cancergene= CancergeneForm(request.POST)
	cancertype= CancertypeForm(request.POST)
	cancergeneadvance= CancergeneAdvanceForm(request.POST)
        cancertypeadvance= CancertypeAdvanceForm(request.POST)
        return render(request, 'query.html', {'advancesearch':advsearch, 'species':speciesForm, 'cancergene':CancergeneForm, 'cancergeneadvance':CancergeneAdvanceForm, 'cancertype':CancertypeForm, 'cancertypeadvance':CancertypeAdvanceForm})
  form = PassForm()
  return render(request, 'index.html', {'passForm':form})

def faq_page(request):
  return render(request, 'faq.html')

def query_page(request):
  advsearch = advForm(request.POST)
  speciesForm = SpeciesForm(request.POST)
  cancergene= CancergeneForm(request.POST)
  cancertype= CancertypeForm(request.POST)
  cancergeneadvance= CancergeneAdvanceForm(request.POST)
  cancertypeadvance= CancertypeAdvanceForm(request.POST)      
  return render(request, 'query.html', {'advancesearch':advsearch, 'species':speciesForm,  'cancergene':CancergeneForm, 'cancergeneadvance':CancergeneAdvanceForm, 'cancertype':CancertypeForm, 'cancertypeadvance':CancertypeAdvanceForm})

def shouldRemoverow(columns, row):
  for column in columns:
     if getattr(row,column)!='':
      return False
  return True    

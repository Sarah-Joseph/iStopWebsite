from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .forms import SpeciesForm
from .forms import PassForm
from .forms import advForm
from .forms import CancergeneForm
from .forms import CancertypeForm
from .forms import CancertypeAdvanceForm
from .forms import CancergeneAdvanceForm
from .forms import SpeciestypeForm
from .forms import SpeciestypeAdvanceForm
import models 
from django.db.models import Q

'''
class HomePageView(TemplateView):
  def get(self, request, **kwarfs):
          speciesForm = SpeciesForm(request.POST)
          advsearch= advForm(request.POST)
    cancergene= CancergeneForm(request.POST)
    cancertype= CancertypeForm(request.POST)
    cancergeneadvance= CancergeneAdvanceForm(request.POST)
          cancertypeadvance= CancertypeAdvanceForm(request.POST)
          speciestype= SpeciestypeForm(request.POST)
          speciestypeadvance= SpeciestypeAdvanceForm(request.POST)
          return render(request, 'query.html', {'advancesearch':advsearch, 'species':speciesForm, 'cancergene':CancergeneForm, 'cancergeneadvance':CancergeneAdvanceForm, 'cancertype':CancertypeForm, 'cancertypeadvance':CancertypeAdvanceForm, 'speciestype':SpeciestypeForm, 'speciestypeadvance':SpeciestypeAdvanceForm})
'''

def post_geneForm(request):
  headers = ['Gene Name', 'Chromosome', 'Strand', 'Genomic Coordinate', 'Targeted Codon', 'Number of Isoforms', 'Percent Isoforms', 'Relative Position in Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'NMD Prediction (%)']
  nameMap = {'Homo sapiens':models.Humans, 'Saccharomyces cerevisiae':models.Yeast, 'Drosophila melanogaster':models.Fly, 'Danio rerio':models.Fish, 'Mus musculus':models.Mouse, 'Rattus norvegicus':models.Rat, 'Arabidopsis thaliana':models.Plant, 'Caenorhabditis elegans':models.Nematode}
  if request.method == 'POST':
    speciesForm = SpeciesForm(request.POST)
    advanceForm = advForm(request.POST)
    if advanceForm.is_valid() and speciesForm.is_valid(): 
      speciesData = speciesForm.cleaned_data
      advanceData = advanceForm.cleaned_data
      table = nameMap[speciesData['species']]
      listgenes = speciesData['gene'].splitlines()
      if speciesData['species'] in ['Homo sapiens']:
          headers = ['Gene Name', 'Chromosome', 'Strand', 'Genomic Coordinate', 'Targeted Codon', 'Number of Isoforms', 'Percent Isoforms', 'Relative Position in Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'NMD Prediction (%)', 'Cancer type(s)']
      if listgenes is not None:
        for i in listgenes:
          if shouldalias(i, speciesData, nameMap) == True:
            table2 = models.Alias
            speciesMap = {'Homo sapiens':'Hsapiens', 'Saccharomyces cerevisiae': 'Scerevisiae', 'Drosophila melanogaster': 'Dmelanogaster', 'Danio rerio': 'Drerio', 'Mus musculus': 'Mmusculus', 'Rattus norvegicus': 'Rnorvegicus', 'Caenorhabditis elegans': 'Celegans', 'Arabidopsis thaliana': 'Athaliana'}
            speciesalias = speciesMap[speciesData["species"]]
            alias = table2.objects.filter(Q(species__exact=speciesalias) & Q(alias__iexact=i)).values('gene')
            symbol = [entry for entry in alias]
            individual = [a['gene'] for a in symbol]
            listgenes.remove(i)
            for b in individual: 
              check = table.objects.filter(gene__iexact=b)
              if len(check) != 0:
                listgenes.append(b)
        genes = table.objects.filter(gene__in=listgenes)

    if advanceData['PAM'] is not None:
       map1 = {'PAM: NGG':'Off-target Prediction PAM: NGG','PAM: NGA':'Off-target Prediction PAM: NGA','PAM: NGCG':'Off-target Prediction PAM: NGCG','PAM: NGAG':'Off-target Prediction PAM: NGAG', 'PAM: NNGRRT':'Off-target Prediction PAM: NNGRRT','PAM: NNNRRT': 'Off-target Prediction PAM: NNNRRT'}
       z = []
       for x in advanceData['PAM']:
         if x in map1:
           y=map1[x]
           z.append(y)
       c = advanceData['PAM'] + z
       c[::2] = advanceData['PAM']
       c[1::2] = z
       advanceData['PAM'] = c
    if advanceData['PAM'] is None or len(advanceData['PAM'])==0:
      advanceData['PAM'] = ['PAM: NGG','Off-target Prediction PAM: NGG','PAM: NGA','Off-target Prediction PAM: NGA','PAM: NGCG','Off-target Prediction PAM: NGCG','PAM: NGAG','Off-target Prediction PAM: NGAG', 'PAM: NNGRRT','Off-target Prediction PAM: NNGRRT','PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT']
    data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt', 'Off-target Prediction PAM: NGG':'sgngg_matches', 'Spacing PAM: NGG':'sgngg_spacing', 'Off-target Prediction PAM: NGA':'sgnga_matches', 'Spacing PAM: NGA':'sgnga_spacing', 'Off-target Prediction PAM: NGCG': 'sgngcg_matches', 'Spacing PAM: NGCG':'sgngcg_spacing', 'Off-target Prediction PAM: NGAG':'sgngag_matches', 'Spacing PAM: NGAG':'sgngag_spacing', 'Off-target Prediction PAM: NNGRRT':'sgnngrrt_matches', 'Spacing PAM: NNGRRT': 'sgnngrrt_spacing', 'Off-target Prediction PAM: NNNRRT': 'sgnnnrrt_matches', 'Spacing PAM: NNNRRT': 'sgnnnrrt_spacing'}
    NaRemove = []
    for x in advanceData['PAM']:
      column = data[x]
      NaRemove.append(column)
      step10 = len(NaRemove)
    headers = headers[0:12]+advanceData['PAM']+headers[12:]
     
    if len(advanceData['RFLP']) != 0:
      genes = genes.exclude(Q(rflp_loss='') & Q(rflp_gain=''))
    if len(advanceData['NMD']) !=0:
      genes = genes.exclude(percent_nmd__lte=50)
    if len(advanceData['off']) !=0:
      if 'Off-target Prediction PAM: NGG' in headers:
        genes = genes.exclude(sgngg_matches__gt=0)
      if 'Off-target Prediction PAM: NGA' in headers:
        genes = genes.exclude(sgnga_matches__gt=0)
      if 'Off-target Prediction PAM: NGCG' in headers:
        genes = genes.exclude(sgngcg_matches__gt=0) 
      if 'Off-target Prediction PAM: NGAG' in headers:
        genes = genes.exclude(sgngag_matches__gt=0) 
      if 'Off-target Prediction PAM: NNGRRT' in headers:      
        genes = genes.exclude(sgnngrrt_matches__gt=0)
      if 'Off-target Prediction PAM: NNNRRT' in headers:
        genes = genes.exclude(sgnnnrrt_matches__gt=0)
  
    if advanceData['noG'] !=0:
      genes = genes.exclude(no_upstream_g='FALSE')
    toRemove = []
    genes = list(genes)
    for row in genes:
      if shouldRemoverow(NaRemove, row) == True:
        toRemove.append(row)
    for remove in toRemove:
      genes.remove(remove)


    if len(genes) == 0:
      return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
    else:
      if len(listgenes) == 1: 
        header = str(speciesData['gene']).upper() +" in " +str(speciesData['species'])
      else:
        header = "Your list of genes in " +str(speciesData['species'])
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
      headers = ['Gene Name','Chromosome', 'Strand', 'Genomic Coordinate', 'Targeted Codon', 'Number of Isoforms', 'Percent Isoforms', 'Relative Position in Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'NMD Prediction (%)', 'Cancer type(s)']
      listgenes = cancergeneData['cancergene'].splitlines()
      if listgenes is not None:
        for i in listgenes:
          if shouldcanceralias(i, cancergeneData) == True:
            table2 = models.Alias
            alias = table2.objects.filter(Q(species__exact='Hsapiens') & Q(alias__iexact=i)).values('gene')
            symbol = [entry for entry in alias]
            individual = [a['gene'] for a in symbol]
            listgenes.remove(i)
            for b in individual: 
              check = table.objects.filter(gene__iexact=b)
              if len(check) != 0:
                listgenes.append(b)
          genes = table.objects.filter(gene__in=listgenes)
 

      if cancergeneData['cancer_type'] == 'Any':
        genes = genes.exclude(cancer_type__exact='')
        step7 = len(genes);
      else:
        cancertype = cancergeneData['cancer_type']
        genes = genes.exclude(~Q(cancer_type__icontains=cancertype))
        step8 = len(genes)
      if cancergeneadvData['PAM'] is not None:
        map1 = {'PAM: NGG':'Off-target Prediction PAM: NGG','PAM: NGA':'Off-target Prediction PAM: NGA','PAM: NGCG':'Off-target Prediction PAM: NGCG','PAM: NGAG':'Off-target Prediction PAM: NGAG', 'PAM: NNGRRT':'Off-target Prediction PAM: NNGRRT','PAM: NNNRRT': 'Off-target Prediction PAM: NNNRRT'}
        z = []
        for x in cancergeneadvData['PAM']:
          if x in map1:
            y=map1[x]
            z.append(y)
        c = cancergeneadvData['PAM'] + z
        c[::2] = cancergeneadvData['PAM']
        c[1::2] = z
        cancergeneadvData['PAM'] = c
     
      if cancergeneadvData['PAM'] is None or len(cancergeneadvData['PAM'])==0:
        cancergeneadvData['PAM'] = ['PAM: NGG','Off-target Prediction PAM: NGG','PAM: NGA','Off-target Prediction PAM: NGA','PAM: NGCG','Off-target Prediction PAM: NGCG','PAM: NGAG','Off-target Prediction PAM: NGAG', 'PAM: NNGRRT','Off-target Prediction PAM: NNGRRT','PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT']
      data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt', 'Off-target Prediction PAM: NGG':'sgngg_matches', 'Spacing PAM: NGG':'sgngg_spacing', 'Off-target Prediction PAM: NGA':'sgnga_matches', 'Spacing PAM: NGA':'sgnga_spacing', 'Off-target Prediction PAM: NGCG': 'sgngcg_matches', 'Spacing PAM: NGCG':'sgngcg_spacing', 'Off-target Prediction PAM: NGAG':'sgngag_matches', 'Spacing PAM: NGAG':'sgngag_spacing', 'Off-target Prediction PAM: NNGRRT':'sgnngrrt_matches', 'Spacing PAM: NNGRRT': 'sgnngrrt_spacing', 'Off-target Prediction PAM: NNNRRT': 'sgnnnrrt_matches', 'Spacing PAM: NNNRRT': 'sgnnnrrt_spacing'}
      NaRemove1 = []
      for x in cancergeneadvData['PAM']:
        column = data[x]
        NaRemove1.append(column)
      headers = headers[0:12]+cancergeneadvData['PAM']+headers[12:]
      if len(cancergeneadvData['RFLP']) != 0:
        genes = genes.exclude(Q(rflp_loss='') & Q(rflp_gain=''))
      if len(cancergeneadvData['NMD']) != 0:
        genes = genes.exclude(percent_nmd__lte=50)
      if len(cancergeneadvData['noG']) != 0:
        genes = genes.exclude(no_upstream_g='FALSE')
      if len(cancergeneadvData['off']) !=0:
        if 'Off-target Prediction PAM: NGG' in headers:
          genes = genes.exclude(sgngg_matches__gt=0)
        if 'Off-target Prediction PAM: NGA' in headers:
          genes = genes.exclude(sgnga_matches__gt=0)
        if 'Off-target Prediction PAM: NGCG' in headers:
          genes = genes.exclude(sgngcg_matches__gt=0) 
        if 'Off-target Prediction PAM: NGAG' in headers:
          genes = genes.exclude(sgngag_matches__gt=0) 
        if 'Off-target Prediction PAM: NNGRRT' in headers:      
          genes = genes.exclude(sgnngrrt_matches__gt=0)
        if 'Off-target Prediction PAM: NNNRRT' in headers:
          genes = genes.exclude(sgnnnrrt_matches__gt=0)
  
 
      toRemove = []
      genes = list(genes)
      for row in genes:
        if shouldRemoverow(NaRemove1, row) == True:
          toRemove.append(row)
      for remove in toRemove:
        genes.remove(remove)

      if len(genes) == 0:
        return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
      else:
        
        if len(listgenes) == 0:
          header = str(cancergeneData['cancergene']).upper()+" for cancer type: " +str(cancergeneData['cancer_type'])
        else:
          header = "Your list of genes for the cancer type: " +str(cancergeneData['cancer_type'])
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
      headers = ['Gene Name','Chromosome', 'Strand', 'Genomic Coordinate', 'Targeted Codon', 'Number of Isoforms', 'Percent Isoforms', 'Relative Position in Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'NMD Prediction (%)', 'Cancer type(s)']
      if cancertypeData['c_type'] is not None:
        name_filter = Q()
        for cancertype in cancertypeData['c_type']:
          name_filter |= Q(cancer_type__icontains=cancertype)
        genes = table.objects.filter(name_filter)
      if cancertypeadvData['PAM'] is not None:
        map1 = {'PAM: NGG':'Off-target Prediction PAM: NGG','PAM: NGA':'Off-target Prediction PAM: NGA','PAM: NGCG':'Off-target Prediction PAM: NGCG','PAM: NGAG':'Off-target Prediction PAM: NGAG', 'PAM: NNGRRT':'Off-target Prediction PAM: NNGRRT','PAM: NNNRRT': 'Off-target Prediction PAM: NNNRRT'}
        z = []
        for x in cancertypeadvData['PAM']:
          if x in map1:
            y=map1[x]
            z.append(y)
        c = cancertypeadvData['PAM'] + z
        c[::2] = cancertypeadvData['PAM']
        c[1::2] = z
        cancertypeadvData['PAM'] = c

      if cancertypeadvData['PAM'] is None or len(cancertypeadvData['PAM'])==0:
        cancertypeadvData['PAM'] = ['PAM: NGG','Off-target Prediction PAM: NGG','PAM: NGA','Off-target Prediction PAM: NGA','PAM: NGCG','Off-target Prediction PAM: NGCG','PAM: NGAG','Off-target Prediction PAM: NGAG', 'PAM: NNGRRT','Off-target Prediction PAM: NNGRRT','PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT']
      data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt', 'Off-target Prediction PAM: NGG':'sgngg_matches', 'Spacing PAM: NGG':'sgngg_spacing', 'Off-target Prediction PAM: NGA':'sgnga_matches', 'Spacing PAM: NGA':'sgnga_spacing', 'Off-target Prediction PAM: NGCG': 'sgngcg_matches', 'Spacing PAM: NGCG':'sgngcg_spacing', 'Off-target Prediction PAM: NGAG':'sgngag_matches', 'Spacing PAM: NGAG':'sgngag_spacing', 'Off-target Prediction PAM: NNGRRT':'sgnngrrt_matches', 'Spacing PAM: NNGRRT': 'sgnngrrt_spacing', 'Off-target Prediction PAM: NNNRRT': 'sgnnnrrt_matches', 'Spacing PAM: NNNRRT': 'sgnnnrrt_spacing'}
      NaRemove2 = []
      for x in cancertypeadvData['PAM']:
        column = data[x]
        NaRemove2.append(column)
      headers = headers[0:12]+cancertypeadvData['PAM']+headers[12:]
      if len(cancertypeadvData['RFLP']) != 0:
        genes = genes.exclude(Q(rflp_loss='') & Q(rflp_gain=''))
      if len(cancertypeadvData['NMD']) != 0:
        genes = genes.exclude(percent_nmd__lte=50)
      if len(cancertypeadvData['noG']) != 0:
        genes = genes.exclude(no_upstream_g='FALSE')
      if len(cancertypeadvData['off']) !=0:
        if 'Off-target Prediction PAM: NGG' in headers:
          genes = genes.exclude(sgngg_matches__gt=0)
        if 'Off-target Prediction PAM: NGA' in headers:
          genes = genes.exclude(sgnga_matches__gt=0)
        if 'Off-target Prediction PAM: NGCG' in headers:
          genes = genes.exclude(sgngcg_matches__gt=0) 
        if 'Off-target Prediction PAM: NGAG' in headers:
          genes = genes.exclude(sgngag_matches__gt=0) 
        if 'Off-target Prediction PAM: NNGRRT' in headers:      
          genes = genes.exclude(sgnngrrt_matches__gt=0)
        if 'Off-target Prediction PAM: NNNRRT' in headers:
          genes = genes.exclude(sgnnnrrt_matches__gt=0)
  

      toRemove = []
      genes = list(genes)
      for row in genes:
        if shouldRemoverow(NaRemove2, row) == True:
          toRemove.append(row)
      for remove in toRemove:
        genes.remove(remove)

      if len(genes) == 0:
          return render(request, 'queryResults.html',{'SpeciesName':'No gene found'});
      else:
        types = u", ".join(cancertypeData['c_type'])
        header = "All sgSTOPS for cancer type(s): " +str(types)
        return render(request, 'queryResults.html',{'query_results':genes, 'headers':headers, 'SpeciesName':header})
  return HttpResponseRedirect('/')

def post_speciesType(request):
  if request.method == 'POST':
    speciesType = SpeciestypeForm(request.POST)
    speciestypeAdvance = SpeciestypeAdvanceForm(request.POST)
    if speciesType.is_valid() and speciestypeAdvance.is_valid():
      speciestypeData= speciesType.cleaned_data
      speciestypeadvData = speciestypeAdvance.cleaned_data
      headers = ['Gene Name', 'Chromosome', 'Strand', 'Genomic Coordinate', 'Targeted Codon', 'Number of Isoforms', 'Percent Isoforms', 'Relative Position in Largest Isoform', 'No Upstream G', 'RFLP Loss', 'RFLP Gain', 'NMD Prediction (%)']
      nameMap = {'Homo sapiens':models.Humans, 'Saccharomyces cerevisiae':models.Yeast, 'Drosophila melanogaster':models.Fly, 'Danio rerio':models.Fish, 'Mus musculus':models.Mouse, 'Rattus norvegicus':models.Rat, 'Arabidopsis thaliana':models.Plant, 'Caenorhabditis elegans':models.Nematode}
      table = nameMap[speciestypeData['species']]
      genes = list(table.objects.all())
      if speciestypeadvData['PAM'] is not None:
        map1 = {'PAM: NGG':'Off-target Prediction PAM: NGG','PAM: NGA':'Off-target Prediction PAM: NGA','PAM: NGCG':'Off-target Prediction PAM: NGCG','PAM: NGAG':'Off-target Prediction PAM: NGAG', 'PAM: NNGRRT':'Off-target Prediction PAM: NNGRRT','PAM: NNNRRT': 'Off-target Prediction PAM: NNNRRT'}
        z = []
        for x in speciestypeadvData['PAM']:
          if x in map1:
            y=map1[x]
            z.append(y)
        c = speciesadvData['PAM'] + z
        c[::2] = speciestypeadvData['PAM']
        c[1::2] = z
        speciestypeadvData['PAM'] = c

      if speciestypeadvData['PAM'] is None or len(speciestypeadvData['PAM'])==0:
        speciestypeadvData['PAM'] = ['PAM: NGG','Off-target Prediction PAM: NGG','PAM: NGA','Off-target Prediction PAM: NGA','PAM: NGCG','Off-target Prediction PAM: NGCG','PAM: NGAG','Off-target Prediction PAM: NGAG', 'PAM: NNGRRT','Off-target Prediction PAM: NNGRRT','PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT']
      data = {'PAM: NGG':'sgngg','PAM: NGA':'sgnga','PAM: NGCG':'sgngcg','PAM: NGAG':'sgngag','PAM: NNGRRT':'sgnngrrt','PAM: NNNRRT':'sgnnnrrt', 'Off-target Prediction PAM: NGG':'sgngg_matches', 'Spacing PAM: NGG':'sgngg_spacing', 'Off-target Prediction PAM: NGA':'sgnga_matches', 'Spacing PAM: NGA':'sgnga_spacing', 'Off-target Prediction PAM: NGCG': 'sgngcg_matches', 'Spacing PAM: NGCG':'sgngcg_spacing', 'Off-target Prediction PAM: NGAG':'sgngag_matches', 'Spacing PAM: NGAG':'sgngag_spacing', 'Off-target Prediction PAM: NNGRRT':'sgnngrrt_matches', 'Spacing PAM: NNGRRT': 'sgnngrrt_spacing', 'Off-target Prediction PAM: NNNRRT': 'sgnnnrrt_matches', 'Spacing PAM: NNNRRT': 'sgnnnrrt_spacing'}
      NaRemove2 = []
      for x in speciestypeadvData['PAM']:
        column = data[x]
        NaRemove2.append(column)
      headers = headers[0:12]+speciestypeadvData['PAM']+headers[12:]
      if len(speciestypeadvData['RFLP']) != 0:
        genes = genes.exclude(Q(rflp_loss='') & Q(rflp_gain=''))
        step3 = len(genes)
      if len(speciestypeadvData['NMD']) != 0:
        genes = genes.exclude(percent_nmd__lte=50)
        step2 = len(genes)
      if len(speciestypeadvData['noG']) != 0:
        genes = genes.exclude(no_upstream_g='FALSE')
        step3 = len(genes)
      if len(speciestypeadvData['off']) !=0:
        if 'Off-target Prediction PAM: NGG' in headers:
          genes = genes.exclude(sgngg_matches__gt=0)
        if 'Off-target Prediction PAM: NGA' in headers:
          genes = genes.exclude(sgnga_matches__gt=0)
        if 'Off-target Prediction PAM: NGCG' in headers:
          genes = genes.exclude(sgngcg_matches__gt=0) 
        if 'Off-target Prediction PAM: NGAG' in headers:
          genes = genes.exclude(sgngag_matches__gt=0) 
        if 'Off-target Prediction PAM: NNGRRT' in headers:      
          genes = genes.exclude(sgnngrrt_matches__gt=0)
        if 'Off-target Prediction PAM: NNNRRT' in headers:
          genes = genes.exclude(sgnnnrrt_matches__gt=0)
  

      toRemove = []
      raise ValueError("hi")
      genes = list(genes)
      for row in genes:
        if shouldRemoverow(NaRemove2, row) == True:
          toRemove.append(row)
      step4 = len(genes)
      for remove in toRemove:
        genes.remove(remove)
      step6 = len(genes)

      if len(genes) == 0:
          return render(request, 'queryResults.html',{'SpeciesName':'No species found'});
      else:
        header = "All sgSTOPS for species " +str(speciestypeData['species'])
        return render(request, 'queryResults.html',{'query_results':genes, 'headers':headers, 'SpeciesName':header})
  return HttpResponseRedirect('/')


#def post_query(request):
 # if request.method == 'POST':
  #  form = PassForm(request.POST)
   # if form.is_valid():
    #  data = form.cleaned_data
    #  password = data['password']
    #  if password in ['Ciccialab','Ciccialabisthebest', 'istop']:
    #    speciesForm = SpeciesForm(request.POST)
    #    advsearch= advForm(request.POST)
# cancergene= CancergeneForm(request.POST)
# cancertype= CancertypeForm(request.POST)
# cancergeneadvance= CancergeneAdvanceForm(request.POST)
 #       cancertypeadvance= CancertypeAdvanceForm(request.POST)
  #      return render(request, 'query.html', {'advancesearch':advsearch, 'species':speciesForm, 'cancergene':CancergeneForm, 'cancergeneadvance':CancergeneAdvanceForm, 'cancertype':CancertypeForm, 'cancertypeadvance':CancertypeAdvanceForm})
 # form = PassForm()
 # return render(request, 'index.html', {'passForm':form})

def faq_page(request):
  return render(request, 'faq.html')

def query_page(request):
  advsearch = advForm(request.POST)
  speciesForm = SpeciesForm(request.POST)
  cancergene= CancergeneForm(request.POST)
  cancertype= CancertypeForm(request.POST)
  cancergeneadvance= CancergeneAdvanceForm(request.POST)
  cancertypeadvance= CancertypeAdvanceForm(request.POST)
  speciestype= SpeciestypeForm(request.POST)
  speciestypeadvance= SpeciestypeAdvanceForm(request.POST)      
  return render(request, 'query.html', {'advancesearch':advsearch, 'species':speciesForm,  'cancergene':CancergeneForm, 'cancergeneadvance':CancergeneAdvanceForm, 'cancertype':CancertypeForm, 'cancertypeadvance':CancertypeAdvanceForm, 'speciestype':SpeciestypeForm, 'speciestypeadvance':SpeciestypeAdvanceForm})

def shouldalias(i, speciesData, nameMap):
  speciesMap = {'Homo sapiens':'Hsapiens', 'Saccharomyces cerevisiae': 'Scerevisiae', 'Drosophila melanogaster': 'Dmelanogaster', 'Danio rerio': 'Drerio', 'Mus musculus': 'Mmusculus', 'Rattus norvegicus': 'Rnorvegicus', 'Caenorhabditis elegans': 'Celegans', 'Arabidopsis thaliana': 'Athaliana'}
  table2 = models.Alias
  speciesalias = speciesMap[speciesData["species"]]
  table = nameMap[speciesData["species"]]
  ingene = table.objects.filter(gene__exact=i)
  if len(ingene) == 0:
    alias = table2.objects.filter(Q(species__exact=speciesalias) & Q(alias__icontains=i)).values('gene')
    if len(alias) != 0: 
      return (True)
    else:
      return False
  return False
def shouldcanceralias(i, cancergeneData):
  table = models.Humans
  ingene = table.objects.filter(gene__exact=i)
  if len(ingene) == 0:
    table2 = models.Alias
    alias = table2.objects.filter(Q(species__iexact= 'Hsapiens') & Q(alias__icontains=i)).values('gene')
    if len(alias) != 0: 
      return (True)
    else:
      return False
  return False
 
def shouldRemoverow(columns, row):
  for column in columns:
     if getattr(row,column)!='':
      return False
  return True    

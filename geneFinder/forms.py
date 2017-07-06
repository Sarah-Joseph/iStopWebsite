from django import forms
from django.forms.widgets import CheckboxChoiceInput
from crispy_forms.layout import *
from crispy_forms.helper import *
from django.template import Template, Context
	       

PAM = [('PAM: NGG', 'PAM: NGG'),
       ('PAM: NGA', 'PAM: NGA'),
       ('PAM: NGCG', 'PAM: NGCG'),
       ('PAM: NGAG', 'PAM: NGAG'),
       ('PAM: NNGRRT', 'PAM: NNGRRT'),
       ('PAM: NNNRRT', 'PAM: NNNRRT')]

class SpeciesForm(forms.Form):
	CHOICES = (('Homo sapiens', 'Homo sapiens'),('Homo sapiens-cancer','Homo sapiens-cancer'), ('Saccharomyces cerevisiae','Saccharomyces cerevisiae'),('Danio rerio', 'Danio rerio'), ('Mus musculus', 'Mus musculus'), ('Arabidopsis thaliana', 'Arabidopsis thaliana'), ('Drosophila melanogaster', 'Drosophila melanogaster'), ('Rattus norvegicus','Rattus norvegicus'), ('Caenorhabditis elegans', 'Caenorhabditis elegans'))
	species = forms.ChoiceField(required=False, label='Species',choices=CHOICES)
        gene = forms.CharField(label='Gene', required=False)

class advForm (forms.Form):
	PAMChoice = PAM
	NMDPred = [('True','True')]
        rflp = [('True','True')]
	PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "Only see results for the checked off PAMs", widget=forms.CheckboxSelectMultiple())
	NMD_Prediction = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Prediction for any transcript", widget=forms.CheckboxSelectMultiple())
	RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "Can use RFLP Assay", widget=forms.CheckboxSelectMultiple())

	
class PassForm(forms.Form):
	password = forms.CharField(label='Password')







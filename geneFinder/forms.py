from django import forms
from django.forms.widgets import CheckboxChoiceInput
from crispy_forms.layout import *
from crispy_forms.helper import *
from django.template import Template, Context
#import floppyforms as forms	       

PAM = [('PAM: NGG', 'PAM: NGG'),
       ('Off-target Prediction PAM: NGG', 'Off-target Prediction PAM: NGG'),
       ('PAM: NGA', 'PAM: NGA'),
       ('Off-target Prediction PAM: NGA', 'Off-target Prediction PAM: NGA'),
       ('PAM: NGCG', 'PAM: NGCG'),
       ('Off-target Prediction PAM: NGCG', 'Off-target Prediction PAM: NGCG'),
       ('PAM: NGAG', 'PAM: NGAG'),
       ('Off-target Prediction PAM: NGAG', 'Off-target Prediction PAM: NGAG'),
       ('PAM: NNGRRT', 'PAM: NNGRRT'),
       ('Off-target Prediction PAM: NNGRRT', 'Off-target Prediction PAM: NNGRRT'),
       ('PAM: NNNRRT', 'PAM: NNNRRT'), 
       ('Off-target Prediction PAM: NNNRRT', 'Off-target Prediction PAM: NNNRRT')]
cancertype = [('Bladder', 'Bladder'),
	      ('Blood', 'Blood'),
	      ('Bone', 'Bone'),
	      ('Breast', 'Breast'),
	      ('Cervical', 'Cervical'),
	      ('Colorectal', 'Colorectal'),
	      ('Endometrial', 'Endometrial'),
	      ('Glioma', 'Glioma'),
	      ('Kidney', 'Kidney'),
	      ('Liver', 'Liver'),
	      ('Lung', 'Lung'),
	      ('Malignant melanoma', 'Malignant melanoma'),
	      ('Non-melanoma skin', 'Non-melanoma skin'),
	      ('Other', 'Other'),
              ('Ovarian', 'Ovarian'),
              ('Pancreatic', 'Pancreatic'),
	      ('Prostate', 'Prostate'),
              ('Stomach', 'Stomach'),
	      ('Thyroid', 'Thyroid'),
	      ('Upper aerodigestive', 'Upper aerodigestive')]
cancertypesearch = (('Any', 'Any'),
              ('Bladder', 'Bladder'),
	      ('Blood', 'Blood'),
	      ('Bone', 'Bone'),
	      ('Breast', 'Breast'),
	      ('Cervical', 'Cervical'),
	      ('Colorectal', 'Colorectal'),
	      ('Endometrial', 'Endometrial'),
	      ('Glioma', 'Glioma'),
	      ('Kidney', 'Kidney'),
	      ('Liver', 'Liver'),
	      ('Lung', 'Lung'),
	      ('Malignant melanoma', 'Malignant melanoma'),
	      ('Non-melanoma skin', 'Non-melanoma skin'),
	      ('Other', 'Other'),
              ('Ovarian', 'Ovarian'),
              ('Pancreatic', 'Pancreatic'),
	      ('Prostate', 'Prostate'),
              ('Stomach', 'Stomach'),
	      ('Thyroid', 'Thyroid'),
	      ('Upper aerodigestive', 'Upper aerodigestive'))


class SpeciesForm(forms.Form):
	CHOICES = (('Homo sapiens', 'Homo sapiens'),('Saccharomyces cerevisiae','Saccharomyces cerevisiae'),('Danio rerio', 'Danio rerio'), ('Mus musculus', 'Mus musculus'), ('Arabidopsis thaliana', 'Arabidopsis thaliana'), ('Drosophila melanogaster', 'Drosophila melanogaster'), ('Rattus norvegicus','Rattus norvegicus'), ('Caenorhabditis elegans', 'Caenorhabditis elegans'))
	species = forms.ChoiceField(required=False, label='Species',choices=CHOICES)
        gene = forms.CharField(label='Gene', required=False)

class advForm (forms.Form):
	PAMChoice = PAM
	NMDPred = [('Only Greater than 50%','Only Greater than 50%')]
        rflp = [('True','True')]
	PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "Only see results for the checked off PAMs", widget=forms.CheckboxSelectMultiple())
	NMD = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Percentage predicted is greater than 50%", widget=forms.CheckboxSelectMultiple())
	RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "Can use RFLP Assay", widget=forms.CheckboxSelectMultiple())
	UpG = [('True','True')]
	noG = forms.MultipleChoiceField(required=False, choices=UpG, label = "Choose only sgSTOPs without an upstream G", widget=forms.CheckboxSelectMultiple())
class CancergeneForm(forms.Form):
	cancer_type= forms.ChoiceField(required=False, label='Cancer Types', choices=cancertypesearch)
	cancergene = forms.CharField(label='Gene', required=False)

class CancergeneAdvanceForm(forms.Form):	
        PAMChoice = PAM
	NMDPred = [('Only Greater than 50%','Only Greater than 50%')]
        rflp = [('True','True')]
	UpG = [('True','True')]
	PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "Only see results for the checked off PAMs", widget=forms.CheckboxSelectMultiple())
	NMD = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Percentage predicted is greater than 50%", widget=forms.CheckboxSelectMultiple())
	RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "Can use RFLP Assay", widget=forms.CheckboxSelectMultiple())
	noG = forms.MultipleChoiceField(required=False, choices=UpG, label = "Choose only sgSTOPs without an upstream G", widget=forms.CheckboxSelectMultiple())


class CancertypeForm(forms.Form):
	c_type= forms.MultipleChoiceField(required=False, choices=cancertype, label= "See a list of sgSTOPs by cancer type", widget=forms.CheckboxSelectMultiple())

class CancertypeAdvanceForm(forms.Form):
	PAMChoice = PAM
	NMDPred = [('Only Greater than 50%','Only Greater than 50%')]
        rflp = [('True','True')]
	UpG = [('True','True')]
	PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "Only see results for the checked off PAMs", widget=forms.CheckboxSelectMultiple())
	NMD = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Percentage predicted is greater than 50%", widget=forms.CheckboxSelectMultiple())
	RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "Can use RFLP Assay", widget=forms.CheckboxSelectMultiple())
	noG = forms.MultipleChoiceField(required=False, choices=UpG, label = "Choose only sgSTOPs without an upstream G", widget=forms.CheckboxSelectMultiple())




class PassForm(forms.Form):
	password = forms.CharField(label='Password')




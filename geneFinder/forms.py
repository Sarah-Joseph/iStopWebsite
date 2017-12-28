from django import forms
from django.forms.widgets import CheckboxChoiceInput
from crispy_forms.layout import *
from crispy_forms.helper import *
from django.template import Template, Context
#import floppyforms as forms           

PAM = [('PAM: NGG', 'PAM: NGG'),
       ('PAM: NGA', 'PAM: NGA'),
       ('PAM: NGCG', 'PAM: NGCG'),
       ('PAM: NGAG', 'PAM: NGAG'),
       ('PAM: NNGRRT', 'PAM: NNGRRT'),
       ('PAM: NNNRRT', 'PAM: NNNRRT'),]

 
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
              ('Ovarian', 'Ovarian'),
              ('Pancreatic', 'Pancreatic'),
          ('Prostate', 'Prostate'),
              ('Stomach', 'Stomach'),
          ('Thyroid', 'Thyroid'),
          ('Upper aerodigestive', 'Upper aerodigestive'),
              ('Other', 'Other')]
cancertypesearch = [('Any', 'Any'),
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
              ('Ovarian', 'Ovarian'),
              ('Pancreatic', 'Pancreatic'),
          ('Prostate', 'Prostate'),
              ('Stomach', 'Stomach'),
          ('Thyroid', 'Thyroid'),
          ('Upper aerodigestive', 'Upper aerodigestive'),
          ('Other', 'Other')]


class SpeciesForm(forms.Form):
    CHOICES = (('Homo sapiens', 'Homo sapiens'),('Saccharomyces cerevisiae','Saccharomyces cerevisiae'),('Danio rerio', 'Danio rerio'), ('Mus musculus', 'Mus musculus'), ('Arabidopsis thaliana', 'Arabidopsis thaliana'), ('Drosophila melanogaster', 'Drosophila melanogaster'), ('Rattus norvegicus','Rattus norvegicus'), ('Caenorhabditis elegans', 'Caenorhabditis elegans'))
    species = forms.ChoiceField(required=False, label='Species',choices=CHOICES)
        gene = forms.CharField(label='Gene', required=False, widget=forms.Textarea(attrs={
            'placeholder':'Enter a single gene or a list of genes. Each gene on a new line. MAXIMUM INPUT: 10 genes.',
            'style': 'width: 60%',
                        

}))

class advForm (forms.Form):
    PAMChoice = PAM
    NMDPred = [('Only greater than 50%','Only greater than 50%')]
        rflp = [('True','True')]
    PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "PAM (check all the PAMs you want displayed)", widget=forms.CheckboxSelectMultiple())
    NMD = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Prediction (%)", widget=forms.CheckboxSelectMultiple())
    RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "RFLP Assay", widget=forms.CheckboxSelectMultiple())
    UpG = [('No Upstream G','No Upstream G')]
    noG = forms.MultipleChoiceField(required=False, choices=UpG, label = "Upstream G", widget=forms.CheckboxSelectMultiple())
        offTarget = [('No off-targets', 'No off-targets')]
        off = forms.MultipleChoiceField(required=False, choices=offTarget, label = "Off-target Prediction", widget=forms.CheckboxSelectMultiple())


class CancergeneForm(forms.Form):
    cancer_type= forms.ChoiceField(required=False, label='Cancer Types', choices=cancertypesearch)
    cancergene = forms.CharField(label='Gene', required=False, widget=forms.Textarea(attrs={
                            'placeholder':'Enter a single gene or a list of genes. Each gene on a new line. MAXIMUM INPUT: 10 genes',
                            'style': 'width: 100%; resize:none'
}))

class CancergeneAdvanceForm(forms.Form):    
        PAMChoice = PAM
    NMDPred = [('Only greater than 50%','Only greater than 50%')]
        rflp = [('True','True')]
    PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "PAM (check all the PAMs you want displayed)", widget=forms.CheckboxSelectMultiple())
    NMD = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Prediction (%)", widget=forms.CheckboxSelectMultiple())
    RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "RFLP Assay", widget=forms.CheckboxSelectMultiple())
    UpG = [('No Upstream G','No Upstream G')]
    noG = forms.MultipleChoiceField(required=False, choices=UpG, label = "Upstream G", widget=forms.CheckboxSelectMultiple())
        offTarget = [('No off-targets', 'No off-targets')]
        off = forms.MultipleChoiceField(required=False, choices=offTarget, label = "Off-target Prediction", widget=forms.CheckboxSelectMultiple())

class CancertypeForm(forms.Form):
    c_type= forms.MultipleChoiceField(required=False, choices=cancertype, label= "See a list of sgSTOPs by cancer type", widget=forms.CheckboxSelectMultiple())

class CancertypeAdvanceForm(forms.Form):
    PAMChoice = PAM
    NMDPred = [('Only greater than 50%','Only greater than 50%')]
        rflp = [('True','True')]
    PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "PAM (check all the PAMs you want displayed)", widget=forms.CheckboxSelectMultiple())
    NMD = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Prediction (%)", widget=forms.CheckboxSelectMultiple())
    RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "RFLP Assay", widget=forms.CheckboxSelectMultiple())
    UpG = [('No Upstream G','No Upstream G')]
    noG = forms.MultipleChoiceField(required=False, choices=UpG, label = "Upstream G", widget=forms.CheckboxSelectMultiple())
        offTarget = [('No off-targets', 'No off-targets')]
        off = forms.MultipleChoiceField(required=False, choices=offTarget, label = "Off-target Prediction", widget=forms.CheckboxSelectMultiple())

class SpeciestypeForm(forms.Form):
    CHOICES = (('Homo sapiens', 'Homo sapiens'),('Saccharomyces cerevisiae','Saccharomyces cerevisiae'),('Danio rerio', 'Danio rerio'), ('Mus musculus', 'Mus musculus'), ('Arabidopsis thaliana', 'Arabidopsis thaliana'), ('Drosophila melanogaster', 'Drosophila melanogaster'), ('Rattus norvegicus','Rattus norvegicus'), ('Caenorhabditis elegans', 'Caenorhabditis elegans'))
    species = forms.ChoiceField(required=False, label='Species',choices=CHOICES)

class SpeciestypeAdvanceForm(forms.Form):
    PAMChoice = PAM
    NMDPred = [('Only greater than 50%','Only greater than 50%')]
        rflp = [('True','True')]
    PAM = forms.MultipleChoiceField(required=False, choices=PAMChoice, label= "PAM (check all the PAMs you want displayed)", widget=forms.CheckboxSelectMultiple())
    NMD = forms.MultipleChoiceField(required=False,choices=NMDPred, label = "NMD Prediction (%)", widget=forms.CheckboxSelectMultiple())
    RFLP = forms.MultipleChoiceField(required=False,choices=rflp, label = "RFLP Assay", widget=forms.CheckboxSelectMultiple())
    UpG = [('No Upstream G','No Upstream G')]
    noG = forms.MultipleChoiceField(required=False, choices=UpG, label = "Upstream G", widget=forms.CheckboxSelectMultiple())
        offTarget = [('No off-targets', 'No off-targets')]
        off = forms.MultipleChoiceField(required=False, choices=offTarget, label = "Off-target Prediction", widget=forms.CheckboxSelectMultiple())



class PassForm(forms.Form):
    password = forms.CharField(label='Password')




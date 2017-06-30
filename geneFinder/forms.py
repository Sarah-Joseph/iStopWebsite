from django import forms

class SpeciesForm(forms.Form):
	CHOICES = (('Homo sapiens', 'Homo sapiens'),('Homo sapiens-cancer','Homo sapiens-cancer'), ('Saccharomyces cerevisiae','Saccharomyces cerevisiae'),('Danio rerio', 'Danio rerio'), ('Mus musculus', 'Mus musculus'), ('Arabidopsis thaliana', 'Arabidopsis thaliana'), ('Drosophila melanogaster', 'Drosophila melanogaster'), ('Rattus norvegicus','Rattus norvegicus'), ('Caenorhabditis elegans', 'Caenorhabditis elegans'))
	species = forms.ChoiceField(label='Species',choices=CHOICES)

	
class GeneForm(forms.Form):
	gene = forms.CharField(label='Gene')
	
class PassForm(forms.Form):
	password = forms.CharField(label='Password')

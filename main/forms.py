from logging import PlaceHolder
from django import forms

class SearchForm(forms.Form):
    start=forms.CharField(label="Start", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'start', 'value':'Arad', 'class':'form-control'}))
    goal=forms.CharField(required=False,label="Goal", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'goal', 'class':'form-control'}))
    
class AddMapForm(forms.Form):
    
    country_map=forms.CharField(widget=forms.Textarea(attrs={'name':'country_map','class':'form-control', 'rows':'10', 'cols':'50', 'placeholder':"Arad-Sibiu-value\nArad-Timisoara-value\n"})
                          ,initial='Arad-Sibiu-140\nArad-Timisoara-118\nArad-Zerind-75\nBucharest-Fagaras-211\nBucharest-Giurgiu-90\nBucharest-Pitesti-101\nBucharest-Urziceni-85\nCraiova-Dobreta-120\nCraiova-Pitesti-138\nCraiova-Rimnicu_Vilcea-146\nDobreta-Mehadia-75\nEforie-Hirsova-86\nFagaras-Sibiu-99\nHirsova-Urziceni-98\nIasi-Neamt-87\nIasi-Vaslui-92\nLugoj-Mehadia-70\nLugoj-Timisoara-111\nOradea-Zerind-71\nOradea-Sibiu-151\nPitesti-Rimnicu_Vilcea-97\nRimnicu_Vilcea-Sibiu-80\nUrziceni-Vaslui-142')
    
    straight_length=forms.CharField(widget=forms.Textarea(attrs={'name':'straight_length','class':'form-control', 'rows':'10', 'cols':'50', 'placeholder':"Arad-value\nIasi-value\n"}), initial='Arad-366\nBucharest-0\nCraiova-160\nDobreta-242\nEforie-161\nFagaras-178\nGiurgiu-77\nHirsova-151\nIasi-226\nLugoj-244\nMehadia-241\nNeamt-234\nOradea-380\nPitesti-98\nRimnicu_Vilcea-193\nSibiu-253\nTimisoara-329\nUrziceni-80\nVaslui-199\nZerind-374')
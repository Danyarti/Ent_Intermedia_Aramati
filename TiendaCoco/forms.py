from django import forms 

class productoform (forms.Form):
    producto= forms.CharField(max_length=50)
    descripcion= forms.CharField(max_length=200)
    precio= forms.IntegerField()
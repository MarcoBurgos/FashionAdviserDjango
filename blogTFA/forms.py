from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='', max_length=128,
                           widget= forms.TextInput
                           (attrs={'class':'form-control','placeholder': 'Ingresa tu correo',
				   'name':'EMAIL', 'id':'email', 'onblur':'this.placeholder = "Ingresa tu correo "',
                   'onfocus':'this.placeholder = ""', 'required':'""',
                   'type':'email'}))

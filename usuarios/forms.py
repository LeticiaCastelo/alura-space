from django import forms
#Cria o formulário de Login

class LoginForms(forms.Form):
  nome_login = forms.CharField(
    label = "Nome de Login",
    required = True,
    max_length = 100,
    widget= forms.TextInput(
      attrs = {
        "class": "form-group"
      }
    )
  )
  
  senha = forms.CharField(
    label = "Senha",
    required = True,
    max_length = 70,
    widget = forms.PasswordInput(
      attrs = {
      "class": "form-group"
      }
    )
  )
  
  
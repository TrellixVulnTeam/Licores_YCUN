from django import forms
from .models import *
from .views import *

class contacto_form(forms.Form):
	correo =forms.EmailField(widget = forms.TextInput())
	titulo =forms.CharField(widget = forms.TextInput())
	texto =forms.CharField(widget = forms.Textarea())

class agregar_producto_form(forms.ModelForm):
	class Meta:
		model = Producto
		fields = '__all__'

class agregar_marca_form(forms.ModelForm):
    class Meta:
        model = Marca
        fields = '__all__'  

class agregar_categoria_form(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class agregar_perfil_form(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'         


class login_form (forms.Form):
	usuario = forms.CharField(widget=forms.TextInput())
	clave   = forms.CharField(widget=forms.PasswordInput(render_value=False))

class register_form (forms.Form):
    username        = forms.CharField(widget=forms.TextInput())
    email           = forms.EmailField(widget=forms.TextInput())
    password_1      = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
    password_2      = forms.CharField(label='Confirmar Password',widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
    	username = self.cleaned_data['username']
    	try:
    		u = User.objects.get(username=username)
    	except user.DoesNotExist:
    		return username
    	raise forms.validationError('Nombre de Usuario ya Registrado')
    def clean_email(self):
    	email = self.cleaned_data['email']
    	try:
    		email = User.objects.get(email=email)
    	except User.DoesNotExist:
    		return email
    		raise forms.validationError('Correo Electronico ya Existe')

    def clan_password_2(self):#hace la validacion del password_2
        password_1 = self.cleaned_data['password_1']
        password_2 = self.cleaned_data['password_2']

        if password_1==password_2:
        	pass
        else:
        	raise forms.validationError('PAsswords no Coinciden')

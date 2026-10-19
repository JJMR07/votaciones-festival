from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmar contraseña"
        self.fields["password1"].help_text = ""
        self.fields["password2"].help_text = ""

    class Meta:
        model = User
        fields = ("username",)
        labels = {
            "username": "Nombre de usuario",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }
        help_texts = {
            "username": "",
            "password1": "",
            "password2": "",
        }

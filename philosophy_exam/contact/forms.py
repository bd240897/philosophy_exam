from django import forms
from .models import Comment
from captcha.fields import CaptchaField


param_name = {"type": "text",
              "class": "form-control",
              "id": "floatingName",
              "placeholder": "Вашe почта",
              "aria-label": "Почта", }

param_email = {"type": "text",
               "class": "form-control",
               "id": "floatingEmail",
               "placeholder": "Ваше Имя",
               "aria-label": "Имя", }

parm_msg = {"type": "text",
            "class": "form-control",
            "id": "floatingText",
            "placeholder": "Напишите Ваше сообщение тут",
            "style": "height: 200px", }

param_purpose = {"class": "form-select",
                 "label": "form-control",
                 "Выбор опций": "Выбор опций",}

class CommentForm(forms.ModelForm):
    # purpose = forms.ModelChoiceField(choices=TITLE_CHOICES, widget=forms.Select(attrs=param_purpose))
    captcha = CaptchaField(label='Are you an human?')

    class Meta:
        model = Comment
        exclude = ['create_at']
        widgets = {
            'name': forms.TextInput(attrs=param_name),
            'email': forms.EmailInput(attrs=param_email),
            'purpose': forms.Select(attrs=param_purpose),
            'message': forms.Textarea(attrs=parm_msg)
        }

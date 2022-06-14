from django import forms
from django.core.exceptions import ValidationError

from .models import CommentLection
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

class CommentLectionForm(forms.ModelForm):
    # captcha = CaptchaField(label='Are you an human?')

    # def clean(self):
    #     print("You have forgotten about Fred!")
    #     raise ValidationError("You have forgotten about Fred!")


    class Meta:
        model = CommentLection
        exclude = ['created_at', 'post']
        widgets = {
            'name': forms.TextInput(attrs=param_name),
            'text': forms.Textarea(attrs=parm_msg)
        }

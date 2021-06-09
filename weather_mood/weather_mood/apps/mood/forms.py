from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field
from .models import Mood

class Mood_Create_Form(forms.ModelForm):


    class Meta:
        model = Mood
        fields =[
            'mood',
        ]
        exclude = ()


    helper = FormHelper()
    helper.form_class = 'form-group'
    helper.layout = Layout(
        Field('mood', css_class='form-control'),
    )
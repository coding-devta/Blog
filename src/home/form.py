from django import forms
from froala_editor.widgets import FroalaEditor
from .models import *

class blogform(forms.ModelForm):
    class Meta :
      model = blogmodel
      fields = ['description']
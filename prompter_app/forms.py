from django import forms
from .models import Prompt, Playwright

class PromptForm(forms.ModelForm):
    
    class Meta:
        model = Prompt
        fields = ('idea', 'category', 'label',)


class PlaywrightForm(forms.ModelForm):

    class Meta:
        model = Playwright
        fields = ('name', 'email',)

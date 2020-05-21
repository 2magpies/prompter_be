from rest_framework import serializers
from .models import Prompt, Playwright

class PlaywrightSerializer(serializers.ModelSerializer):
    
    class Meta:
       model = Playwright
       fields = '__all__'  

class PromptSerializer(serializers.ModelSerializer):
    playwrights = PlaywrightSerializer(many=True, read_only=True)

    class Meta:
       model = Prompt
       fields = ['idea', 'category', 'label', 'playwright',]
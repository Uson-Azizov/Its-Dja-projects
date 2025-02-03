from django import forms
from.models import Blog, Areas


class Formblog(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'



class FormArea(forms.ModelForm):
    class Meta:
        model = Areas
        fields = '__all__'



class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'


class UpdateAreaForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = '__all__'











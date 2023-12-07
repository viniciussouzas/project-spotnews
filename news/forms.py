from django import forms
from .models import Category, User, News


class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=200, label='Nome', widget=forms.TextInput())


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        exclude = ['categories']
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['title'].label = 'Título'
        self.fields['title'].widget = forms.TextInput(
            attrs={'type': 'text', 'name': 'title'}
        )
        self.fields['content'].label = 'Conteúdo'
        self.fields['content'].widget = forms.Textarea(
            attrs={'type': 'text', 'name': 'content'}
        )
        self.fields['author'].label = 'Autoria'
        self.fields['author'].widget = forms.Select(
            attrs={'type': 'text', 'name': 'author'},
            choices=[(user.id, user.name) for user in User.objects.all()]
        )
        self.fields['created_at'].label = 'Criado em'
        self.fields['created_at'].widget = forms.DateInput(
            attrs={'type': 'date', 'name': 'created_at'}
        )
        self.fields['image'].label = 'URL da Imagem'
        self.fields['image'].widget = forms.FileInput(
            attrs={'type': 'file', 'name': 'image'}
        )

        self.fields['categories'] = forms.ModelMultipleChoiceField(
            queryset=Category.objects.all(),
            widget=forms.CheckboxSelectMultiple,
        )

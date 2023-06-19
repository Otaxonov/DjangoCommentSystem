from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'parent']

        content = forms.CharField(
            label="Comment",
            required=True,
            max_length=100,
            widget=forms.TextInput(
                attrs={
                    'class': 'form-control mb-3',
                    'placeholder': 'Type Comment Here...'
                }
            )
        )
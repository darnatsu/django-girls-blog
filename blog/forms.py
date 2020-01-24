from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    error_css_class = 'required'

    title = forms.CharField(
        label='Title', 
        max_length=100, 
        widget = forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'This is the title'
            }
        ),
        error_messages = {
            'required':'Please input the Post Title'
        }
    )

    text = forms.CharField(
        label="Context",
        widget = forms.Textarea(
            attrs={
                'class':'form-control',
                'placeholder':'Describe what the post is all about'
            }
        ),
        error_messages = {
            'required':'Please add the Post Context'
        }
    )

    class Meta:
        model = Post
        fields = ('title', 'text',)


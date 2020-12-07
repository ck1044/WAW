from django import forms
# from .widgets import DatePickerWidget

from .models import Post


class WriteForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['date', 'content']
        labels = {
            'date': 'date',
            'content': 'content',
            # 'date_write': 'date_write',
        }
        # widgets = {
        #     'date_write': DatePickerWidget,
        # }

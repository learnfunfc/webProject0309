from django import forms


class EditCourseForm(forms.Form):
    unitName = forms.CharField(label="課程名稱", widget=forms.TextInput(attrs={'class':'form-control'}), max_length=100)
    content = forms.CharField(label="內容",widget=forms.Textarea(attrs={'class':'form-control'}))


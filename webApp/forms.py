from django import forms


class EditCourseForm(forms.Form):
    name = forms.CharField(label="課程名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="內容", widget=forms.Textarea(attrs={'class': 'form-control'}))
    file = forms.FileField(label="上傳檔案")

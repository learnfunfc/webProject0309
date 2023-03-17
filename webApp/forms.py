from django import forms


class CreateCatalogForm(forms.Form):
    name = forms.CharField(label="系統名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="內容", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    file = forms.FileField(label="上傳圖片", required=False)


class CreateCourseForm(forms.Form):
    name = forms.CharField(label="課程名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="內容", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    file = forms.FileField(label="上傳圖片", required=False)


class CreateUnitForm(forms.Form):
    name = forms.CharField(label="單元名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="內容", widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    file = forms.FileField(label="上傳檔案", required=False)

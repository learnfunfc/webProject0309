from django import forms
from .models import Question, Choice


class CreateCatalogForm(forms.Form):
    name = forms.CharField(label="目錄名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="內容", widget=forms.Textarea(attrs={'class': 'form-control'}))
    file = forms.FileField(label="圖片上傳", required=False)


class CreateCourseForm(forms.Form):
    name = forms.CharField(label="課程名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="內容", widget=forms.Textarea(attrs={'class': 'form-control'}))
    file = forms.FileField(label="圖片上傳", required=False)


class CreateUnitForm(forms.Form):
    name = forms.CharField(label="單元名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="內容", widget=forms.Textarea(attrs={'class': 'form-control'}))
    file = forms.FileField(label="上傳檔案", required=False)

# ----------create question form-----------

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice  # 要參照的哪一個model
        fields = ('text', 'is_correct')  # 使用choice model 欄位名稱
        
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'is_correct': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {"text":"選項內容", "is_correct": "正確答案"}


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        num_choices = kwargs.pop('num_choices', 4)  # default 4 choices
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.choice_forms = [ChoiceForm(
            prefix=f'choice_{i}') for i in range(num_choices)]
        self.fields["text"].label="題目"
        

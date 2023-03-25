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
        fields = ('text','tag')
        #表單中輸入逗號分隔的標籤，如 "tag1, tag2, tag3", tags_list = question.tags.split(', ')逗號分隔的字符串，並在需要時將其轉換為列表
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'tag': forms.TextInput(attrs={'class': 'form-control'})
        }
        

    def __init__(self, *args, **kwargs):
        #要創建的相關 ChoiceForm 的數量。如果未提供，則將其設置為 4（表示有 4 個選擇）
        num_choices = kwargs.pop('num_choices', 4)  # 
        super(QuestionForm, self).__init__(*args, **kwargs)
        #創建一個名為 choice_forms 的屬性，該屬性包含 num_choices 數量的 ChoiceForm 實例列表。我們為每個 ChoiceForm 提供了一個唯一的前綴（例如，choice_0，choice_1 等），以便在提交表單時能夠區分這些表單。
        self.choice_forms = [ChoiceForm(
            prefix=f'choice_{i}') for i in range(num_choices)]
        self.fields["text"].label="題目"


class createQuizForm(forms.Form):
    name = forms.CharField(label="測驗名稱", widget=forms.TextInput(
        attrs={'class': 'form-control'}), max_length=100)
    descript = forms.CharField(
        label="測驗敘述", widget=forms.Textarea(attrs={'class': 'form-control'}))

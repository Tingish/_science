from django import forms

class ParagraphFormLabbook(forms.Form):
    textFormTitle = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Title", "row": 5,}))
    textFormText = forms.CharField(widget=forms.Textarea())
    textFormTag = forms.CharField()
        
class ImageFormLabbook(forms.Form):
    imageFormTitle = forms.CharField()
        
class TimelikeFormLabbook(forms.Form):
    timelikeFormTitle = forms.CharField()

        
        
from django import forms
import datetime
from .models import Dayoff


class RequestModelForm(forms.ModelForm):
    type = forms.ChoiceField(widget=forms.RadioSelect, choices=Dayoff.TYPES)
    approve_status = forms.ChoiceField(widget=forms.HiddenInput, required=False)
    date_start = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_end = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Dayoff
        exclude = ['create_by']

    def clean_date_start(self):
        data = self.cleaned_data['date_start']
        if data < datetime.date.today():
            raise forms.ValidationError("เลือกวันในอดีตไม่ได้")
        print(data)
        return data

    def clean_date_end(self):
        data = self.cleaned_data['date_end']
        if data < datetime.date.today():
            raise forms.ValidationError("เลือกวันในอดีตไม่ได้")
        print(data)
        return data

    def clean(self):
        data = super().clean()
        date_start = data.get('date_start')
        date_end = data.get('date_end')

        if str(date_end) < str(date_start):
            self.add_error('date_start', 'วันไม่ถูก')
            self.add_error('date_end', 'วันไม่ถูก')
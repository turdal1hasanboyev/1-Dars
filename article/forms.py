from django import forms

from .models import Member, Jurnal, User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'surname']
        exclude = ['updated_at', 'created_at']

        
class JurnalForm(forms.ModelForm):
    class Meta:
        model = Jurnal
        fields = ['student', 'baho']
        exclude = ['updated_at', 'created_at']


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'
        
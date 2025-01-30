from django import forms

from Catalog.models import Course, Teacher


class CourseForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)


# class CourseForm(forms.ModelForm):
#     class Meta:
#         model = Course
#         fields = ['name', 'description', 'teacher']

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@example.com'):
            raise forms.ValidationError('El correo electrónico debe terminar en @example.com')
        return email
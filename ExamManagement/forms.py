from django import forms
from .models import Exam, MCQQuestion


class AddExamForm(forms.Form):
    exam_title = forms.CharField(label='Exam Title')
    exam_code = forms.IntegerField(label='Exam Code')
    exam_marks = forms.IntegerField(label='Exam Marks')
    # exam_datetime = forms.DateTimeField()
    exam_duration = forms.IntegerField(label='Exam Duration')

    class Meta:
        model = Exam
        fields = [
            'exam_title',
            'exam_code',
            'exam_datetime',
            'exam_marks',
            'exam_duration',
        ]

    def clean(self):
        return super(AddExamForm, self).clean()


class AddMCQquestionform(forms.ModelForm):
    class Meta:
        model = MCQQuestion
        fields = ('question_text', 'option1', 'option2', 'option3', 'option4', 'ques_marks', 'question')

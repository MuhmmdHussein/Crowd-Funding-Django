from django import forms
from .models import Project, Category, Tag, Register


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'details', 'category', 'pictures', 'total_target', 'tags', 'start_time', 'end_time']

    title = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={"placeholder": "Title", "class": "form-control"}
        )
    )
    details = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": "Details", "class": "form-control"}
        )
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={"class": "form-control"}
        )
    )
    pictures = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={"class": "form-control-file"}
        )
    )
    total_target = forms.DecimalField(
        max_digits=10, decimal_places=2,
        widget=forms.NumberInput(
            attrs={"placeholder": "Total Target", "class": "form-control"}
        )
    )
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check"}
        )
    )
    start_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        )
    )
    end_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        )
    )

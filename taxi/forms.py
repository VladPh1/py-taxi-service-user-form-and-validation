from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from taxi.models import Driver, Car


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "license_number",
        )

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        license_validate_format(license_number)
        return license_number


class DriverForm(forms.ModelForm):
    cars = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = get_user_model()
        fields = ("license_number", )


def license_validate_format(value):
    if len(value) == 8:
        raise forms.ValidationError(
            "You must write format like (AAA12345)"
        )
    if not value[:3].isalpha() or not value[:3].isupper():
        raise forms.ValidationError(
            "You must write format like (AAA12345)"
        )
    if not value[4:8].isdigit():
        raise forms.ValidationError(
            "You must write format like (AAA12345)"
        )


class DriverLicenseUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("license_number", )

    def clean_license_number(self):
        license_number = self.cleaned_data.get("license_number")
        license_validate_format(license_number)
        return license_number


class CarForm(forms.ModelForm):
    drivers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Car
        fields = "__all__"

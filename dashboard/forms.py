
from .models import *
from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter First Name'}),
    )
    last_name = forms.CharField(
        required=False,
        label='Last Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Last Name'}),
    )
    addressLine1 = forms.CharField(
        required=True,
        label='Address Line 1',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address Line 1'}),
    )
    addressLine2 = forms.CharField(
        required=False,
        label='Address Line 2',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address Line 1'}),
    )
    city = forms.CharField(
        required=True,
        label='City',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter City'}),
    )
    province = forms.CharField(
        required=True,
        label='Province',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Province'}),
    )
    country = forms.CharField(
        required=True,
        label='Country',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Country'}),
    )
    postalCode = forms.CharField(
        required=True,
        label='Postal Code',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Postal Code'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6'),
                Column('last_name', css_class='form-group col-md-6')
            ),
            Row(
                Column('addressLine1', css_class='form-group col-md-6'),
                Column('addressLine2', css_class='form-group col-md-6')
            ),
            Row(
                Column('city', css_class='form-group col-md-6'),
                Column('province', css_class='form-group col-md-6')
            ),
            Row(
                Column('country', css_class='form-group col-md-6'),
                Column('postalCode', css_class='form-group col-md-6')
            ),
            Submit('submit', 'Save Changes',
                   css_class="btn btn-primary me-2 col-md-2")
        )

    class Meta:
        model = Profile
        fields = ['addressLine1', 'addressLine2',
                  'city', 'province', 'country', 'postalCode']

    def save(self, *args, **kwargs):
        user = self.instance.user
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        profile = super(ProfileForm, self).save(*args, **kwargs)
        return profile


class ProfileImageForm(forms.ModelForm):
    profileImage = forms.ImageField(
        required=False,
        label='Upload Profile Image',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('profileImage', css_class='form-group col-md-12')
            ),
            Submit('submit', 'Save Image',
                   css_class="btn btn-primary me-2 mb-4 mt-3")
        )

    class Meta:
        model = Profile
        fields = ['profileImage']


class HomeForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Title'}),
    )

    content = forms.CharField(
        required=True,
        label='Content',
        widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Content'}),
    )

    image = forms.ImageField(
        required=False,
        label='Upload Profile Image',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-12'),
            ),
            Row(
                Column('content', css_class='form-group col-md-12')
            ),

            Row(
                Column('image', css_class='form-group col-md-12')
            ),

            Submit('submit', 'Save Changes',
                   css_class="btn btn-primary me-2 col-md-2")
        )

    class Meta:
        model = Home
        fields = ['title', 'content', 'image']


class PricingForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Title'}),
    )

    price = forms.CharField(
        required=True,
        label='Price',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Price'}),
    )

    duration = forms.CharField(
        required=True,
        label='Duration',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Duration'}),
    )

    quantity = forms.CharField(
        required=True,
        label='Quantity',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Quantity'}),
    )

    speed = forms.CharField(
        required=True,
        label='Speed',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Speed'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-12'),
            ),
            Row(
                Column('price', css_class='form-group col-md-12')
            ),

            Row(
                Column('duration', css_class='form-group col-md-12')
            ),
            Row(
                Column('quantity', css_class='form-group col-md-12')
            ),
            Row(
                Column('speed', css_class='form-group col-md-12')
            ),

            Submit('submit', 'Save Changes',
                   css_class="btn btn-primary me-2 col-md-2")
        )

    class Meta:
        model = Pricing
        fields = ['title', 'price', 'duration', 'quantity', 'speed']


class FeedbackForm(forms.ModelForm):

    name = forms.CharField(
        required=True,
        label='Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Name'}),
    )
    location = forms.CharField(
        required=True,
        label='Location',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Address'}),
    )

    content = forms.CharField(
        required=True,
        label='Content',
        widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Content'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='form-group col-md-12'),
            ),
            Row(
                Column('location', css_class='form-group col-md-12')
            ),

            Row(
                Column('content', css_class='form-group col-md-12')
            ),

            Submit('submit', 'Save Changes',
                   css_class="btn btn-primary me-2 col-md-2")
        )

    class Meta:
        model = Feedback
        fields = ['name', 'location', 'content']


class FaqsForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Title'}),
    )

    content = forms.CharField(
        required=True,
        label='Content',
        widget=forms.Textarea(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Content'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-12'),
            ),

            Row(
                Column('content', css_class='form-group col-md-12')
            ),

            Submit('submit', 'Save Changes',
                   css_class="btn btn-primary me-2 col-md-2")
        )

    class Meta:
        model = Faqs
        fields = ['title', 'content']


class CoverageForm(forms.ModelForm):

    coverage_name = forms.CharField(
        required=True,
        label='Coverage Name',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Coverage Name'}),
    )

    strength = forms.CharField(
        required=True,
        label='Coverage Strength',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Strength'}),
    )

    status = forms.IntegerField(
        required=True,
        label='Coverage Status',
        widget=forms.NumberInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Enter Status', 'min':0, 'max':1}), 
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('coverage_name', css_class='form-group col-md-12'),
            ),

            Row(
                Column('strength', css_class='form-group col-md-12')
            ),

            Row(
                Column('status', css_class='form-group col-md-12')
            ),

            Submit('submit', 'Save Changes',
                   css_class="btn btn-primary me-2 col-md-2")
        )

    class Meta:
        model = Coverage
        fields = ['coverage_name', 'strength', 'status']
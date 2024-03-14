from django import forms
from .models  import *

class mail_form(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class BncRegisterForm(forms.ModelForm):
    class Meta:
        model = bnc_register_mem
        fields = ['name', 'gmail']

class ImagesForm(forms.ModelForm):
    pic = forms.FileField(widget=forms.TextInput(attrs={
        "name": "images",
        "type": "file",
        "multiple": "true",
    }), required=False, label="")
    
    class Meta:
        model = Image
        fields = ["title", "pic"]

class UserProfileForm(forms.ModelForm):
    instagram_link = forms.CharField(max_length=200, required=False)  
    user_image = forms.FileField(widget=forms.FileInput(attrs={'id': 'file', 'onchange': 'loadFile(event)'}))
    class Meta:
        model = UserProfile
        fields = '__all__'


    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        self.fields['email_address'].widget.attrs['readonly'] = 'readonly'
        self.fields['register_id'].widget.attrs['id'] = 'id_register_id'
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'input'

class UsereditForm(forms.ModelForm):
    instagram_link = forms.CharField(
    max_length=200,
    required=False,
    widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Instagram Link'})
)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative'}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative'}))
    company_address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-alternative'}))

    class Meta:
        model = UserProfile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Username'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Email Address'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Last Name'}),
            'address': forms.Textarea(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Address'}),
            'city': forms.Textarea(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter City'}),
            'pincode': forms.Textarea(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Pincode'}),
            'instagram_link': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Instagram Link'}),
            'whatsapp_number': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Whatsapp Number'}),
            'brand_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Brand Name'}),
            'service_name': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Service Name'}),
            'company_address': forms.Textarea(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Company Address'}),
            'register_id': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Register ID'}),
            'user_image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'position': forms.TextInput(attrs={'class': 'form-control form-control-alternative', 'placeholder': 'Enter Position'}),
            
        }

class MeetingForm(forms.ModelForm):
    class Meta:
        model = meeting_assign
        fields = '__all__'


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

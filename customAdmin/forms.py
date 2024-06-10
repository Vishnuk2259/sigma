from django.forms import ModelForm
from django import forms
from banners.models import *
from clients.models import *
from facilities.models import *
from partners.models import *
from services.models import *
from shared.models import *
from team.models import *

class BannerForm(ModelForm):
    image = forms.ImageField(widget = forms.FileInput, required = False)

    class Meta:
        model = Banner
        fields = ('page_url','banner_type','content', 'image', 'title', 'about')

    def __init__(self, *args, **kwargs):
        super(BannerForm, self).__init__(*args, **kwargs)
        self.fields['page_url'].widget.attrs.update({'class': 'form-control'})
        self.fields['banner_type'].widget.attrs.update({'class': 'form-control'})
        self.fields['content'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['about'].widget.attrs.update({'class': 'form-control'})


class ClientForm(ModelForm):
    image = forms.ImageField(widget = forms.FileInput, required = False)

    class Meta: 
        model = Client
        fields = ('name', 'description', 'image', 'feedback')

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['feedback'].widget.attrs.update({'class': 'form-control'})

class FacilitiesForm(ModelForm):
    image = forms.ImageField(widget = forms.FileInput, required = False)

    class Meta:
        model = Facilities
        fields = ('name', 'description', 'image', 'sub_heading', 'sub_description', 'sub_heading2', 'sub_description2')

    def __init__(self, *args, **kwargs):
        super(FacilitiesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_heading'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_heading2'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_description2'].widget.attrs.update({'class': 'form-control'})


class PartnersForm(ModelForm):
    image = forms.ImageField(widget = forms.FileInput, required = False)

    class Meta:
        model = Partners
        fields = ('name', 'description', 'image', 'website')

    def __init__(self, *args, **kwargs):
        super(PartnersForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['website'].widget.attrs.update({'class': 'form-control'})

class ServicesForm(ModelForm):
    image = forms.ImageField(widget = forms.FileInput, required = False)

    class Meta:
        model = Services
        fields = ('name', 'description', 'image', 'sub_heading', 'sub_description', 'sub_heading2', 'sub_description2')

    def __init__(self, *args, **kwargs):
        super(ServicesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_heading'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_description'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_heading2'].widget.attrs.update({'class': 'form-control'})
        self.fields['sub_description2'].widget.attrs.update({'class': 'form-control'})

class GalleryForm(ModelForm):
    image = forms.ImageField(widget = forms.FileInput)

    class Meta:
        model = Gallery
        fields = ('image', 'title', 'description')

    def __init__(self, *args, **kwargs):
        super(GalleryForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

class ContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})
        self.fields['message'].widget.attrs.update({'class': 'form-control'})

class SettingsForm(ModelForm):
    logo = forms.ImageField(widget = forms.FileInput, required = False)
    favicon = forms.ImageField(widget = forms.FileInput, required = False)

    class Meta:
        model = Settings
        fields = ('name', 'logo', 'description', 'favicon', 'address', 'phone', 'email', 'facebook', 'twitter', 'instagram')

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['facebook'].widget.attrs.update({'class': 'form-control'})
        self.fields['twitter'].widget.attrs.update({'class': 'form-control'})
        self.fields['instagram'].widget.attrs.update({'class': 'form-control'})

class TeamForm(ModelForm):
    image = forms.ImageField(widget = forms.FileInput, required = False)

    class Meta:
        model = Team
        fields = ('name', 'member_category', 'member_designation', 'image', 'linkedin')

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['member_category'].widget.attrs.update({'class': 'form-control'})
        self.fields['member_designation'].widget.attrs.update({'class': 'form-control'})
        self.fields['linkedin'].widget.attrs.update({'class': 'form-control'})

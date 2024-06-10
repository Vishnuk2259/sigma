from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import *
from shared.pagination import *
from django.core.paginator import Paginator


@login_required(login_url='admin_login')
def admin_home(request):

    banner_count = Banner.objects.count()

    client_count = Client.objects.count()

    facility_count = Facilities.objects.count()

    partner_count = Partners.objects.count()

    service_count = Services.objects.count()

    gallery_count = Gallery.objects.count()

    contact_count = Contact.objects.count()

    settings_count = Settings.objects.count()

    team_count = Team.objects.count()

    context  = {
        'banner_count': banner_count, 
        'client_count': client_count, 
        'facility_count': facility_count, 
        'partner_count': partner_count, 
        'gallery_count': gallery_count, 
        'service_count': service_count, 
        'contact_count': contact_count, 
        'settings_count': settings_count, 
        'team_count': team_count
    }

    return render(request, 'custom_admin/index.html', context)





@never_cache
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_home')
            else:
                return render(request, 'accounts/login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def admin_logout(request):
    logout(request)
    return redirect('admin_login')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('admin_home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})





@login_required(login_url='admin_login')
@never_cache
def add_banner(request):
    form = BannerForm()
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Banner added successfully')
            return redirect('banner_view') 
    context = {
        'form': form,
        'table_name': 'Add Banner'
    }
    return render(request, 'custom_admin/add_banner.html', context)

@login_required(login_url='admin_login')
def banner_view(request):

    banners = Banner.objects.all().order_by('created_at')

    paginator = Paginator(banners, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_banner.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_banner(request, id):
    if Banner.objects.filter(id=id).exists():
        banner_instance = Banner.objects.get(id=id)
        banner_instance.delete()
        return redirect('banner_view')
    else:
        return redirect('banner_view')

@login_required(login_url='admin_login')
@never_cache
def edit_banner(request, id):
        banner_instance = get_object_or_404(Banner, id=id)

        if request.method == 'POST':
            form = BannerForm(request.POST, request.FILES, instance=banner_instance)
            if form.is_valid():
                form.save()
                return redirect('banner_view')

        else:
            form = BannerForm(instance=banner_instance)

        context = {
            'form': form,
            'table_name': banner_instance.title,
            'banner_id': banner_instance.id
        }
        return render(request, 'custom_admin/edit_banner.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_client(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Client added successfully')
            return redirect('client_view') 
    context = {
        'form': form,
        'table_name': 'Add Client'
    }
    return render(request, 'custom_admin/add_client.html', context)

@login_required(login_url='admin_login')
def client_view(request):

    clients = Client.objects.all().order_by('created_at')

    paginator = Paginator(clients, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_client.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_client(request,id):
    if Client.objects.filter(id=id).exists():
        client_instance = Client.objects.get(id=id)
        client_instance.delete()
        return redirect('client_view')
    else:
        return redirect('client_view')

@login_required(login_url='admin_login')
@never_cache
def edit_client(request, id):
        client_instance = get_object_or_404(Client, id=id)

        if request.method == 'POST':
            form = ClientForm(request.POST, request.FILES, instance=client_instance)
            if form.is_valid():
                form.save()
                return redirect('client_view')

        else:
            form = ClientForm(instance = client_instance)

        context = {
            'form': form,
            'table_name': client_instance.name,
            'client_id': client_instance.id
        }
        return render(request, 'custom_admin/edit_client.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_facilities(request):
    form = FacilitiesForm()
    if request.method == 'POST':
        form = FacilitiesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Facility added successfully')
            return redirect('facility_view') 
    context = {
        'form': form,
        'table_name': 'Add Facility'
    }
    return render(request, 'custom_admin/add_facility.html', context)

@login_required(login_url='admin_login')
def facilities_view(request):

    facilities = Facilities.objects.all().order_by('created_at')

    paginator = Paginator(facilities, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_facility.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_facilities(request,id):
    if Facilities.objects.filter(id=id).exists():
        facility_instance = Facilities.objects.get(id=id)
        facility_instance.delete()
        return redirect('facility_view')
    else:
        return redirect('facility_view')
    
@login_required(login_url='admin_login')
@never_cache
def edit_facilities(request, id):
        facility_instance = get_object_or_404(Facilities, id=id)

        if request.method == 'POST':
            form = FacilitiesForm(request.POST, request.FILES, instance=facility_instance)
            if form.is_valid():
                form.save()
                return redirect('facility_view')

        else:
            form = FacilitiesForm(instance = facility_instance)

        context = {
            'form': form,
            'table_name': facility_instance.name,
            'facility_id': facility_instance.id
        }
        return render(request, 'custom_admin/edit_facility.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_partners(request):
    form = PartnersForm()
    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Partner added successfully')
            return redirect('partner_view') 
    context = {
        'form': form,
        'table_name': 'Add Partner'
    }
    return render(request, 'custom_admin/add_partner.html', context)

@login_required(login_url='admin_login')
def partners_view(request):

    partners = Partners.objects.all().order_by('created_at')

    paginator = Paginator(partners, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_partner.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_partners(request,id):
    if Partners.objects.filter(id=id).exists():
        partner_instance = Partners.objects.get(id=id)
        partner_instance.delete()
        return redirect('partner_view')
    else:
        return redirect('partner_view')
    
@login_required(login_url='admin_login')
@never_cache
def edit_partners(request, id):
        partner_instance = get_object_or_404(Partners, id=id)

        if request.method == 'POST':
            form = PartnersForm(request.POST, request.FILES, instance=partner_instance)
            if form.is_valid():
                form.save()
                return redirect('partner_view')

        else:
            form = PartnersForm(instance = partner_instance)

        context = {
            'form': form,
            'table_name': partner_instance.name,
            'partner_id': partner_instance.id
        }
        return render(request, 'custom_admin/edit_partner.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_services(request):
    form = ServicesForm()
    if request.method == 'POST':
        form = ServicesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service added successfully')
            return redirect('service_view') 
    context = {
        'form': form,
        'table_name': 'Add Service'
    }
    return render(request, 'custom_admin/add_service.html', context)

@login_required(login_url='admin_login')
def services_view(request):

    services = Services.objects.all().order_by('created_at')

    paginator = Paginator(services, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_service.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_services(request,id):
    if Services.objects.filter(id=id).exists():
        service_instance = Services.objects.get(id=id)
        service_instance.delete()
        return redirect('service_view')
    else:
        return redirect('service_view')
    
@login_required(login_url='admin_login')
@never_cache
def edit_services(request, id):
        service_instance = get_object_or_404(Services, id=id)

        if request.method == 'POST':
            form = ServicesForm(request.POST, request.FILES, instance = service_instance)
            if form.is_valid():
                form.save()
                return redirect('service_view')

        else:
            form = ServicesForm(instance = service_instance)

        context = {
            'form': form,
            'table_name': service_instance.name,
            'service_id': service_instance.id
        }
        return render(request, 'custom_admin/edit_service.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_gallery(request):
    form = GalleryForm()
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gallery added successfully')
            return redirect('gallery_view') 
    context = {
        'form': form,
        'table_name': 'Add Gallery'
    }
    return render(request, 'custom_admin/add_gallery.html', context)

@login_required(login_url='admin_login')
def gallery_view(request):

    galleries = Gallery.objects.all().order_by('created_at')

    paginator = Paginator(galleries, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_gallery.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_gallery(request,id):
    if Gallery.objects.filter(id=id).exists():
        gallery_instance = Gallery.objects.get(id=id)
        gallery_instance.delete()
        return redirect('gallery_view')
    else:
        return redirect('gallery_view')
    
@login_required(login_url='admin_login')
@never_cache
def edit_gallery(request, id):
        gallery_instance = get_object_or_404(Gallery, id=id)

        if request.method == 'POST':
            form = GalleryForm(request.POST, request.FILES, instance = gallery_instance)
            if form.is_valid():
                form.save()
                return redirect('gallery_view')

        else:
            form = GalleryForm(instance = gallery_instance)

        context = {
            'form': form,
            'table_name': 'Edit Gallery',
            'gallery_id': gallery_instance.id
        }
        return render(request, 'custom_admin/edit_gallery.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact added successfully')
            return redirect('contact_view') 
    context = {
        'form': form,
        'table_name': 'Add Contact'
    }
    return render(request, 'custom_admin/add_contact.html', context)

@login_required(login_url='admin_login')
def contact_view(request):

    contacts = Contact.objects.all().order_by('created_at')

    paginator = Paginator(contacts, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_contact.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_contact(request,id):
    if Contact.objects.filter(id=id).exists():
        contact_instance = Contact.objects.get(id=id)
        contact_instance.delete()
        return redirect('contact_view')
    else:
        return redirect('contact_view')
    
@login_required(login_url='admin_login')
@never_cache
def edit_contact(request, id):
        contact_instance = get_object_or_404(Contact, id=id)

        if request.method == 'POST':
            form = ContactForm(request.POST, request.FILES, instance = contact_instance)
            if form.is_valid():
                form.save()
                return redirect('contact_view')

        else:
            form = ContactForm(instance = contact_instance)

        context = {
            'form': form,
            'table_name': contact_instance.name,
            'contact_id': contact_instance.id
        }
        return render(request, 'custom_admin/edit_contact.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_settings(request):
    form = SettingsForm()
    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Setting added successfully')
            return redirect('settings_view') 
    context = {
        'form': form,
        'table_name': 'Add Settings'
    }
    return render(request, 'custom_admin/add_setting.html', context)

@login_required(login_url='admin_login')
def settings_view(request):

    settings = Settings.objects.all().order_by('created_at')

    paginator = Paginator(settings, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_setting.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_settings(request,id):
    if Settings.objects.filter(id=id).exists():
        setting_instance = Settings.objects.get(id=id)
        setting_instance.delete()
        return redirect('settings_view')
    else:
        return redirect('settings_view')
    
@login_required(login_url='admin_login')
@never_cache
def edit_settings(request, id):
        setting_instance = get_object_or_404(Settings, id=id)

        if request.method == 'POST':
            form = SettingsForm(request.POST, request.FILES, instance = setting_instance)
            if form.is_valid():
                form.save()
                return redirect('settings_view')

        else:
            form = SettingsForm(instance = setting_instance)

        context = {
            'form': form,
            'table_name': setting_instance.name,
            'settings_id': setting_instance.id
        }
        return render(request, 'custom_admin/edit_setting.html', context)





@login_required(login_url='admin_login')
@never_cache
def add_team(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Team member added successfully')
            return redirect('team_view') 
    context = {
        'form': form,
        'table_name': 'Add Team'
    }
    return render(request, 'custom_admin/add_team.html', context)

@login_required(login_url='admin_login')
def team_view(request):

    teams = Team.objects.all().order_by('created_at')

    paginator = Paginator(teams, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'custom_admin/view_team.html', {'page_obj': page_obj})

@login_required(login_url='admin_login')
def delete_team(request,id):
    if Team.objects.filter(id=id).exists():
        team_instance = Team.objects.get(id=id)
        team_instance.delete()
        return redirect('team_view')
    else:
        return redirect('team_view')
    
@login_required(login_url='admin_login')
@never_cache
def edit_team(request, id):
        if request.method == 'POST':
            team_instance = Team.objects.get(id=id)
            form = TeamForm(request.POST, request.FILES, instance = team_instance)
            if form.is_valid():
                form.save()
                return redirect('team_view')

        else:
            team_instance = Team.objects.get(id=id)
            form = TeamForm(instance = team_instance)

        context = {
            'form': form,
            'table_name': team_instance.name,
            'team_id': team_instance.id
        }
        return render(request, 'custom_admin/edit_team.html', context)
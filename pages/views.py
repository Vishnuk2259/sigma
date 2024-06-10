from django.shortcuts import render,redirect
from banners.models import Banner
from partners.models import Partners
from shared.models import Settings, Gallery, Contact
from team.models import Team
from clients.models import Client
from services.models import Services
from facilities.models import Facilities
from django.views.decorators.http import require_POST
from django.templatetags.static import static

def index(request):
    try:
        hero_banner = Banner.objects.filter(page_url = '/index', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try:
        body_banners = Banner.objects.filter(page_url = '/index', about = 'Body banner', banner_type = 'Body').all
    except Banner.DoesNotExist:
        body_banners = None

    try:
        whatwedo_banner = Banner.objects.filter(page_url = '/index', about = 'What we do', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        whatwedo_banner = None

    try:
        whatwedo_contents = Banner.objects.filter(page_url = '/index', about = 'What we do content', banner_type = 'Body').all
    except Banner.DoesNotExist:
        whatwedo_contents = None
    
    try:
        partner_banner = Banner.objects.filter(page_url = '/index', about = 'Partners', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        partner_banner = None
    
    try:
        partners = Partners.objects.all
    except Partners.DoesNotExist:
        partners = None

    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'index.html', {'hero_banner': hero_banner, 'body_banners': body_banners, 'whatwedo_banner': whatwedo_banner, 'whatwedo_contents': whatwedo_contents, 'partner_banner': partner_banner, 'partners': partners, 'settings': settings})

def client(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/clients', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try:
        clients = Client.objects.all
    except Client.DoesNotExist:
        clients = None

    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'clients.html', {'hero_banner': hero_banner, 'clients': clients, 'settings': settings})

def contact(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/contact', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try:
        get_in_touch_banner = Banner.objects.filter(page_url = '/contact', about = 'Get in touch', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        get_in_touch_banner = None

    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'contact.html', {'hero_banner': hero_banner, 'settings': settings, 'get_in_touch_banner': get_in_touch_banner})

@require_POST
def submit_contact_form(request):
    name = request.POST.get('name', '')
    email = request.POST.get('email', '')
    phone = request.POST.get('phone', '')
    message = request.POST.get('message', '')

    contact = Contact.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message
    )

    php_script_url = static('forms/send_email.php')

    return redirect(php_script_url)


def facilities(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/facilities', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try: 
        facilities = Facilities.objects.all
    except Facilities.DoesNotExist:
        facilities = None

    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'facilities.html', {'hero_banner': hero_banner, 'facilities': facilities, 'settings': settings})

def gallery(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/gallery', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try:
        galleries = Gallery.objects.all
    except Gallery.DoesNotExist:
        galleries = None
    
    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'gallery.html', {'hero_banner': hero_banner, 'galleries': galleries, 'settings': settings}) 

def partners(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/partners', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try: 
        partners = Partners.objects.all
    except Partners.DoesNotExist:
        partners = None
    
    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'partners.html', {'hero_banner': hero_banner, 'partners': partners, 'settings': settings}) 

def profile(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/profile', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try:
        mission_banner = Banner.objects.filter(page_url = '/profile', about = 'Mission', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        mission_banner = None

    try:
        vission_banner = Banner.objects.filter(page_url = '/profile', about = 'Vission', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        vission_banner = None
        
    try:
        body_banner = Banner.objects.filter(page_url = '/profile', about = 'Body banner', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        body_banner = None
    
    try:
        value_banner = Banner.objects.filter(page_url = '/profile', about = 'Value', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        value_banner = None

    try:
        team_banner = Banner.objects.filter(page_url = '/profile', about = 'Team', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        team_banner = None

    try:
        teams = Team.objects.all
    except Team.DoesNotExist:
        teams = None

    try:
        why_sigma_banner = Banner.objects.filter(page_url = '/profile', about = 'Why sigma', banner_type = 'Body').latest('created_at')
    except Banner.DoesNotExist:
        why_sigma_banner = None

    try:
        clients = Client.objects.exclude(feedback = '')
    except Client.DoesNotExist:
        clients = None

    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'profile.html', {'hero_banner': hero_banner, 'mission_banner': mission_banner, 'vission_banner': vission_banner, 'value_banner': value_banner, 'team_banner': team_banner, 'teams':teams, 'why_sigma_banner': why_sigma_banner, 'settings': settings, 'clients': clients, 'body_banner': body_banner})

def services(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/service', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try: 
        services = Services.objects.all
    except Services.DoesNotExist:
        services = None

    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'services.html', {'hero_banner': hero_banner, 'services': services, 'settings': settings})

def team(request):

    try:
        hero_banner = Banner.objects.filter(page_url = '/team', about = 'Hero banner', banner_type = 'Header').latest('created_at')
    except Banner.DoesNotExist:
        hero_banner = None

    try:
        management_teams = Team.objects.filter(member_category = 'Top management team')
    except Team.DoesNotExist:
        management_teams = None
    
    try:
        engineering_teams = Team.objects.filter(member_category = 'Engineering team')
    except Team.DoesNotExist:
        engineering_teams = None

    try:
        settings = Settings.objects.latest('created_at')
    except Settings.DoesNotExist:
        settings = None

    return render(request, 'team.html', {'hero_banner': hero_banner, 'management_teams': management_teams, 'engineering_teams': engineering_teams, 'settings': settings})

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Session
from .models import Febes
from .models import FebeParameters
from .models import Sources
from .models import Setup
from .models import Integrations
from .models import Cal
from .models import Aim
from .models import Foc
from .forms import SessionForm
from .forms import AdminFebesForm
from .forms import FebeForm
from .forms import SourcesForm
from .forms import SetupForm
from .forms import SetupShortForm
from .forms import IntegrationsForm
from .forms import CalForm
from .forms import AimForm
from .forms import FocForm

import json
import os
from django.core import serializers
from django.shortcuts import redirect

from datetime import date




def home(request):

    try:
        creation_form = SessionForm()
        available_sessions = Session.objects.all()
        return render(request, 'sessions_library.html', {
                                                    'sessions_list': available_sessions, 
                                                    'form':creation_form})
 

    except:

        sessionId="void"
        return render(request, 'error.html', {'st':sessionId})
    
    

def admin_febes(request):

    try:
        creation_form = AdminFebesForm()
        available_admin_febes = Febes.objects.all()
        return render(request, 'admin_febes_library.html', {
                                                    'febes_list': available_admin_febes, 
                                                    'form':creation_form})
 

    except:

        sessionId="void"
        return render(request, 'error.html', {'st':sessionId})
    

def create_configurated_febe(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        new_form = AdminFebesForm(request.POST) # Bound form
        if new_form.is_valid():
            new_adminfebe = new_form.save()

            creation_form = AdminFebesForm()
            available_admin_febes = Febes.objects.all()
            return render(request, 'admin_febes_library.html', {
                                                    'febes_list': available_admin_febes, 
                                                    'form':creation_form})
        else:
            creation_form = AdminFebesForm()
            available_admin_febes = Febes.objects.all()
            return render(request, 'admin_febes_library.html', {
                                                    'febes_list': available_admin_febes, 
                                                    'form':creation_form})

        
def remove_admin_febe(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = Febes.objects.get(id=item_id)
        item.delete()
        creation_form = AdminFebesForm()
        available_admin_febes = Febes.objects.all()
        return render(request, 'admin_febes_library.html', {
                                                'febes_list': available_admin_febes, 
                                                'form':creation_form})
def upload_admin_febe(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = Febes.objects.get(id=item_id)
        update_form = AdminFebesForm(instance=item)
        return render(request, 'update_febes_library.html', {
                                                    'item_id': item_id, 
                                                    'form':update_form})


def update_configurated_febe(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        item = Febes.objects.get(id=item_id)
        form = AdminFebesForm(request.POST, instance=item) # Bound form
        if form.is_valid():
            form.save()

            creation_form = AdminFebesForm()
            available_admin_febes = Febes.objects.all()
            return render(request, 'admin_febes_library.html', {
                                                    'febes_list': available_admin_febes, 
                                                    'form':creation_form})
        else:
            item_id = int(request.POST.get('item_id'))
            item = Febes.objects.get(id=item_id)
            update_form = AdminFebesForm(instance=item)
            return render(request, 'update_febes_library.html', {'form':update_form})



def upload_session(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        item_id = int(request.POST.get('item_id'))
        item = Session.objects.get(id=item_id)
        #available_febes = Febe_parameters.objects.all()
        available_febes = FebeParameters.objects.filter(session=item)
        available_sources = Sources.objects.filter(session=item)
        available_setups = Setup.objects.filter(session=item)
        available_integrations = Integrations.objects.filter(session=item)
        available_admin_febes = Febes.objects.all()
 
        return render(request, 'session_main.html', {
                                                    'session': item,
                                                    'febes_list': available_febes, 
                                                    'sources_list': available_sources,
                                                    'setups_list': available_setups,
                                                    'integrations_list': available_integrations,
                                                    'admin_febes_list': available_admin_febes })

def remove_session(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))  
        item = Session.objects.get(id=item_id)
        item.delete()
        creation_form = SessionForm
        available_sessions = Session.objects.all()
        return render(request, 'sessions_library.html', {
                                                    'sessions_list': available_sessions, 
                                                    'form':creation_form})



def create_session(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        new_form = SessionForm(request.POST) # Bound form
        if new_form.is_valid():
            new_session = new_form.save()

            creation_form = SessionForm
            available_sessions = Session.objects.all()
            return render (request, 'sessions_library.html', {
                                                    'sessions_list': available_sessions, 
                                                    'form':creation_form})
        
def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file)
def append_to_json_file(file_path, data):
    with open(file_path, 'a') as file:
        json.dump(data, file)

        
def json_file(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        item_id = int(request.POST.get('item_id'))
        item = Session.objects.get(id=item_id)
        available_febes = FebeParameters.objects.filter(session=item)
        available_sources = Sources.objects.filter(session=item)
        available_setups = Setup.objects.filter(session=item)
        available_integrations = Integrations.objects.filter(session=item)
        available_admin_febes = Febes.objects.all()
        filename = str (item) +"_" + str(date.today()) +".json"
        data = serializers.serialize("json", available_febes)
        write_json_file (filename, data)
        data = serializers.serialize("json", available_sources)
        append_to_json_file (filename, data)
        data = serializers.serialize("json", available_setups)
        append_to_json_file (filename, data)
        data = serializers.serialize("json", available_integrations)
        append_to_json_file (filename, data)
 
        return render(request, 'session_main.html', {
                                                    'session': item,
                                                    'febes_list': available_febes, 
                                                    'sources_list': available_sources,
                                                    'setups_list': available_setups,
                                                    'integrations_list': available_integrations,
                                                    'admin_febes_list': available_admin_febes })


def add_febe1(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))  
        session_id = Session.objects.get(id=item_id)
        available_admin_febes = Febes.objects.all()
        return render(request, 'febe_main1.html', {
                                                    'febes_list': available_admin_febes,
                                                    'session': session_id,})







        creation_form = FebeForm(item_id)
        return render (request, 'febe_main.html', {
                                                    'session': session_id, 
                                                    'form':creation_form})
        
def add_febe(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))  
        session_id = Session.objects.get(id=item_id)
        febe_id = int(request.POST.get('actual_febe_id'))  
        febe = Febes.objects.get(id=febe_id)

        creation_form = FebeForm(item_id,febe_id)
        return render (request, 'febe_main.html', {
                                                    'session': session_id, 
                                                    'febe': febe, 
                                                    'form':creation_form})
        





def create_febe(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        item2_id = int(request.POST.get('item2_id'))
        new_form = FebeForm(item_id, item2_id, request.POST) # Bound form
        if new_form.is_valid():
            new_session = new_form.save()

            #item_id = int(request.POST.get('item_id'))
            item = Session.objects.get(id=item_id)
            available_febes = FebeParameters.objects.filter(session=item)
            available_sources = Sources.objects.filter(session=item)
            available_setups = Setup.objects.filter(session=item)
            available_integrations = Integrations.objects.filter(session=item)
    
            return render(request, 'session_main.html', {
                                                        'session': item,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })




def remove_febe(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = FebeParameters.objects.get(id=item_id)
        item.delete()

        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        available_febes = FebeParameters.objects.filter(session=session)
        available_sources = Sources.objects.filter(session=session)
        available_setups = Setup.objects.filter(session=session)
        available_integrations = Integrations.objects.filter(session=session)
 
        return render(request, 'session_main.html', {
                                                    'session': session,
                                                    'febes_list': available_febes, 
                                                    'sources_list': available_sources,
                                                    'setups_list': available_setups,
                                                    'integrations_list': available_integrations })





"""
def upload_febe(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = FebeParameters.objects.get(id=item_id)
        #item.delete()

        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        available_febes = FebeParameters.objects.filter(session=session)
        available_sources = Sources.objects.filter(session=session)
        available_setups = Setup.objects.filter(session=session)
        available_integrations = Integrations.objects.filter(session=session)
 
        return render(request, 'session_main.html', {
                                                    'session': session,
                                                    'febes_list': available_febes, 
                                                    'sources_list': available_sources,
                          sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
                                  'setups_list': available_setups,
                                                    'integrations_list': available_integrations })
"""

def upload_febe(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = FebeParameters.objects.get(id=item_id)
        #item.delete()





        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        item_id = int(request.POST.get('item_id'))
        item = FebeParameters.objects.get(id=item_id)
#        febe_id = int(request.POST.get('actual_febe_id'))
        febe_id = 3
        #febe = Febes.objects.get(id=febe_id)
        update_form = FebeForm(sessionid, febe_id, instance=item)
        return render(request, 'update_febe.html', {
                                                    'item_id': item_id,
                                                    'session_id': sessionid,
                                                    'actual_febe_id': febe_id,
                                                    'form':update_form})


        febe_id = int(request.POST.get('actual_febe_id'))  
        febe = Febes.objects.get(id=febe_id)

        creation_form = FebeForm(item_id,febe_id)





def update_febe(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        item = FebeParameters.objects.get(id=item_id)
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)

        febe_id = int(request.POST.get('actual_febe_id'))  
        febe = Febes.objects.get(id=febe_id)



        form = FebeForm(item_id, febe_id, request.POST, instance=item) # Bound form
        #form = FebeForm(sessionid, request.POST, instance=item) # Bound form

        if form.is_valid():
            form.save()
            available_febes = FebeParameters.objects.filter(session=session)
            available_sources = Sources.objects.filter(session=session)
            available_setups = Setup.objects.filter(session=session)
            available_integrations = Integrations.objects.filter(session=session)
    
            return render(request, 'session_main.html', {
                                                        'session': session,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })
        else:
            item_id = int(request.POST.get('item_id'))
            item = FebeParameters.objects.get(id=item_id)
            update_form = FebeForm(item_id, febe_id, request.POST, instance=item) # Bound form
            #update_form = FebeForm(sessionid, instance=item)
            return render(request, 'update_febe.html', {
                                                            'item_id': item_id, 
                                                            'form':update_form})





def add_source(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))  
        item = Session.objects.get(id=item_id)

        creation_form = SourcesForm(item_id)
        return render (request, 'sources_main.html', {
                                                    'session': item, 
                                                    'form':creation_form})
        

def create_source(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        new_form = SourcesForm(item_id, request.POST) # Bound form
        if new_form.is_valid():
            new_source = new_form.save()

            #item_id = int(request.POST.get('item_id'))
            item = Session.objects.get(id=item_id)
            available_febes = FebeParameters.objects.filter(session=item)
            available_sources = Sources.objects.filter(session=item)
            available_setups = Setup.objects.filter(session=item)
            available_integrations = Integrations.objects.filter(session=item)
    
            return render(request, 'session_main.html', {
                                                        'session': item,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })



def remove_source(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = Sources.objects.get(id=item_id)
        item.delete()
        #creation_form = session_form
        #available_sessions = session.objects.all()
        #return render(request, 'sessions_library.html', {
        #                                            'sessions_list': available_sessions,
        #                                            'form':creation_form})

        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        available_febes = FebeParameters.objects.filter(session=session)
        available_sources = Sources.objects.filter(session=session)
        available_setups = Setup.objects.filter(session=session)
        available_integrations = Integrations.objects.filter(session=session)
 
        return render(request, 'session_main.html', {
                                                    'session': session,
                                                    'febes_list': available_febes, 
                                                    'sources_list': available_sources,
                                                    'setups_list': available_setups,
                                                    'integrations_list': available_integrations })



def upload_source(request):

    if request.method == 'POST':

        sessionid = int(request.POST.get('session_id'))
        #session = Session.objects.get(id=sessionid)
        item_id = int(request.POST.get('item_id'))
        item = Sources.objects.get(id=item_id)
        update_form = SourcesForm(sessionid, instance=item)
        return render(request, 'update_source.html', {
                                                    'item_id': item_id, 
                                                    'session_id': sessionid, 
                                                    'form':update_form})
    
def update_source(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        item = Sources.objects.get(id=item_id)
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        form = SourcesForm(sessionid, request.POST, instance=item) # Bound form

        if form.is_valid():
            form.save()
            available_febes = FebeParameters.objects.filter(session=session)
            available_sources = Sources.objects.filter(session=session)
            available_setups = Setup.objects.filter(session=session)
            available_integrations = Integrations.objects.filter(session=session)
    
            return render(request, 'session_main.html', {
                                                        'session': session,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })
        else:
            item_id = int(request.POST.get('item_id'))
            item = Sources.objects.get(id=item_id)
            update_form = SourcesForm(sessionid, instance=item)
            return render(request, 'update_setup.html', {
                                                            'item_id': item_id, 
                                                            'form':update_form})



def add_setup(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        item = Session.objects.get(id=item_id)

        creation_form = SetupForm(item_id)
        return render (request, 'setup_main.html', {
                                                    'session': item, 
                                                    'form':creation_form})
        

def create_setup(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        new_form = SetupForm(item_id,request.POST) # Bound form
        if new_form.is_valid():
            new_setup = new_form.save()

            #item_id = int(request.POST.get('item_id'))
            item = Session.objects.get(id=item_id)
            available_febes = FebeParameters.objects.filter(session=item)
            available_sources = Sources.objects.filter(session=item)
            available_setups = Setup.objects.filter(session=item)
            available_integrations = Integrations.objects.filter(session=item)
    
            return render(request, 'session_main.html', {
                                                        'session': item,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })


def remove_setup(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('setup_id'))
        item = Setup.objects.get(id=item_id)
        item.delete()
        #creation_form = session_form
        #available_sessions = session.objects.all()
        #return render(request, 'sessions_library.html', {
        #                                            'sessions_list': available_sessions,
        #                                            'form':creation_form})

        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        available_febes = FebeParameters.objects.filter(session=session)
        available_sources = Sources.objects.filter(session=session)
        available_setups = Setup.objects.filter(session=session)
        available_integrations = Integrations.objects.filter(session=session)
 
        return render(request, 'session_main.html', {
                                                    'session': session,
                                                    'febes_list': available_febes, 
                                                    'sources_list': available_sources,
                                                    'setups_list': available_setups,
                                                    'integrations_list': available_integrations })

def upload_setup(request):

    if request.method == 'POST':

        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)
        update_form = SetupForm(sessionid, instance=setup)
        available_cals = Cal.objects.filter(session=session, setup=setup)
        available_aims = Aim.objects.filter(session=session, setup=setup)
        available_focs = Foc.objects.filter(session=session, setup=setup)
        return render(request, 'update_setup.html', {
                                                    'item_id': setup_id,
                                                    'setup': setup,
                                                    'session_id': sessionid,
                                                    'session': session,
                                                    'form':update_form,
                                                    'cals_list': available_cals,
                                                    'focs_list': available_focs,
                                                    'aims_list': available_aims})









def update_setup(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setupid = int(request.POST.get('setup_id'))
        item = Setup.objects.get(id=setupid)
        form = SetupForm(sessionid, request.POST, instance=item) # Bound form

        if form.is_valid():
            form.save()
            available_febes = FebeParameters.objects.filter(session=session)
            available_sources = Sources.objects.filter(session=session)
            available_setups = Setup.objects.filter(session=session)
            available_integrations = Integrations.objects.filter(session=session)
    
            return render(request, 'session_main.html', {
                                                        'session': session,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })
        else:
            item_id = int(request.POST.get('item_id'))
            item = Setup.objects.get(id=item_id)
            update_form = SetupForm(sessionid, instance=item)
            return render(request, 'update_setup.html', {
                                                            'item_id': item_id, 
                                                            'form':update_form})






def add_integrations(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))  
        item = Session.objects.get(id=item_id)

        creation_form = IntegrationsForm(item_id)
        return render (request, 'integrations_main.html', {
                                                    'session': item, 
                                                    'form':creation_form})
        

def create_integrations(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        new_form = IntegrationsForm(item_id, request.POST) # Bound form
        if new_form.is_valid():
            new_integration = new_form.save()

            #item_id = int(request.POST.get('item_id'))
            item = Session.objects.get(id=item_id)
            available_febes = FebeParameters.objects.filter(session=item)
            available_sources = Sources.objects.filter(session=item)
            available_setups = Setup.objects.filter(session=item)
            available_integrations = Integrations.objects.filter(session=item)
    
            return render(request, 'session_main.html', {
                                                        'session': item,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })


def remove_integrations(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = Integrations.objects.get(id=item_id)
        item.delete()
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        available_febes = FebeParameters.objects.filter(session=session)
        available_sources = Sources.objects.filter(session=session)
        available_setups = Setup.objects.filter(session=session)
        available_integrations = Integrations.objects.filter(session=session)
 
        return render(request, 'session_main.html', {
                                                    'session': session,
                                                    'febes_list': available_febes, 
                                                    'sources_list': available_sources,
                                                    'setups_list': available_setups,
                                                    'integrations_list': available_integrations })


def upload_integrations(request):

    if request.method == 'POST':

        sessionid = int(request.POST.get('session_id'))
        #session = Session.objects.get(id=sessionid)
        item_id = int(request.POST.get('item_id'))
        item = Integrations.objects.get(id=item_id)
        update_form = IntegrationsForm(sessionid, instance=item)
        return render(request, 'update_integrations.html', {
                                                    'item_id': item_id, 
                                                    'session_id': sessionid, 
                                                    'form':update_form})
    
def update_integrations(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        item_id = int(request.POST.get('item_id'))
        item = Integrations.objects.get(id=item_id)
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        form = IntegrationsForm(sessionid, request.POST, instance=item) # Bound form

        if form.is_valid():
            form.save()
            available_febes = FebeParameters.objects.filter(session=session)
            available_sources = Sources.objects.filter(session=session)
            available_setups = Setup.objects.filter(session=session)
            available_integrations = Integrations.objects.filter(session=session)
    
            return render(request, 'session_main.html', {
                                                        'session': session,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })
        else:
            item_id = int(request.POST.get('item_id'))
            item = Integrations.objects.get(id=item_id)
            update_form = IntegrationsForm(sessionid, instance=item)
            return render(request, 'update_integrations.html', {
                                                            'item_id': item_id, 
                                                            'form':update_form})


def add_cal(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)

        creation_form = CalForm(session_id,setup_id)
        return render (request, 'cal_main.html', {
                                                    'session': session, 
                                                    'setup': setup, 
                                                    'form':creation_form})
        
def create_cal(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)


        new_form = CalForm(session_id, setup_id, request.POST) # Bound form
        if new_form.is_valid():
            new_cal = new_form.save()
            print("cojonudo hasta aqui")

            sessionid = int(request.POST.get('session_id'))
            session = Session.objects.get(id=sessionid)
            setup_id = int(request.POST.get('setup_id'))
            setup = Setup.objects.get(id=setup_id)
            update_form = SetupForm(sessionid, instance=setup)
            available_cals = Cal.objects.filter(session=session, setup=setup)
            available_aims = Aim.objects.filter(session=session, setup=setup)
            available_focs = Foc.objects.filter(session=session, setup=setup)
            return render(request, 'update_setup.html', {
                                                        'item_id': setup_id,
                                                        'setup': setup,
                                                        'session_id': sessionid,
                                                        'session': session,
                                                        'form':update_form,
                                                        'cals_list': available_cals,
                                                        'focs_list': available_focs,
                                                        'aims_list': available_aims})





            #item_id = int(request.POST.get('item_id'))
            item = Session.objects.get(id=session_id)
            available_febes = FebeParameters.objects.filter(session=item)
            available_sources = Sources.objects.filter(session=item)
            available_setups = Setup.objects.filter(session=item)
            available_integrations = Integrations.objects.filter(session=item)
    
            return render(request, 'session_main.html', {
                                                        'session': item,
                                                        'febes_list': available_febes, 
                                                        'sources_list': available_sources,
                                                        'setups_list': available_setups,
                                                        'integrations_list': available_integrations })

def remove_cal(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = Cal.objects.get(id=item_id)
        item.delete()
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)


        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)
        update_form = SetupForm(sessionid, instance=setup)
        available_cals = Cal.objects.filter(session=session, setup=setup)
        available_aims = Aim.objects.filter(session=session, setup=setup)
        available_focs = Foc.objects.filter(session=session, setup=setup)
        return render(request, 'update_setup.html', {
                                                    'item_id': setup_id,
                                                    'setup': setup,
                                                    'session_id': sessionid,
                                                    'session': session,
                                                    'form':update_form,
                                                    'cals_list': available_cals,
                                                    'focs_list': available_focs,
                                                    'aims_list': available_aims})


def upload_cal(request):

    if request.method == 'POST':


        item_id = int(request.POST.get('item_id'))
        item = Cal.objects.get(id=item_id)
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setupid = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setupid)


        update_form = CalForm(sessionid, setupid, instance=item)


        return render (request, 'update_cal.html', {
                                                    'item_id': item_id,
                                                    'session': session, 
                                                    'setup': setup, 
                                                    'form':update_form})


def update_cal(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)


        item_id = int(request.POST.get('item_id'))
        item = Cal.objects.get(id=item_id)
        form = CalForm(session_id, setup_id, request.POST, instance=item) # Bound form

        if form.is_valid():
            form.save()
            print("mas cojonudo hasta aqui")


            sessionid = int(request.POST.get('session_id'))
            session = Session.objects.get(id=sessionid)
            setup_id = int(request.POST.get('setup_id'))
            setup = Setup.objects.get(id=setup_id)
            update_form = SetupForm(sessionid, instance=setup)
            available_cals = Cal.objects.filter(session=session, setup=setup)
            available_aims = Aim.objects.filter(session=session, setup=setup)
            available_focs = Foc.objects.filter(session=session, setup=setup)
            return render(request, 'update_setup.html', {
                                                        'item_id': setup_id,
                                                        'setup': setup,
                                                        'session_id': sessionid,
                                                        'session': session,
                                                        'form':update_form,
                                                        'cals_list': available_cals,
                                                        'focs_list': available_focs,
                                                        'aims_list': available_aims})



def add_aim(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)

        creation_form = AimForm(session_id,setup_id)
        return render (request, 'aim_main.html', {
                                                    'session': session, 
                                                    'setup': setup, 
                                                    'form':creation_form})
        
def create_aim(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)


        new_form = AimForm(session_id, setup_id, request.POST) # Bound form
        if new_form.is_valid():
            new_aim = new_form.save()
            print("cojonudo hasta aqui")

            sessionid = int(request.POST.get('session_id'))
            session = Session.objects.get(id=sessionid)
            setup_id = int(request.POST.get('setup_id'))
            setup = Setup.objects.get(id=setup_id)
            update_form = SetupForm(sessionid, instance=setup)
            available_cals = Cal.objects.filter(session=session, setup=setup)
            available_aims = Aim.objects.filter(session=session, setup=setup)
            available_focs = Foc.objects.filter(session=session, setup=setup)
            return render(request, 'update_setup.html', {
                                                        'item_id': setup_id,
                                                        'setup': setup,
                                                        'session_id': sessionid,
                                                        'session': session,
                                                        'form':update_form,
                                                        'cals_list': available_cals,
                                                        'focs_list': available_focs,
                                                        'aims_list': available_aims})





def remove_aim(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = Aim.objects.get(id=item_id)
        item.delete()
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)


        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)
        update_form = SetupForm(sessionid, instance=setup)
        available_cals = Cal.objects.filter(session=session, setup=setup)
        available_aims = Aim.objects.filter(session=session, setup=setup)
        available_focs = Foc.objects.filter(session=session, setup=setup)
        return render(request, 'update_setup.html', {
                                                    'item_id': setup_id,
                                                    'setup': setup,
                                                    'session_id': sessionid,
                                                    'session': session,
                                                    'form':update_form,
                                                    'cals_list': available_cals,
                                                    'focs_list': available_focs,
                                                    'aims_list': available_aims})


def upload_aim(request):

    if request.method == 'POST':


        item_id = int(request.POST.get('item_id'))
        item = Aim.objects.get(id=item_id)
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setupid = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setupid)


        update_form = AimForm(sessionid, setupid, instance=item)


        return render (request, 'update_aim.html', {
                                                    'item_id': item_id,
                                                    'session': session, 
                                                    'setup': setup, 
                                                    'form':update_form})


def update_aim(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)


        item_id = int(request.POST.get('item_id'))
        item = Aim.objects.get(id=item_id)
        form = AimForm(session_id, setup_id, request.POST, instance=item) # Bound form

        if form.is_valid():
            form.save()
            print("mas cojonudo hasta aqui")


            sessionid = int(request.POST.get('session_id'))
            session = Session.objects.get(id=sessionid)
            setup_id = int(request.POST.get('setup_id'))
            setup = Setup.objects.get(id=setup_id)
            update_form = SetupForm(sessionid, instance=setup)
            available_cals = Cal.objects.filter(session=session, setup=setup)
            available_aims = Aim.objects.filter(session=session, setup=setup)
            available_focs = Foc.objects.filter(session=session, setup=setup)
            return render(request, 'update_setup.html', {
                                                        'item_id': setup_id,
                                                        'setup': setup,
                                                        'session_id': sessionid,
                                                        'session': session,
                                                        'form':update_form,
                                                        'cals_list': available_cals,
                                                        'focs_list': available_focs,
                                                        'aims_list': available_aims})




def add_foc(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)

        creation_form = FocForm(session_id,setup_id)
        return render (request, 'foc_main.html', {
                                                    'session': session, 
                                                    'setup': setup, 
                                                    'form':creation_form})
        
def create_foc(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)


        new_form = FocForm(session_id, setup_id, request.POST) # Bound form
        if new_form.is_valid():
            new_foc = new_form.save()
            print("cojonudo hasta aqui")

            sessionid = int(request.POST.get('session_id'))
            session = Session.objects.get(id=sessionid)
            setup_id = int(request.POST.get('setup_id'))
            setup = Setup.objects.get(id=setup_id)
            update_form = SetupForm(sessionid, instance=setup)
            available_cals = Cal.objects.filter(session=session, setup=setup)
            available_aims = Aim.objects.filter(session=session, setup=setup)
            available_focs = Foc.objects.filter(session=session, setup=setup)
            return render(request, 'update_setup.html', {
                                                        'item_id': setup_id,
                                                        'setup': setup,
                                                        'session_id': sessionid,
                                                        'session': session,
                                                        'form':update_form,
                                                        'cals_list': available_cals,
                                                        'focs_list': available_focs,
                                                        'aims_list': available_aims})





def remove_foc(request):

    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))
        item = Foc.objects.get(id=item_id)
        item.delete()
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)


        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)
        update_form = SetupForm(sessionid, instance=setup)
        available_cals = Cal.objects.filter(session=session, setup=setup)
        available_aims = Aim.objects.filter(session=session, setup=setup)
        available_focs = Foc.objects.filter(session=session, setup=setup)
        return render(request, 'update_setup.html', {
                                                    'item_id': setup_id,
                                                    'setup': setup,
                                                    'session_id': sessionid,
                                                    'session': session,
                                                    'form':update_form,
                                                    'cals_list': available_cals,
                                                    'focs_list': available_focs,
                                                    'aims_list': available_aims})


def upload_foc(request):

    if request.method == 'POST':


        item_id = int(request.POST.get('item_id'))
        item = Foc.objects.get(id=item_id)
        sessionid = int(request.POST.get('session_id'))
        session = Session.objects.get(id=sessionid)
        setupid = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setupid)


        update_form = FocForm(sessionid, setupid, instance=item)


        return render (request, 'update_foc.html', {
                                                    'item_id': item_id,
                                                    'session': session, 
                                                    'setup': setup, 
                                                    'form':update_form})


def update_foc(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos

        session_id = int(request.POST.get('session_id'))
        session = Session.objects.get(id=session_id)
        setup_id = int(request.POST.get('setup_id'))
        setup = Setup.objects.get(id=setup_id)


        item_id = int(request.POST.get('item_id'))
        item = Foc.objects.get(id=item_id)
        form = FocForm(session_id, setup_id, request.POST, instance=item) # Bound form

        if form.is_valid():
            form.save()
            print("mas cojonudo hasta aqui")


            sessionid = int(request.POST.get('session_id'))
            session = Session.objects.get(id=sessionid)
            setup_id = int(request.POST.get('setup_id'))
            setup = Setup.objects.get(id=setup_id)
            update_form = SetupForm(sessionid, instance=setup)
            available_cals = Cal.objects.filter(session=session, setup=setup)
            available_aims = Aim.objects.filter(session=session, setup=setup)
            available_focs = Foc.objects.filter(session=session, setup=setup)
            return render(request, 'update_setup.html', {
                                                        'item_id': setup_id,
                                                        'setup': setup,
                                                        'session_id': sessionid,
                                                        'session': session,
                                                        'form':update_form,
                                                        'cals_list': available_cals,
                                                        'focs_list': available_focs,
                                                        'aims_list': available_aims})






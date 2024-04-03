from django.shortcuts import render

#######################
from .forms import SessionId
from .forms import telescop_parameters
from .forms import telescop_parameters_form
from .forms import febe_parameters
from .forms import febe_parameters_form, select_sources_form, setup_form, integration_form, select_all_parameters_form
from .forms import select_febe_parameters_id_form

from session_manager_app.models import config_parameters




# Create your views here.



def home(request):

    try:
        form = SessionId()
        febe_parameters_vivas = febe_parameters.objects.all()
        return render(request, 'sessions_library.html', {
                                                    'febe_parameters_list': febe_parameters_vivas, 
                                                    'form':form})
 

    except:

        sessionId="void"
        return render(request, 'error.html', {'st':sessionId})
    
    

def create_telescop_parameters(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = telescop_parameters_form(request.POST) # Bound form
        if form.is_valid():
            new_telescop_parameters = form.save()
            #return render(request, 'averias.html', {'form':form })
  
            new_antenna_parameters = {
                    'frontends': 'void',
                    'febename':  'void'
                }
            #escribimos el fichero
            fronteds_id = str(request.POST.get('frontends'))  
            febename_id = str(request.POST.get('febename'))  
            new_antenna_parameters = {
                    'frontends': fronteds_id,
                    'febename':  febename_id
              }

            # Write JSON data to a file
            config_parameters.write_antenna_parameters_data('antenna_parameters.json', new_antenna_parameters)

            with open('salida.macro', 'w') as f:
                print(f'esta es la macro frontend = {fronteds_id} febename : {febename_id}', file=f)
            
        actual_telescop_parameters = telescop_parameters.objects.all()
        form_telescop_parameters  = telescop_parameters_form() # Unbound form

        return render(request, 'main.html', {'form_telescop_parameters':form_telescop_parameters,'telescop_parameters_list': actual_telescop_parameters, 'form':form})
            


    else:
        telescop_parameters_vivas = telescop_parameters.objects.all()
        form_telescop_parameters  = telescop_parameters_form() # Unbound form

        return render(request, 'main.html', {'form_telescop_parameters':form_telescop_parameters,'telescop_parameters_list': telescop_parameters_vivas, 'form':form})



def remove_items(request):
    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))  
        item = telescop_parameters.objects.get(id=item_id)       
        item.delete()
        form_telescop_parameters = telescop_parameters_form()
        form = SessionId()
        telescop_parameters_vivas = telescop_parameters.objects.all()
        return render(request, 'main.html', {'form_telescop_parameters':form_telescop_parameters,'telescop_parameters_list': telescop_parameters_vivas, 'form':form})
        #return render(request, 'main.html', {'form_averias':form_averias,'listado_averias': averias_vivas, 'form':form})

        return render_to_response('averias.html', {
            'form':form, 'listado_averias':inventory, 
            }, RequestContext(request))


###------------------------------------------------------------------



def febe(request):

    try:
        form = SessionId()
        febe_parameters_vivas = febe_parameters.objects.all()
        form = select_all_parameters_form()
        form_febe_parameters  = febe_parameters_form() # Unbound form
        form_select_sources  = select_sources_form() # Unbound form
        form_setup  = setup_form() # Unbound form
        form_integration  = integration_form() # Unbound form
        return render(request, 'febe_select.html', {'form_select_sources':form_select_sources,
                                                    'form_setup':form_setup,
                                                    'form_integration':form_integration,
                                                    'form_febe_parameters':form_febe_parameters,
                                                    'febe_parameters_list': febe_parameters_vivas, 
                                                    'form':form})
 

    except:

        sessionId="void"
        return render(request, 'error.html', {'st':sessionId})
    

def create_febe_parameters(request):

    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = febe_parameters_form(request.POST) # Bound form
        if form.is_valid():
            new_febe_parameters = form.save()
            #return render(request, 'averias.html', {'form':form })
            """
            new_antenna_parameters = {
                    'frontends': 'void',
                    'febename':  'void'
                }
            #escribimos el fichero
            fronteds_id = str(request.POST.get('frontends'))  
            febename_id = str(request.POST.get('febename'))  
            new_antenna_parameters = {
                    'frontends': fronteds_id,
                    'febename':  febename_id
              }

            # Write JSON data to a file
            config_parameters.write_antenna_parameters_data('antenna_parameters.json', new_antenna_parameters)

            with open('salida.macro', 'w') as f:
                print(f'esta es la macro frontend = {fronteds_id} febename : {febename_id}', file=f)
            """
        actual_febe_parameters = febe_parameters.objects.all()
        form_febe_parameters  = febe_parameters_form() # Unbound form

        return render(request, 'febe_select.html', {'form_febe_parameters':form_febe_parameters,'febe_parameters_list': actual_febe_parameters, 'form':form})
            


    else:
        febe_parameters_vivas = febe_parameters.objects.all()
        form_febe_parameters  = febe_parameters_form() # Unbound form

        return render(request, 'febe_select.html', {'form_febe_parameters':form_febe_parameters,'febe_parameters_list': febe_parameters_vivas, 'form':form})



def remove_febe_items(request):
    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))  
        item = febe_parameters.objects.get(id=item_id)       
        item.delete()
        form_febe_parameters = febe_parameters_form()
        form = SessionId()
        febe_parameters_vivas = febe_parameters.objects.all()
        return render(request, 'febe_select.html', {'form_febe_parameters':form_febe_parameters,'febe_parameters_list': febe_parameters_vivas, 'form':form})

def upload_febe_items(request):
    if request.method == 'POST':

        item_id = int(request.POST.get('item_id'))  
        instance = febe_parameters.objects.get(id=item_id)       
        #item.delete()
        form = SessionId()
        febe_parameters_vivas = febe_parameters.objects.all()

        form_febe_parameters  = febe_parameters_form(instance=instance) # Unbound form
        form_select_sources  = select_sources_form(instance=instance) # Unbound form
        form_setup  = setup_form(instance=instance) # Unbound form
        form_integration  = integration_form(instance=instance) # Unbound form
        return render(request, 'febe_parameters.html', {'form_select_sources':form_select_sources,
                                                        'form_setup':form_setup,
                                                        'form_integration':form_integration,
                                                        'form_febe_parameters':form_febe_parameters,
                                                        'febe_parameters_list': febe_parameters_vivas, 
                                                        'form':form
                                                        }
                    )








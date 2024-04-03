from django.db import models
import pathlib
import json
import os



# void antenna configurations parameters python format    
void_antenna_parameters = {
        'frontends': 'void',
        'febename':  'void'
    }
# void antenna configurations parameters json format
void_antenna_parameters_json = json.dumps(void_antenna_parameters)
  

#class config_parameters (models.Model):
class config_parameters ():

    
    def __str__(self) -> str:
        return self.name

    # antenna configurations parameters python format    
    antenna_parameters = {
        'frontends': 'void',
        'febename':  'void'
    }

    # antenna configurations parameters json format
    antenna_parameters_json = json.dumps(antenna_parameters)

    
    def read_json_file(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    def write_json_file(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)
    
    def read_text_file(file_path):
            with open(file_path, 'r') as file:
                data = file.read()
            return data

    def write_text_file(file_path, data):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
    




    def get_antenna_parameters_data(file_path, session="void"):

        #data reading from session file
        #filespath = os.path.join('/', 'home', 'syssop','Documents', 'preproduccion', 'django_servers', 'session_manager_app')
        #os.chdir(filespath)
        try:
            antenna_parameters_json = config_parameters.read_json_file (file_path)
            return antenna_parameters_json
        except:
            #failure reading file, returning void
            print (f"{file_path} does not contain a json parameters file")
            return  void_antenna_parameters_json
        
    def write_antenna_parameters_data(file_path ,data, session="void"):

        #sesion data writing to file
        #filespath = os.path.join('/', 'home', 'syssop','Documents', 'preproduccion', 'django_servers', 'session_manager_app')
        #os.chdir(filespath)

        try:
            config_parameters.write_json_file(file_path, data)
        except:
            #failure writing, printing log
            print (f"antenna parameters {data} not writing onto file {file_path} ")


    def get_antenna_parameters_macro(file_path, session="void"):

        #data reading from session file
        #filespath = os.path.join('/', 'home', 'syssop','Documents', 'preproduccion', 'django_servers', 'session_manager_app')
        #os.chdir(filespath)
        try:

            macro_text = config_parameters.read_text_file (file_path)
            return macro_text
        except:
            #failure reading file, returning void
            print (f"{file_path} does not contain a macro file")
            return  None
        
    def write_antenna_parameters_macro(file_path, data, session="void"):

        #sesion data writing to file
        #filespath = os.path.join('/', 'home', 'syssop','Documents', 'preproduccion', 'django_servers', 'session_manager_app')
        #os.chdir(filespath)

        try:
            config_parameters.write_text_file(file_path, data)
        except:
            #failure writing, printing log
            print (f"antenna parameters {data} not writint onto macro file")






"""    
#probamos el invento

#data reading from session file
filespath = os.path.join('/', 'home', 'sysop','Documents', 'telescop', 'testing','control_app')
os.chdir(filespath)
print(f"{filespath}")


kiko_antenna_parameters = {
        'frontends': 'kiko_inicial',
        'febename':  'kiko_inicial'
    }
#escribimos el fichero


# Write JSON data to a file
config_parameters.write_antenna_parameters_data('kiko.json', kiko_antenna_parameters)


#     
# Read JSON data from a file
json_leido = config_parameters.get_antenna_parameters_data('kiko.json')
print(json_leido)

# Modify the data
json_leido['frontends'] = 'kiko_inicial_modified'

# Write JSON data to a file
config_parameters.write_json_file('kiko.json', json_leido)

#     
# Read JSON data from a file
json_leido = config_parameters.read_json_file('kiko.json')
print(json_leido)



# Write  data to a file
kiko_macro_text = "este es el texto de la macro sdsa"
config_parameters.write_antenna_parameters_macro('kiko.macro', kiko_macro_text)


#     
# Read macro from a file
macro_leido = config_parameters.get_antenna_parameters_macro('kiko.macro')
print(macro_leido)
"""




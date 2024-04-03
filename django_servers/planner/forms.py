from django import forms
from django.forms import ModelForm
from .models import Febes
from .models import Session
from .models import FebeParameters
from .models import Sources
from .models import Setup
from .models import Integrations
from .models import Cal
from .models import Aim
from .models import Foc



class SessionForm (ModelForm):

    class Meta:
        model = Session
        fields = ['session_name','description']


class AdminFebesForm (ModelForm):

    class Meta:
        model = Febes
        fields = "__all__"


class FebeShortForm (ModelForm):

    class Meta:
        model = FebeParameters
        fields = ['febe_name']

class FebeForm (ModelForm):

    class Meta:
        model = FebeParameters
        fields = "__all__"
    

    def __init__(self, session_id, febe_id, *args, **kwargs):
        super(FebeForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()
        self.fields['febe_name'].initial = febe_id
        self.fields['febe_name'].widget = forms.HiddenInput()

class SourceShortForm (ModelForm):

    class Meta:
        model = Sources
        fields = ['source_name','description']

class SourcesForm (ModelForm):

    class Meta:
        model = Sources
        fields = "__all__"

    def __init__(self, session_id, *args, **kwargs):
        super(SourcesForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()





class SetupShortForm (ModelForm):

    class Meta:
        model = Setup
        fields = ['session','setup_name']
        #fields = "__all__"
    def __init__(self, session_id, *args, **kwargs):
        super(SetupShortForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()
        #fields = ['setup_name']

class SetupForm (ModelForm):

    class Meta:
        model = Setup
        fields = "__all__"
    def __init__(self, session_id, *args, **kwargs):
        super(SetupForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()




class IntegrationsShortForm (ModelForm):

    class Meta:
        model = Integrations
        fields = ['integration_name']

class IntegrationsForm (ModelForm):

    class Meta:
        model = Integrations
        fields = "__all__"
    def __init__(self, session_id, *args, **kwargs):
        super(IntegrationsForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()


class CalForm (ModelForm):

    class Meta:
        model = Cal
        fields = "__all__"
    def __init__(self, session_id, setup_id, *args, **kwargs):
        super(CalForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()
        self.fields['setup'].initial = setup_id
        self.fields['setup'].widget = forms.HiddenInput()

class AimForm (ModelForm):

    class Meta:
        model = Aim
        fields = "__all__"
    def __init__(self, session_id, setup_id, *args, **kwargs):
        super(AimForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()
        self.fields['setup'].initial = setup_id
        self.fields['setup'].widget = forms.HiddenInput()

class FocForm (ModelForm):

    class Meta:
        model = Foc
        fields = "__all__"
    def __init__(self, session_id, setup_id, *args, **kwargs):
        super(FocForm, self).__init__(*args, **kwargs)
        self.fields['session'].initial = session_id
        self.fields['session'].widget = forms.HiddenInput()
        self.fields['setup'].initial = setup_id
        self.fields['setup'].widget = forms.HiddenInput()



        
        
        
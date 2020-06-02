from django import forms
from django.forms.forms import BoundField
from django.template import Context, loader
from ams.models import *


class TemplatedForm(forms.ModelForm):
    '''
    From http://djangosnippets.org/snippets/121/
    '''
    def output_via_template(self):
        """Helper function for fieldsting fields data from form"""

        bound_fields = [BoundField(self, field, name) for name, field \
                        in self.fields.items()]

        c = Context(dict(form=self, bound_fields=bound_fields))
        t = loader.get_template('forms/form.html')
        return t.render(c)

    def __unicode__(self):
        return self.output_via_template()

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
	fields = ('__all__')

##
##class SmsForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
##    sms = forms.CharField(max_length=255)

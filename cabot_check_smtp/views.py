from django import forms
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from cabot.cabotapp.models import StatusCheck
from cabot.cabotapp.views import (CheckCreateView, CheckUpdateView,
                                  StatusCheckForm, base_widgets)

from .models import SmtpStatusCheck

class SmtpStatusCheckForm(StatusCheckForm):
    symmetrical_fields = ('service_set', 'instance_set')

    class Meta:
        model = SmtpStatusCheck
        fields = (
            'name',
            'host',
            'port',
            'helo_address',
            'sender',
            'recipient',
            'timeout',
            'frequency',
            'active',
            'importance',
            'debounce',
        )

        widgets = dict(**base_widgets)
        widgets.update({
            'host': forms.TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'smtp.example.org',
            }),
            'helo_address': forms.TextInput(attrs={
                'style': 'width: 100%',
                'placeholder': 'my-smtp.example.org',
            })
        })


class SmtpCheckCreateView(CheckCreateView):
    model = SmtpStatusCheck
    form_class = SmtpStatusCheckForm


class SmtpCheckUpdateView(CheckUpdateView):
    model = SmtpStatusCheck
    form_class = SmtpStatusCheckForm


def duplicate_check(request, pk):
    pc = StatusCheck.objects.get(pk=pk)
    npk = pc.duplicate()
    return HttpResponseRedirect(reverse('update-smtp-check', kwargs={'pk': npk}))

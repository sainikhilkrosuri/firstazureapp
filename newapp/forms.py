from .models import *
from django import forms
from django.utils.translation import gettext_lazy as _

class pipe_inspection(forms.ModelForm):
    class Meta:
        model = ghd_pipe_inspection
        fields = ['sampler', 'inspector', 'leak_location', 'time_notified_tva', 'wts_shutdown_time', 'action_taken', 'data_image']
        labels = {
            'sampler': 'Sampler',
            'leak_location': 'Leak Location',
            'time_notified_tva': 'Time Notified TVA',
            'wts_shutdown_time': 'WTS Shutdown Time',
            'action_taken': 'Action Taken',
            'data_image': 'Upload Image'
        }
        help_texts = {
            "sampler": _("Some useful help text."),
        }
        error_messages = {
            "sampler": {
                "max_length": _("This writer's name is too long."),
            },
        }
        widgets = {
            "sampler": forms.Textarea(attrs={"cols": 10, "rows": 2}),
        }
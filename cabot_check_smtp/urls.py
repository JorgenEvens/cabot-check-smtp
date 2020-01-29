from django.conf.urls import url

from .views import (SmtpCheckCreateView, SmtpCheckUpdateView,
                    duplicate_check)

urlpatterns = [

    url(r'^smtpcheck/create/',
        view=SmtpCheckCreateView.as_view(),
        name='create-smtp-check'),

    url(r'^smtpcheck/update/(?P<pk>\d+)/',
        view=SmtpCheckUpdateView.as_view(),
        name='update-smtp-check'),

    url(r'^smtpcheck/duplicate/(?P<pk>\d+)/',
        view=duplicate_check,
        name='duplicate-smtp-check')

]

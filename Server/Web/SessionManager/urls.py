from django.urls import path
from . import views


urlpatterns = [
    path('sessions', views.sessionmanagement, name='Session Management'),
    path('sessions/send-message', views.sendmessage, name='Send Message'),
    path('sessions/print-queue', views.printqueue, name='Print Queue'),
    path('sessions/adjust-funds', views.adjustfunds, name='Adjust Funds'),
    path('sessions/express-session', views.expresssession, name='Express Sessions'),
    path('restrictions', views.restrictedaccounts, name='Restricted Accounts'),
    path('locked-systems', views.lockedsystems, name='Locked Systems'),
    path('multi-session-cards', views.multi_sessioncards, name='Multi-Session Cards'),
    path('break-override', views.breakoverride, name='Break Override'),
    path('reports', views.reports, name='Reports')
]
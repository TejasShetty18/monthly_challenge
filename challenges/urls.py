from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("<int:month>",views.monthly_challenges_by_number),
    path("<str:month>",views.monthly_challenges , name="month-challenges"),
   
    # path("january",views.january),
    # path("february",views.february),
    # path("march",views.march),
    # path("April",views.april),
    # path("may",views.may),
    # path("june",views.june),
    # path("july",views.  july),
    # path("august",views.august),
    # path("sept",views.september),
    # path("oct",views.october),
    # path("nov",views.november),
    # path("dec",views.december),
]
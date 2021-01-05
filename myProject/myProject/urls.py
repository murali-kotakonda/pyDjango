from django.contrib import admin
from django.urls import path , include

urlpatterns = [


    path('admin/', admin.site.urls),
    path('login/', include('login.urls')),
    # path(r'^login/$', include('login.urls')),
    path('customer/', include('customer.urls')),
    path('account/', include('account.urls'))
    #path('student/', include('student.urls'))

]

"""
patterns('',
    (r'^login/$', login, {'template_name':'login.html'} ),
    (r'^logout/$', logout,{'template_name':'logout.html'}),
    ...the other urls for your app...
)
"""


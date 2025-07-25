"""
URL configuration for envChemistry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


class CustomGraphQLView(GraphQLView):
    def __init__(self, *args, **kwargs):
        kwargs["introspection"] = True
        super().__init__(*args, **kwargs)
        

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/user/', include("users.urls")),
    path('api/v1/chemical/', include("rest.urls")),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True)))
]

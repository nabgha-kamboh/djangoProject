from django.urls import path


from home import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="home"),
    path('nabgha', views.contacts.as_view(), name="nabgha"),
    path('jelani', views.jelani.as_view(), name="jelani")


]
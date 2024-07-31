from django.contrib import admin
from django.urls import path, include
from .view import MyCoursesList, HomePageView, verifyPayment, coursepage, SignupView, LoginView, signout, checkout
from django.conf.urls.static import static
from lms_proj.settings import MEDIA_ROOT, MEDIA_URL
from django.conf import settings

urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('logout', signout, name='logout'),
    path('my-courses', MyCoursesList.as_view(), name='my-courses'),
    path('signup',SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('course/<str:slug>', coursepage, name='Course Page'),
    path('checkout/<str:slug>', checkout, name='checkout'),
    path('verify_payment', verifyPayment, name='verify_payment')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

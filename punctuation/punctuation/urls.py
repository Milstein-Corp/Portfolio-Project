from django.urls import path
from punctuation.views import indexView, predictView

urlpatterns = [
    path("", indexView, name="punc_home"),
    path("predict", predictView, name="punc_predict"),
]

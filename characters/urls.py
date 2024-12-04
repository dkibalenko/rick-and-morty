from django.urls import include, path

from characters import views


urlpatterns = [
    path(
        "characters/random/",
        views.get_random_character_view,
        name="random-character"
    ),
]

app_name = "characters"

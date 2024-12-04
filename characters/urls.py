from django.urls import include, path

from characters import views


urlpatterns = [
    path(
        "characters/random/",
        views.get_random_character_view,
        name="random-character"
    ),
    path(
        "characters/",
        views.CharacterListView.as_view(),
        name="characters"
    ),
]

app_name = "characters"

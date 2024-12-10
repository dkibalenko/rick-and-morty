from unittest.mock import patch
from django.test import TestCase
from django.urls import reverse

from characters.models import Character
from characters.views import get_random_character
from characters.serializers import CharacterSerializer


class CharactersViewTests(TestCase):
    def setUp(self):
        self.character1 = Character.objects.create(
            api_id=1,
            name="Rick Sanchez",
            status="Alive",
            species="Human",
            gender="Male",
            image="test1.jpg",
        )
        self.character2 = Character.objects.create(
            api_id=2,
            name="Morty Smith",
            status="Alive",
            species="Human",
            gender="Male",
            image="test2.jpg",
        )

    def test_get_characters_list_queryset(self):
        res = self.client.get(reverse("characters:characters"))
        characters = Character.objects.all()
        serializer = CharacterSerializer(characters, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["results"], serializer.data)

    def test_get_characters_list_queryset_filtered_by_name(self):
        res = self.client.get(
            reverse("characters:characters"),
            data={"name": "rick"}
        )
        characters = Character.objects.filter(name__icontains="rick")
        serializer = CharacterSerializer(characters, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["results"], serializer.data)

    def test_get_random_character_function(self):
        with patch("characters.views.choice", return_value=5):
            result = get_random_character()
            assert result == self.character1

    def test_get_random_character_view(self):
        with patch(
            "characters.views.get_random_character",
            return_value=self.character1
        ):
            serializer = CharacterSerializer(self.character1)
            res = self.client.get(reverse("characters:random-character"))
            self.assertEqual(res.status_code, 200)
            self.assertEqual(res.data, serializer.data)

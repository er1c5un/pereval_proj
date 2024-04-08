from rest_framework import serializers
from rest_framework.exceptions import APIException
from rest_framework.relations import PrimaryKeyRelatedField

from .models import Tourists, Pereval, Coords, Level, Images


class TouristsSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100, label='Почта')

    class Meta:
        model = Tourists
        fields = (
            'fam',
            'name',
            'otc',
            'email',
            'phone'
        )


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = (
            'latitude',
            'longitude',
            'height'
        )


class LevelSerializer(serializers.ModelSerializer):
    winter = serializers.ChoiceField(choices=Level.Levels.labels, label='Зима')
    spring = serializers.ChoiceField(choices=Level.Levels.labels, label='Весна')
    summer = serializers.ChoiceField(choices=Level.Levels.labels, label='Лето')
    autumn = serializers.ChoiceField(choices=Level.Levels.labels, label='Осень')

    class Meta:
        model = Level
        fields = (
            'winter',
            'spring',
            'summer',
            'autumn'
        )


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['images', 'title']


class PerevalSerializer(serializers.ModelSerializer):
    tourists_id = TouristsSerializer()
    coord_id = CoordsSerializer()
    level_id = LevelSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pereval
        fields = (
            'beauty_title',
            'title',
            'other_titles',
            'connect',
            'users_id',
            'coord_id',
            'level_id',
            'images',
            'status'
        )
        extra_kwargs = {
            'status': {'choices': Pereval.Status.labels}
        }

    def create(self, validated_data):
        tourist_id = validated_data.get('tourist_id', {})
        coord_id = validated_data.get('coord_id', {})
        level = validated_data.get('level', {})
        images = validated_data.get('images', {})

        tourist_id, created = Tourists.object.get_or_create(**tourist_id)
        coord_id = Coords.objects.create(**coord_id)
        level = Level.objects.create(**level)
        pereval = Pereval.objects.create(**validated_data, tourist_id=tourist_id, coord_id=coord_id, level=level,
                                         status="NW")

        for i in images:
            image = i.pop('image')
            title = i.pop('title')
            Images.objects.create(image=image, pereval_id=pereval, title=title)

        return pereval
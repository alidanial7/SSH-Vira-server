# from _typeshed import OpenTextMode
from rest_framework import serializers
from rest_framework import generics
from . import models
from django_restql.mixins import DynamicFieldsMixin

from users.serializers import UserSerializer


class mealSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Meal
        fields = ['id', 'name']


class foodSerializer(serializers.ModelSerializer):
    meal = mealSerializer(many=False, read_only=False)

    class Meta:
        model = models.Food
        fields = ['id', 'name', 'meal']


class chefSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    person = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.Chef
        fields = ['id', 'person']


class distributorSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    person = UserSerializer(many=False, read_only=True)

    class Meta:
        model = models.Chef
        fields = ['id', 'person']


class reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Report
        fields = ['id', 'personnel_mistake_report', 'daily_report',
                  'step', 'report_date', 'comment']
        extra_kwargs = {
            "report_date": {
                "error_messages": {
                    "invalid": "مقدار فیلد تاریخ صحیح نمی باشد",
                    "required": "فیلد تاریخ الزامی است",
                },
                'required': True
            },
            "extra_food_number": {
                "error_messages": {
                    "invalid": "مقدار فیلد تعداد غذای اضافه صحیح نمی باشد",
                    "required": "فیلد تعداد غذای اضافه الزامی است"
                },
                'required': True
            }
        }


class cookSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Cook
        fields = ['id', 'food', 'preparation_chef',
                  'cook_chef', 'report', 'number_of_foods', 'number_of_extra_foods']
        extra_kwargs = {
            "report": {
                "error_messages": {
                    "invalid": "مقدار فیلد گزارش صحیح نمی باشد",
                    "required": "فیلد گزارش الزامی است"
                },
            },
        }

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['food'] = foodSerializer(instance.food).data
        response['preparation_chef'] = chefSerializer(
            instance.preparation_chef).data
        response['cook_chef'] = chefSerializer(instance.cook_chef).data
        return response


class distributionSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = models.Distribution
        fields = ['section', 'meal', 'distributor1', 'distributor2', 'report']

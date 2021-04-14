
from django.http.response import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets, generics
from django.views.decorators.csrf import csrf_exempt
from . import serializers
from . import models
import json
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import Permission
from users.serializers import UserSerializer
from users.models import CustomUser


# Create your views here.


class mealViewSet(viewsets.ModelViewSet):
    queryset = models.Meal.objects.all().order_by('name')
    serializer_class = serializers.mealSerializer


class foodViewSet(viewsets.ModelViewSet):
    queryset = models.Food.objects.all().order_by('-created_at')
    serializer_class = serializers.foodSerializer

    @action(methods=['GET'], detail=False)
    def by_meal(self, request):
        meals = request.GET['meals'].split(",")
        mealItems = []
        for meal in meals:
            items = models.Food.objects.filter(meal=meal)
            if not items:
                return JsonResponse({'errors': ['غذایی برای وعده غذایی انتخاب شده موجود نمیباشد.']}, status=status.HTTP_400_BAD_REQUEST)
            meal = {
                'id': items[0].meal.id,
                'name': items[0].meal.name,
            }
            mealItem = {'meal': meal, 'foods': []}
            for item in items:
                mealItem['foods'].append({'name': item.name, 'id': item.id})
            mealItems.append(mealItem)

        return JsonResponse({'data': mealItems})


class chefViewSet(viewsets.ModelViewSet):
    queryset = models.Chef.objects.all().order_by('-id')
    serializer_class = serializers.chefSerializer


class distributorViewSet(viewsets.ModelViewSet):
    queryset = models.Distributor.objects.all().order_by('-id')
    serializer_class = serializers.distributorSerializer


class cookViewSet(viewsets.ModelViewSet):
    queryset = models.Cook.objects.all().order_by('created_at')
    serializer_class = serializers.cookSerializer

    def create(self, request, *args, **kwargs):
        body = json.loads(request.body)
        if isinstance(body, list):
            if len(body) == 0:
                return JsonResponse({'message': ['لیست ارسالی خالی است.']}, status=status.HTTP_400_BAD_REQUEST)
            for item in body:
                print(item)
                serializer = serializers.cookSerializer(data=item)
                if not serializer.is_valid():
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            for item in body:
                serializer = serializers.cookSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
            return JsonResponse({'message': 'cooks created'}, status=status.HTTP_201_CREATED)

        elif isinstance(body, dict):
            serializer = serializers.cookSerializer(data=body)
            if serializer.is_valid():
                print(serializer.validated_data)
                serializer.save()
                return JsonResponse({'message': 'cook created'}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return JsonResponse({'message': 'unsupported'}, status=403)

    @ action(methods=['GET'], detail=False)
    def getByDate(self, request):
        start = request.GET['start']
        end = request.GET['end']
        items = models.Cook.objects.filter(
            report__report_date__gte=start).filter(report__report_date__lte=end).filter(report__step__gte=1)
        return_data = []
        for item in items:
            return_data.append(
                {'food': item.food.id,
                 'food_name': item.food.name,
                 'food_meal': item.food.meal.id,
                 'food_meal_name': item.food.meal.name,
                 'preparation_chef': item.preparation_chef.id,
                 'preparation_chef_name': item.preparation_chef.person.first_name + ' ' + item.preparation_chef.person.last_name,
                 'cook_chef': item.cook_chef.id,
                 'cook_chef_name': item.cook_chef.person.first_name + ' ' + item.cook_chef.person.last_name,
                 'number_of_foods': item.number_of_foods,
                 'number_of_extra_foods': item.number_of_extra_foods
                 }
            )
        return JsonResponse(return_data, safe=False)

    @ action(methods=['GET'], detail=False)
    def getByReportID(self, request):
        id = request.GET['id']
        items = models.Cook.objects.filter(report=id)
        return_data = []
        for item in items:
            return_data.append({
                'food': item.food.id,
                'food_name': item.food.name,
                'food_meal': item.food.meal.id,
                'food_meal_name': item.food.meal.name,
                'preparation_chef': item.preparation_chef.id,
                'preparation_chef_name': item.preparation_chef.person.first_name + ' ' + item.preparation_chef.person.last_name,
                'cook_chef': item.cook_chef.id,
                'cook_chef_name': item.cook_chef.person.first_name + ' ' + item.cook_chef.person.last_name,
                'report': item.report.id,
                'report_date': item.report.report_date,
                'number_of_foods': item.number_of_foods,
                'number_of_extra_foods': item.number_of_extra_foods
            }
            )
        return JsonResponse(return_data, safe=False)


class distributionViewSet(viewsets.ModelViewSet):
    queryset = models.Distribution.objects.all().order_by('created_at')
    serializer_class = serializers.distributionSerializer

    def create(self, request, *args, **kwargs):
        body = json.loads(request.body)
        if isinstance(body, list):
            if len(body) == 0:
                return JsonResponse({'message': ['لیست ارسالی خالی است.']}, status=status.HTTP_400_BAD_REQUEST)
            for item in body:
                serializer = serializers.distributionSerializer(data=item)
                if not serializer.is_valid():
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            for item in body:
                serializer = serializers.distributionSerializer(data=item)
                if serializer.is_valid():
                    serializer.save()
            return JsonResponse({'message': 'reports created'}, status=status.HTTP_201_CREATED)

        elif isinstance(body, dict):
            serializer = serializers.distributionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': 'report created'}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            return JsonResponse({'message': 'unsupported'}, status=403)

    @ action(methods=['GET'], detail=False)
    def getByReportID(self, request):
        id = request.GET['id']
        items = models.Distribution.objects.filter(report=id)
        return_data = []
        for item in items:
            return_data.append(
                {
                    'section': item.section.id,
                    'section_name': item.section.name,
                    'meal': item.meal.id,
                    'meal_name': item.meal.name,
                    'distributor1': item.distributor1.id,
                    'distributor1_name': item.distributor1.person.first_name + ' ' + item.distributor1.person.last_name,
                    'distributor2': item.distributor2.id,
                    'distributor2_name': item.distributor2.person.first_name + ' ' + item.distributor2.person.last_name,
                    'report': item.report.id,
                    'report_date': item.report.report_date,
                }
            )
        return JsonResponse(return_data, safe=False)


class reportViewSet(viewsets.ModelViewSet):
    queryset = models.Report.objects.all().order_by('report_date')
    serializer_class = serializers.reportSerializer

    def destroy(self, request, pk=None):
        try:

            user = CustomUser.objects.get(username=request.user)
            perm_tuple = [x.name
                          for x in Permission.objects.filter(user=user)]
            if 'Can delete report' in perm_tuple:
                report = models.Report.objects.get(pk=pk)
                report.delete()
                content = {
                    'message': 'گزارش با موفقیت حذف شد.'
                }
                return JsonResponse(content, status=status.HTTP_200_OK)
            else:
                content = {
                    'message': 'شما دسترسی لازم برای این عملیات را ندارید'
                }
                return JsonResponse(content, status=status.HTTP_200_OK)
        except:
            content = {
                'message': 'مشکلی پیش آمده است.'
            }
            return JsonResponse(content, status=status.HTTP_404_NOT_FOUND)

    @ action(methods=['GET'], detail=False)
    def acceptReport(self, request):
        report_id = request.GET['report_id']
        report = models.Report.objects.get(id=report_id)
        if report:
            report.step = report.step + 1
            report.save()
            content = {
                'message': 'تاییدیه شما با موفقیت اعمال شد'
            }
            return JsonResponse(content, status=status.HTTP_200_OK)
        else:
            content = {
                'message': 'اطاعات با موفقیت ثبت شد'
            }
            return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)

    @ action(methods=['delete'], detail=True)
    def deleteReport(self, request, pk=None):
        # report = self.get_object(pk)
        print(pk)
        # report_id = request.GET['report_id']
        # report = models.Report.objects.get(id=report_id)
        # if report:
        #     report.step = report.step + 1
        #     report.save()
        #     content = {
        #         'message': 'تاییدیه شما با موفقیت اعمال شد'
        #     }
        #     return JsonResponse(content, status=status.HTTP_200_OK)
        # else:
        content = {
            'message': 'اطاعات با موفقیت ثبت شد'
        }
        return JsonResponse(content, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def cookReport(request):
#     body = json.loads(request.body)
#     # check and save report
#     reportRequest = body['report']
#     reportSerializer = serializers.reportSerializer(data=reportRequest)
#     reportValidation = reportSerializer.is_valid()
#     if not reportValidation:
#         return JsonResponse(reportSerializer.errors, status=406)
#     report = reportSerializer.save()

#     # check and save distributors
#     distributorsRequests = body['distributors']
#     for distributorsRequest in distributorsRequests:
#         print(distributorsRequest)
#     return JsonResponse({'foo': 'bar'}, status=404)

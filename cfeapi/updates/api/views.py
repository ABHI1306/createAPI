from updates.models import Update as UpdateModel
from django.views.generic import View
from django.http import HttpResponse
from django.core.serializers import serialize

class UpdateModelDetailAPIView(View):
    def get(self,request,id,*args,**kwrgs):
        obj = UpdateModel.objects.get(id=id)
        json_data = obj.serialize()
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwrgs):
        return HttpResponse({},content_type='application/json')

    def put(self,request,*args,**kwrgs):
        return HttpResponse({},content_type='application/json')

    def delete(self,request,*args,**kwrgs):
        return HttpResponse({},content_type='application/json')

class UpdateModelListAPIView(View):
    def get(self,request,*args,**kwrgs):
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return HttpResponse(json_data,content_type='application/json')
 
    def post(self,request,*args,**kwrgs):
        return HttpResponse({},content_type='application/json')


    def put(self,request,*args,**kwrgs):
        return

    def delete(self,request,*args,**kwrgs):
        return
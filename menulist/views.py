from rest_framework import status,views,response
from django.shortcuts import render,redirect,get_object_or_404

from django.http.response import JsonResponse
from django.template.loader import render_to_string

from .models import Menu,Category,Allergy
from .serializer import MenuSerializer


class MenuView(views.APIView):

    def get(self, request, *args, **kwargs):

        cates   = Category.objects.all()
        alles   = Allergy.objects.all()

        data    = Menu.objects.order_by("category","name")
        context = { "data":data,
                    "cates":cates,
                    "alles":alles }

        return render(request,"menulist/index.html",context)
    
    def post(self, request, *args, **kwargs):

        serializer      = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        data        = Menu.objects.order_by("category","name")
        context     = {"data":data}
        content_data_string     = render_to_string('menulist/content.html', context ,request)
        json_data               = { "content" : content_data_string }

        return JsonResponse(json_data)

index   = MenuView.as_view()

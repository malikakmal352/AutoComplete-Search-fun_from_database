from django.shortcuts import render
from .models import Lab
from django.http import JsonResponse


# Create your views here.
def index(request):
    labs = Lab.objects.all()
    data = {'labs': labs}
    return render(request, 'index.html', data)


# def get_name(request):
#     search = request.GET.get('search')
#     payload = []
#
#     if search:
#         print(search)
#         Labs = Lab.objects.filter(Labname__startswith=search)
#         print(Labs)
#         for obj in Labs:
#             payload.append({
#                 'name': obj.Labname,
#             })
#     return JsonResponse(
#         {
#             'status': True,
#             'payload': payload,
#         })



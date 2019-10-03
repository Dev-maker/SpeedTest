
from django.shortcuts import render
import pyspeedtest
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials, db
from .models import Data
from django.http import HttpResponse

cred = credentials.Certificate(
    "/Users/dev/PycharmProjects/0000/geotutorial/geodjango/first-251520-firebase-adminsdk-2basx-1678420d8f.json")
firebase_admin.initialize_app(cred)


def speed(request):
    st = pyspeedtest.SpeedTest()
    download = st.download()
    upload = st.upload()
    return HttpResponse(download)



db = firestore.client()


def location(request):
    response_string = 'o'.format(
        request.ipinfo.all

    )




    if request.method == 'GET' or 'POST':

        # doc_ref = db.collection('Data').document()
        # doc_ref.set({
        #     'IpAddress': request.ipinfo.POST.ip,
        #     'city': request.ipinfo.POST['region'],
        #     'post': request.ipinfo.POST['post'],
        #     'location': request.ipinfo.POST['loc'],
        #     'hostname': request.ipinfo.POST['hostname']
        # }
        #
        # )
        data = Data.objects.all()

        for _ in data:
            info = {
                'IpAddress': request['ip'],
                'city': request['region'],
                'post': request['post'],
                'location': request['loc'],
                'hostname': request['hostname']
            }
            data.save()

    context = {'response_string': response_string}
    return render(request, 'world/index.html', context)

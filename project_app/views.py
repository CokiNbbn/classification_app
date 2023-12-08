from django.shortcuts import render

from joblib import load
model = load('./savedModels/model.joblib')

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    useful_medsos = int(request.GET['useful_medsos'])
    freq_medsos = int(request.GET['freq_medsos'])
    useful_course = int(request.GET['useful_course'])
    freq_course = int(request.GET['freq_course'])
    useful_app = int(request.GET['useful_app'])
    freq_app = int(request.GET['freq_app'])
    ipk = float(request.GET['ipk'])
    y_pred = model.predict([[useful_medsos, freq_medsos, useful_course, freq_course, useful_app, freq_app, ipk]])
    
    cluster_number = ''
    cluster_description = ''
    if y_pred == 0:
        cluster_number = 'Klaster 0'
        cluster_description = 'Anda termasuk kategori yang JARANG menggunakan media pembelajaran non-formal'
    elif y_pred == 1:
        cluster_number = 'Klaster 1'
        cluster_description = 'Anda termasuk kategori yang SERING menggunakan media pembelajaran non-formal'

    return render(request, 'result.html', {'cluster_number': cluster_number, 'cluster_description': cluster_description})

    return render(request, 'result.html', {'result': y_pred})
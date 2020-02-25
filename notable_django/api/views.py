import os
import pickle
import pandas
import sklearn
from datetime import datetime
from api.models import InputData
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def input_data_view(request):
    if request.method == 'GET':
        model_path = settings.MODEL_PATH
        model_name = 'Linear_regression_model.p'
        model = pickle.load(open(os.path.join(model_path, model_name), 'rb'))
        input_data = pandas.DataFrame(list(InputData.objects.all().values()))
        input_data['max_occured_sublocation'] = model['encoder'].transform(input_data['max_occured_sublocation'])
        input_data['day_of_week'] = input_data['hourly_timestamp'].apply(lambda timestamp: datetime.strptime(timestamp, '%m-%d-%Y %H:%M:%S.%f').weekday())
        input_data['day_of_month'] = input_data['hourly_timestamp'].apply(lambda timestamp: datetime.strptime(timestamp, '%m-%d-%Y %H:%M:%S.%f').day)
        input_data['month_of_year'] = input_data['hourly_timestamp'].apply(lambda timestamp: datetime.strptime(timestamp, '%m-%d-%Y %H:%M:%S.%f').month)
        input_data['hour'] = input_data['hourly_timestamp'].apply(lambda timestamp: timestamp.split(' ')[1][:2])
        input_data = input_data.drop(['id', 'hourly_timestamp'], axis=1)
        predicted = model['regressor'].predict(input_data)
        up_time_dict = {"Up time "+str(id):predicted_value[0] for id,predicted_value in zip(range(predicted.shape[0]), predicted)}
        return JsonResponse(up_time_dict)
    elif request.method == 'POST':
        return JsonResponse({"Request": "POST"})

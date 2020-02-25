from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from api.models import InputData


class InputDataResource(ModelResource):
    class Meta:
        queryset = InputData.objects.all()
        resource_name = 'input_data'
        authorization = Authorization()

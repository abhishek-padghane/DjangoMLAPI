import sklearn


class DataCreator:

    __categorical_column = 'max_occured_sublocation'
    __drop_column_list = ['id', 'hourly_timestamp']

    def __init__(self, data, model):
        self.__data = data
        self.__model = model
        self.__encode_label()
        self.__create_features()
        self.__drop_columns()
        self.__prediction_list = self.__generate_predictions()

    def __encode_label(self):
        self.__data = self.__model['encoder'].transform(self.__categorical_column)

    def __create_features(self):
        self.__data['day_of_week'] = input_data['hourly_timestamp'].apply(lambda timestamp: datetime.strptime(timestamp, '%m-%d-%Y %H:%M:%S.%f').weekday())
        self.__data['day_of_week'] = input_data['hourly_timestamp'].apply(lambda timestamp: datetime.strptime(timestamp, '%m-%d-%Y %H:%M:%S.%f').day)
        self.__data['day_of_week'] = input_data['hourly_timestamp'].apply(lambda timestamp: datetime.strptime(timestamp, '%m-%d-%Y %H:%M:%S.%f').month)
        self.__data['hour'] = input_data['hourly_timestamp'].apply(lambda timestamp: timestamp.split(' ')[1][:2])

    def __drop_columns(self):
        self.__data = self.__data.drop(self.__drop_column_list, axis=1)

    def __generate_predictions(self):
        return self.__model['regressor'].predict(self.__data)

    def get_predictions(self):
        return {"Up time " + str(id): predicted_value[0] for id, predicted_value in zip(range(self.__prediction_list.shape[0]), self.__prediction_list)}

from bottle import post, request, run
from image_recognition import predict
import os
import uuid

NUMBER_OF_RESULTS_DEFAULT_VALUE = 5

NUMBER_OF_RESULTS_PARAM_NAME = "number_of_results"

FILE_EXTENSION = '.jpg'

TEMP_DIRECTORY = 'tmp'


@post('/api/predict')
def save_temp_excel_file():
    if not os.path.exists(TEMP_DIRECTORY):
        os.makedirs(TEMP_DIRECTORY)

    temp_file_name = str(uuid.uuid4()) + FILE_EXTENSION
    path_to_temp_file = _build_path_to_temp_file(temp_file_name)

    with open(path_to_temp_file, 'wb') as out:
        out.write(request.body.read())

    result = predict(path_to_temp_file, _get_number_of_results())

    os.remove(path_to_temp_file)

    return {'predictions': result}


def _get_number_of_results():
    if NUMBER_OF_RESULTS_PARAM_NAME in request.query:
        return int(request.query[NUMBER_OF_RESULTS_PARAM_NAME])
    return NUMBER_OF_RESULTS_DEFAULT_VALUE


def _build_path_to_temp_file(temp_file_name):
    return os.path.join(TEMP_DIRECTORY, temp_file_name)


run(host='0.0.0.0', port=5000, debug=True)
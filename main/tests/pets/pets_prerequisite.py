import os
import json
import logging as logger
from main.utilities.requests_handle import RequestsUtilities

endpoint = 'pet'


class PetsPrerequisite(object):

    @staticmethod
    def create_static_pets():
        """
        Create several pets from a static json file
        """
        # make sure there is users type
        path = os.path.dirname(os.path.realpath(__file__))
        payload_template = os.path.join(path, '../../../../main-old/tests', '..', 'json_data/', 'pet_payload', 'create_pet.json')
        with open(payload_template, 'r') as f:
            petsList = json.loads(f.read())
        # create pets from json
        list_dict = []
        for payload in petsList:
            respond = RequestsUtilities.json_request('POST', endpoint=endpoint, payload=payload)
            objects_data = respond.content
            list_dict.append(objects_data)

        return list_dict

    @staticmethod
    def pet_setup():
        """
        Perform several actions that are mandatory to run the pet tests
        """
        logger.debug(F"Running prerequisite pet_setup")
        # create users from json file
        list_of_dicts = PetsPrerequisite.create_static_pets()
        random_existing_pet_data = json.loads(list_of_dicts[0])
        # prerequisite data
        static_password = '1234'
        info = {
            'static_password': static_password,
            'endpoint': endpoint,
            'random_existing_pet_data': random_existing_pet_data
        }
        return info

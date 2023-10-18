import logging as logger
import os
import json
from pydantic import BaseModel
from utilities.requests_handle import RequestsUtilities


class PetStoreGeneric(BaseModel):
    positive_test_validation: bool = None
    expected_status_code_validation: int = None
    additional_args_validation: dict = None
    object_type_validation: str = None

    @staticmethod
    def get_object_by_id_or_name(endpoint, object_id_or_name):
        """
        Get a specific existing object using its ID/name
        """
        # verify the data is correct
        PetStoreGeneric(object_type_validation=endpoint)
        # Build the API endpoint
        if not object_id_or_name:
            raise ValueError(f"You must use id or name")
        api_endpoint = f'{endpoint}/{object_id_or_name}'
        # make the call
        object_respond = RequestsUtilities.json_request('GET', endpoint=f'{endpoint}/{object_id_or_name}')
        object_json = object_respond.json()
        # check the respond
        if object_json:
            assert isinstance(object_json, dict), f"Object must be a dictionary"

        logger.debug(f"We successfully received object: {api_endpoint}/{object_id_or_name}")

        return object_json

    @staticmethod
    def create_object(endpoint, additional_args=None, expected_status_code=200):
        """
        Create a new object, we can chose not to use the payload json file, and we can add data using the additional_args
        """
        # verify the data is correct
        PetStoreGeneric(object_type_validation=endpoint, additional_args_validation=additional_args,
                        expected_status_code_validation=expected_status_code)
        # get data for the call
        filePath = os.path.dirname(os.path.realpath(__file__))
        payload_template = os.path.join(filePath, '../', 'json_data/', f'{endpoint}_payload',
                                        f'create_{endpoint}.json')
        # update payload
        with open(payload_template) as f:
            temp = json.load(f)
            payload = temp[0]
        if additional_args:
            payload.update(additional_args)
        # make the call
        respond_api = RequestsUtilities.json_request('POST', endpoint=endpoint, payload=payload)
        status_code = respond_api.status_code
        respond_json = respond_api.json()
        # verify status code respond
        RequestsUtilities.assert_status_code(status_code=status_code, expected_status_code=expected_status_code,
                                             endpoint=endpoint, respond_json=respond_json)
        logger.debug(f"We successfully created object: {additional_args['name']}")
        return respond_json

    @staticmethod
    def update_object(endpoint, object_id=None, additional_args=None, expected_status_code=200):
        """
        Update an existing object with static data using his ID
        """
        # verify the data is correct
        PetStoreGeneric(object_type_validation=endpoint, additional_args_validation=additional_args,
                        expected_status_code_validation=expected_status_code)
        # get existing data for the call
        filePath = os.path.dirname(os.path.realpath(__file__))
        payload_template = os.path.join(filePath, '../', 'json_data/', f'{endpoint}_payload', f'update_{endpoint}.json')
        # update payload
        with open(payload_template) as f:
            payload = json.load(f)
        if additional_args:
            payload.update(additional_args)
        # make the call
        if object_id:
            specific_object_data = PetStoreGeneric.get_object_by_id_or_name(endpoint=endpoint, object_id_or_name=object_id)
            payload.update(specific_object_data)
            respond_api = RequestsUtilities.json_request('PUT', endpoint=f'{endpoint}/{object_id}', payload=payload)
            endpoint = f'{endpoint}/{object_id}'
        else:
            respond_api = RequestsUtilities.json_request('PUT', endpoint=f'{endpoint}', payload=payload)
            endpoint = f'{endpoint}'
        status_code = respond_api.status_code
        respond_json = respond_api.json()
        # verify status code respond
        RequestsUtilities.assert_status_code(status_code=status_code, expected_status_code=expected_status_code,
                                             endpoint=endpoint, respond_json=respond_json)
        return respond_json

    @staticmethod
    def remove_existing_object_by_id_or_name(endpoint, object_id_or_name, expected_status_code=200):
        """
        Remove an existing object using its ID
        """
        # verify the data is correct
        PetStoreGeneric(object_type_validation=endpoint)
        logger.debug(f"We are removing object: {object_id_or_name}")
        respond_api = RequestsUtilities.json_request('DELETE', endpoint=f'{endpoint}/{object_id_or_name}')
        status_code = respond_api.status_code
        respond_json = respond_api.json()
        RequestsUtilities.assert_status_code(status_code=status_code, expected_status_code=expected_status_code,
                                             endpoint=endpoint, respond_json=respond_json)

        return respond_json

    @staticmethod
    def get_random_existing_object(endpoint):
        """
        Get all entity type objects that exist in the system and select a random one
        """
        # make the call
        respond_api = PetStoreGeneric.get_object_by_id_or_name(endpoint=endpoint)
        # check the respond
        random_obj = next((obj for obj in respond_api if obj.get('name') != ""), None)
        logger.debug(f"We successfully received a random existing object")

        return random_obj

    @staticmethod
    def get_specific_type_objects(endpoint):
        """
        Get all specific existing object type
        """
        # verify the data is correct
        PetStoreGeneric(object_type_validation=endpoint)
        # Build the API endpoint
        api_endpoint = f'{endpoint}'
        # perform api request and make sure we don't use system objects
        object_respond = RequestsUtilities.json_request('GET', endpoint=f'{endpoint}')
        objects_json = object_respond.json()
        logger.debug(f"We successfully received all objects from type: {api_endpoint}")

        return objects_json

import json
import pytest
import logging as logger
from tests.pets.pets_prerequisite import PetsPrerequisite
from utilities.generic import GenericUtilities
from utilities.petstore_generic import PetStoreGeneric


@pytest.fixture()
def setup():
    setup = PetsPrerequisite.pet_setup()
    return setup


@pytest.mark.pets
def test_create_pet(setup):
    """
    Create pet object
    """
    # generate data for the call
    name = GenericUtilities.generate_random_string()
    pet_id = GenericUtilities.generate_random_integer()
    payload = json.dumps(
        {
            "id": pet_id,
            "category": {"id": 1, "name": "category1"},
            "name": name,
            "photoUrls": ["string"],
            "tags": [{"id": 1, "name": "tags1"}],
            "status": "available"
        }
    )
    payload = json.loads(payload)
    # make the call
    respond_api = PetStoreGeneric.create_object(endpoint=setup['endpoint'], additional_args=payload)
    # verify respond
    assert respond_api, f"Response api of create a pet in empty"
    logger.info(f"We successfully create a pet")

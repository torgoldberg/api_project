import pytest
import logging as logger

from main.json_data.tests.pets.pets_prerequisite import PetsPrerequisite
from main.json_data.utilities.generic import GenericUtilities
from main.json_data.utilities.petstore_generic import PetStoreGeneric


@pytest.fixture()
def setup():
    setup = PetsPrerequisite.pet_setup()
    return setup


@pytest.mark.pets
def test_update_pet_name(setup):
    """
    Update pet object name
    """
    # generate data for the call
    random_existing_pet_data = setup['random_existing_pet_data']
    pet_name = GenericUtilities.generate_random_string()
    random_existing_pet_data['name'] = pet_name
    payload = random_existing_pet_data
    # make the call
    respond_api = PetStoreGeneric.update_object(endpoint=setup['endpoint'], additional_args=payload)
    # verify respond
    assert respond_api, f"Response api of create a pet in empty"
    logger.info(f"We verified we can update pet")

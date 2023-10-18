import pytest
import logging as logger

from tests.pets.pets_prerequisite import PetsPrerequisite
from utilities.petstore_generic import PetStoreGeneric


@pytest.fixture()
def setup():
    setup = PetsPrerequisite.pet_setup()
    return setup


@pytest.mark.pets
def test_get_specific_pet(setup):
    """
    Get all the pets
    """
    # generate data for the call
    random_existing_pet_data = setup['random_existing_pet_data']
    pet_id = random_existing_pet_data['id']
    # make the call
    respond_api = PetStoreGeneric().get_object_by_id_or_name(endpoint=setup['endpoint'], object_id_or_name=pet_id)
    # verify the respond is not empty
    assert respond_api, f"Response api of get specific pet in empty"
    logger.info(f"We successfully receive specific pet")

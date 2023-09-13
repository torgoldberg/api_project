import pytest
import logging as logger
from main.tests.pets.pets_prerequisite import PetsPrerequisite
from main.utilities.petstore_generic import PetStoreGeneric


@pytest.fixture()
def setup():
    setup = PetsPrerequisite.pet_setup()
    return setup


@pytest.mark.pets
def test_delete_pet_using_id(setup):
    """
    Delete specific pet using its ID
    """
    # generate data for the call
    random_existing_pet_data = setup['random_existing_pet_data']
    pet_id = random_existing_pet_data['id']
    # make the call
    PetStoreGeneric().remove_existing_object_by_id_or_name(endpoint=setup['endpoint'], object_id_or_name=pet_id)
    # verify respond
    logger.info(f'We successfully removed pet: {pet_id}')

from unittest import mock
from unittest.mock import MagicMock, Mock, PropertyMock
import pytest_asyncio
from python_mocking.patching import Patching

@pytest_asyncio.fixture
async def studio_ghibli_response():
    async def _(**kwargs):
        _ = {**{
                "film": {
                    "title": "Spirited Away",
                    "director": "Hayao Miyazaki",
                    "release_date": "2001",
                    "rating": 8.6,
                    "genre": ["Animation", "Adventure", "Family"],
                    "description": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits, and where humans are changed into beasts."
                },
                "characters": [
                    {
                        "name": "Chihiro Ogino",
                        "gender": "Female",
                        "age": 10,
                        "role": "Protagonist"
                    },
                    {
                        "name": "Haku",
                        "gender": "Male",
                        "age": "Unknown",
                        "role": "Supporting"
                    }
                ],
                "location": {
                    "name": "The Bathhouse",
                    "setting": "A magical world",
                    "description": "The Bathhouse is a place where eight million gods come to rest and replenish their energy."
                }
            }
            , **kwargs}

        return _

    return _

@pytest_asyncio.fixture
async def patching__method_mock(mocker, studio_ghibli_response):
    module = Patching.__module__
    name = Patching.__name__
    # mocker.patch(f"{module}.{name}._{name}__method", return_value=await jwt_access_token_decodificado(film = {"title": "Other"}))
    mocker.patch.object(Patching, f"_{Patching.__name__}__method", return_value=await studio_ghibli_response(film = {"title": "Other"}))

#    with mock.patch.object(Patching, f'_{Patching.__name__}__method', new_callable=Mock()) as obj_mock:
#        obj_mock.return_value = jwt_access_token_decodificado(film = {"title": "Other"})
#
#        yield

#    with mock.patch.object(Patching, f'_{Patching.__name__}__method', return_value=await jwt_access_token_decodificado(film = {"title": "Other"})) as obj_mock:
#        yield


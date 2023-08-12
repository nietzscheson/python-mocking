from unittest.mock import Mock
import pytest
import pytest_asyncio
from python_mocking.patching import Patching

@pytest.mark.asyncio
async def test_patching(patching__method_mock):
    patching = Patching()
    patching_response = await patching()

    print("The response", patching_response)

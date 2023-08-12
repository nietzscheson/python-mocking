from unittest.mock import Mock
import pytest
from python_mocking.mocking_async import MockingAsync


@pytest.mark.asyncio
async def test_mocking_async(mocker):
    patch = f"{MockingAsync.__module__}.{MockingAsync.__name__}"
    instance_mock = mocker.patch(f"{patch}.instance_method", return_value=Mock())
    static_mock = mocker.patch(f"{patch}.static_method", return_value=Mock())
    class_method_mock = mocker.patch(f"{patch}.class_method", return_value=Mock())
    pvt_instance_mock = mocker.patch(f"{patch}._{MockingAsync.__name__}__private_instance_method", return_value=Mock())
    pvt_class_mock = mocker.patch(f"{patch}._{MockingAsync.__name__}__private_class_method", return_value=Mock())
    pvt_static_mock = mocker.patch(f"{patch}._{MockingAsync.__name__}__private_static_method", return_value=Mock())

    await MockingAsync().call()

    assert instance_mock.call_count == 1
    assert static_mock.call_count == 1
    assert class_method_mock.call_count == 1
    assert pvt_instance_mock.call_count == 1
    assert pvt_class_mock.call_count == 1


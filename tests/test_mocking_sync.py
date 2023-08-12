from unittest.mock import Mock

from python_mocking.mocking_sync import Mocking



def test_mocking_sync(mocker):
    patch = f"{Mocking.__module__}.{Mocking.__name__}"
    instance_mock = mocker.patch(f"{patch}.instance_method", return_value=Mock())
    static_mock = mocker.patch(f"{patch}.static_method", return_value=Mock())
    class_method_mock = mocker.patch(f"{patch}.class_method", return_value=Mock())
    pvt_instance_mock = mocker.patch(f"{patch}._{Mocking.__name__}__private_instance_method", return_value=Mock())
    pvt_class_mock = mocker.patch(f"{patch}._{Mocking.__name__}__private_class_method", return_value=Mock())
    pvt_static_mock = mocker.patch(f"{patch}._{Mocking.__name__}__private_static_method", return_value=Mock())

    Mocking().call()

    assert instance_mock.call_count == 1
    assert static_mock.call_count == 1
    assert class_method_mock.call_count == 1
    assert pvt_instance_mock.call_count == 1
    assert pvt_class_mock.call_count == 1


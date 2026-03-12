"""Make sure that all "essential" services are present."""
from importlib.metadata import requires

from mypy_boto3_builder.service_name import ServiceName

essential_service_names = ServiceName.ESSENTIAL_NAMES

for name in essential_service_names:
    res = requires("mypy_boto3_" + name)
    print("Service '" + name + "' provided by " + str(res) + ".")

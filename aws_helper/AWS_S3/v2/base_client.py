from abc import ABC
import boto3


class Client(ABC):
    """Class that creates low-level/high-level default session"""
    @classmethod
    def get_resource(cls, aws_access_key_id, aws_secret_access_key):
        """Create a high-level service class client by name using the default session"""
        return boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)

    @classmethod
    def get_client(cls, aws_access_key_id, aws_secret_access_key):
        """Create a low-level service class client by name using the default session"""
        return boto3.client("s3",
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key)

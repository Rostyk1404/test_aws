from abc import ABC, abstractmethod
import boto3
from configparser import ConfigParser


class Client(ABC):
    def __init__(self):
        conf_file = ConfigParser()
        conf_file.read("/home/ross/test_aws_task/aws_helper/aws.conf")
        self.aws_access_key_id = conf_file.get("AWS", "aws_access_key_id")
        self.aws_secret_access_key = conf_file.get("AWS", "aws_secret_access_key")

    def get_client(self):
        """Create a low-level service client by name using the default session"""
        return boto3.client("s3",
                            aws_access_key_id=self.aws_access_key_id,
                            aws_secret_access_key=self.aws_secret_access_key)

    # @abstractmethod
    # def run(self):
    #     pass

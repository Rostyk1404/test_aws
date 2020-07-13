from aws_helper.interfaces.aws_folder_interface import AwsFolderInterface
from aws_helper.aws_s3_helper.v2.base_client import Client
from configparser import ConfigParser

conf_file = ConfigParser()
conf_file.read("/home/ross/test_aws_task/aws_helper/aws.conf")
credentials = (conf_file.get("AWS", "aws_access_key_id"),
               conf_file.get("AWS", "aws_secret_access_key"))


class AWSFolder(AwsFolderInterface, Client):
    """The current class provides delete folders and files in bucket
            :param
                    bucket_name  name of your bucket in AWS
            :param
                    credentials access to AWS account
            :param
                    folder_name folder name which you want to delete
        """

    @classmethod
    def create_folder(cls, credentials: tuple, bucket_name: str, folder_name: str):
        """Give us ability to create folder inside bucket"""
        cls.get_client(*credentials).put_object(Bucket=bucket_name, Key=(folder_name + '/'))
        
    @classmethod
    def delete_all_data_in_bucket(cls, credentials: tuple, bucket_name: str):
        """Give us ability to clear a bucket"""
        cls.get_resource(*credentials).Bucket(bucket_name).objects.all().delete()

    @classmethod
    def delete_folder_recursively(cls, credentials: tuple, bucket_name: str, folder_name: str):
        """Provides to delete folder/folders with file/files in AWS S3"""

        bucket = cls.get_resource(*credentials).Bucket(bucket_name)
        bucket.objects.filter(Prefix=folder_name).delete()



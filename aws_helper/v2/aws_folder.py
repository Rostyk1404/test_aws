from aws_helper.interfaces.aws_folder_interface import AwsFolderInterface
from aws_helper.v2.base_client import Client


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
    def delete_all_data_in_bucket(cls, credentials: tuple, bucket_name: str):
        """Give us ability to clear a bucket"""
        cls.get_resource(*credentials).Bucket(bucket_name).objects.all().delete()

    @classmethod
    def delete_folder_recursively(cls, credentials: tuple, bucket_name: str, folder_name: str):
        """Provides to delete folder/folders with file/files in AWS S3"""

        bucket = cls.get_resource(*credentials).Bucket(bucket_name)
        bucket.objects.filter(Prefix=folder_name).delete()

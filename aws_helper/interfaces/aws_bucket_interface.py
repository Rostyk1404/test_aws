from abc import ABC, abstractmethod


class AwsBucketInterface(ABC):
    @classmethod
    @abstractmethod
    def create(cls, credentials: tuple, bucket_name: str, region: str = None):
        pass

    @classmethod
    @abstractmethod
    def get_list_of_buckets(cls, credentials: tuple):
        pass

    @classmethod
    @abstractmethod
    def delete_bucket_recursively(cls, credentials: tuple, bucket_name: str):
        pass

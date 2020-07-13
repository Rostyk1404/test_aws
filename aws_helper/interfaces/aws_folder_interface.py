from abc import ABC, abstractmethod


class AwsFolderInterface(ABC):

    @abstractmethod
    def create_folder(cls, credentials: tuple, bucket_name: str, folder_name: str):
        pass

    @abstractmethod
    def delete_all_data_in_bucket(cls, credentials: tuple, bucket_name: str):
        pass

    @abstractmethod
    def delete_folder_recursively(cls, credentials: tuple, bucket_name: str, folder_name: str):
        pass

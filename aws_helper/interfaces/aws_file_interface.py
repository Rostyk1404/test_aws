from abc import ABC, abstractmethod


class AwsFileInterface(ABC):
    @classmethod
    @abstractmethod
    def upload_files(cls, credentials: tuple, bucket_name: str, file_lists: str):
        pass

    @classmethod
    @abstractmethod
    def download_file(cls, credentials: tuple,  bucket_name: str, source: str, file_path=None):
        pass

    @abstractmethod
    def delete_file(self, credentials: tuple, file_name: str):
        pass

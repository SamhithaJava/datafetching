import boto3
__all__ = ['download_single_document_from_s3', 'download_multiple_documents_from_s3']


def download_single_document_from_s3(bucket_name, document_key, destination_path, aws_access_key_id,
                                     aws_secret_access_key, region_name=None):
    """
    Download a single document from an S3 bucket.

    Parameters:
    - bucket_name: Name of the S3 bucket.
    - document_key: Key of the document to download from the bucket.
    - destination_path: Local path where the document will be saved.
    - aws_access_key_id (optional): AWS access key ID.
    - aws_secret_access_key (optional): AWS secret access key.
    - region_name (optional): AWS region name where the bucket is located.

    Returns:
    - True if the document was successfully downloaded, False otherwise.
    """
    try:
        s3_resource = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                                     aws_secret_access_key=aws_secret_access_key, region_name=region_name)
        """s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                                 region_name=region_name)
        s3_client.download_file(bucket_name, document_key, destination_path)"""

        bucket = s3_resource.Bucket(bucket_name)

        # Download the file
        bucket.download_file(document_key, destination_path)
        return True
    except Exception as e:
        print(f"Error downloading document from S3: {e}")
        return False


def download_multiple_documents_from_s3(bucket_name, document_keys, destination_folder, aws_access_key_id=None,
                                        aws_secret_access_key=None, region_name=None):
    """
    Download multiple documents from an S3 bucket.

    Parameters:
    - bucket_name: Name of the S3 bucket.
    - document_keys: List of document keys to download from the bucket.
    - destination_folder: Local folder where the documents will be saved.
    - aws_access_key_id (optional): AWS access key ID.
    - aws_secret_access_key (optional): AWS secret access key.
    - region_name (optional): AWS region name where the bucket is located.

    Returns:
    - True if all documents were successfully downloaded, False otherwise.
    """
    try:
        s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                                 region_name=region_name)
        for document_key in document_keys:
            destination_path = f"{destination_folder}/{document_key.split('/')[-1]}"
            s3_client.download_file(bucket_name, document_key, destination_path)
        return True
    except Exception as e:
        print(f"Error downloading documents from S3: {e}")
        return False

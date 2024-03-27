from operations import download_single_document_from_s3, download_multiple_documents_from_s3
import boto3

bucket_name = 'qdmintegrationpoc'
document_key = 'Flyer.pdf'
destination_path = 'local/path/to/save/document.txt'
access_key= 'AKIAYKAVP22M2S3GTZGH'
secret_access_key='0u97yiIqy0WVj6Zcs3iyNDvbwyDF+VmzBLayejh'
region_name = 'us-east-1'

"""s3_client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_access_key,
                         region_name=region_name)
response = s3_client.list_buckets()

# Extract bucket names from the response
bucket_names = [bucket['Name'] for bucket in response['Buckets']]

# Print the bucket names
print("List of S3 buckets:")
for bucket_name in bucket_names:
    print(bucket_name) """

result = download_single_document_from_s3(bucket_name, document_key, destination_path,access_key,secret_access_key, 'us-east-1')
if result:
    print("Document downloaded successfully.")
else:
    print("Failed to download document.")

document_keys = ['path/to/first/document.txt', 'path/to/second/document.txt']
destination_folder = 'local/path/to/save/documents/'

result = download_multiple_documents_from_s3(bucket_name, document_keys, destination_folder,access_key,secret_access_key, 'us-east-1')
if result:
    print("All documents downloaded successfully.")
else:
    print("Failed to download one or more documents.")

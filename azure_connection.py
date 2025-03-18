from azure.storage.blob import BlobServiceClient

ACCOUNT_URL="https://<compte>.blob.core.windows.net"

ACCOUNT_KEY="""
TO ADD
"""

def get_blob_service_client():
    """
    Crée un client de service Blob pour interagir avec le stockage Azure.

    :param account_url: URL du compte de stockage Azure.
    :param account_key: Clé du compte de stockage Azure.
    :return: BlobServiceClient
    """
    blob_service_client = BlobServiceClient(account_url=ACCOUNT_URL, credential=ACCOUNT_KEY)
    return blob_service_client

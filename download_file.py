from azure_connection import get_blob_service_client

def download_blob(container_name, blob_name, download_file_path):
    """
    Télécharge un blob depuis un conteneur Azure.

    :param container_name: Nom du conteneur.
    :param blob_name: Nom du blob à télécharger.
    :param download_file_path: Chemin où enregistrer le fichier téléchargé.
    """
    blob_service_client = get_blob_service_client()
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    print(f"Téléchargement du blob en cours : {blob_name}")

    with open(download_file_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())

    print(f"Téléchargement terminé : {blob_name}")

if __name__ == "__main__":
    CONTAINER_NAME = "<conteneur>"
    BLOB_NAME = "<blob>"
    DOWNLOAD_FILE_PATH = "<chemin-de-destination>"

    download_blob(CONTAINER_NAME, BLOB_NAME, DOWNLOAD_FILE_PATH)

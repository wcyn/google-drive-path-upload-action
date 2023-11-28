from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def upload_file(service, file_path, parent_folder_id, file_name=""):
    """Create and upload a file and return the file ID
    Returns : File Id of the newly created file
    """
    try:
        # create drive api client
        file_metadata = {
            # Allow renaming the file on upload
            "name": file_name if file_name else file_path.split("/")[-1],
            "parents": [parent_folder_id]
        }

        media = MediaFileUpload(file_path)
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id,name,webContentLink")
            .execute()
        )
        print(f"File created:\n - name: {file['name']}\n - id: {file['id']}\n - link: {file['webContentLink']}")

        return file["id"], file["webContentLink"]

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


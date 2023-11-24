from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

def create_file(service, file_name, parent_folder_id):
    """Create a file and returns the file ID
    Returns : File Id
    """

    try:
        # create drive api client
        file_metadata = {
            "name": file_name,
            # "mimeType": "application/vnd.google-apps.file",
            "parents": [parent_folder_id]
        }

        media = MediaFileUpload(file_name)
        # pylint: disable=maybe-no-member
        file = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id")
            .execute()
        )

        file_id = file.get("id")
        print(f'File ID: "{file_id}".')
        return file_id

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


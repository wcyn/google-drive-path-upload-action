from googleapiclient.errors import HttpError

def create_folder(service, folder_path, parent_folder_id):
    """Create a folder and prints the folder ID
    Returns : Folder Id
    """
    folder_names = folder_path.split("/")
    current_parent_folder = parent_folder_id

    try:
        for folder_name in folder_names:
            if folder_name:
                # create drive api client
                file_metadata = {
                    "name": folder_name,
                    "mimeType": "application/vnd.google-apps.folder",
                    "parents": [current_parent_folder]
                }

                # pylint: disable=maybe-no-member
                folder = service.files().create(body=file_metadata, fields="id").execute()
                folder_id = folder.get("id")
                current_parent_folder = folder_id
                print(f'Folder ID: "{folder_id}".')
        return folder_id
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None




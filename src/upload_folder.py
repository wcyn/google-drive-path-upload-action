import os
from googleapiclient.errors import HttpError
from upload_file import upload_file

# TODO: Reuse code for upload_file.
# TODO: Prevent string quote errors in env variables for parent_folder_id
def upload_folder(service, entry_path, parent_folder_id):
    """Create a folder and prints the folder ID
    entry_path: path of the current file or folder
    """
    if os.path.isfile(entry_path):
        upload_file(service, entry_path, parent_folder_id)
        return
    else:
        new_folder_id = create_folder(service, entry_path.split("/")[-1], parent_folder_id)
        with os.scandir(entry_path) as entries:
            for entry in entries:
                upload_folder(service, entry.path, new_folder_id)


def create_folder(service, folder_name, parent_folder_id):
    try:
        file_metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [parent_folder_id]
        }

        folder = service.files().create(body=file_metadata, fields="id,name,webViewLink").execute()
        print(f"Folder created:\n - name: {folder['name']}\n - id: {folder['id']}\n - link: {folder['webViewLink']}")
        return folder["id"], folder["webViewLink"]

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

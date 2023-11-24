# from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account
from create_folder import create_folder
from create_file import create_file
from list_files_and_folders import list_files_and_folders

import json
import sys
import os

def get_service(api_name, api_version, scopes, gdrive_creds):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        gdrive_creds: JSON Credentials for the Google Service Account.

    Returns:
        A service that is connected to the specified API.
    """

    credentials = service_account.Credentials.from_service_account_info(json.loads(gdrive_creds, strict=False))

    scoped_credentials = credentials.with_scopes(scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=scoped_credentials)

    return service


def main():
    """Gets args and creates a file or folder to drive
    """
    gdrive_sa_key = os.environ["INPUT_GDRIVE-SA-KEY"]

    script, folder_or_file, name, parent_folder_id = sys.argv

    # Define the auth scopes to request.
    scope = 'https://www.googleapis.com/auth/drive.file'

    try:
        # Authenticate and construct service.
        service = get_service(
            api_name='drive',
            api_version='v3',
            scopes=[scope],
            gdrive_creds=gdrive_sa_key)

        # list_files_and_folders(service)
        if folder_or_file == "folder":
            new_folder_id = create_folder(service, name, parent_folder_id )
        elif folder_or_file == "file":
            new_file_id = create_file(service, name, parent_folder_id)

    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')

if __name__ == '__main__':
    main()

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

import json

def get_scoped_service(api_name, api_version, scopes, gdrive_creds):
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


def get_gdrive_service(gdrive_sa_key):
    """Creates a file or folder to drive
    """

    # Define the auth scopes to request. https://developers.google.com/drive/api/guides/api-specific-auth
    scope = 'https://www.googleapis.com/auth/drive'

    try:
        # Authenticate and construct service.
        service = get_scoped_service(
            api_name='drive',
            api_version='v3',
            scopes=[scope],
            gdrive_creds=gdrive_sa_key)
        return service

    except HttpError as error:
        # TODO Handle errors from drive API.
        print(f'An error occurred: {error}')

from googleapiclient.errors import HttpError

def list_files_and_folders(service):
    """ Prints and returns out a list of all files and folders accessible to the service
    Returns : File and Folder Ids
    """

    try:
        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

        return items

    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


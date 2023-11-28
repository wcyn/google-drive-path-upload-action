import os
from gdrive_service import get_gdrive_service
from upload_folder import upload_folder
from upload_file import upload_file

# Set the output value by writing to the outputs in the Environment File, mimicking the behavior defined here:
#  https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter
def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'\n{output_name}={output_value}')
    f.close()

def main():
    """
    Uploads a file or creates a folder on Google Drive and sets the new item id as the action output
    """
    gdrive_sa_key = os.environ["INPUT_GDRIVE_SA_KEY"]
    parent_folder_id = os.environ["INPUT_GDRIVE_FOLDER_ID"]
    item_path = os.environ["INPUT_ITEM_PATH"] # Path to the file or folder to upload
    name = os.environ["INPUT_NAME"]

    gdrive_service = get_gdrive_service(gdrive_sa_key)
    uploaded_item_id, download_link = None, None
    if os.path.isdir(item_path):
        uploaded_item_id, download_link = upload_folder(gdrive_service, item_path, parent_folder_id )
    else:
        uploaded_item_id, download_link = upload_file(gdrive_service, item_path, parent_folder_id, name)

    print(f"**ID: {uploaded_item_id}\n**Link: {download_link}")

    set_github_action_output('uploaded_item_id', uploaded_item_id)
    set_github_action_output('download_link', download_link)

if __name__ == "__main__":
    main()

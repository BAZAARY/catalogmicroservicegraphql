from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

#data retrieved from google drive-----------------------------------

# Below code does the authentication 
gauth = GoogleAuth()
# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Authenticate if they're not there

    # This is what solved the issues:
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})

    # Usa el cliente_secrets.json file
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
    # Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth) 

def get_folder_ids(parent_folder_id):
    folder_ids = []
    # Get the list of files and folders within the parent_folder_id
    folder_list = drive.ListFile({'q': f"'{parent_folder_id}' in parents and trashed=false"}).GetList()

    for item in folder_list:
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            folder_ids.append({'id': item['id'], 'title': item['title']})

    return folder_ids

def get_root_folder_ids():
    root_folder_id = 'root'  # Use 'root' for the root folder of Google Drive
    folder_ids = get_folder_ids(root_folder_id)
    return folder_ids

def get_file_ids(folder_id):
    file_ids = []
    # Obtén la lista de archivos y carpetas en la carpeta raíz (folder_id = 'root')
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents"}).GetList()

    for file in file_list:
        file_ids.append({'id': file['id'], 'title': file['title']})

    return file_ids

def getFilesIdsOfFolderWithId(folderId):
    file_ids = get_file_ids(folderId)
    return file_ids
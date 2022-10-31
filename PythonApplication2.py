from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

print("Here 1");
service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
print("Here 2");
folder_id = '1gqseuICm3ibtr-lE-G2oUYxXZ0f_iMeF'
file_names = ['untitled.png'] 
mime_types = ['image/png']
print("Here 3");
for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {
    'name': file_name,
    'parents': [folder_id]
    }
    media = MediaFileUpload('./Untitled folder/{0}'.format(file_name), mimetype=mime_type)
    
    service.files().create( 
        body=file_metadata,
        media_body=media, 
        fields='id'
    ).execute()


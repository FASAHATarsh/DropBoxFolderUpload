import os
import dropbox
from dropbox.files import WriteMode
class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, f_from, f_to):
        db = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(f_from):
            for files in dirs:
                local_path = os.path.join(root, files)
                relative_path = os.path.relpath(local_path, f_from)
                dropbox_path = os.path.join(f_to, relative_path)                
                with open(local_path, 'rb') as f:
                    db.files_upload(f.read(), dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token=''
    transferData = TransferData(access_token)
    f_from = str(input("Enter the path to transfer : "))
    f_to = input("Enter the path to dropbox : ")     
    transferData.upload_file(f_from,f_to)
    print("Folder moved!")

if __name__ == '__main__':
	main()
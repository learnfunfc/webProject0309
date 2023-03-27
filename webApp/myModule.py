from uuid_upload_path import uuid  # not used
import os
from django.conf import settings
from hashlib import sha256

def save_File(f, filetype):
    filename = f.name
    filename = filename.split(".")[0]  # remove file extention
    if filetype == "html":
        target = os.path.join(settings.BASE_DIR, "webApp",
                              "templates2", hashEncoding(filename) + "." + filetype)
    if filetype == "jpg":
        target = os.path.join(settings.BASE_DIR,
                              "media", hashEncoding(filename) + "." + filetype)

    with open(target, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    return os.path.basename(target)  # 回傳檔名.副檔名


def hashEncoding(string, length=15):
    nameut8 = string.encode('utf-8')
    hashValue = sha256(nameut8).hexdigest()
    return hashValue[:length]

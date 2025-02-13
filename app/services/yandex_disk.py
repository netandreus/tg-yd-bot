import yadisk

from app.config import YANDEX_TOKEN, YANDEX_FOLDER



yadisk_instance = yadisk.YaDisk(token=YANDEX_TOKEN)

def upload(file_stream, file_id) -> bool:
    """
    Uploads a file to Yandex.Disk.

    :param file_stream: Byte stream containing the file.
    :type file_stream: BytesIO
    :param file_id: Unique file identifier.
    :type file_id: str
    :return: True if upload was successful, False otherwise.
    :rtype: bool
    """

    try:
        yadisk_instance.upload(file_stream, f"{YANDEX_FOLDER}/{file_id}", overwrite=True)
        return True

    except Exception as e:
        print(f"Upload error. {e}")
        return False

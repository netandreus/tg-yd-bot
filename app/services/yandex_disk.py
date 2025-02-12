import yadisk

from app.config import YANDEX_TOKEN, YANDEX_FOLDER



yadisk_instance = yadisk.YaDisk(token=YANDEX_TOKEN)

def upload(file_stream, file_id) -> bool:
    """
    Загружает файл на Яндекс.Диск.

    :param file_stream: Поток байтов, содержащий файл.
    :type file_stream: BytesIO
    :param file_id: Уникальный идентификатор файла.
    :type file_id: str
    :return: True, если загрузка прошла успешно, иначе False.
    :rtype: bool
    """

    try:
        yadisk_instance.upload(file_stream, f"{YANDEX_FOLDER}/{file_id}", overwrite=True)
        return True

    except Exception as e:
        print(f"Ошибка загрузки. {e}")
        return False

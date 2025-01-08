from io import BufferedReader
from math import nan
import os
from typing import Tuple

import aiohttp
from config import Config
from pdf_validater import PdfValidater
from pandas import Series


class Downloader:
    validater = PdfValidater()
    download_path: str = Config.DownloadDir.value

    def __init__(self):
        os.makedirs(self.download_path, exist_ok=True)

    async def download_file(self, url) -> Tuple[int, bytes]:
        async with aiohttp.ClientSession() as session:
            for _ in range(3):
                try:
                    async with session.get(url, timeout=Config.DownloadTimeout.value) as res:
                        res.raise_for_status()
                        content = await res.read()
                        if res.content_type == 'application/pdf':
                            return (res.status, content)
                except aiohttp.ClientError:
                    continue
            return (404, b'')

    async def download_row(self, row: Series) -> bool:
        primary_url: str = row[Config.PrimaryUrl.value]
        secondary_url: str = row[Config.SecondaryUrl.value]
        file_name: str = row[Config.IdCol.value] + '.pdf'
        file_path = os.path.join(self.download_path, file_name)

        for i, url in enumerate([primary_url, secondary_url]):
            if type(url) != str:
                continue

            if len(url) == 0:
                continue

            try:
                status, content = await self.download_file(url)
                if status == 200:
                    with open(file_path, 'wb') as pdf_out:
                        pdf_out.write(content)
                        return True
                    # if self.validater.is_valid_pdf(file_path):
                    #     return True
                    # else:
                    #     os.remove(file_path)
            except aiohttp.NonHttpUrlClientError as e:
                pass
            except TypeError as e:
                pass
            except:
                pass

        return False
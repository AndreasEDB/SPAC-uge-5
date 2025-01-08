import asyncio
import os
import gc
import pandas as pd
from config import Config
from downloader import Downloader
from excel import Excel

downloader = Downloader()
meta_data = Excel(os.path.join(Config.BaseDir.value, Config.MetadataFile.value))
gri = Excel(os.path.join(Config.BaseDir.value, Config.GRIFile.value))
new_rows = []

semaphore = asyncio.Semaphore(200)  # Adjust based on system capabilities

async def download_row(i, row):
    async with semaphore:
        print(f"Downloading {i}")
        new_row = {}
        downloaded = await downloader.download_row(row)
        for col in meta_data.df.columns:
            if col in gri.df.columns:
                new_row[col] = row[col]
            else:
                new_row[col] = None

        new_row[Config.DownLoadedCol.value] = Config.Downloaded.value if downloaded else Config.NotDownloaded.value
        new_rows.append(new_row)
        print(f"Downloaded {row[Config.IdCol.value]}.pdf: {downloaded}")


def write_metadata():
    new_rows.sort(key=lambda x: x[Config.IdCol.value])
    for row in new_rows:
        if row[Config.IdCol.value] in meta_data.df[Config.IdCol.value].values:
            meta_data.df.loc[meta_data.df[Config.IdCol.value] == row[Config.IdCol.value]] = row
        else:
            meta_data.df = pd.concat([meta_data.df, pd.DataFrame([row])], ignore_index=True)
    meta_data.write_file(os.path.join(Config.BaseDir.value, Config.OutputFile.value))
    new_rows.clear()  # Clear new_rows after writing to file

async def main():
    batch_size = 10
    rows = list(gri.df.iterrows())
    for i in range(0, len(rows), batch_size):
        batch = rows[i:i + batch_size]
        tasks = [download_row(i, row) for i, row in batch]
        await asyncio.gather(*tasks)
        gc.collect()
        # Write metadata file after each batch
        write_metadata()

asyncio.run(main())
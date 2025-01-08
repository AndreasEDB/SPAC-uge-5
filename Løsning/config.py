from enum import Enum
import os

class Config(Enum):
    # Paths
    BaseDir = os.path.dirname(os.path.abspath(__file__))
    DownloadDir = os.path.join(BaseDir, 'download')

    # Columns
    PrimaryUrl = 'Pdf_URL'
    SecondaryUrl = 'Report Html Address'
    DownLoadedCol = 'pdf_downloaded'
    IdCol = 'BRnum'

    # Values
    Downloaded = 'Downloaded'
    NotDownloaded = 'Not downloaded'

    # Files
    MetadataFile = 'Metadata2006_2016.xlsx'
    GRIFile = 'GRI_2017_2020.xlsx'
    OutputFile = 'Metadata2006_2020.xlsx'

    # Debug
    FileLimit = 0

    # Other
    DownloadTimeout = 3
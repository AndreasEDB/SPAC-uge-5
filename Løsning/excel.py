from typing import List
import pandas as pd 
from pandas import DataFrame


class Excel:
    file_path: str = ''
    df: DataFrame = None
    columns: List[str] = None
    
    def __init__(self, file_path: str, columns: List[str] = None, from_df: DataFrame = None) -> None:
        self.file_path = file_path
        self.columns = columns
        self.from_df = from_df
        self.df = self.read_excel()
    
    def read_excel(self) -> DataFrame:
        try:
            return pd.read_excel(self.file_path, engine='openpyxl')
        except FileNotFoundError as e:
            return pd.DataFrame(columns=self.columns)
    
    def write_file(self, new_file_path: str = None) -> None:
        self.df.to_excel(new_file_path or self.file_path, index=False, engine='openpyxl')
import pandas as pd
import openpyxl as op
from pathlib import Path


PATH_EXT = Path(Path.cwd(), 'brotherETL', 'extract', 'extract.xlsx')
PATH_DC = Path(Path.cwd(), 'brotherETL', 'extract', 'mapping_dc.xlsx')
PATH_NAME = Path(Path.cwd(), 'brotherETL', 'extract', 'mapping_names.xlsx')


class Extract():
    @staticmethod
    def get_init_df():
        """extract first dataframe from exel"""
        wb = op.load_workbook(PATH_EXT)
        active_sheet = wb.active
        wb.close()
        return pd.DataFrame(active_sheet.values)

    @staticmethod
    def get_dict_dc():
        """get dictionary from exel"""
        df = pd.read_excel(PATH_DC)
        return df.set_index('id').T.to_dict('list')

    @staticmethod
    def get_dict_names():
        """get dictionary from exel"""
        df = pd.read_excel(PATH_NAME)
        return df.set_index('id').T.to_dict('list')
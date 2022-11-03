import shutil
import openpyxl as op
import pandas as pd
from pathlib import Path


PATH_LOAD_TEMPLATE = Path(Path.cwd(), 'brotherETL', 'load', 'template', 'load.xlsx')


class Load():
    def __init__(self, date, df_dict):
        self.date = date
        self.df_dict = df_dict

    def to_xlsx(self):
        """create reports"""
        for name, df in self.df_dict.items():
            # create file and path
            PL = Load.copy_file(name, self.date)
            # append df to file
            with pd.ExcelWriter(PL, mode="a", engine="openpyxl", if_sheet_exists="overlay",) as writer:
                df.to_excel(writer, sheet_name="Лист1", index=False, startrow=12) 

    @staticmethod
    def copy_file(name, date):
        """copy report templates"""
        PATH_LOAD = Path(Path.cwd(), 'brotherETL', 'load', f'{name}{date}.xlsx')
        shutil.copy(PATH_LOAD_TEMPLATE, PATH_LOAD)
        return PATH_LOAD

    def change_date(self):
        """change date in report header"""
        wb = op.load_workbook(PATH_LOAD_TEMPLATE)
        sheet = wb.active
        # change date to inserted
        sheet['G2'] = self.date
        wb.save(PATH_LOAD_TEMPLATE)
        wb.close()
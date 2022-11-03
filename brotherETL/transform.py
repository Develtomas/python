import copy
import pandas as pd

from extract import Extract


class Transform():
    def __init__(self, date, df_dict) -> None:
        self.date = date
        self.data = df_dict

    @staticmethod
    def drop_excess_col(df):
        """date extrs columns from initial df"""
        df = df.drop([0, 2, 3, 7], axis='columns')
        return df

    @staticmethod
    def date_column_transform(df):
        """datetime -> date format, rename columns"""
        df["date"] = pd.to_datetime(df[1]).dt.date
        df = df.drop([1], axis='columns')
        df.rename(columns = {4: 'location', 5: 'name', 6: 'price'}, inplace = True)
        return df

    @staticmethod
    def filter_company_name(df, name):
        """keyword = 'Тандер' or something else"""
        df = df[df.location.str.contains(name, na=False)]
        return df

    @staticmethod
    def split_product(df):
        """split df by product"""
        df_sugar = df[df.name.str.contains("Сахар")]
        df_salt = df[df.name.str.contains("Соль")]
        df_soda = df[df.name.str.contains("Сода")]
        df_grain = df[~df.name.str.contains("Соль|Сахар|Сода")]
        return {'sugar': df_sugar, 'salt': df_salt, 'grain': df_grain, 'soda': df_soda}

    def filter_by_date(self):
        """filter df via date, create two dict filtered/raw"""
        date_ = pd.to_datetime(self.date, format='%d.%m.%Y', errors='ignore').date()
        filtered_frame_dict ={}
        for key, frame in self.data.items():
            # check df_sugar or else is empty
            if frame.empty:
                continue
            # create filtered by data df
            df = frame[frame.date == date_]
            # check this df is empty
            if df.empty:
                continue
            else:
                # filter initial df by date(if date < now)
                df_before = frame[frame.date <= date_]
            # add to new df dict
            filtered_frame_dict.setdefault(key, [df, df_before, date_])
        self.data = filtered_frame_dict

    @staticmethod
    def add_last_price(filtered, raw, date_):
        """add old price to df"""
        old_price = []
        # step into df filtered by date
        for ind, row in filtered.iterrows():
            # find all product with same name, location in nonfiltered df
            new_raw = raw[(raw.name == row['name']) & (raw.location == row['location']) & (raw.date != date_)]
            if new_raw.empty:
                # if no previous -> current
                old_price.append(row['price'])
            else:
                old_price.append(new_raw['price'].values[-1])
        df = copy.copy(filtered)
        df['old_price'] = old_price
        return df

    @staticmethod
    def add_price_diff(df):
        """add % column to df"""
        percent = []
        for ind, row in df.iterrows():
            dif = row['price'] - row['old_price']
            p = f"{round(dif/row['old_price'] * 100, 1)}%"
            percent.append(p)
        df['percent'] = percent
        return df

    @staticmethod
    def change_names(df):
        """change names in df to names from external dictionaries"""
        # get dicts from excel
        dict_names =  Extract.get_dict_names()
        dict_dc = Extract.get_dict_dc()
        # df for writing
        new_df = copy.copy(df)
        codes = []
        for ind, row in df.iterrows():
            # change location
            if row['location'] in dict_dc.keys():
                new_df.loc[ind, 'location'] = dict_dc[row['location']][0]
            # change name
            if row['name'] in dict_names.keys():
                new_df.loc[ind, 'name'] = dict_names[row['name']][1]
                # add prod code to list
                codes.append(round(dict_names[row['name']][0]))
            else:
                # add plug
                codes.append('No code')
        # add new column -> codes
        new_df['code'] = codes
        return new_df

    @staticmethod
    def group_by_location(df):
        """group df by location"""
        # change columns order
        df = df[['location', 'code', 'name', 'old_price', 'price', 'percent', 'date']]
        col_names = {
            'location': 'Получатель', 
            'code': 'Шифр в Тандер-склад', 
            'name': 'Наименование товара',
            'old_price': 'Предыдущая цена',
            'price': 'Новая цена',
            'percent': '%',
            'date': 'Дата введения цен'
        }
        # rename to russian
        df.rename(columns = col_names, inplace = True)
        # grouping
        order = df.groupby('Получатель')
        # create empty frame for location header
        main = pd.DataFrame(columns=[
            'Получатель',
            'Шифр в Тандер-склад',
            'Наименование товара',
            'Предыдущая цена',
            'Новая цена',
            '%',
            'Дата введения цен'
        ])
        for name, frame in order:
            # add location name as separate df
            list_row = ['Получатель', 'АО Тандер', name] + ['------------']*4
            main.loc[len(main)] = list_row
            # remove redundant location
            frame.loc[frame['Получатель'] > 'a', 'Получатель'] = '>'
            # add df groups to main df
            main = pd.concat([main, frame], ignore_index=True)
        return main


    def transformer(self):
        report_dict = {}
        # filter init df dict by date
        self.filter_by_date()
        # change each df in df_dict
        for name, list_ in self.data.items():
            df = self.add_last_price(*list_)
            df = self.add_price_diff(df)
            df = self.change_names(df)
            df = self.group_by_location(df)
            # add each to dictionary
            report_dict.setdefault(name, df)
        # into attribute
        self.data = report_dict
        return self.data

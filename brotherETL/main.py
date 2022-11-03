from datetime import datetime
from extract import Extract
from transform import Transform
from load import Load


def is_correct_date(date):
    """date in %d.%m.%Y"""
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


def main():
    # variables
    COMPANY = 'Тандер'

    # data insert
    DATE = ''
    while not is_correct_date(DATE):
        DATE = input('Enter date in dd.mm.yyyy format: ')

    # extract first df
    df = Extract.get_init_df()

    # del excess columns
    df = Transform.drop_excess_col(df)

    # datime->date, rename columns
    df = Transform.date_column_transform(df)

    # filter columns by company name
    df = Transform.filter_company_name(df, COMPANY)

    # split df, transfrom to df dict
    df_dict = Transform.split_product(df)

    # create Transform obj
    tr = Transform(DATE, df_dict)

    # transform data_dict
    df_dict = tr.transformer()

    # create Load obj
    load = Load(DATE, df_dict)

    # change date in load template
    load.change_date()

    # create -> load reports
    load.to_xlsx()
    

if __name__ == '__main__':
    main()
from pandas.io.html import read_html
from .functions import assign_industry_codes
import random 
import pandas as pd


def scrape_data():
    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

    tables = read_html(url, attrs={'class':'wikitable sortable'})

    return tables


df = pd.read_csv('../datasets/raw_data.csv')

def preprocessing():
    df.drop(index=[0], inplace=True)
    df.reset_index(drop=True, inplace = True)
    df.rename(columns={'Rank.': 'Rank', 'Name.': 'Name', 'Industry under which the companies are': 'Industry', 'Revenue': 'Revenue(USD millions)',
                   'Profit': 'Profit(USD millions)', 'Employed members of the Company are:': 'Employees', 'Headquarters[note 1]': 'Headquarters' }, inplace=True)
    df['Revenue(USD millions)'] = df['Revenue(USD millions)'].astype(str).str.replace('$', '').str.replace(',', '')
    df['Revenue(USD millions)'] = pd.to_numeric(df['Revenue(USD millions)'], errors='coerce')
    df['Profit(USD millions)'] = df['Profit(USD millions)'].astype(str).str.replace('$', '').str.replace(',', '')
    df['Profit(USD millions)'] = pd.to_numeric(df['Revenue(USD millions)'], errors='coerce')
    df['Headquarters'] = df['Headquarters'].replace({'United States': 'United States of America'})
    clean_df = assign_industry_codes(df, 'Industry', code_column='industry_codes')
    

    return clean_df





from pandas.io.html import read_html
from .functions import assign_industry_codes
import random 
import pandas as pd


def scrape_data():
    url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_by_revenue'

    tables = read_html(url, attrs={'class':'wikitable sortable'})

    return tables


df = pd.read_csv('../datasets/raw_data.csv')


def preprocessing(data):
    data.drop(index=[0], inplace=True)
    #data.drop(['State-owned', 'Ref.'], axis=1, inplace=True)
    data.reset_index(drop=True, inplace = True)
    data.rename(columns={'Rank.': 'Rank', 'Name.': 'Name', 'Industry under which the companies are': 'Industry', 'Revenue': 'Revenue(USD millions)',
                   'Profit': 'Profit(USD millions)', 'Employed members of the Company are:': 'Employees', 'Headquarters[note 1]': 'Headquarters' }, inplace=True)
    data['Revenue(USD millions)'] = data['Revenue(USD millions)'].astype(str).str.replace('$', '').str.replace(',', '')
    data['Revenue(USD millions)'] = pd.to_numeric(data['Revenue(USD millions)'], errors='coerce')
    data['Profit(USD millions)'] = data['Profit(USD millions)'].astype(str).str.replace('$', '').str.replace(',', '')
    data['Profit(USD millions)'] = pd.to_numeric(data['Revenue(USD millions)'], errors='coerce')
    data['Headquarters'] = data['Headquarters'].replace({'United States': 'United States of America'})
    clean_df = assign_industry_codes(data, 'Industry', code_column='industry_codes')
    #print(clean_df.describe(include='all'))

    return clean_df






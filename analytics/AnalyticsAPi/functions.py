import pandas as pd
import requests 
import random
import locale

def assign_industry_codes(df, industry_column, code_column='industry_code'):
    unique_industries = df[industry_column].unique()
    #random.shuffle(unique_industries)
    codes = [f'{random.randint(3000, 5000)}' for i in range(len(unique_industries))]
    industry_code_mapping = dict(zip(unique_industries, codes))
    df[code_column] = df[industry_column].map(industry_code_mapping)

    return df

def get_country_details(country_iso_code):
    iso_api_url = f"https://restcountries.com/v2/alpha/{country_iso_code}"  
    response = requests.get(iso_api_url)
    if response.status_code == 200:
        country_details = response.json()
        country_name = country_details['name']
        return country_name
    else: 
        country_name= country_iso_code
        return country_name
    

def get_company_details(company_name, dataframe):
    company_data = dataframe[dataframe['Name'] == company_name]

    revenue = company_data['Revenue(USD millions)'].values[0]
    employees = company_data['Employees'].values[0]
    profit = company_data['Profit(USD millions)'].values[0]
    industry = company_data['Industry'].values[0]
    headquarters = company_data['Headquarters'].values[0]
    
    
    industry_total_revenue = dataframe[dataframe['Industry'] == industry]['Revenue(USD millions)'].sum()
    revenue_share = (revenue / industry_total_revenue).round(2)
    revenue_share = revenue_share*100
    
    company_details = {
        'Revenue': revenue,
        'Employees': employees,
        'Profit': profit,
        'Revenue Share%': revenue_share,
        'Headquarters': headquarters,
        'Industry': industry,
        'Chart/Graph' : 'A stacked bar chart or a grouped bar chart'

    }
    
    return company_details

def largest_revenue_industry(dataframe):
    industries_by_revenue = pd.DataFrame(dataframe.groupby('Industry')['Revenue(USD millions)'].sum().reset_index().values,
                                         columns = ['Industry', 'Revenue(USD millions)'])
    # print(industries_by_revenue)
    largest_industry_df = industries_by_revenue.sort_values('Revenue(USD millions)', ascending=False)
    # print(largest_industry_df)
    largest_industry_revenue = largest_industry_df['Revenue(USD millions)'].max()
    largest_industry = largest_industry_df[largest_industry_df['Revenue(USD millions)'] == largest_industry_revenue]['Industry'].values
    
    
    result = {
        'Largest revenue industry' : largest_industry,
        'Revenue (USD millions)': largest_industry_revenue,
        'Chart/Graph' : 'Score Card'
    }
    
    return result

def top5_companies_by_revenue(dataframe):
    companies_by_revenue = dataframe.sort_values('Revenue(USD millions)', ascending=False)
    largest_companies = companies_by_revenue[['Name', 'Revenue(USD millions)']].head(5)
    print(largest_companies)
    # largest_companies['Revenue(USD millions)'] = largest_companies['Revenue(USD millions)'].apply(lambda x: f'${x:,}')
    
    largest_companies_by_revenue = {
        'Largest revenue companies' : largest_companies.to_dict(orient='records'),
        'Chart/Graph' : 'Horizontal Bar Chart'
    }
    
    return largest_companies_by_revenue

def top5_companies_by_employees(dataframe):
    companies_by_employees = dataframe.sort_values('Employees', ascending=False)
    largest_companies = companies_by_employees[['Name', 'Employees']].head(5)
    
    largest_companies_by_employees = {
        'Largest employee companies' : largest_companies.to_dict(orient='records'),
        'Chart/Graph' : 'Horizontal Bar Chart'
    }
    
    return largest_companies_by_employees

def revenue_share_by_industry(dataframe):
    dataframe.sort_values(by='Industry')
    industry_revenue = dataframe.groupby('Industry')['Revenue(USD millions)'].sum()
    total_revenue = industry_revenue.sum()
    revenue_share_by_industry = (industry_revenue/total_revenue) * 100
    revenue_share_by_industry = revenue_share_by_industry.round(2)

    
    revenue_share = pd.DataFrame({
        'Industry': industry_revenue.index,
        'Revenue share %': revenue_share_by_industry.values,
    })

    revenue_share['Industry ; Revenue Share'] = revenue_share['Industry'] + ' ; ' + revenue_share['Revenue share %'].astype(str) + '%'
    graph_type = 'Graph/chart : Stacked Bar Chart'
    
    return revenue_share['Industry ; Revenue Share'], graph_type

def top5_companies_by_employee_effeciency(dataframe):
    dataframe['Employee Efficiency'] = dataframe['Revenue(USD millions)'] / dataframe['Employees'].astype(float)
    employee_effeciency = dataframe.sort_values('Employee Efficiency', ascending=False)
    top_5_companies = employee_effeciency.head(5)[['Name', 'Employee Efficiency']]
    top_5_companies['Employee Efficiency'] = top_5_companies['Employee Efficiency'].apply(lambda x: f'{x:.2f}')
    
    companies_by_employee_effeciency = {
        'Top 5 companies by employee effeciency' : top_5_companies.to_dict(orient='records'),
        'Chart/Graph' : 'Horizontal Bar Chart'
    }
    
    return  companies_by_employee_effeciency

def companies_revenue_share(company_name, dataframe):
    industry_revenue = dataframe.groupby('Industry')['Revenue(USD millions)'].transform('sum')
    dataframe['Revenue Share%'] = (dataframe['Revenue(USD millions)'] / industry_revenue) * 100
    dataframe['Revenue Share%'] = dataframe['Revenue Share%'].round(2)

    company_info = dataframe[dataframe['Name'] == company_name]

    industry = company_info['Industry'].iloc[0]
    revenue_share = company_info['Revenue Share%'].iloc[0]

    result = {
        'Company': company_name,
        'Industry': industry,
        'Revenue Share%': revenue_share
    }

    return result

def industry_stats(dataframe):
    industry_revenue = dataframe.groupby('Industry')['Revenue(USD millions)'].sum()
    total_revenue = dataframe['Revenue(USD millions)'].sum()
    revenue_share = (industry_revenue / total_revenue)
    industry_stats = dataframe.groupby('Industry')['Revenue(USD millions)'].agg(['min', 'mean', 'max', 'sum'])
    industry_stats['Revenue Share'] = revenue_share * 100
    industry_stats['Revenue Share'] = industry_stats['Revenue Share'].round(2)
    formatted_stats = pd.DataFrame({
        'Min Revenue': industry_stats['min'],
        'Mean Revenue': industry_stats['mean'],
        'Max Revenue': industry_stats['max'],
        'Total Revenue': industry_stats['sum'],
        'Revenue Share': industry_stats['Revenue Share']
    })

    formatted_stats = formatted_stats.sort_values(by='Revenue Share', ascending=False)
    industry_statistics = {}

    for index, row in formatted_stats.iterrows():
        industry_stat = {
            'Mean': row['Mean Revenue'],
            'Max': row['Max Revenue'],
            'Min': row['Min Revenue'],
            'Total': row['Total Revenue'],
            'Revenue Share': row['Revenue Share']
        }
        industry_statistics[index] = industry_stat

    graph_type = 'Graph/chart : Grouped bar chart'
    return industry_statistics, graph_type




def best_performing_companies(dataframe):
    sorted_dataframe = dataframe.sort_values('Revenue(USD millions)', ascending=False)
    top_companies = sorted_dataframe.groupby('Industry').first()
    top_company_info = []

    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    for industry, row in top_companies.iterrows():
        revenue = locale.currency(row['Revenue(USD millions)'] * 1_000_000, grouping=True)
        company_info = {
            'Industry': industry,
            'Company': row['Name'],
            'Revenue': revenue 
        }
        top_company_info.append(company_info)
    
    return top_company_info


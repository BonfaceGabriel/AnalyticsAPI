import pandas as pd
import requests 
import random

def assign_industry_codes(df, industry_column, code_column='industry_code'):
    unique_industries = df[industry_column].unique()
    #random.shuffle(unique_industries)
    codes = [f'{random.randint(3000, 5000)}' for i in range(len(unique_industries))]
    industry_code_mapping = dict(zip(unique_industries, codes))
    df[code_column] = df[industry_column].map(industry_code_mapping)

    return df

def get_country_details(dataframe, country_iso_code):
    iso_api_url = f"https://restcountries.com/v2/alpha/{country_iso_code}"  
    response = requests.get(iso_api_url)
    if response.status_code == 200:
        country_details = response.json()
        country_name = country_details['name']

        filtered_df = dataframe[dataframe['Headquarters'] == country_name]
        filtered_df['Employees'] = filtered_df['Employees'].astype(int)
        top_3_companies = filtered_df.nlargest(3, 'Revenue(USD millions)')['Name'].tolist()
        total_revenue = filtered_df['Revenue(USD millions)'].sum()
        total_employees = filtered_df['Employees'].sum()

        return {
            'name': country_details['name'],
            'top_3_companies': top_3_companies,
            'total_revenue': total_revenue,
            'total_employees': total_employees,
            'graph': 'two separate bar charts, one for revenue and one for employees, with the country names on the x-axis and the respective values on the y-axis.'
        }
    else:
        return {}

def get_company_details(company_name, dataframe):
    company_data = dataframe[dataframe['Name'] == company_name]
    
    if company_data.empty:
        return {}  
    
    revenue = company_data['Revenue(USD millions)'].values[0]
    employees = company_data['Employees'].values[0]
    profit = company_data['Profit(USD millions)'].values[0]
    industry = company_data['Industry'].values[0]
    headquarters = company_data['Headquarters'].values[0]
    
    
    industry_total_revenue = dataframe[dataframe['Industry'] == industry]['Revenue(USD millions)'].sum()
    revenue_share = revenue / industry_total_revenue
    
    company_details = {
        'Revenue': revenue,
        'Employees': employees,
        'Profit': profit,
        'Revenue Share': revenue_share,
        'Headquarters': headquarters,
        'Industry': industry,
        'Chart/Graph' : 'A stacked bar chart or a grouped bar chart'

    }
    
    return company_details

def largest_revenue_industry(dataframe):
    industries_by_revenue = dataframe.groupby('Industry')['Revenue(USD millions)'].sum()
    largest_industry = industries_by_revenue.idxmax()
    
    largest_industry_by_revenue = {
        'Largest revenue industry' : largest_industry,
        'Chart/Graph' : 'Pie Chart'
    }
    
    return largest_industry_by_revenue

def top5_companies_by_revenue(dataframe):
    companies_by_revenue = dataframe.sort_values('Revenue(USD millions)', ascending=False)
    largest_companies = companies_by_revenue['Name'].head(5).tolist()
    
    largest_companies_by_revenue = {
        'Largest revenue companies' : largest_companies,
        'Chart/Graph' : 'Horizontal Bar Chart'
    }
    
    return largest_companies_by_revenue

def top5_companies_by_employees(dataframe):
    companies_by_employees = dataframe.sort_values('Employees', ascending=False)
    largest_companies = companies_by_employees['Name'].head(5).tolist()
    
    largest_companies_by_employees = {
        'Largest employee companies' : largest_companies,
        'Chart/Graph' : 'Horizontal Bar Chart'
    }
    
    return largest_companies_by_employees

def revenue_share_by_industry(dataframe):
    industry_revenue = dataframe.groupby('Industry')['Revenue(USD millions)'].sum()
    total_revenue = industry_revenue.sum()
    revenue_share_by_industry = industry_revenue/total_revenue

    
    revenue_share = pd.DataFrame({
        'Industry': industry_revenue.index,
        'Revenue share': revenue_share_by_industry.values,
    })

    revenue_share['Industry ; Revenue Share'] = revenue_share['Industry'] + ' ; ' + revenue_share['Revenue share'].astype(str)
    graph_type = 'Graph/chart : Stacked Bar Chart'
    
    return revenue_share['Industry ; Revenue Share'], graph_type

def top5_companies_by_employee_effeciency(dataframe):
    dataframe['Employee Efficiency'] = dataframe['Revenue(USD millions)'] / dataframe['Employees'].astype(float)
    employee_effeciency = dataframe.sort_values('Employee Efficiency', ascending=False)
    top_5_companies = employee_effeciency.head(5)['Name'].tolist()
    
    companies_by_employee_effeciency = {
        'Top 5 companies by employee effeciency' : top_5_companies,
        'Chart/Graph' : 'Horizontal Bar Chart'
    }
    
    return  companies_by_employee_effeciency

def companies_revenue_share(dataframe):
    industry_revenue = dataframe.groupby('Industry')['Revenue(USD millions)'].sum()
    total_revenue = industry_revenue.sum()
    dataframe['Revenue Share'] = dataframe['Revenue(USD millions)'] / total_revenue
    revenue_share_df = dataframe[['Name', 'Revenue Share']]
    sorted_data = revenue_share_df.values.tolist()
 
    companies_revenue_share= {
        'Revenue share by company' : sorted_data,
        'Chart/Graph' : 'Stacked Bar Chart'
    }
    
    return  companies_revenue_share

def industry_stats(dataframe):

    industry_revenue = dataframe.groupby('Industry')['Revenue(USD millions)'].sum()
    total_revenue = industry_revenue.sum()
    revenue_share = industry_revenue / total_revenue
    industry_stats = dataframe.groupby('Industry')['Revenue(USD millions)'].agg(['min', 'mean', 'max', 'sum'])
    industry_stats['Revenue Share'] = revenue_share
    formatted_stats = pd.DataFrame({
        'Min Revenue': industry_stats['min'],
        'Mean Revenue': industry_stats['mean'],
        'Max Revenue': industry_stats['max'],
        'Total Revenue': industry_stats['sum'],
        'Revenue Share': industry_stats['Revenue Share']
    })

    formatted_stats = formatted_stats.sort_values(by='Revenue Share', ascending=False)
    formatted_stats['Industry Statistics'] = formatted_stats.apply(
        lambda row: f"{row.name}: Min={row['Min Revenue']}, Mean={row['Mean Revenue']}, Max={row['Max Revenue']}, Total={row['Total Revenue']}, Share={row['Revenue Share']}",
        axis=1)
    graph_type = 'Graph/chart : Grouped bar chart'

    return formatted_stats['Industry Statistics'], graph_type


def best_performing_companies(dataframe):
    top_companies = dataframe.groupby('Industry').apply(lambda x: x.nlargest(1, 'Revenue(USD millions)'))
    top_company_names = top_companies['Name'].tolist()
    
    return top_company_names 


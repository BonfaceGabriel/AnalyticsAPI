# Django Company Analytics API
This Django project provides an API that allows users to retrieve information about companies in the US. <br>
The API supports various endpoints to answer statistical questions related to company profiles, industry statistics, and more.<br>
You can also check out the general overview of the data, statistical visualizations, as well as key insights on the demo app.

## Installation
To run the Django Company Analytics API, follow these steps:

Clone the repository: 
```bash
git clone <repository-url>
```

Navigate to the project directory: 
```bash
cd AnalyticsAPI
```
Create a virtual environment: 
```bash
python3 -m venv env
```
Activate the virtual environment:
On Windows: 
```bash
env\Scripts\activate
```
On macOS/Linux:
```bash
source env/bin/activate
```
Install the dependencies:
```bash
pip install -r requirements.txt
```
Set up the database: 
```bash
python3 manage.py migrate
```
Start the development server:
```bash
python3 manage.py runserver
```
## Dashboard App
Demo app: [*Company Data Analysis Dashboard*](https://company-dashboard.streamlit.app/)

## API Endpoints
The API provides the following endpoints:

1. Get Country Profile
    Endpoint: /api/country/

    Request Method: POST

    Parameters:

    iso_code: The ISO code of the country (e.g., USA for the United States).
    Response:

    If the country is found, the response will include the following information:
    name: The name of the country.
    top_companies: A list of the top three companies headquartered in the country.
    total_revenue: The total revenue for all companies in the country.
    total_employees: The total number of employees for all companies in the country.
    If the country is not found, an empty response will be returned.

2. Get Company Profile
    Endpoint: /api/company/

    Request Method: POST

    Parameters:

    company_name: The name of the company.
    Response:

    If the company is found, the response will include the following information:
    revenue: The revenue of the company.
    employees: The number of employees in the company.
    profit: The profit of the company.
    revenue share%: The revenue share of the company in its industry.
    headquarter: The country where the company is headquartered
    industry: The industry to which the company belongs.
    chart/graph: chart to best represent the information
    If the company is not found, an empty response will be returned.
  
3. Get Largest Industry by Revenue
    Endpoint: /api/revenue-industry/

    Request Method: GET

    Response:

    The response will include the name of the largest industry by revenue.
  
4. Get Top 5 Companies by Revenue
    Endpoint: /api/top-five-companies/

    Request Method: GET

    Response:

    The response will include a list of the top five companies ranked by revenue.
  
5. Get Top 5 Companies by Number of Employees
    Endpoint: /api/top-five-by-employees/

    Request Method: GET

    Response:

    The response will include a list of the top five companies ranked by the number of employees.
  
6. Get Revenue Share by Industry
    Endpoint: /api/revenue-share/

    Request Method: GET

    Response:

    The response will include the revenue share of each industry calculated as the revenue of the industry divided by the total revenue of all listed companies in that industry.

7. Get Top 5 Companies with Highest Employee Efficiency
    Endpoint: /api/top-five-by-efficiency/

    Request Method: GET

    Response:

    The response will include a list of the top five companies ranked by employee efficiency, calculated as the total revenue divided by the number of employees.
  
8. Get Revenue Share per Company by Industry
    Endpoint: /api/company-revenue/

    Request Method: POST

    Parameters:

    company_name: The name of the company.
    Response:

    The response will include the revenue share of the company within its industry.
  
9. Get Industry Revenue Statistics
    Endpoint: /api/industry-summary/

    Request Method: GET

    Response:

    The response will include the minimum, average, maximum, and total revenue, as well as the revenue share for each industry.
  
10. Get Best Performing Companies by Industry
    Endpoint: /api/company-rank/

    Request Method: GET

    Response:

    The response will include the best performing companies in each industry based on revenue.

  
## Conclusion
This Django Company Profile API provides a comprehensive set of endpoints to retrieve information about countries, companies, and industry profiles. With these endpoints, users can gather insights into company statistics, industry revenue, top-performing companies, and more.

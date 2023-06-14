import pandas as pd
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from .functions import get_country_details, get_company_details, largest_revenue_industry, top5_companies_by_revenue, top5_companies_by_employees, top5_companies_by_employee_effeciency,best_performing_companies, companies_revenue_share, industry_stats, revenue_share_by_industry
from .preprocessing import preprocessing


df = pd.read_csv('../datasets/raw_data.csv')
# clean_data = pd.read_csv('../datasets/clean_data.csv')


class CountryViewSets(viewsets.ViewSet):
      def get_country_profile(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'POST':
                        country_iso_code = request.data['iso_code']
                        data = preprocessing(df_copy)
                        country_name = get_country_details(country_iso_code)
                        if country_name not in data['Headquarters'].unique():
                              return Response({"status": status.HTTP_204_NO_CONTENT, "message": f"No record found for the iso code {country_iso_code}", "payload":None})
                        else:
                              filtered_df = data[data['Headquarters'] == country_name]
                              filtered_df['Employees'] = filtered_df['Employees'].astype(int)
                              top_3_companies = filtered_df.nlargest(3, 'Revenue(USD millions)')['Name'].tolist()
                              total_revenue = filtered_df['Revenue(USD millions)'].sum()
                              total_employees = filtered_df['Employees'].sum()

                              result = {
                                    'name': country_name,
                                    'top_3_companies': top_3_companies,
                                    'total_revenue': total_revenue,
                                    'total_employees': total_employees,
                                    'graph': 'two separate bar charts, one for revenue and one for employees, with the country names on the x-axis and the respective values on the y-axis.'
                              }
                  
                              return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
      
      
      def get_company_profile(self, request):
            df_copy = df.copy()
            try: 
                  if request.method == 'POST':
                        company_name = request.data['company_name']
                        data = preprocessing(df_copy)
                        if company_name not in data['Name'].unique():
                              return Response({"status": status.HTTP_204_NO_CONTENT, "message": f"No record found for the company {company_name}", "payload":None})
                        else:
                              result = get_company_details(company_name, data)
                              return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
      
      def get_largest_revenue_industry(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'GET':
                        data = preprocessing(df_copy)
                        # print(data['Revenue(USD millions)'].max())
                        result = largest_revenue_industry(data)
                  return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
      
      def get_top5_companies_by_revenue(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'GET':
                        data = preprocessing(df_copy)
                        result = top5_companies_by_revenue(data)
                  return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
      
      def get_top5_companies_by_employees(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'GET':
                        data = preprocessing(df_copy)
                        result = top5_companies_by_employees(data)
                  return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
            
      def get_revenue_share_by_industry(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'GET':
                        data = preprocessing(df_copy)
                        result = revenue_share_by_industry(data)
                        return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
      
      def get_top5_companies_by_employee_effeciency(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'GET':
                        data = preprocessing(df_copy)
                        result = top5_companies_by_employee_effeciency(data)
                  return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})

      def get_companies_revenue_share(self, request):
            df_copy = df.copy()
            try :
                  if request.method == 'POST':
                        company_name = request.data['company_name']
                        data = preprocessing (df_copy)
                        print(data["Name"].unique())
                        if company_name not in data['Name'].unique():
                              return Response({"status": status.HTTP_204_NO_CONTENT, "message": f"No record found for the company {company_name}", "payload":None})
                        else:
                              result = companies_revenue_share(company_name, data)
                              return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
      
            

      def get_industry_stats(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'GET':
                        data = preprocessing(df_copy)
                        result = industry_stats(data)
                  return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
                 
      def get_best_performing_companies(self, request):
            df_copy = df.copy()
            try:
                  if request.method == 'GET':
                        data = preprocessing(df_copy)
                        result = best_performing_companies(data)
                  return Response({"status": status.HTTP_200_OK, "message": "Succesfull", "payload":result})
            except Exception as e:
                  print(e)
                  return Response({"status": status.HTTP_501_NOT_IMPLEMENTED, 
                                   "message": "Error occured during implementation",
                                   "payload": None})
            

            
      
            
import pandas as pd
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from .functions import get_country_details, get_company_details, largest_revenue_industry, top5_companies_by_revenue, top5_companies_by_employees, top5_companies_by_employee_effeciency,best_performing_companies, companies_revenue_share, industry_stats, revenue_share_by_industry
from .preprocessing import preprocessing




class CountryViewSets(viewsets.ViewSet):
      def get_country_profile(self, request):
            if request.method == 'POST':
                  country_iso_code = request.data['iso_code']
                  data = preprocessing()
                  result = get_country_details(data, country_iso_code)
            return Response(result)
      
      
      def get_company_profile(self, request):
            if request.method == 'POST':
                  company_name = request.data['company_name']
                  data = preprocessing()
                  result = get_company_details(company_name, data)
            return Response(result)
      
      def get_largest_revenue_industry(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = largest_revenue_industry(data)
            return Response(result)
      
      def get_top5_companies_by_revenue(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = top5_companies_by_revenue(data)
            return Response(result)
      
      def get_top5_companies_by_employees(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = top5_companies_by_employees(data)
            return Response(result)
      
      def get_revenue_share_by_industry(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = revenue_share_by_industry(data)
            return Response(result)
      
      def get_top5_companies_by_employee_effeciency(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = top5_companies_by_employee_effeciency(data)
            return Response(result)
            

      def get_companies_revenue_share(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = companies_revenue_share(data)
            return Response(result)
            

      def get_industry_stats(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = industry_stats(data)
            return Response(result)
            
      def get_best_performing_companies(self, request):
            if request.method == 'POST':
                  data = preprocessing()
                  result = best_performing_companies(data)
            return Response(result)
            

            
      
            
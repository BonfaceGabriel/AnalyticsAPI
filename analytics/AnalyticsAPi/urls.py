from django.urls import path
from .views import CountryViewSets


urlpatterns = [
    path('country/', CountryViewSets.as_view({'post': 'get_country_profile'}), name='country'),
    path('company/', CountryViewSets.as_view({'post': 'get_company_profile'}), name='company_name'),
    path('revenue-industry/', CountryViewSets.as_view({'get': 'get_largest_revenue_industry'}), name='revenue-industry'),
    path('top-five-companies/', CountryViewSets.as_view({'get': 'get_top5_companies_by_revenue'}), name='companies-by-revenue' ),
    path('top-five-by-employees/', CountryViewSets.as_view({'get': 'get_top5_companies_by_employees'}), name='companies-by-employees'),
    path('top-five-by-effeciency/', CountryViewSets.as_view({'get': 'get_top5_companies_by_employee_effeciency'}), name='companies-by-employee-effeciency'),
    path('revenue-share/', CountryViewSets.as_view({'get': 'get_revenue_share_by_industry'}), name='revenue-share-by-industry'),
    path('company-rank/', CountryViewSets.as_view({'get': 'get_best_performing_companies'}), name='company-rank-by-industry'),
    path('company-revenue/', CountryViewSets.as_view({'post': 'get_companies_revenue_share'}), name='company-revenue-share'),
    path('industry-summary/', CountryViewSets.as_view({'get': 'get_industry_stats'}), name='industry-statistics')
 
]


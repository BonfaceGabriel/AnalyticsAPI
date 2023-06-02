from django.urls import path
from .views import CountryViewSets


urlpatterns = [
    path('country/', CountryViewSets.as_view({'post': 'get_country_profile'}), name='country'),
    path('company/', CountryViewSets.as_view({'post': 'get_company_profile'}), name='company_name'),
    path('revenue-industry/', CountryViewSets.as_view({'post': 'get_largest_revenue_industry'})),
    path('top5-companies/', CountryViewSets.as_view({'post': 'get_top5_companies_by_revenue'})),
    path('top5-by-employees/', CountryViewSets.as_view({'post': 'get_top5_companies_by_employees'})),
    path('top5-by-effeciency/', CountryViewSets.as_view({'post': 'get_top5_companies_by_employee_effeciency'})),
    path('revenue-share/', CountryViewSets.as_view({'post': 'get_revenue_share_by_industry'})),
    path('company-rank/', CountryViewSets.as_view({'post': 'get_best_performing_companies'})),
    path('company-revenue/', CountryViewSets.as_view({'post': 'get_companies_revenue_share'})),
    path('industry-stats/', CountryViewSets.as_view({'post': 'get_industry_stats'}))
 
]


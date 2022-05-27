from django.urls import path
from analysis_service.views.compare_games import CompareGamesChartData, CompareGamesView , compareGamesInAPeriodOfTime
from analysis_service.views.compare_sale_by_year import CompareSaleByYearChartData, CompareSaleByYearView
from analysis_service.views.compare_publisher_by_year import ComparePublisherByYearChartData, ComparePublisherByYearView
from analysis_service.views.compare_genre_by_year import CompareGenreByYearChartData, CompareGenreByYearView

urlpatterns = [
    path('compare_game/chart/<str:name1>/<str:name2>/', CompareGamesView.as_view(), name='compare_two_game'),
    path('compare_game/<str:name1>/<str:name2>/', CompareGamesChartData.as_view()),
    #option : 1. category 2.sale
    path('compare_game/<int:start_year>/<int:end_year>/<str:option>/', compareGamesInAPeriodOfTime.as_view()),
    path('compare_sale_by_year/chart/<int:start_year>/<int:end_year>/', CompareSaleByYearView.as_view(), name='compare_sale_by_year'),
    path('compare_sale_by_year/<int:start_year>/<int:end_year>/', CompareSaleByYearChartData.as_view()),
    path('compare_publisher_by_year/chart/<str:publisher1>/<str:publisher2>/<int:start_year>/<int:end_year>/', ComparePublisherByYearView.as_view(), name='compare_publisher_by_year'),
    path('compare_publisher_by_year/<str:publisher1>/<str:publisher2>/<int:start_year>/<int:end_year>/', ComparePublisherByYearChartData.as_view()),
    path('compare_genre_by_year/chart/<int:start_year>/<int:end_year>/', CompareGenreByYearView.as_view(), name='compare_genre_by_year'),
    path('compare_genre_by_year/<int:start_year>/<int:end_year>/', CompareGenreByYearChartData.as_view()),
]
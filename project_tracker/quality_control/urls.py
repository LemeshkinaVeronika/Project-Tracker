#Function-Based Views
# from django.urls import path
# from quality_control import views

# app_name = 'quality_control'

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('bugreports/', views.bugreports_list, name='bugreports_list'),
#     path('bugreports/<int:bug_id>/', views.bug_detail, name='bug_detail'),
#     path('featurerequests/', views.featurerequests_list, name='featurerequests_list'),
#     path('featurerequests/<int:feature_id>/', views.feature_detail, name='feature_detail'),
#     path('add_bug_report/', views.add_bug_report, name='add_bug_report'),
#     path('add_feature_request/', views.add_feature_request, name='add_feature_request'),
#     path('bugreports/<int:bug_id>/update/', views.bugreport_update, name='bugreport_update'),
#     path('bugreports/<int:bugreport_id>/delete/', views.bugreport_delete, name='bugreport_delete'),
#     path('featurerequests/<int:feature_id>/update/', views.featurerequest_update, name='featurerequest_update'),
#     path('featurerequests/<int:pk_id>/delete/', views.featurerequest_delete, name='featurerequest_delete'),
# ]

# #Class-Based Views

from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugreports/', views.BugReportsListView.as_view(), name='bugreports_list'),
    path('featurerequests/', views.FeatureRequestsListView.as_view(), name='featurerequests_list'),
    path('bugreports/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('featurerequests/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('featurerequests/create/', views.AddFeatureRequestView.as_view(), name='add_feature_request'),
    path('bugreports/create/', views.AddBugReportView.as_view(), name='add_bug_report'),
    path('bugreports/<int:bug_id>/update/', views.BugReportUpdateView.as_view(), name='bugreport_update'),
    path('bugreports/<int:pk_id>/delete/', views.BugReportDeleteView.as_view(), name='bugreport_delete'),
    path('featurerequests/<int:feature_id>/update/', views.FeatureRequestUpdateView.as_view(), name='featurerequest_update'),
    path('featurerequests/<int:pk_id>/delete/', views.FeatureRequestDeleteView.as_view(), name='featurerequest_delete'),
   ]
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy


# Create your views here.
#Function-Based Views
from django.urls import reverse
from .models import BugReport, FeatureRequest
from .forms import BugReportForm, FeatureRequestForm


# def index(request):
#     return render(request, 'quality_control/index.html')

# def bugreports_list(request):
#     bugreports = BugReport.objects.all()
#     return render(request, 'quality_control/bugreports_list.html', {'bugreports': bugreports})

# def featurerequests_list(request):
#     featurerequests = FeatureRequest.objects.all()
#     return render(request, 'quality_control/featurerequests_list.html', {'featurerequests': featurerequests})

# def bug_detail(request, bug_id):
#     bug = get_object_or_404(BugReport, pk=bug_id)
#     return render(request, 'quality_control/bug_detail.html', {'bug': bug})
# def feature_detail(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, pk=feature_id)
#     return render(request, 'quality_control/feature_detail.html', {'feature': feature})

# def add_bug_report(request):
#     if request.method == 'POST':
#         form = BugReportForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/quality_control')  
#     else:
#         form = BugReportForm()
#     return render(request, 'quality_control/bug_report_form.html', {'form': form})

# def add_feature_request(request):
#     if request.method == 'POST':
#         form = FeatureRequestForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/quality_control')
#     else:
#         form = FeatureRequestForm()
#     return render(request, 'quality_control/feature_request_form.html', {'form': form})

# def bugreport_update(request, bug_id):
#     bug_report = get_object_or_404(BugReport, pk=bug_id)
#     if request.method == 'POST':
#         form = BugReportForm(request.POST, instance=bug_report)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:bug_detail', bug_id=bug_id)
#     else:
#         form = BugReportForm(instance=bug_report)
#     return render(request, 'quality_control/bug_report_form.html', {'form': form})

# def featurerequest_update(request, feature_id):
#     feature_request = get_object_or_404(FeatureRequest, pk=feature_id)
#     if request.method == 'POST':
#         form = FeatureRequestForm(request.POST, instance=feature_request)
#         if form.is_valid():
#             form.save()
#             return redirect('quality_control:feature_detail', feature_id=feature_id)
#     else:
#         form = FeatureRequestForm(instance=feature_request)
#     return render(request, 'quality_control/feature_request_form.html', {'form': form})

# def bugreport_delete(request, bugreport_id):
#     bug_report = get_object_or_404(BugReport, pk=bugreport_id)
#     bug_report.delete()
#     return redirect('quality_control:bugreports_list')


# def featurerequest_delete(request, pk_id):
#     feature_request = get_object_or_404(FeatureRequest, pk=pk_id)
#     feature_request.delete()
#     return redirect('quality_control:featurerequests_list')



#Class-Based Views
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import BugReport, FeatureRequest
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

class IndexView(ListView):
    template_name = 'quality_control/index.html'
    context_object_name = 'home'

    def get_queryset(self):
        """Return the last five published questions."""
        return None  

class BugReportsListView(ListView):
    model = BugReport
    template_name = 'quality_control/bugreports_list.html'
    context_object_name = 'bugreports'

class FeatureRequestsListView(ListView):
    model = FeatureRequest
    template_name = 'quality_control/featurerequests_list.html'
    context_object_name = 'featurerequests'

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    context_object_name = 'bug'
    template_name = 'quality_control/bug_detail.html'

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    context_object_name = 'feature'
    template_name = 'quality_control/feature_detail.html'

class AddBugReportView(CreateView):
    model = BugReport
    template_name = 'quality_control/bug_report_form.html'
    fields = '__all__'
    success_url = reverse_lazy('quality_control:index')

class AddFeatureRequestView(CreateView):
    model = FeatureRequest
    template_name = 'quality_control/feature_request_form.html'
    fields = '__all__'
    success_url = reverse_lazy('quality_control:index')

class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bugreport_update.html'
    pk_url_kwarg = 'bug_id'  
    success_url = reverse_lazy('quality_control:index')
    def get_success_url(self):
        return reverse_lazy('quality_control:bug_detail',
                            kwargs={'bug_id': self.object.project.id, 'bug_id': self.object.id})

class FeatureRequestUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/featurerequest_update.html'
    pk_url_kwarg = 'feature_id'  
    success_url = reverse_lazy('quality_control:index')
    def get_success_url(self):
        return reverse_lazy('quality_control:feature_detail',
                            kwargs={'feature_id': self.object.project.id, 'feature_id': self.object.id})

class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'pk_id'
    def get_success_url(self):
        return reverse_lazy('quality_control:bugreports_list')

class FeatureRequestDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'pk_id'
    def get_success_url(self):
        return reverse_lazy('quality_control:featurerequests_list')
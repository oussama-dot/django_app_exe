from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import JobPosting
# Create your views here.
def main(request):
    active_jobs = JobPosting.objects.filter(is_active = True)
    context = {
        'active_jobs' : active_jobs
    }
   
    return HttpResponse( render(request,"job_board/jobs_post.html",context)) 
def details(request , pk):
    job_posting  = get_object_or_404(JobPosting, pk = pk )
    
    context = {
        'job_posting' : job_posting
    }
    return render(request,"job_board/details.html",context)
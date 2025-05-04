from django.shortcuts import get_object_or_404, redirect, render
from .forms import FeedbackForm
from .models import Feedback

# Create your views here.

def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedbacks') 
    else:
        form = FeedbackForm()
    return render(request, 'feedbacks/add_feedback.html', {'form': form})


def feedbacks(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedbacks/feedbacks.html', {'feedbacks': feedbacks})

def feedback_detail(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    return render(request, 'feedbacks/feedback_details.html', {'feedback': feedback})

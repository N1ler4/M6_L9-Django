from .models import Feedback

def recent_feedbacks(request):
    return {
        'recent_feedbacks': Feedback.objects.order_by('-date_submitted')[:5]
    }

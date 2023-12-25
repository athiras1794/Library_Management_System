from celery import shared_task
from .models import BookRequest, ProblemReport
from django.core.mail import send_mail
from decimal import Decimal
from datetime import datetime, date
from django.utils import timezone
from django.shortcuts import render




@shared_task
def check_overdue_books(request):
    # Get the current date and time
    current_date = timezone.now().date()

    # Identify overdue books
    overdue_books = BookRequest.objects.filter(due_date__lt=current_date, status='Borrowed')

    notifications = []

    for book_request in overdue_books:
        # Calculate fine amount (customize this logic based on your requirements)
        fine_amount = calculate_fine1(book_request.due_date, current_date)

        # Create a ProblemReport instance for the overdue book
        problem_report = ProblemReport(
            user=book_request.user,
            issued_book=book_request,
            problem_type='Overdue',
            problem_description='The book is overdue',
            fine_amount=fine_amount
        )
        problem_report.save()

        # Create a notification message with username and book name
        notification_message = f"{book_request.user.username} and {book_request.book.book_name}, book is overdue, please return it on time to avoid a penalty"
        notifications.append(notification_message)

  

    return render(request, 'adminhome.html', {'overdue_books': overdue_books, 'notifications': notifications})

def send_user_notification(problem_report):
    # Send an email notification to the user
    # You can customize the email content and template
    send_mail(
        'Overdue Book Notification',
        f'The book you borrowed is overdue. Please return it.',
        
        [problem_report.user.email],
        fail_silently=False,
    )
def calculate_fine1(due_date, current_date):
    # Convert date strings to date objects if needed
    due_date = date.fromisoformat(due_date)
    current_date = date.fromisoformat(current_date)

    # Calculate the number of days overdue
    days_overdue = (current_date - due_date).days

    # Check if the book is overdue
    if days_overdue > 0:
        overdue_charge_per_day = Decimal('1.00')  # Customize this value as needed
        fine_amount = days_overdue * overdue_charge_per_day
        return fine_amount
    else:
        return Decimal('0.00')
    
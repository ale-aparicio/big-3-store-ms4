from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm, ContactForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

def contact(request):
    """ A view to return the contact page """

    contact_email_sent = False
    if request.method == 'POST':
        # Instantiate COntactForm from POST data
        contact_form = ContactForm(
            request.POST)
        # Check if form is valid
        if contact_form.is_valid():
            # Get email, subject and message from cleaned form data
            email = (contact_form.cleaned_data['from_email'])
            subject = (contact_form.cleaned_data['subject'])
            contact_message = (contact_form.cleaned_data['message'])
            # Instantiate EmailMessage object from cleaned form data
            email = EmailMessage(
                subject,
                contact_message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                reply_to=[email],
            )
            # Try to send email
            try:
                email.send(fail_silently=False)
                # Success message
                messages.success(
                    request, "Contact email sent successfully.",
                    extra_tags='admin')
                contact_email_sent = True
            except SMTPException as smtp_error:
                errstr = 'Error sending contact email, ' + smtp_error
                # Error message
                messages.error(request, errstr, extra_tags='admin')

    if contact_email_sent:
        # Redirect to all products
        return redirect(reverse('products'))
    # If user is authenticated
    if request.user.is_authenticated:
        # Get User object
        userobj = User.objects.get(username=request.user)
        # Instantiate ContactForm with email address populated from User object
        contact_form = ContactForm(initial={'from_email': userobj.email})
    else:
        # Instantiate blank ContactForm
        contact_form = ContactForm

    # Set template
    template = 'profiles/contact.html'
    # Set context
    context = {
        'contact_form': contact_form,
    }
    # Render contact page
    return render(request, template, context)




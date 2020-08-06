from django.shortcuts import render


from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response



from api.serializers import ContactSerializer
from api.models import ContactForm

from django.core.mail import send_mail

# Create your views here.
@api_view(['GET'])
def apiOverview(request):

  api_urls = {
    'Create': '/contact-form/',
    'View': '/contact-see/',
  }

  return Response(api_urls)

@api_view(['GET'])
def messageList(request):
  msgs = ContactForm.objects.all().order_by('-date_created')
  serializer = ContactSerializer(msgs, many=True)
  return Response(serializer.data)


@api_view(['POST'])
def contactformCreate(request):
  serializer = ContactSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    #Please uncomment the following lines if you want to get e-mail triggered when you get a message
    # send_mail(
    #   'Portfolio Contact Form Message',
    #   'Please check your contact form',
    #   'rajkumar.nits@gmail.com',
    #   ['rajkumar.nits@gmail.com'],
    #   fail_silently = False,

    # )
  return Response(serializer.data)


def index(request):
  return render(request, 'contactform.html')
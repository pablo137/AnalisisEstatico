from venv import logger
from django.shortcuts import render, redirect
from django.urls import reverse
from store.forms.perfilForms import ContactoForms, ContactoMensajeForms
from django.core.mail import EmailMessage
from django.contrib import messages
from twilio.rest import Client

def contacto(request):
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactoForms()
    
    if request.method == 'POST':
        # Estoy enviando el formulario
        contact_form = ContactoForms(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('nombre', '')
            email = request.POST.get('correo', '')
            message = request.POST.get('mensaje', '')

            # Enviar el correo electrónico
            email = EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ['523a1a06ac16bd@inbox.mailtrap.io','dahofcmmejia@gmail.com'],
                reply_to=[email],
            )
            
            try:
                email.send()
                # Está todo OK
                return redirect(reverse('contacto')+'?ok')
            except Exception as e:
                # Ha habido un error y retorno a ERROR
                logger.error("Error al enviar correo: %s", str(e))
                return redirect(reverse('contacto')+'?error')

    return render(request, 'contacto.html', {'form':contact_form}) 

def contactanos(request):

    if request.method == 'POST':
        form = ContactoMensajeForms(request.POST, request.FILES)
        if form.is_valid():
            # account_sid = 'AC6b6ffc0469b49c70652ce4bb9014adb3'
            account_sid = 'AC6b6ffc0469b49c70652ce4bb9014adb3'
            # print(settings.ACCOUNT_SID_TWILIO)
            # auth_token = '4fc8e454be511d81e386d4fbe5031757'
            auth_token = 'f33ade014c543cc32b2a5351d07488c3'
            # print(settings.TOKEN_TWILIO)
            client = Client(account_sid, auth_token)
            message = client.messages.create(
                from_='whatsapp:+14155238886',
                body=form.cleaned_data['mensaje'],
                to='whatsapp:+59164888167'
            )
            messages.success(request,"Ha sido enviado correctamente")
            # return render(request, 'contactanos.html')
            return redirect('contactanos')
    else:
        form = ContactoMensajeForms()
    context = {'form': form}
    return render(request, 'contactanos.html', context)
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail
import json

from .models import MainInfo, MenuItem, Article, Schedule, Registration
from .forms import RegistrationForm


# Create your views here.

def index(request):

    userName = ""

    current_user = request.user

    isLogged = int(0 if current_user.id is None else current_user.id)

    if isLogged:
        userName = current_user.username

    siteInfo = MainInfo.objects.get(pk=1)

    menuItems = MenuItem.objects.filter(active=1).order_by('order')
    
    apresentacao = Article.objects.get(keyCode='apresentacao')
    contactos = Article.objects.get(keyCode='contactos')
    valores = Article.objects.get(keyCode='valores')

    try:
        schedule = Schedule.objects.filter(active=1).order_by('order')
    except:
        schedule = {}

    #----------------------------------------

    try:
        oradores = Article.objects.filter(active=1).filter(keyCode='oradores').order_by('order').values()
    except:
        oradores = {}

    # --------------------------------------
    
    try:
        locaisdeinteresse = Article.objects.filter(active=1).filter(keyCode='locaisdeinteresse').order_by('order').values()
    except:
        locaisdeinteresse = {}

    # --------------------------------------
    
    try:
        #cfp = Article.objects.filter(active=1).filter(keyCode='CFP').order_by('order').values()
        cfp = Article.objects.get(keyCode='CFP')
    except:
        cfp = {}

    print "cfp: "
    print cfp
    # --------------------------------------
    
    context = {
                'isLogged': isLogged, 
                'userName': userName, 
                'siteInfo': siteInfo, 
                "menuItems": menuItems,
                'apresentacao': apresentacao, 
                'contactos': contactos,
                'schedule': schedule,
                'valores': valores,
                'oradores': oradores,
                'locaisdeinteresse': locaisdeinteresse,
                'cfp': cfp
              }

    return render(request, 'main/index.html', context)
    
    
def registrationForm(request):

    if request.method == "POST":
        
        regDict = {}
        for item in request.POST:
            print item + " " + request.POST[item]
            regDict[item] = request.POST[item]

        recordId = int(regDict['recordId'])
        confirmData = int(regDict['confirmData'])
        
        print "recordId: ", recordId
        print "confirmData: ", confirmData
        print "regDict: ", regDict

        regDict['email'] = regDict['email'].strip()

        try:
            existingRecord = Registration.objects.filter(email=regDict['email'])[:1].get()

            if existingRecord.id != recordId:
                print "existingRecord: ", existingRecord
                print "existingRecord.id: ", existingRecord.id
                returnMsg = {
                        'msg': "RecordExist",
                        'recId': existingRecord.id
                     }
                
                return HttpResponse(json.dumps(returnMsg))


        except:
            pass
        

        del regDict['recordId']
        del regDict['confirmData']
        del regDict['csrfmiddlewaretoken']

        print "recordId: ", recordId
        print "Type recordId: ", type(recordId)
      
        if recordId > 0:
            print "updating"
            #regData = Registration.objects.get(pk=recordId)
            regData = Registration(**regDict)
            regData.id = recordId
        else:
            print "creating"
            regData = Registration(**regDict)
        
        regData.save()

        print "After Save regData.id: "
        print regData.id
        
        if confirmData > 0:

            mailData = {}

            #mailData['from'] = "register.me.alubrat2017@gmail.com"
            mailData['from'] = "inscricoes@alubrat.pt"

            #mailData['to'] = ["rtavares@gmail.com", "marioresende@almasoma.pt"]
            #mailData['to'] = [regData.email, "inscricoes@alubrat.pt", "rtavares@gmail.com", "marioresende@almasoma.pt"]
            mailData['to'] = [regData.email, "inscricoes@alubrat.pt"]

            mailData['subject'] = "Confirmação da sua Inscrição no Congresso ALUBRAT 2017 - Número  " + str(regData.id) + "."
            mailData['body'] = "Caro/a "+str(regData.name)+" "+str(regData.lname)+", confirmamos a sua inscrição no Congresso ALUBRAT 2017. \n"
            mailData['body'] += "Os seus dados de registo são os seguintes: \n"
        
            mailData['body'] += "Contacto telefónico 1: "
            mailData['body'] += str(regData.cell)
            mailData['body'] += " \n"
            mailData['body'] += "Contacto telefónico 2: "
            mailData['body'] += str(regData.phone)
            mailData['body'] += " \n"
            mailData['body'] += "Morada: "
            #mailData['body'] += (regData.address).encode('ascii', 'ignore').decode('ascii')
            mailData['body'] += str(regData.address)
            mailData['body'] += " \n"
            mailData['body'] += "Código Postal/CEP: "
            mailData['body'] += str(regData.zipCode)
            mailData['body'] += " \n"
            mailData['body'] += "Localidade: "
            mailData['body'] += str(regData.city)
            mailData['body'] += " \n"
            mailData['body'] += "País: "
            mailData['body'] += str(regData.country)
            mailData['body'] += " \n"
            mailData['body'] += "NIF/CPF: "
            mailData['body'] += str(regData.nif)
            mailData['body'] += " \n"

            
            mailData['body'] += "Fcturar a: "

            if(regData.f2fname):
                mailData['body'] += "Nome: "
                mailData['body'] += str(regData.f2fname)
                mailData['body'] += " \n"
                mailData['body'] += "Contacto telefónico 1: "
                mailData['body'] += str(regData.f2cell)
                mailData['body'] += " \n"
                mailData['body'] += "Contacto telefónico 2: "
                mailData['body'] += str(regData.f2phone)
                mailData['body'] += " \n"

                mailData['body'] += "Morada: "
                mailData['body'] += str(regData.f2address)
                mailData['body'] += " \n"
                mailData['body'] += "Código Postal/CEP: "
                mailData['body'] += str(regData.f2zip)
                mailData['body'] += " \n"
                mailData['body'] += "Localidade: "
                mailData['body'] += str(regData.f2city)
                mailData['body'] += " \n"
                mailData['body'] += "País: "
                mailData['body'] += str(regData.f2country)
                mailData['body'] += " \n"

                mailData['body'] += "NIF/CPF: "
                mailData['body'] += str(regData.f2nif)
                mailData['body'] += " \n"
            else:
                mailData['body'] += "Próprio."
                mailData['body'] += " \n"

            mailData['body'] += "Modalidade de inscrição: "
            mailData['body'] += str(regData.modalidade)

            mailData['body'] += " \n"

            mailData['body'] += "Forma de Pagamento: "
            mailData['body'] += str(regData.modPag)
            mailData['body'] += " \n"
            mailData['body'] += "Observações: "
            mailData['body'] += str(regData.remarks)

            mailData['body'] += " \n---------------------------------------------------\n"
            mailData['body'] += " O seu registo de inscrição está efectivado, a aguardar confirmação do pagamento. \n"
            mailData['body'] += " Após efectuar o seu pagamento, por favor envie o comprovativo respectivo para  pagamentos@alubrat.pt . \n"
            mailData['body'] += "  \n"
            mailData['body'] += "Gratos. \n A Comissão Organizadora do Congresso ALUBRAT 2017."

            mailData['body'] += " \n"
            mailData['body'] += "Em caso de qualuqer dúvida o Secretariado està à sua disposição através dos contactos constantes em " 
            mailData['body'] += "http://alubrat2017cong.pt/#contactos \n" 
            mailData['body'] += "Com os melhores cumprimentos, \n"
            mailData['body'] += "A Comissão Organizadora do X Congresso ALUBRAT - 2017, Tomar. \n"

            mailData['body'] += " \n"



            mailSend = send_mail(mailData['subject'], mailData['body'], mailData['from'], mailData['to'], fail_silently=False,)
            print "mailSend 1: "
            print mailSend
                        #mailData['to'] = ["rtavares@gmail.com", "marioresende@almasoma.pt"]
            mailData['to'] = ["rtavares@gmail.com", "marioresende@almasoma.pt"]

            mailData['body'] += "Email de registo: "
            mailData['body'] += regData.email
            mailData['body'] += "\n-------- COPY CONTROL MSG ------------\n"


            mailSend = send_mail(mailData['subject'], mailData['body'], mailData['from'], mailData['to'], fail_silently=False,)
            print "mailSend 2 - COntrol Copy: "
            print mailSend

            returnMsg = {
                'msg': "mailSent",
                'recId': recordId
                }
            return HttpResponse(json.dumps(returnMsg))



        if regData.id:

            # ---------------------
            # Notifications
            # To System
            
            returnMsg = {
                            'msg': "Success",
                            'recId': regData.id
                         }
            #---------------
        else:
            returnMsg = {
                    'msg': "NOT Success",
                    'recId': regData.id
                 }
            
        return HttpResponse(json.dumps(returnMsg))
    else:
        print "GET"
        #formData['toConfirm'] = 0
    payPalForm = request.GET.get('paypal')

    if payPalForm is None:
        payPalForm = 0
        
    print "payPalForm: ", payPalForm
    userName = ""

    current_user = request.user

    isLogged = int(0 if current_user.id is None else current_user.id)

    if isLogged:
        userName = current_user.username

    siteInfo = MainInfo.objects.get(pk=1)
    contactos = Article.objects.get(keyCode='contactos')

    #print "formData 2: "
    #print formData
    #'formData': formData,
    
    context = {
                'payPalForm': payPalForm, 
                'siteInfo': siteInfo, 
                'isLogged': isLogged, 
                'contactos': contactos, 
                'userName': userName 
              }

    return render(request, 'main/registrationForm.html', context)
    
def cfpForm(request):

    if request.method == "POST":
        
        regDict = {}
        for item in request.POST:
            print item + " " + request.POST[item]
            regDict[item] = request.POST[item]

        recordId = int(regDict['recordId'])
        confirmData = int(regDict['confirmData'])
        
        print "recordId: ", recordId
        print "confirmData: ", confirmData
        print "regDict: ", regDict

        regDict['email'] = regDict['email'].strip()

        try:
            existingRecord = Registration.objects.filter(email=regDict['email'])[:1].get()

            if existingRecord.id != recordId:
                print "existingRecord: ", existingRecord
                print "existingRecord.id: ", existingRecord.id
                returnMsg = {
                        'msg': "RecordExist",
                        'recId': existingRecord.id
                     }
                
                return HttpResponse(json.dumps(returnMsg))


        except:
            pass
        

        del regDict['recordId']
        del regDict['confirmData']
        del regDict['csrfmiddlewaretoken']

        print "recordId: ", recordId
        print "Type recordId: ", type(recordId)
      
        if recordId > 0:
            print "updating"
            #regData = Registration.objects.get(pk=recordId)
            regData = Registration(**regDict)
            regData.id = recordId
        else:
            print "creating"
            regData = Registration(**regDict)
        
        regData.save()

        print "After Save regData.id: "
        print regData.id
        
        if confirmData > 0:

            mailData = {}

            #mailData['from'] = "register.me.alubrat2017@gmail.com"
            mailData['from'] = "inscricoes@alubrat.pt"

            #mailData['to'] = ["rtavares@gmail.com", "marioresende@almasoma.pt"]
            #mailData['to'] = [regData.email, "inscricoes@alubrat.pt", "rtavares@gmail.com", "marioresende@almasoma.pt"]
            mailData['to'] = [regData.email, "inscricoes@alubrat.pt"]

            mailData['subject'] = "Confirmação da sua Inscrição no Congresso ALUBRAT 2017 - Número  " + str(regData.id) + "."
            mailData['body'] = "Caro/a "+str(regData.name)+" "+str(regData.lname)+", confirmamos a sua inscrição no Congresso ALUBRAT 2017. \n"
            mailData['body'] += "Os seus dados de registo são os seguintes: \n"
        
            mailData['body'] += "Contacto telefónico 1: "
            mailData['body'] += str(regData.cell)
            mailData['body'] += " \n"
            mailData['body'] += "Contacto telefónico 2: "
            mailData['body'] += str(regData.phone)
            mailData['body'] += " \n"
            mailData['body'] += "Morada: "
            #mailData['body'] += (regData.address).encode('ascii', 'ignore').decode('ascii')
            mailData['body'] += str(regData.address)
            mailData['body'] += " \n"
            mailData['body'] += "Código Postal/CEP: "
            mailData['body'] += str(regData.zipCode)
            mailData['body'] += " \n"
            mailData['body'] += "Localidade: "
            mailData['body'] += str(regData.city)
            mailData['body'] += " \n"
            mailData['body'] += "País: "
            mailData['body'] += str(regData.country)
            mailData['body'] += " \n"
            mailData['body'] += "NIF/CPF: "
            mailData['body'] += str(regData.nif)
            mailData['body'] += " \n"

            
            mailData['body'] += "Fcturar a: "

            if(regData.f2fname):
                mailData['body'] += "Nome: "
                mailData['body'] += str(regData.f2fname)
                mailData['body'] += " \n"
                mailData['body'] += "Contacto telefónico 1: "
                mailData['body'] += str(regData.f2cell)
                mailData['body'] += " \n"
                mailData['body'] += "Contacto telefónico 2: "
                mailData['body'] += str(regData.f2phone)
                mailData['body'] += " \n"

                mailData['body'] += "Morada: "
                mailData['body'] += str(regData.f2address)
                mailData['body'] += " \n"
                mailData['body'] += "Código Postal/CEP: "
                mailData['body'] += str(regData.f2zip)
                mailData['body'] += " \n"
                mailData['body'] += "Localidade: "
                mailData['body'] += str(regData.f2city)
                mailData['body'] += " \n"
                mailData['body'] += "País: "
                mailData['body'] += str(regData.f2country)
                mailData['body'] += " \n"

                mailData['body'] += "NIF/CPF: "
                mailData['body'] += str(regData.f2nif)
                mailData['body'] += " \n"
            else:
                mailData['body'] += "Próprio."
                mailData['body'] += " \n"

            mailData['body'] += "Modalidade de inscrição: "
            mailData['body'] += str(regData.modalidade)

            mailData['body'] += " \n"

            mailData['body'] += "Forma de Pagamento: "
            mailData['body'] += str(regData.modPag)
            mailData['body'] += " \n"
            mailData['body'] += "Observações: "
            mailData['body'] += str(regData.remarks)

            mailData['body'] += " \n---------------------------------------------------\n"
            mailData['body'] += " O seu registo de inscrição está efectivado, a aguardar confirmação do pagamento. \n"
            mailData['body'] += " Após efectuar o seu pagamento, por favor envie o comprovativo respectivo para  pagamentos@alubrat.pt . \n"
            mailData['body'] += "  \n"
            mailData['body'] += "Gratos. \n A Comissão Organizadora do Congresso ALUBRAT 2017."

            mailData['body'] += " \n"
            mailData['body'] += "Em caso de qualuqer dúvida o Secretariado està à sua disposição através dos contactos constantes em " 
            mailData['body'] += "http://alubrat2017cong.pt/#contactos \n" 
            mailData['body'] += "Com os melhores cumprimentos, \n"
            mailData['body'] += "A Comissão Organizadora do X Congresso ALUBRAT - 2017, Tomar. \n"

            mailData['body'] += " \n"



            mailSend = send_mail(mailData['subject'], mailData['body'], mailData['from'], mailData['to'], fail_silently=False,)
            print "mailSend 1: "
            print mailSend
                        #mailData['to'] = ["rtavares@gmail.com", "marioresende@almasoma.pt"]
            mailData['to'] = ["rtavares@gmail.com", "marioresende@almasoma.pt"]

            mailData['body'] += "Email de registo: "
            mailData['body'] += regData.email
            mailData['body'] += "\n-------- COPY CONTROL MSG ------------\n"


            mailSend = send_mail(mailData['subject'], mailData['body'], mailData['from'], mailData['to'], fail_silently=False,)
            print "mailSend 2 - COntrol Copy: "
            print mailSend

            returnMsg = {
                'msg': "mailSent",
                'recId': recordId
                }
            return HttpResponse(json.dumps(returnMsg))



        if regData.id:

            # ---------------------
            # Notifications
            # To System
            
            returnMsg = {
                            'msg': "Success",
                            'recId': regData.id
                         }
            #---------------
        else:
            returnMsg = {
                    'msg': "NOT Success",
                    'recId': regData.id
                 }
            
        return HttpResponse(json.dumps(returnMsg))
    else:
        print "GET"
        #formData['toConfirm'] = 0
    payPalForm = request.GET.get('paypal')

    if payPalForm is None:
        payPalForm = 0
        
    print "payPalForm: ", payPalForm
    userName = ""

    current_user = request.user

    isLogged = int(0 if current_user.id is None else current_user.id)

    if isLogged:
        userName = current_user.username

    siteInfo = MainInfo.objects.get(pk=1)
    contactos = Article.objects.get(keyCode='contactos')

    #print "formData 2: "
    #print formData
    #'formData': formData,
    
    context = {
                'payPalForm': payPalForm, 
                'siteInfo': siteInfo, 
                'isLogged': isLogged, 
                'contactos': contactos, 
                'userName': userName 
              }

    return render(request, 'main/cfpForm.html', context)
    

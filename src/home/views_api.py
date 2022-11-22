from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import profile
from .helpers import * 

class Login_view(APIView):

    def post(self , request):

        response = {}
        response['status'] = 500 
        response['message'] = 'Something went wrong'

        try:
            data = request.data

            if data.get('username')  is None:
                response['message'] = 'username is not available'
                raise Exception('username is not available')
            
            if data.get('password')  is None:
                response['message'] = 'password is not available'
                raise Exception('password is not available')
            
            check_user =  User.objects.filter(username = data.get('username')).first()

            if check_user is None:
                response['message'] = 'User is invalid'
                raise Exception('User is invalid')
            
            # if not profile.objects.filter(user = check_user).first().is_verified:
            #     response['message'] = 'User not verified'
            #     raise Exception('User not verified')
            # if not profile.objects.filter(user = check_user).first().is_verified:
            #     response['message'] = 'your profile is not verified'
            #     raise Exception('profile not verified')

            user_obj = authenticate(username= data.get('username'), password=data.get('password'))

            if user_obj is not None:
                login(request,user_obj)
                response['status'] = 200
                response['message'] ='welcome'
            else:
                response['message'] = 'Incorrect username or password'
                raise Exception('Incorrect username or password')
        
        except Exception as e:
            print(e)
        
        return Response(response)

Login_view = Login_view.as_view()          



class Register_view(APIView):

    def post(self , request):

        response = {}
        response['status'] = 500 
        response['message'] = 'Something went wrong'

        try:
            # data = request.data

            # if data.get('username')  is None:
            #     response['message'] = 'username is not available'
            #     raise Exception('username is not available')
            
            # if data.get('password')  is None:
            #     response['message'] = 'password is not available'
            #     raise Exception('password is not available')
            
            # check_user =  User.objects.filter(username = data.get('username')).first()

            # if check_user :
            #     response['message'] = 'User is already taken'
            #     raise Exception('User is already taken')
            
            # user_obj = User.objects.create(email = data.get('username') , username = data.get('username'))
            # user_obj.set_password(data.get('password'))
            # user_obj.save()
            
            # token = random_string_generator(20)
            # profile.objects.create(user = user_obj,token = token )
            # #send_mail_to_user(token , data.get('username'))
            # response['message'] = 'User created'
            # response['status'] = 200
           
        ############################################
            data = request.data
            
            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')
            
            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')
            
            
            check_user = User.objects.filter(username = data.get('username')).first()
            
            if check_user:
                response['message'] = 'username  already taken'
                raise Exception('username  already taken')
            
            user_obj = User.objects.create(email = data.get('username') , username = data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            token = random_string_generator(20)
            profile.objects.create(user = user_obj , token = token)
            send_mail_to_user(token , data.get('username'))
            response['message'] = 'User created '
            response['status'] = 200
        except Exception as e:
            print(e)
        
        return Response(response)

Register_view = Register_view.as_view()    
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError

from pyramid.view import view_config
    
import transaction 

from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )


from shop_pyramid.models.meta import DBSession
from shop_pyramid.models import User


class UserViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='view_user', renderer='jsonp' , permission='access')
    def view(self):
        user = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        return {'firstname': user.first_name, 'lastname': user.last_name, 'username':user.username,
        'email':user.email,'country':user.country}


    @view_config(route_name='registration',renderer='jsonp',request_method='POST',permission='view')
    def sign_up(self):
        session = DBSession()
        user = User(
                first_name=self.request.json_body.get('first_name'),
                last_name=self.request.json_body.get('last_name'),
                username=self.request.json_body.get('username'),
                password=self.request.json_body.get('password'),
                email=self.request.json_body.get('email'),
            )
        session.add(user)
        transaction.commit()

        return {"successful":True}
  

    @view_config(route_name='login', renderer='jsonp',request_method='POST')
    def login(self):
            phone = self.request.json_body.get('phone')
            password = self.request.json_body.get('password')
            email= self.request.json_body.get('email')
            if phone:
                user = DBSession.query(User).filter_by(phone1 = phone).first()
                if user and user.password == password:
                    userid=user.user_id
                    headers = remember(self.request, userid)
                    self.request.response.headerlist.extend(headers)
                    return { 'successful': True,'type':user.groups,'name':user.first_name+" "+user.last_name}
                return { 'successful': False}

            elif email:
                user = DBSession.query(User).filter_by(email = email).first()
                if user and user.password == password:
                    userid=user.user_id
                    headers = remember(self.request, userid)
                    self.request.response.headerlist.extend(headers)
                    return { 'successful': True,'type':user.groups,'name':user.first_name+" "+user.last_name}
                return { 'successful': False}
       

    @view_config(route_name='logout',renderer='jsonp',request_method='DELETE')
    def logout(self):
        headers = forget(self.request)
        self.request.response.headerlist.extend(headers)
        return { 'successful': False}


    @view_config(route_name='update_user',renderer='jsonp',request_method='POST',permission='access')
    def update(self):
        user = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        if user:
            user.first_name=self.request.json_body.get('first_name')
            user.last_name=self.request.json_body.get('last_name')
            user.password=self.request.json_body.get('password')
            user.email=self.request.json_body.get('email')
            user.country=self.request.json_body.get('country')
            transaction.commit()
            return Response('success')
        return Response('error')
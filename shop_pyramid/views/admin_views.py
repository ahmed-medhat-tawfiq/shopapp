from __future__ import division
from pyramid.response import Response
from sqlalchemy.exc import DBAPIError

from pyramid.view import view_config
    
import transaction 
from datetime import datetime,timedelta
import datetime
from pyramid.security import (
    remember,
    forget,
    authenticated_userid,
    )


from shop_pyramid.models.meta import DBSession
from shop_pyramid.models import User,Shop,Phone,Month


class SalesViews:
    def __init__(self, request):
        self.request = request


    @view_config(route_name='registration_admin',renderer='jsonp',request_method='POST')
    def signup_admin(self):
        session = DBSession()
        user = User(
                first_name=self.request.json_body.get('first_name'),
                last_name=self.request.json_body.get('last_name'),
                # username=self.request.json_body.get('username'),
                password=self.request.json_body.get('password'),
                email=self.request.json_body.get('email'),
                phone1=self.request.json_body.get('phone'),
                groups='a',
                block=False,
            )
        session.add(user)
        transaction.commit()
        return {"message":"success"}


    @view_config(route_name='view_sales', renderer='jsonp' ,request_method='GET', permission='admin')
    def view(self):
        sales = DBSession.query(User).filter_by(user_id = int(self.request.matchdict.get('id'))).first()
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        
        if admin.block == False: 
            return {'fullname': sales.first_name +" "+sales.last_name, 'phone':sales.phone1,'email':sales.email}


    @view_config(route_name='add_sales',renderer='jsonp',request_method='POST',permission='admin')
    def add_sales(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        sales = DBSession.query(User).filter_by(user_id =self.request.json_body.get('id')).first()
        session = DBSession()
        if admin.block == False:
            if sales:
                sales.block=False
                sales.admin_id = authenticated_userid(self.request)
                userid= sales.user_id
                month = Month(user=userid)
                session.add(month)
                transaction.commit()
                return {"message":"success"}
            return {"message":"wrong"}
        return{"message":"blocked"}


       

    @view_config(route_name='block_sales',renderer='jsonp',request_method='POST',permission='admin')
    def block_sales(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        sales = DBSession.query(User).filter_by(user_id = self.request.json_body.get('id')).first()
        if admin.block == False:
            sales.block=True
            return {"message":"success"}
        return{"message":"blocked"}



    @view_config(route_name='activate_sales',renderer='jsonp',request_method='POST',permission='admin')
    def activate_sales(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        sales = DBSession.query(User).filter_by(user_id = self.request.json_body.get('id')).filter_by(
            block=True).first()
        if admin.block == False:
            if sales:
                sales.block=False
                return {"message":"success"}
            return {"message":"wrong"}
        return{"message":"blocked"}
            


    @view_config(route_name='index_newsales',renderer='jsonp',request_method='GET',permission='admin')
    def index_newsales(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        sales = DBSession.query(User).filter_by(admin_id =0).filter_by(groups='s')

        if admin.block == False:
            return list({"id":d.user_id,"name":d.first_name+" "+d.last_name} for d in sales)



    @view_config(route_name='index_mysales',renderer='jsonp',request_method='GET',permission='admin')
    def index_mysales(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        adminid=admin.user_id
        sales = DBSession.query(User).filter_by(admin_id =adminid).filter_by(groups='s').filter_by(block=False)
        
        ss = list({"id":d.user_id,"name":d.first_name+" "+d.last_name,
         "month_purse":(DBSession.query(Month).filter_by(user =d.user_id).
            filter_by(old=False).first()).m_purse} for d in sales)


        if admin.block == False:
            return list({"id":x['id'],"name":x['name'],"month_purse":x['month_purse']} for x in ss)

       

    
    @view_config(route_name='block_list',renderer='jsonp',request_method='GET',permission='admin')
    def block_list(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        adminid=admin.user_id
        sales = DBSession.query(User).filter_by(admin_id =adminid).filter_by(groups='s').filter_by(block=True)

        if admin.block == False:
            return list({"id":d.user_id,"name":d.first_name+" "+d.last_name} for d in sales)


    
    @view_config(route_name='new_month',renderer='jsonp',request_method='POST',permission='admin')
    def new_month(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        sales = DBSession.query(User).filter_by(admin_id = authenticated_userid(self.request))

        session = DBSession()
        if admin.block == False:
            for d in sales:
                old_month = DBSession.query(Month).filter_by(user= d.user_id).filter_by(old=False).first()
                if old_month:
                    old_month.old=True

                month = Month(user=d.user_id)
                session.add(month)

            old_amonth = DBSession.query(Month).filter_by(user= authenticated_userid(self.request)).filter_by(
                old=False).first()

            if old_amonth:
                    old_amonth.old=True
            amonth = Month(user=authenticated_userid(self.request))
            session.add(amonth)
            transaction.commit()
            return {"message":"success"}
        return{"message":"blocked"}


    
    @view_config(route_name='inspect_sales',renderer='jsonp',request_method='GET',permission='admin')
    def inspect_sales(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        sales = DBSession.query(User).filter_by(user_id = int(self.request.matchdict.get('id'))).first()
        salesid=sales.user_id
        month = DBSession.query(Month).filter_by(user=salesid).filter_by(old=False).first()

        if admin.block == False:
            if month:
                if month.m_time==0:
                    m_time = 1
                else:
                    m_time = month.m_time

                if month.t_time==0:
                     t_time = 1
                else:
                    t_time = month.t_time

                if month.m_customer==0:
                     m_customer = 1
                else:
                    m_customer = month.m_customer

                if month.t_customer==0:
                     t_customer = 1
                else:
                    t_customer = month.t_customer

                t_persuasion=float((month.t_pcustomer))/(t_customer)
                t_againts= float((month.t_customer))/(t_time)
                m_persuasion=float((month.m_pcustomer))/(m_customer)
                m_againts= float((month.m_customer))/(m_time)
                      
                return {"today_purse":month.t_purse,"today_customers":month.t_customer,
                "today_pcustomers":month.t_pcustomer,"today_vcustomers":month.t_vcustomer,
                "today_time":month.t_time,"today_rate":t_againts,"today_persuasion":t_persuasion,
                "month_purse":month.m_purse,"month_customers":month.m_customer,
                "month_pcustomers":month.m_pcustomer,"month_vcustomers":month.m_vcustomer,
                "month_time":month.m_time,"month_rate":m_againts,"month_persuasion":m_persuasion}
            return{"message":"wrong"}
        return{"message":"blocked"} 


    
    @view_config(route_name='total_details',renderer='jsonp',request_method='GET',permission='admin')
    def total_details(self):
        admin = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        month = DBSession.query(Month).filter_by(user= authenticated_userid(self.request)).filter_by(
            old=False).first()

        if admin.block == False:
            if month:
                # if month.m_time==0:
                #     m_time = 1
                # else:
                #     m_time = month.m_time

                # if month.t_time==0:
                #      t_time = 1
                # else:
                #     t_time = month.t_time

                # if month.m_customer==0:
                #      m_customer = 1
                # else:
                #     m_customer = month.m_customer

                # if month.t_customer==0:
                #      t_customer = 1
                # else:
                #     t_customer = month.t_customer

                # t_persuasion=float((month.t_pcustomer))/(t_customer)
                # t_againts= float((month.t_customer))/(t_time)
                # m_persuasion=float((month.m_pcustomer))/(m_customer)
                # m_againts= float((month.m_customer))/(m_time)
                      
                return {"today_purse":month.t_purse,"today_customers":month.t_customer,
                "today_pcustomers":month.t_pcustomer,"today_vcustomers":month.t_vcustomer,
                "month_purse":month.m_purse,"month_customers":month.m_customer,
                "month_pcustomers":month.m_pcustomer,"month_vcustomers":month.m_vcustomer}
            return{"message":"wrong"}
        return{"message":"blocked"} 

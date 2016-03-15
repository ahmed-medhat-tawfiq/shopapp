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




    @view_config(route_name='view_admin', renderer='jsonp' ,request_method='GET', permission='boss')
    def view_admin(self):
        admin = DBSession.query(User).filter_by(user_id = int(self.request.matchdict.get('id'))).first()
        boss = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        
        if boss.block == False: 
            return {'fullname': admin.first_name +" "+admin.last_name, 'phone':admin.phone1,'email':admin.email}

       

    @view_config(route_name='block_admin',renderer='jsonp',request_method='POST',permission='boss')
    def block_admin(self):
        boss = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        admin = DBSession.query(User).filter_by(user_id = self.request.json_body.get('id')).first()
        adminid=admin.user_id
        sales = DBSession.query(User).filter_by(admin_id = adminid)
        if boss.block == False:
            if admin:
                admin.block=True
                if sales:
                    for d in sales:
                        d.block=True

                return {"message":"success"}
            return {"message":"wrong"}
        return{"message":"blocked"}



    @view_config(route_name='activate_admin',renderer='jsonp',request_method='POST',permission='boss')
    def activate_admin(self):
        boss = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        admin = DBSession.query(User).filter_by(user_id = self.request.json_body.get('id')).filter_by(
            block=True).first()
        adminid=admin.user_id
        sales = DBSession.query(User).filter_by(admin_id = adminid)
        if boss.block == False:
            if admin:
                admin.block=False
                if sales:
                    for d in sales:
                        d.block=False

                return {"message":"success"}
            return {"message":"wrong"}
        return{"message":"blocked"}
            


    @view_config(route_name='index_admins',renderer='jsonp',request_method='GET',permission='boss')
    def index_admins(self):
        boss = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        admins = DBSession.query(User).filter_by(admin_id =0).filter_by(groups='a')

        if boss.block == False:
            return list({"id":d.user_id,"name":d.first_name+" "+d.last_name,"block":d.block} for d in admins)
    

    @view_config(route_name='index_sales',renderer='jsonp',request_method='GET',permission='boss')
    def index_sales(self):
        
        team = DBSession.query(User).filter_by(admin_id =int(self.request.matchdict.get('id'))).filter_by(
            groups='s')
        boss = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()

        ss = list({"id":d.user_id,"name":d.first_name+" "+d.last_name,"month_purse":(DBSession.query(Month).
            filter_by(user =d.user_id).filter_by(old=False).first()).m_purse} for d in team)

        if boss.block == False:
            return list({"id":x['id'],"name":x['name'],"month_purse":x['month_purse']} for x in ss)
        
        
    
    @view_config(route_name='sales_details',renderer='jsonp',request_method='GET',permission='boss')
    def sales_details(self):
        boss = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        sales = DBSession.query(User).filter_by(user_id = int(self.request.matchdict.get('id'))).first()
        salesid=sales.user_id
        month = DBSession.query(Month).filter_by(user=salesid).filter_by(old=False).first()

        if boss.block == False:
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


    
    @view_config(route_name='admin_details',renderer='jsonp',request_method='GET',permission='boss')
    def admin_details(self):
        boss = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        month = DBSession.query(Month).filter_by(user= int(self.request.matchdict.get('id'))).filter_by(
            old=False).first()

        if boss.block == False:
            if month:
               
                      
                return {"today_purse":month.t_purse,"today_customers":month.t_customer,
                "today_pcustomers":month.t_pcustomer,"today_vcustomers":month.t_vcustomer,
                "month_purse":month.m_purse,"month_customers":month.m_customer,
                "month_pcustomers":month.m_pcustomer,"month_vcustomers":month.m_vcustomer}
            return{"message":"wrong"}
        return{"message":"blocked"} 

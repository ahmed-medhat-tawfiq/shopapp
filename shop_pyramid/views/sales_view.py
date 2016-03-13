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


    @view_config(route_name='registration_sales',renderer='jsonp',request_method='POST')
    def signup_sales(self):
        session = DBSession()
        user = User(
                first_name=self.request.json_body.get('first_name'),
                last_name=self.request.json_body.get('last_name'),
                # username=self.request.json_body.get('username'),
                password=self.request.json_body.get('password'),
                email=self.request.json_body.get('email'),
                phone1=self.request.json_body.get('phone'),
                groups='s',
                block=True,
            )
        session.add(user)
        transaction.commit()
        return {"message":"success"}
    

    @view_config(route_name='index_customers',renderer='jsonp',request_method='GET',permission='sales')
    def index_customers(self):
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        salesid=sales.user_id
        customers = DBSession.query(User).filter_by(sales_id =salesid).filter_by(groups='o')

        if sales.block == False:
            return list({"id":d.user_id,"name":d.first_name+" "+d.last_name} for d in customers)




    @view_config(route_name='index_team',renderer='jsonp',request_method='GET',permission='sales')
    def index_team(self):
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        adminid=sales.admin_id
        team = DBSession.query(User).filter_by(admin_id =adminid).filter_by(groups='s').filter_by(block=False)

        ss = list({"id":d.user_id,"name":d.first_name+" "+d.last_name,"month_purse":(DBSession.query(Month).
            filter_by(user =d.user_id).filter_by(old=False).first()).m_purse} for d in team)


        if sales.block == False:
            return list({"id":x['id'],"name":x['name'],"month_purse":x['month_purse']} for x in ss)





    @view_config(route_name='view_customer', renderer='jsonp' ,request_method='GET', permission='sales')
    def view_customer(self):
        user = DBSession.query(User).filter_by(sales_id = authenticated_userid(self.request)).filter_by(
            user_id = int(self.request.matchdict.get('id'))).first()
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        
        if sales.block == False: 
            return {'fullname': user.first_name +" "+user.last_name, 'phone':user.phone1,
            'email':user.email,'location':user.location}



    @view_config(route_name='index_cshop', renderer='jsonp' ,request_method='GET', permission='sales')
    def index_cshop(self):
        shops = DBSession.query(Shop).filter_by(user = int(self.request.matchdict.get('id')))
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        
        if sales.block == False: 
            return list({"id":d.shop_id,"name":d.name} for d in shops)



    @view_config(route_name='view_cshop', renderer='jsonp' ,request_method='GET', permission='sales')
    def view_cshop(self):
        shop = DBSession.query(Shop).filter_by(shop_id = int(self.request.matchdict.get('id'))).first()
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        
        if sales.block == False: 
            return {'name':shop.name,'category':shop.category,'description':shop.description,
            'latitude':float(shop.latitude),'longitude':float(shop.longitude)}



    @view_config(route_name='release_shop',renderer='jsonp',request_method='POST',permission='sales')
    def release_shop(self):
        session = DBSession()

        user = DBSession.query(User).filter_by(phone1 = self.request.json_body.get('phone')).first()
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        
        period=self.request.json_body.get('period')
        typ = self.request.json_body.get('type')

        if typ == 0:
            p=0
            v=0
            t="no"
        elif typ == 1:
            p=1
            v=0
            s=20*period
            t="normal"
        elif typ == 2:
            p=1
            v=1
            s=period*50
            t="special"
        elif typ == 3:
            p=1
            v=1
            s=100
            period=0.5*period
            t="full page"

        if sales.block == False:
            if user:
                userid = user.user_id
                user.shop_no+=1
                transaction.commit()
                shop = Shop(
                        name=self.request.json_body.get('name'),
                        category=self.request.json_body.get('category'),
                        description=self.request.json_body.get('description'),
                        user=userid,
                        types=t,
                        latitude=self.request.json_body.get('latitude'),
                        longitude=self.request.json_body.get('longitude'),
                        start_date = datetime.datetime.now(),
                        end_date = datetime.datetime.now()+datetime.timedelta(days=(period*30)),
                    ) 
                session.add(shop)
                session.flush()
                shopid=shop.shop_id
                phs = self.request.json_body.get('phones')
                phones = phs.replace(';', ' ').replace(',', ' ')
                phones = [phone.lower() for phone in phones.split()]
                phones = set(phones)

                for phone_number in phones:
                    phone = Phone(number=phone_number ,shop=shopid)    
                    DBSession.add(phone)
              
                sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()

                month = DBSession.query(Month).filter_by(user= authenticated_userid(self.request)).filter_by(
                    old=False).first()
                amonth = DBSession.query(Month).filter_by(user=sales.admin_id).filter_by(old=False).first()

                if month and amonth:
                    if month.t_customer==0 or (month.t_customer>0 and month.t_sdate.strftime("%d") !=  datetime.datetime.now().strftime("%d") and  (int(datetime.datetime.now().strftime("%H"))) > 4):
                        time_start = datetime.datetime.now()
                        time_end = datetime.datetime.now()+datetime.timedelta(hours=12)
                        month.t_sdate=datetime.datetime.now()
                        month.t_edate=datetime.datetime.now()+datetime.timedelta(hours=12)
                        month.m_time+=month.t_time
                        month.t_customer=0
                        month.t_pcustomer=0
                        month.t_vcustomer=0
                        month.t_time=0
                        
                        amonth.t_customer=0
                        amonth.t_pcustomer=0
                        amonth.t_vcustomer=0
                    else:
                        time_start= month.t_sdate
                        time_end= month.t_edate
                       
                    month.t_purse+=s
                    month.t_customer+=1
                    month.t_pcustomer+=p
                    month.t_vcustomer+=v

                    amonth.t_purse+=s
                    amonth.t_customer+=1
                    amonth.t_pcustomer+=p
                    amonth.t_vcustomer+=v

                    if int(datetime.datetime.now().strftime("%H"))< int(time_start.strftime("%H")):
                        month.t_time=24-int(time_start.strftime("%H"))+int(datetime.datetime.now().strftime("%H"))
                        
                    else:
                        month.t_time=int(datetime.datetime.now().strftime("%H"))-int(time_start.strftime("%H"))
                        
                    month.m_purse+=s
                    month.m_customer+=1
                    month.m_pcustomer+=p
                    month.m_vcustomer+=v

                    amonth.m_purse+=s
                    amonth.m_customer+=1
                    amonth.m_pcustomer+=p
                    amonth.m_vcustomer+=v
                    
                    transaction.commit()

                return {"message":"success"}
            return {"message":"wrong"}
        return {"message":"blocked"}



    @view_config(route_name='add_customer',renderer='jsonp',request_method='POST',permission='sales')
    def add_customer(self):
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        
        if sales.block == False:
            session = DBSession()
            user = User(
                    first_name=self.request.json_body.get('first_name'),
                    last_name=self.request.json_body.get('last_name'),
                    email=self.request.json_body.get('email'),
                    phone1=self.request.json_body.get('phone'),
                    location=self.request.json_body.get('location'),
                    sales_id=authenticated_userid(self.request),
                    groups='o',
                )
            session.add(user)
            transaction.commit()
            return {"message":"success"}
        return{"message":"blocked"}
            


    @view_config(route_name='details',renderer='jsonp',request_method='GET',permission='sales')
    def details(self):
        sales = DBSession.query(User).filter_by(user_id = authenticated_userid(self.request)).first()
        month = DBSession.query(Month).filter_by(user= authenticated_userid(self.request)).filter_by(
            old=False).first()

        if sales.block == False:
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

     
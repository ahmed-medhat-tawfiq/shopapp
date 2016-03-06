from pyramid.response import Response

from pyramid.view import view_config

from pyramid.security import authenticated_userid
import json
import transaction 

from shop_pyramid.models.meta import DBSession    
from shop_pyramid.models import Shop,User,Code
from datetime import datetime,timedelta
import datetime

from math import radians, cos, sin, asin, sqrt,atan2

# def ToRadian(value):
#     return (value * 3.141592654)/180


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    float(lon1)
    float(lon2)
    float(lat1)
    float(lat2)
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    return km

    # dlon = lon2 - lon1
    # dlat = lat2 - lat1

    # dlon_rad = ToRadian(dlon)
    # dlat_rad = ToRadian(dlat)

    # lat1_rad = ToRadian(lat1)
    # lon1_rad = ToRadian(lon1)

    # lat2_rad = ToRadian(lat2)
    # lon2_rad = ToRadian(lon2)

    # a = float((sin(dlat_rad/2))**2 +cos(lat1_rad) * cos(lat2_rad) * (sin(dlon_rad/2))**2)
    # c = 2 * atan2( sqrt(a), sqrt(1-a))
    # d = sqrt(((dlon_rad)**2)+((dlat_rad)**2))
    #   #puts c * 6371000
    # return c * 6371000

class ShopViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name='code_create',renderer='jsonp',request_method='POST' ,permission='access')
    def code_create(self):
        userid=authenticated_userid(self.request)
        user=DBSession.query(User).filter_by(user_id = userid).first()
        code=DBSession.query(Code).filter_by(code=self.request.json_body.get('code')).filter_by(
            used=False).first()
        
        if user.block ==False:
            if code:
                code.used=True
                user.groups='o'
                user.shop_no+=1
                transaction.commit()
                return {'message':'success'}
            return {'message':'wrong'}
        return{'message':'blocked'}    

    @view_config(route_name='codeit',renderer='jsonp',request_method='POST' ,permission='view')
    def codeit(self):
        session = DBSession()
        code = Code(
                    answer_image=self.request.json_body.get('name'),
                    code=self.request.json_body.get('code'),        
                )
        session.add(code)
        transaction.commit()
        return {'message':'success'}
        


    @view_config(route_name='code_renew',renderer='jsonp',request_method='PUT' ,permission='owner')
    def code_renew(self):
        userid=authenticated_userid(self.request)
        user=DBSession.query(User).filter_by(user_id = userid).first()
        shop = DBSession.query(Shop).filter_by(shop_id = int(self.request.matchdict.get('id'))).filter_by(
            user=userid).first()
        code=DBSession.query(Code).filter_by(code=self.request.json_body.get('code')).filter_by(
            used=False).first()
        
        if user.block ==False:
            if code and shop:
                code.used=True
                shop.start_date = end+datetime.timedelta(days=1)
                shop.end_date = end+datetime.timedelta(days=(code.period*30))
                transaction.commit()
                return {'message':'success'}
            return {'message':'wrong'}
        return{'message':'blocked'}    


    @view_config(route_name='create_shop',renderer='jsonp',request_method='POST' ,permission='owner')
    def create(self):
        userid=authenticated_userid(self.request)
        user=DBSession.query(User).filter_by(user_id = userid).first()
        shops=DBSession.query(Shop).filter_by(user = userid).count()
        
        if user.block ==False:
            if user.shop_no > shops:
                session = DBSession()
                shop = Shop(
                        name=self.request.json_body.get('name'),
                        category=self.request.json_body.get('category'),
                        description=self.request.json_body.get('description'),
                        user=userid,
                        latitude=self.request.json_body.get('latitude'),
                        longitude=self.request.json_body.get('longitude'),
                        start_date = datetime.datetime.now(),
                        end_date = datetime.datetime.now()+datetime.timedelta(days=30)
                    )
               
                session.add(shop)
                transaction.commit()
                return {'message':'success'}
            return {'message':'wrong'}
        return{'message':'blocked'}    


    @view_config(route_name='update_shop',renderer='jsonp',request_method='PUT',permission='owner')
    def update(self):

        user=DBSession.query(User).filter_by(user_id =authenticated_userid(self.request)).first()
        shop = DBSession.query(Shop).filter_by(shop_id = int(self.request.matchdict.get('id'))).filter_by(
	    	user=authenticated_userid(self.request)).filter_by(end_date > datetime.datetime.now()).first()
        if user.block==False:
            if shop:
                shop.name=self.request.json_body.get('name')
                shop.category=self.request.json_body.get('category')
                shop.description=self.request.json_body.get('description')
                shop.phone=self.request.json_body.get('phone')
                shop.ads=self.request.json_body.get('ads')
                shop.latitude=self.request.json_body.get('latitude')
                shop.longitude=self.request.json_body.get('longitude')
                transaction.commit()
                return {'message':'success'}
            return {'message':'expired'}
        return {'message':'blocked'}


    @view_config(route_name='delete_shop',renderer='jsonp',request_method='DELETE',permission='owner')
    def delete(self):

        user=DBSession.query(User).filter_by(user_id =authenticated_userid(self.request)).first()
        shop = DBSession.query(Shop).filter_by(shop_id = int(self.request.matchdict.get('id'))).filter_by(
            user=authenticated_userid(self.request)).first()
         
        if user.block==False:
            if shop:
                DBSession.delete(shop)
                return {'message':'success'}
            return {'message':'wrong'}
        return{'message':'blocked'}    

    

    @view_config(route_name='index_shop',renderer='jsonp',request_method='GET',permission='owner')
    def index(self):
        user=DBSession.query(User).filter_by(user_id =authenticated_userid(self.request)).first()
        shop = DBSession.query(Shop).filter_by(user=authenticated_userid(self.request)).filter(
            Shop.end_date >= datetime.datetime.now())
        if shop and user.block==False:
            return list({"id":d.shop_id,"name":d.name} for d in shop)
            # return {'shops':list({"id":d.shop_id,"name":d.name} for d in shop)}



    @view_config(route_name='view_shop',renderer='jsonp',request_method='GET',permission='view')
    def view(self): 
        shop = DBSession.query(Shop).filter_by(shop_id = int(self.request.matchdict.get('id'))).first()
        user=DBSession.query(User).filter_by(user_id =authenticated_userid(self.request)).first()
        
        if shop and user.block==False:
            return {'name':shop.name,'category':shop.category,
            'description':shop.description,'phone':shop.phone,'latitude':float(shop.latitude),
            'longitude':float(shop.longitude)}


    @view_config(route_name='search_by_name',renderer='jsonp',request_method='POST',permission='view')
    def search_by_name(self):
        shops = []
        # shop = DBSession.query(Shop).filter_by(name = self.request.json_body.get('name'))
        lat2 =self.request.json_body.get('latitude')
        lon2 =self.request.json_body.get('longitude')
        n = self.request.json_body.get('name')
        sp = DBSession.query(Shop).filter(Shop.name.like('%'+n+'%')).all()
        shop = list({"id":d.shop_id,"name":d.name, "longitude":d.longitude,"latitude":d.latitude} for d in sp)
        for s in shop:
            if haversine(s["longitude"], s["latitude"], lon2, lat2) <= 2:
                shops.append({"id":s["id"],"name":s["name"],
                    "distance":int(haversine(s["longitude"], s["latitude"], lon2, lat2)*1000)})
                

        return list({"id":x['id'],"name":x['name'],"distance":x['distance']} for x in shops)


    @view_config(route_name='search_by_category',renderer='jsonp',request_method='POST',permission='view')
    def search_by_category(self):
        shops = []
        # shop = DBSession.query(Shop).filter_by(category = self.request.json_body.get('category'))
        lat2 =self.request.json_body.get('latitude')
        lon2 =self.request.json_body.get('longitude')
        sp = DBSession.query(Shop).filter_by(category = self.request.json_body.get('category')).all()
        shop = list({"id":d.shop_id,"name":d.name, "longitude":d.longitude,"latitude":d.latitude} for d in sp)
        for s in shop:
            if haversine(s["longitude"], s["latitude"], lon2, lat2) <= 2:
                shops.append({"id":s["id"],"name":s["name"],"distance":int(haversine(s["longitude"], s["latitude"], lon2, lat2)*1000)})
                

        return list({"id":x['id'],"name":x['name'],"distance":x['distance']} for x in shops)


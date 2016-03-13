from pyramid.config import Configurator
from sqlalchemy import engine_from_config
from pyramid.renderers import JSONP
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from .models.meta import (
    DBSession,
    Base,
    )


from .models import*
from .security import*

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    authn_policy = AuthTktAuthenticationPolicy(settings['auth.secret'], callback=groupfinder, hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()

    config = Configurator(settings=settings, root_factory='.models.meta.RootFactory')

    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)

    # add sacrud and project models
    config.include('pyramid_sacrud', route_prefix = 'admin')
    settings = config.registry.settings
    settings['pyramid_sacrud.models'] = (('Users', [User , Month]),('Shops', [Shop , Phone]),
        ('Code', [Code]))

    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('view_user', '/view/user')
    config.add_route('registration', '/signup')
    config.add_route('update_user', '/update/user')
    config.add_route('code_create', '/code/create')
    config.add_route('code_renew', '/code/renew/{id}')
    config.add_route('create_shop', '/create/shop')
    config.add_route('update_shop', '/update/shop/{id}')
    config.add_route('delete_shop', '/delete/shop/{id}')
    config.add_route('index_shop', '/index/shop')
    config.add_route('view_shop', '/view/shop/{id}')
    config.add_route('search_by_name', '/search/shop/name')
    config.add_route('search_by_category', '/search/shop/category')

    config.add_route('view_customer', '/view/customer/{id}')
    config.add_route('index_customers', '/index/customers')
    config.add_route('add_customer', '/add/customer')
    config.add_route('release_shop', '/release/shop')
    config.add_route('registration_sales', '/sales/signup')
    config.add_route('details', '/sales/details')
    config.add_route('index_cshop', '/index/cshop/{id}')
    config.add_route('view_cshop', '/view/cshop/{id}')
    config.add_route('index_team', '/index/team')

    config.add_route('view_sales', '/view/sales/{id}')
    config.add_route('add_sales', '/add/sales')
    config.add_route('block_sales', '/block/sales')
    config.add_route('activate_sales', '/activate/sales')
    config.add_route('index_newsales', '/index/newsales')
    config.add_route('index_mysales', '/index/mysales')
    config.add_route('block_list', '/blocklist')
    config.add_route('new_month', '/new/month')
    config.add_route('inspect_sales', '/inspect/sales/{id}')
    config.add_route('registration_admin', '/admin/signup')
    config.add_route('total_details', '/total/details')


    config.add_route('view_admin', '/view/admin/{id}')
    config.add_route('block_admin', '/block/admin')
    config.add_route('activate_admin', '/activate/admin')
    config.add_route('index_sales', '/index/sales/{id}')
    config.add_route('index_admins', '/index/admins')
    config.add_route('sales_details', '/sales/details/{id}')
    config.add_route('admin_details', '/admin/details/{id}')

    config.add_route('codeit', '/codeit')

    config.add_renderer('jsonp', JSONP(param_name='callback'))


    config.scan()
    return config.make_wsgi_app()

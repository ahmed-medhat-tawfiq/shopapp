from pyramid.security import (
    Allow,
    Deny,
    Everyone,
    Authenticated,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class RootFactory(object):
    __acl__ = [ (Allow, Everyone, 'view'),
                (Allow, Authenticated, 'access'),
                (Allow,'o','owner'),
                (Allow,'s','sales'),
                (Allow,'a','admin'),
                (Allow, Everyone, ['pyramid_sacrud_home','pyramid_sacrud_list','pyramid_sacrud_update',
                    'pyramid_sacrud_create','pyramid_sacrud_mass_delete'])]
                
    def __init__(self, request):
        pass
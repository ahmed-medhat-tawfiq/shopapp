from .models.meta import (
    DBSession,
    )
from .models.user import (
    User,
    )

from sqlalchemy.orm.exc import NoResultFound

def groupfinder(userid, request):
    
    try:
        user = DBSession.query(User).filter(User.user_id == userid).one()
    except NoResultFound:
        pass
    else:
        groups = user.groups
    return groups
    
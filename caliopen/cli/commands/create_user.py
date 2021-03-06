"""
Create a user with a password in a Calipen instance
"""
import logging
log = logging.getLogger(__name__)


def create_user(**kwargs):

    from caliopen.base.user.core import User
    from caliopen.base.user.parameters import NewUser
    from caliopen.base.user.parameters import NewContact
    param = NewUser()
    param.name = kwargs['email']
    param.password = kwargs['password']
    contact = NewContact()
    contact.given_name = kwargs.get('given_name')
    contact.family_name = kwargs.get('family_name')
    param.contact = contact
    user = User.create(param)
    user.save()
    log.info('User %s (%s) created' % (user.user_id, user.user_name))

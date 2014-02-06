import random
import string
from wsc.Configuration import Configuration
from wsc.iam import *
from hashlib import sha1
from wsc.model import Printing, User
from wsc.repo import TransactionRepository, UserRepository
import hashlib
import datetime

start = datetime.datetime.now()

config = Configuration()
config.iam_endpoint = 'http://localhost:5001'
config.invoicing_endpoint = 'http://localhost:5000'

iam = IAM(config)

session = iam.login('john.doe', sha1('1234').hexdigest())

print 'Session {} opened for user {}'.format(session.session_id, session.user_id)

# Transactions test
repo = TransactionRepository(config, session)

tr = Printing()
tr.amount = -1.5
tr.currency = 'EUR'
tr.pages_grey_levels = 1
tr.pages_color = 0
tr.copies = 4
tr.user_id = session.user_id

tr = repo.create(tr)

tr2 = repo.get(tr.id)
print 'Got amount ' + tr2.amount

# Users test
repo_users = UserRepository(config, session)
u = User()
u.first_name = 'Lucky'
u.last_name = 'Luke'
u.login = 'lucky_'.join(random.choice(string.ascii_uppercase + string.digits) for x in range(3))
u.role = 'admin'
u.entity_id = '1ca5e4506c5d41ac89b7adf6ec291bbf'
u.password_hash = hashlib.sha1('qwerty').hexdigest()


u = repo_users.create(u)
u2 = repo_users.get(u.id)

print 'Login IAM : ' +u2.login

r = iam.logout(session)

print 'Duration : ' + str(datetime.datetime.now() - start)

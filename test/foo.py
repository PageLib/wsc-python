from wsc.Configuration import Configuration
from wsc.iam import *
from hashlib import sha1
from wsc.model import Printing, User
from wsc.repo import TransactionRepository, UserRepository

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
u.login = 'luckyl'
u.role = 'admin'
u.entity_id = '2ec396002779492aa8897e0cd918c15d'

u = repo_users.create(u)
u2 = repo_users.get(u.id)

print 'Login IAM : ' +u2.login

r = iam.logout(session)

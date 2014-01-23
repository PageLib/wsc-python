from wsc.Configuration import Configuration
from wsc.iam import *
from hashlib import sha1
from wsc.model import Printing
from wsc.repo import TransactionRepository

config = Configuration()
config.iam_endpoint = 'http://localhost:5001'
config.invoicing_endpoint = 'http://localhost:5000'

iam = IAM(config)

session = iam.login('john.doe', sha1('1234').hexdigest())

print 'Session {} opened for user {}'.format(session.session_id, session.user_id)

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

r = iam.logout(session)

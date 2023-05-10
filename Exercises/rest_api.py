import json
class RestAPI:
    def __init__(self, database=None):
        users = database and database['users'] or []
        self.db = {user['name']: user for user in users}
    def get(self, url, payload=None):
        if payload:
            req = json.loads(payload)
        users = [user for user in self.db.values(
        ) if not payload or user['name'] in req['users']]
        return json.dumps({'users': sorted(users, key=lambda x: x['name'])})
    # update a user with new amount owed by who
    # amount can be negative is which case a user name owes money
    def update_balance(self, name, who, amount):
        user = self.db[name]
        owned_by, owes = user['owed_by'], user['owes']
        amount_owed_by_who = owned_by.get(who, 0) - owes.get(who, 0) + amount
        if amount_owed_by_who > 0:
            # who owes money to user
            owes.pop(who, None)
            owned_by[who] = amount_owed_by_who
        elif amount_owed_by_who < 0:
            # user owes money to who
            owned_by.pop(who, None)
            owes[who] = -amount_owed_by_who
        else:
            # scores are settled
            owes.pop(who, None)
            owned_by.pop(who, None)
        user['balance'] += amount
    def post(self, url, payload=None):
        req = json.loads(payload)
        if url == '/add':
            name = req['user']
            new_user = {'name': name, 'owes': {}, 'owed_by': {}, 'balance': 0}
            return json.dumps(self.db.setdefault(name, new_user))
        elif url == '/iou':
            self.update_balance(req['lender'], req['borrower'], req['amount'])
            self.update_balance(req['borrower'], req['lender'], -req['amount'])
            return json.dumps({'users': sorted([self.db[req['lender']], self.db[req['borrower']]], key=lambda x: x['name'])})

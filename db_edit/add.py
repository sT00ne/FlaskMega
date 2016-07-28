from app import db, models

u = models.User(nickname='john', email='john@email.com')
db.session.add(u)
db.session.commit()
# u = models.User(nickname='susan', email='susan@email.com')
# db.session.add(u)
# db.session.commit()
# users = models.User.query.all()
# print(users)

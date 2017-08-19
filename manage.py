# -*- encoding = UTF-8 -*-

from nowstagram import app,db
from flask_script import Manager
from nowstagram.models import User,Image,Comment
import random


manager =Manager(app)

def get_image_url():
    return 'http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'


@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    for i in range(0, 50):
        db.session.add(User('zhanghan'+str(i),'zzz'+str(i)))
        for j in range(0,4):
            db.session.add(Image(get_image_url(),i+1))
            for k in range(0,5):
                db.session.add(Comment('zhengbang'+str(k),1+j+4*i,i+1))
    db.session.commit()

    for i in range(20,40):
        user = User.query.get(i)
        user.username= 'new zhanghan' +str(i)
    db.session.commit()

    for i in range(20,40):
        comment = Comment.query.get(i)
        db.session.delete(comment)
    db.session.commit()

    print 1,User.query.all()
    print 2,User.query.get(4)
    print 3,User.query.filter_by(id =4).all()
    user= User.query.get(3)
    print 4,user.images
    image= Image.query.get(6)
    print 5,image.user

if __name__ ==  '__main__':
    manager.run()

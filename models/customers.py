from . import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age
        
    @classmethod
    def create_customer(cls, name, city, age):
        book = cls(name=name, city=city, age=age,)
        db.session.add(customer)
        db.session.commit()
        return Customer

    @classmethod
    def get_customer(cls):
        return cls.query.all()

    @classmethod
    def get_custmer_by_id(cls, customer_id):
        return cls.query.get(customer_id)

    def update(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age
        db.session.commit()

    @classmethod
    def delete_customer(cls, customer_id):
        book = cls.query.get(customer_id)
        if book:
            db.session.delete(customer)
            db.session.commit()
            return True
        return False

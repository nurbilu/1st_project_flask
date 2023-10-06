from flask import Blueprint 
from . import db

loans_blueprint = Blueprint('loans', __name__)

class Loan(db.Model):
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), primary_key=True)
    loan_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=False)

    customer = db.relationship('Customer', backref='loans')
    book = db.relationship('Book', backref='loans')

    @classmethod
    def create_loan(cls, cust_id, book_id, loan_date, return_date):
        loan = cls(cust_id=cust_id, book_id=book_id, loan_date=loan_date, return_date=return_date)
        db.session.add(loan)
        db.session.commit()
        return loan

    @classmethod
    def get_loans(cls):
        return cls.query.all()

    @classmethod
    def get_loan_by_ids(cls, cust_id, book_id):
        return cls.query.filter_by(cust_id=cust_id, book_id=book_id).first()

    def update(self, loan_date, return_date):
        self.loan_date = loan_date
        self.return_date = return_date
        db.session.commit()

    @classmethod
    def delete_loan(cls, cust_id, book_id):
        loan = cls.query.filter_by(cust_id=cust_id, book_id=book_id).first()
        if loan:
            db.session.delete(loan)
            db.session.commit()
            return True
        return False

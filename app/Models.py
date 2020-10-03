from app import db

class Consultations(db.Model):
    __tablename__ = 'consultation'
    id = db.Column(db.Integer, primary_key=True)
    idPatient = db.Column(db.Integer)
    idDoctor = db.Column(db.Integer)
    observation = db.Column(db.String)
    healthStatus = db.Column(db.String)
    userpatient = db.relationship('users',
        backref=db.backref('consultation', lazy=True))
    userdoctor = db.relationship('users',
        backref=db.backref('doctorservices', lazy=True))

    def __init__(self, idPatient, idDoctor, observation,healthStatus):
        self.idPatient = idPatient
        self.idDoctor = idDoctor
        self.observation = observation,
        self.healthStatus = healthStatus


class DoctorServices(db.Model):
    __tablename__ = 'doctorservices'
    idUser = db.Column(db.Integer)
    idServices = db.Column(db.Integer)
    user = db.relationship('users',
        backref=db.backref('doctorservices', lazy=True))
    service = db.relationship('services',
        backref=db.backref('doctorservices', lazy=True))

    def __init__(self, iduser,idservices):
        self.idUser = iduser
        self.idServices = idservices

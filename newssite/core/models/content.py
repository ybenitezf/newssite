from sqlalchemy.orm import backref, relationship
from newssite.services import db
from flask import json


class Author(db.Model):
    __tablename__ = "author"
    id = db.Column(db.String(32), primary_key=True)
    name = db.Column(db.String(120))
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(254), index=True)
    author_type = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_identity": "author",
        "polymorphic_on": author_type,
    }

    def __repr__(self) -> str:
        return f"Author {self.nickname}"


class Photographer(Author):
    __tablename__ = "photographer"
    id = db.Column(db.ForeignKey("author.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "photographer"}

    def __repr__(self) -> str:
        return f"Photographer {self.nickname}"


class Writer(Author):
    __tablename__ = "writer"
    id = db.Column(db.ForeignKey("author.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "writer"}

    def __repr__(self) -> str:
        return f"Writer {self.nickname}"


class ImageModel(db.Model):
    __tablename__ = "image"

    id = db.Column(db.String(32), primary_key=True)
    filename = db.Column(db.Text())
    width = db.Column(db.Integer(), default=0)
    height = db.Column(db.Integer(), default=0)
    orientation = db.Column(db.String(10), default='cuadrada')
    image_type = db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_identity": "author",
        "polymorphic_on": image_type,
    }

    def __repr__(self) -> str:
        return f"Image {self.filename}"

class Photo(ImageModel):

    __mapper_args__ = {"polymorphic_identity": "photo"}

    id = db.Column(db.ForeignKey('image.id'), primary_key=True)
    store_data = db.Column(db.Text(), default='')
    author_id = db.Column(db.String(32), db.ForeignKey('photographer.id'))
    photographer = relationship('Photographer', backref=backref('photos'))

    def __repr__(self) -> str:
        return f"Photo {self.filename}"

    def getStoreData(self) -> dict:
        if self.store_data:
            return json.loads(self.store_data)
        
        return {}

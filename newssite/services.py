from flask_static_digest import FlaskStaticDigest
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


static_digest = FlaskStaticDigest()
db = SQLAlchemy()
migrate = Migrate(db=db)

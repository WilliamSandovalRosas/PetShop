from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship


from app import app, db          #,ma


# defino las tablas
class Producto(db.Model):   # la clase Producto hereda de db.Model    
    idProducto=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombreProd=db.Column(db.String(30))
    marca=db.Column(db.String(20))
    descripcion=db.Column(db.String(100))
    precio=db.Column(db.Double)
    #stock=db.Column(db.Integer)
    categoria = db.Column(db.Integer)
    proveedor=db.Column(db.String(30))
    #tipoproducto = db.relationship('tipoproducto', backref='funciones')

    #imagen=db.Column(db.String(400))
    def __init__(self,nombreProd,marca,descripcion,precio,categoria,proveedor):   #crea el  constructor de la clase
        self.nombreProd=nombreProd   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.marca=marca
        self.descripcion=descripcion
        self.precio=precio
        self.categoria=categoria
        self.proveedor=proveedor
        #self.imagen=imagen


with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************



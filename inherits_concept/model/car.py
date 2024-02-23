from odoo import models, fields, api

class CarModel(models.Model):
    _name = "car.car"

    name_car = fields.Char(string="name")
    speed = fields.Integer(string="Speed")
    cc = fields.Integer(string="CC")
    check = fields.Integer(string="Check")
    price = fields.Integer(string="Price")
    index = fields.Integer(string="index", readonly="1")

    def increment_button(self):
        self.index += 1



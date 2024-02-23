from odoo import models, fields, api

class CarModel(models.Model):
    _name = "car.super"
    _inherit = "car.car"
    name = fields.Char(string="name")
    super = fields.Char(string="Super")
    speed = fields.Integer(string="Speed")
    cc = fields.Integer(string="CC")
    price = fields.Integer(string="Price")
    index = fields.Integer(string="index")


from odoo import models, fields, api

class CarModel(models.Model):
    _name = "car.inherits"
    _inherits = {'car.super': 'car_super_id'}

    car_super_id = fields.Many2one('car.super', string="Super Car")
    name = fields.Char(string="Name")
    speed = fields.Integer(string="Speed")
    cc = fields.Integer(string="CC")
    price = fields.Integer(string="Price")
    final_price = fields.Integer(string="F Price")


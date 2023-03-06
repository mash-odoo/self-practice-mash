from odoo import models,fields

class ResUsers(models.Model):
    _inherit = "res.partner"

    product_ids = fields.One2many("shufflestuff.products", "customer_id")
    name= fields.Char()
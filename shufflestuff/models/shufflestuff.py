from odoo import models,fields

class Shufflestuff(models.Model):
    _name = "shufflestuff"
    _description = "Model for Upcycling"

    name = fields.Many2one("res.partner")
    company_name = fields.Char()
    street_1 = fields.Text()
    street_2 = fields.Text()
    city = fields.Text()
    state = fields.Text()
    country = fields.Many2one("res.country",string="Country")
    postcode = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    email = fields.Char()
    website = fields.Text()


    




    
    
    
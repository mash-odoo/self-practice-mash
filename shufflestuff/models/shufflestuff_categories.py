from odoo import models,fields

class ShufflestuffCategories(models.Model):
    _name="shufflestuff.categories"
    _description = "Shufflestuff Category"

    name = fields.Char()

    


from odoo import models,fields

class ShufflestuffProduct(models.Model):
    _name = 'shufflestuff.products'
    _description='Products'

    name = fields.Char(string='Name', required=True)
    description = fields.Text()
    brand = fields.Char()
    customer_id = fields.Many2one('shufflestuff', string='Customer')
    customer_mobile = fields.Many2one('shufflestuff', string='Mobile')
    category_id = fields.Many2one("shufflestuff.categories", string="Category")
    tag_id = fields.Many2many("shufflestuff.tags", string="Tags")
    price = fields.Integer(required=True)
    quality = fields.Selection([
        ('good', 'Good'),
        ('average', 'Average'),
        ('bad', 'Bad'),
    ], string='Quality', default='good', required=True)
    usage = fields.Selection([
        ('less', 'Less'),
        ('average', 'Average'),
        ('extensive', 'Extensive'),
    ], string='Usage', default='less', required=True)
    status = fields.Selection([
        ('reselling', 'Reselling'),
        ('maintenance', 'Maintenance'),
        ('scrapping', 'Scrapping'),
    ], string='Status', default='reselling', required=True)
    date = fields.Date("Date", default=lambda self:fields.Date.today())
    image = fields.Binary()
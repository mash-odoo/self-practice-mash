from odoo import models,fields,api
from odoo.addons.helpdesk.models.helpdesk_ticket import TICKET_PRIORITY

class ShufflestuffProduct(models.Model):
    _name = 'shufflestuff.products'
    _description='Products'

    name = fields.Char(string='Name', required=True)
    id = fields.Char()
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
        ('maintenance', 'Maintenance'),
        ('scrapping', 'Scrapping'),
        ('reselling', 'Reselling')
    ], string='Status', compute="compute_status")
    date = fields.Date("Date", default=lambda self:fields.Date.today())
    image = fields.Binary()

    mobile = fields.Char()
    email = fields.Char()
    country = fields.Char() 

    RATING = [
    ('0','Quality'),
    ('1', 'Worst'),
    ('2', 'Bad'),
    ('3', 'Average'),
    ('4', 'Good'),
    ('5','Best')
    ]

    rating = fields.Selection(RATING,string="Rating")

    @api.depends('rating','usage')
    def compute_status(self):
        for records in self:
            if records.rating in ['4','5'] and records.usage=='less':
                records.status = 'reselling'
            elif records.rating in ['4','5'] and records.usage=='average':
                records.status = 'reselling'
            elif records.rating in ['4','5'] and records.usage=='extensive':
                records.status = 'maintenance'
            elif records.rating in ['2','3'] and records.usage=='less':
                records.status = 'maintenance'
            elif records.rating in ['2','3'] and records.usage=='average':
                records.status = 'maintenance'
            elif records.rating in ['2','3'] and records.usage=='extensive':
                records.status = 'scrapping'
            else:
                records.status = 'scrapping'


    
        
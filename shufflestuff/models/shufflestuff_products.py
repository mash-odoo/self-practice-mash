from odoo import models,fields,api
from odoo.addons.helpdesk.models.helpdesk_ticket import TICKET_PRIORITY

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

    mobile = fields.Char()
    email = fields.Char()
    country = fields.Char() 

    priority = fields.Selection(
        TICKET_PRIORITY, string='Priority',
        default='0', required=True)

    
    # icon_1visi = fields.Boolean(default=True)
    # icon_2visi = fields.Boolean(default=True)

    # iconFields = [icon_1visi, icon_2visi]

    # def icon1_i(self):
    #     for i in range(1):
    #         self.iconFields[i] = False

    #     for i in range(1,len(self.iconFields)):
    #         self.iconFields[i] = True

    # def icon1_v(self):
    #     for i in range(1):
    #         self.iconFields[i] = True

    #     for i in range(1,len(self.iconFields)):
    #         self.iconFields[i] = False

    # def icon2_i(self):
    #     for i in range(2):
    #         self.iconFields[i] = False

    #     for i in range(2,len(self.iconFields)):
    #         self.iconFields[i] = True

    # def icon2_v(self):
    #     for i in range(2):
    #         self.iconFields[i] = True

    #     for i in range(2,len(self.iconFields)):
    #         self.iconFields[i] = False

        
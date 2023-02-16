from odoo import models,fields,api

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
    
    icon_1visi = fields.Boolean(default=True)
    icon_2visi = fields.Boolean(default=True)
    icon_3visi = fields.Boolean(default=True)
    icon_4visi = fields.Boolean(default=True)
    icon_5visi = fields.Boolean(default=True)

    icon_1visi = fields.Boolean()

    def icon1_i(self):
        self.icon_1visi = False

    def icon1_v(self):
        self.icon_1visi = True

    # stars = [icon_1visi, icon_2visi, icon_3visi, icon_4visi, icon_5visi]

    # def icon1_i(self):
    #     for i in range(1):
    #         self.stars[i].invisible = True

    # def icon2_i(self):
    #     for i in range(2):
    #         self.stars[i].invisible = True

    # def icon3_i(self):
    #     for i in range(3):
    #         self.stars[i].invisible = True

    # def icon4_i(self):
    #     for i in range(4):
    #         self.stars[i].invisible = True

    # def icon5_i(self):
    #     for i in range(5):
    #         self.stars[i].invisible = True

    # def icon1_v(self):
    #     for i in range(1):
    #         self.stars[i].invisible = False

    # def icon2_v(self):
    #     for i in range(2):
    #         self.stars[i].invisible = False

    # def icon3_v(self):
    #     for i in range(3):
    #         self.stars[i].invisible = False

    # def icon4_v(self):
    #     for i in range(4):
    #         self.stars[i].invisible = False

    # def icon5_v(self):
    #     for i in range(5):
    #         self.stars[i].invisible = False
    
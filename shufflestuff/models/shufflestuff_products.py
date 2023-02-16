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
    
    icon1_i = fields.Boolean()
    icon2_i = fields.Boolean()
    icon3_i = fields.Boolean()
    icon4_i = fields.Boolean()
    icon5_i = fields.Boolean()
    icon1_v = fields.Boolean()
    icon2_v = fields.Boolean()
    icon3_v = fields.Boolean()
    icon4_v = fields.Boolean()
    icon5_v = fields.Boolean()
    # icon1_v,icon2_v,icon3_v,icon4_v,icon5_v = fields.Char()

    stars_i = [icon1_i,icon2_i,icon3_i,icon4_i,icon5_i]
    stars_v = [icon1_v,icon2_v,icon3_v,icon4_v,icon5_v]

    def icon1_i(self):
        for i in range(1):
            self.icon1_i[i].invisible = False

    def icon2_i(self):
        for i in range(2):
            self.icon1_i[i].invisible = False

    def icon3_i(self):
        for i in range(3):
            self.icon1_i[i].invisible = False

    def icon4_i(self):
        for i in range(4):
            self.icon1_i[i].invisible = False

    def icon5_i(self):
        for i in range(5):
            self.icon1_i[i].invisible = False
                
    # def change_icon_color(self):
    #     self.write({'icon': 'fa-star', 'icon_color': 'yellow'})

    # def change_icon_color(self):
    #     if self.icon=='fa-times':
    #         print("hi")
    #         self.icon='fa-check'

    icon_1visi = fields.Boolean(default=True)

    def icon_1(self):
        self.icon_1visi=False

    def icon_2(self):
        self.icon_1visi=True
    
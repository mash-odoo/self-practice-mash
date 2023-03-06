# from odoo import models,fields,api

# class ShufflestuffOrders(models.Model):
#     _name = 'shufflestuff.orders'
#     _description='Products'
#     _inherit = "sale.order"
#     # name = fields.Char(string='Name', required=True)
#     # id = fields.Char()
#     # description = fields.Text()

#     customer_id = fields.Many2one('shufflestuff', options="{'no_create':True}", string='Customer')
#     mobile = fields.Char(related="customer_id.mobile")
#     email = fields.Char(related="customer_id.email")
#     country = fields.Many2one(related="customer_id.country") 
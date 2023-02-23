from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ShufflestuffCategories(models.Model):
    _name="shufflestuff.categories"
    _description = "Shufflestuff Category"

    name = fields.Char()

    @api.constrains('name')
    def _check_unique_name(self):
        tag_ids = self.search([]) - self
        value = [x.name.lower() for x in tag_ids]
        if self.name and self.name.lower() in value:
            raise ValidationError(('This category already Exists'))
        return True

    


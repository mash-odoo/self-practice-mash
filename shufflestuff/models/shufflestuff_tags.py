from odoo import models,fields,api
from odoo.exceptions import ValidationError

class ShufflestuffTag(models.Model):
    _name="shufflestuff.tags"
    _description = "Shufflestuff Tag"

    name = fields.Char()

    @api.constrains('name')
    def _check_unique_name(self):
        tag_ids = self.search([]) - self
        value = [x.name.lower() for x in tag_ids]
        if self.name and self.name.lower() in value:
            raise ValidationError(('This tag already Exists'))
        return True

    

    


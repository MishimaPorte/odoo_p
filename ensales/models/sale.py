from odoo import models, fields as f, api
import random
import json

def get_random(self):
    return random.randint(0, 1000000000)


class Sale(models.Model):
    _inherit = "sale.order"

    test = f.Char(string="Test", default = get_random)

    @api.onchange("test")
    def _onchange_test_warning_50_symbols(self):
        if self.test.__len__() > 50:
            self.test = self.test[0:50]
            return {"warning": {"title": "Too many symbols!", "message": "Your message should be less then 50 symbols long. Violation of this principle results in the message being cropped to be 50 symbols maximum"}}

    @api.onchange("date_order")
    def _onchenge_date_order(self):
        total_json = json.loads(self.tax_totals_json)
        self.test = f"{total_json['amount_total']} - {self.date_order}"

    @api.onchange("tax_totals_json")
    def _onchenge_total(self):
        total_json = json.loads(self.tax_totals_json)
        self.test = f"{total_json['amount_total']} - {self.date_order}"

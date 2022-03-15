# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tests import Form


class MrpProduction(models.Model):
    _inherit = "mrp.production"

    def set_qty_producing(self, qty):
        fo = Form(self)
        fo.qty_producing = qty
        fo.save()
        return True

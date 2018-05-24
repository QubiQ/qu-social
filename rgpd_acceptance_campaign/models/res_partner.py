# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jiménez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    response_rgpd = fields.Selection([
        ('yes', 'Sí'),
        ('no', 'No',)],
        string="RGPD Response",
        readonly=True,
    )
    date_response = fields.Char(
        string="Response date",
        readonly=True,
    )

    def partner_get_access_token(self):
        response = self.env['rgpd.acceptance.response'].filtered(
            lambda x: x.partner_id.id == self.id and not x.consumed)
        if not response:
            response = self.env['rgpd.acceptance.response'].create({
                'partner_id': self.id,
            })
        return response.access_token

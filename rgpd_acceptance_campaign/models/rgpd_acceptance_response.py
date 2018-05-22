# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jiménez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import uuid

from openerp import models, fields, api


class RGPDAcceptanceResponse(models.Model):
    _name = "rgpd.acceptance.response"

    @api.model
    def new_access_token(self):
        return uuid.uuid4().hex

    partner_id = fields.Many2one(
        'res.partner',
        string="Partner",
    )
    access_token = fields.Char(
        string="Security Token",
        default=new_access_token,
        help="Access token to set the rating of the value",
    )
    consumed = fields.Boolean(
        string="Consumed",
        default=False,
    )
    response = fields.Selection([
        ('yes', 'Sí'),
        ('no', 'No',)],
        string="Accepted RGPD",
    )

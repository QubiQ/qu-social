# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jiménez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openerp import http
from openerp.http import request

import logging
_logger = logging.getLogger(__name__)


class RGPDAcceptanceResponse(http.Controller):

    @http.route(
        '/rgpd/<string:token>/<string:response>', type='http', auth="public")
    def get_rgpd_response(self, token, response, **kwargs):
        response_obj = request.env['rgpd.acceptance.response'].sudo().search([(
            'access_token', '=', token)])
        if not response_obj:
            return request.not_found()

        response_obj.write({
            'consumed': True,
            'response': response,
        })
        response_obj.partner_id.write({
            'accepted_rgpd': response,
        })
        return request.render(
            'rgpd_acceptance_campaign.rgpd_response_confirmation_template')

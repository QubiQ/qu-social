# -*- coding: utf-8 -*-
# Copyright 2018 Xavier Jiménez <xavier.jimenez@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'RGPD Acceptance Campaign',
    'version': '8.0.1.0.1',
    'summary': 'RGPD Acceptance Campaign',
    'category': 'Mailing',
    "website": "https://www.qubiq.es",
    "author": "QubiQ",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "base",
        "sale",
        "mail",
    ],
    "data": [
        "data/rgpd_partner_template.xml",
        "data/rgpd_response_confirmation_template.xml",
        "views/res_partner_view.xml",
    ],
}

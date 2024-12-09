#  Copyright 2024 Simone Rubino - Aion Tech
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).


from odoo import models


class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _require_login_whitelist_paths(cls):
        whitelist_paths = super()._require_login_whitelist_paths()
        whitelist_paths.extend(
            [
                "/queue_job/runjob",
            ]
        )
        return whitelist_paths

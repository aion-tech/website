#  Copyright 2024 Simone Rubino - Aion Tech
#  License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

from pathlib import Path
from urllib import parse

from odoo.tests import HttpCase
from odoo.tools import mute_logger


class TestIrHttp(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.website = cls.env["website"].sudo().get_current_website()

    def test_authorize_queue_job_controller(self):
        """Requiring "/" does not prevent Jobs to run."""
        # Arrange
        authorized_path = "/"
        self.env["website.auth.url"].create(
            [
                {
                    "website_id": self.website.id,
                    "path": authorized_path,
                },
            ],
        )
        queue_job_path = "/queue_job/runjob"
        # pre-condition
        self.assertIn(Path(authorized_path), Path(queue_job_path).parents)

        # Assert
        with mute_logger("odoo.addons.queue_job.controllers.main"):
            # Muted because it logs that the called job does not exist
            response = self.url_open("%s?db=''&job_uuid=''" % queue_job_path)
        self.assertEqual(parse.urlparse(response.url).path, queue_job_path)

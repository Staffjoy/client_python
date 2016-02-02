import os

from staffjoy import Client

from . import logger
"""
This test file is intended for use in continuous integration. It runs
against the Staging environment of Staffjoy in a dedicated functional
testing organization. We will not be giving public access to Staffjoy
stage, but you can modify this script to run against your own org.
For a developer access, please email help@staffjoy.com
"""

TEST_ORG = 18
ENV = "stage"
KEY = os.environ.get("STAFFJOY_STAGE_API_KEY")


def test_org_crud():
    c = Client(key=KEY, env=ENV)

    logger.debug("Fetching organization")
    o = c.get_organization(TEST_ORG)

    # Changing org name
    o.patch(name="[Start] Continuous integration test")

    logger.debug("Finishing up")
    o.patch(name="Continuous integration test")

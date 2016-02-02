import os

import pytest

from staffjoy import Client, UnauthorizedException

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
TEST_WORKER = "feynman@7bridg.es"


def test_org_crud():
    c = Client(key=KEY, env=ENV)

    # Just some basic stuff
    assert len(c.get_plans()) > 0
    assert len(c.get_timezones()) > 0

    logger.debug("Fetching organization")
    o = c.get_organization(TEST_ORG)

    assert o.get_id() == TEST_ORG

    location_count = len(o.get_locations())

    logger.debug("Changing organization name")
    o.patch(name="[In Progress] Continuous integration test")

    logger.debug("Creating a location")
    l = o.create_location(name="El Farolito", timezone="America/Los_Angeles")
    l_id = l.get_id()
    logger.debug("Location id {}".format(l_id))

    assert l.data.get("name") == "El Farolito"
    logger.debug("Changing location name")
    l.patch(name="La Taqueria")

    logger.debug("Checking that location is created")
    new_location_count = len(o.get_locations())
    assert new_location_count == (location_count + 1)
    del l

    logger.debug("Fetching location by ID")
    l = o.get_location(l_id)
    assert l.data.get("name") == "La Taqueria"

    logger.debug("Testing role crud")
    r = l.create_role(name="Kitchen")
    r.patch(name="Cocina")
    logger.debug("Adding worker")
    r.get_workers()
    r.create_worker(email=TEST_WORKER)
    r.delete()

    logger.debug("Deleting location")
    l.delete()
    del l
    logger.debug("Making sure location no longer exists")

    with pytest.raises(UnauthorizedException):
        o.get_location(l_id)

    logger.debug("Finishing up")
    o.patch(name="Continuous integration test")
    all_locations = o.get_locations()
    for location in all_locations:
        location.delete()

    assert 0 == len(o.get_locations())

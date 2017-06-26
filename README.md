# client_python

A light wrapper for the [Staffjoy](https://www.staffjoy.com) API in Python.

This library does not include permissions management, and it is primarily used across microservices internally. Some of its features include internal-only endpoints.

[![Build Status](https://travis-ci.org/Staffjoy/client_python.svg?branch=master)](https://travis-ci.org/Staffjoy/client_python) [![Moonlight contractors](https://img.shields.io/badge/contractors-1147-brightgreen.svg)](https://moonlightwork.com/for/staffjoy)

## Installation

`pip install --upgrade staffjoy`

## Self-Hosted Use

If you are self-hosting Staffjoy on a custom domain, please pass a `url_base` to the client. It defaults to `https://suite.staffjoy.com/api/v2/"`. (Trailing slash may matter).

```python
from Staffjoy import Client
c = Client(key=YOUR_API_KEY, url_base="https://staffjoy.example.com/api/v2/")
```

## Authentication

Authentication keys are currently tied to an individual user's account. To issue multiple keys, we currently suggest 

* **Permanent**: Every Staffjoy account includes a permanent API token that can be accessed from [My Account](https://www.staffjoy.com/auth/api-key) while logged in. 
* **Time-based (6-hour)**: To issue an API token that is valid for 6 hours, visit [this link](https://www.staffjoy.com/auth/api-token) while logged in (note: it is JSON-encoded)
* **Time-based (other lengths)**: Please email help@staffjoy.com

To get your organization ID, look at the URL path when you go to the Manager app while logged in.

## Rate Limits

This client sleeps after every request in order to limit requests to 120 per minute. This is done to avoid rate limiting. Staffjoy's API currently rate limits to 300 requests per second across keys and IPs. Thus, by using this library, you should never encounter a rate limit (assuming one executing thread per IP address).

## Usage

Start with the client, then traverse the tree.

```python
from Staffjoy import Client

c = Client(key=YOUR_API_KEY)

# To get your organization id, look at the URL path for the Manager
# or email help@staffjoy.com
org = c.get_organization(ORG_ID)

# See the org name
print(org.data.get("name))

# See all locations
org.get_locations()

# Add an new location
loc = org.create_location(name="Staffjoy HQ", timezone="America/Los_Angeles")

# Modify its name
loc.patch(name="San Francisco")

# See roles
roles = loc.get_roles()

# Create a role and add a worker for scheduling
role = loc.create_role(name="Mathematicians")
role.create_worker(email="dantzig@7bridg.es")

# Then clean it all up (recursively deletes node children)
loc.delete()

```



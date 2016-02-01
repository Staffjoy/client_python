# staffjoy-python

A light wrapper for the [Staffjoy](https://www.staffjoy.com) API. 

This library does not include permissions management, and it is primarily used across microservices internally. Some of its features include internal-only endpoints.

## Installation

TODO - Pypi / pip?

## Authentication

Authentication keys are currently tied to an individual user's account. To issue multiple keys, we currently suggest 

** Permanant: Every Staffjoy account includes a permanent API token that can be accessed from [My Account](https://www.staffjoy.com/auth/api-key) while logged in. 
** Time-based (6-hour): To issue an API token that is valid for 6 hours, visit [this link]({https://www.staffjoy.com/auth/api-token) while logged in: (note: it is JSON-encoded)
** Time-based (other lengths): Please email help@staffjoy.com


To get your organization ID, look at the URL path when you go to the Manager app while logged in.

## Updates

If you use this library, please subscribe to the [Staffjoy API Updates Google Group](https://groups.google.com/forum/#!forum/staffjoy-api-updates) for important notifications about changes and deprecations.

## Usage


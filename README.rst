Python Client for Service Usage API
===================================

|ga| |pypi| |versions|

`Service Usage`_: is an infrastructure service of Google Cloud that lets you list and manage other APIs 
and services in your Cloud projects. You can list and manage Google Cloud services and their APIs, as 
well as services created using Cloud Endpoints.

- `Client Library Documentation`_
- `Product Documentation`_

.. |ga| image:: https://img.shields.io/badge/support-ga-gold.svg
   :target: https://github.com/googleapis/google-cloud-python/blob/main/README.rst#ga-support
.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-service-usage.svg
   :target: https://pypi.org/project/google-cloud-service-usage/
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-service-usage.svg
   :target: https://pypi.org/project/google-cloud-service-usage/
.. _Service Usage: https://cloud.google.com/service-usage
.. _Client Library Documentation: https://cloud.google.com/python/docs/reference/serviceusage/latest
.. _Product Documentation:  https://cloud.google.com/service-usage/docs

Quick Start
-----------

In order to use this library, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`_
2. `Enable billing for your project.`_
3. `Enable the Service Usage API.`_
4. `Setup Authentication.`_

.. _Select or create a Cloud Platform project.: https://console.cloud.google.com/project
.. _Enable billing for your project.: https://cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project
.. _Enable the Service Usage API.:  https://cloud.google.com/service-usage/docs/getting-started#enable
.. _Setup Authentication.: https://googleapis.dev/python/google-api-core/latest/auth.html

Installation
~~~~~~~~~~~~

Install this library in a `virtualenv`_ using pip. `virtualenv`_ is a tool to
create isolated Python environments. The basic problem it addresses is one of
dependencies and versions, and indirectly permissions.

With `virtualenv`_, it's possible to install this library without needing system
install permissions, and without clashing with the installed system
dependencies.

.. _`virtualenv`: https://virtualenv.pypa.io/en/latest/


Mac/Linux
^^^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    source <your-env>/bin/activate
    <your-env>/bin/pip install google-cloud-service-usage


Windows
^^^^^^^

.. code-block:: console

    pip install virtualenv
    virtualenv <your-env>
    <your-env>\Scripts\activate
    <your-env>\Scripts\pip.exe install google-cloud-service-usage

Next Steps
~~~~~~~~~~

-  Read the `Client Library Documentation`_ for Service Usage API
   to see other available methods on the client.
-  Read the `Service Usage API Product documentation`_ to learn
   more about the product and see How-to Guides.
-  View this `README`_ to see the full list of Cloud
   APIs that we cover.

.. _Service Usage API Product documentation:  https://cloud.google.com/service-usage/docs
.. _README: https://github.com/googleapis/google-cloud-python/blob/main/README.rst
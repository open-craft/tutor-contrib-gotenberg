unoserver plugin for `Tutor <https://docs.tutor.edly.io>`__
###########################################################

Plugin to set up unoserver in a docker container for converting documents.

The [unoserver](https://github.com/unoconv/unoserver-docker) project uses
LibreOffice for converting between documents. This tutor plugin will set up the
tool in a docker container which can then be used by other services to perform
document conversions.

It was developed for use with the PDF XBlock to allow course authors to
automatically provide students with a PDF version of their documents.


Installation
************

.. code-block:: bash

    pip install git+https://github.com/open-craft/tutor-contrib-unoserver

Usage
*****

.. code-block:: bash

    tutor plugins enable unoserver

Testing
*******

To test this XBlock in development mode, you can install the "unoserver" pip
package locally, making sure to use version specified in "UNOSERVER_PACKAGE_VERSION"
for best compatibility. You can then run `unoconvert` as follows:

.. code-block:: bash

    unoconvert --host-location remote --port 20003 [INFILE] [OUTFILE]

This will have the tool connect to the server running in the docker container.

License
*******

This software is licensed under the terms of the AGPLv3.

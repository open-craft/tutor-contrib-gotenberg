Gotenberg plugin for `Tutor <https://docs.tutor.edly.io>`__
###########################################################

Plugin to set up Gotenberg in a docker container for converting documents.

The [Gotenberg](https://github.com/gotenberg/gotenberg) project uses Chrome and
LibreOffice for converting between documents. This tutor plugin will set up the
service in a Docker container or in Kubernetes for use by other services to
perform document conversions.

It was developed for use with the PDF XBlock to allow course authors to
automatically provide students with a PDF version of their documents.


Installation
************

.. code-block:: bash

    pip install tutor-contrib-gotenberg@git+https://gitlab.com/opencraft/dev/tutor-contrib-gotenberg.git

Usage
*****

.. code-block:: bash

    tutor plugins enable gotenberg

Testing
*******

To test this XBlock in development mode, you can install the "gotenberg" pip
package locally, making sure to use version specified in "GOTENBERG_PACKAGE_VERSION"
for best compatibility. You can then test it as follows:

.. code-block:: bash

    curl --request POST http://localhost:3000/forms/libreoffice/convert --form files=@infile.docx -o outfile.pdf

This will have the tool connect to the server running in the docker container.

License
*******

This software is licensed under the terms of the AGPLv3.

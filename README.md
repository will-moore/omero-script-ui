
[![Actions Status](https://github.com/will-moore/omero-script-ui/workflows/OMERO/badge.svg)](https://github.com/will-moore/omero-script-ui/actions)


OMERO.omero_script_ui
==================================

This is an experimental repo to explore the steps needed to create custom user interfaces
for running OMERO scripts. It is hoped that this process can be improved and documented
to make it easier for users who wish to develop UIs for their OMERO scripts.

The process currently involves these key steps, as followed when creating
the first example UI for [Import_from_csv.py](https://github.com/ome/omero-scripts/blob/8dc923b3206cbc1334dbcb7eead6e60f222982c3/omero/annotation_scripts/Import_from_csv.py). NB: these steps can be seen in the first few commits of this repo:

 - Create a new repo from [cookiecutter-omero-webapp](https://github.com/ome/cookiecutter-omero-webapp).
 - Run `git init` and start tracking changes.
 - In the OMERO webclient, launch the script you wish to create a UI for and copy the html for the script dialog.
 - Add a url to urls.py with a corresponding views.py method and html template, using the script dialog html.
 - Remove all the script tags. This aims to reduce dependencies on jQuery etc that are used in the webclient script dialog, but removal of ajax-form functionality does result in a less smooth user experience. Needs more investigation on best approach.
 - In the views.py we need to look-up the correct script based on path, pass the ID to the template and use it to render the correct path to submit the form to webclient.
 - Add a `csrf_token` to the form.
 - Add `enctype='multipart/form-data'` attribute to the `<form>` element to all inclusion of Files.
 - Ajax form handling for script UI with vanilla JavaScript.
 - Add [open_with](https://omero.readthedocs.io/en/stable/developers/Web/LinkingFromWebclient.html#open-with) functionality: Add config to the README and handle query parameters in views.py to process and pass objects to the html template.


 At this point you should have a working UI that you can then customise further as desired, e.g.

 - Rearrange form inputs to present a more intuitive and helpful layout to users.
 - Load additional data based on selected objects to improve the script UI. E.g. load images in a selected Dataset or show Images or thumbnails in the UI.
 - Add some interactivity to the form, so users can appreciate the effect of choosing different options.
 - Based on the user's interactions, it may be possible to auto-populate various form fields (script parameters).

In the case of `Import_from_csv.py`, the following improvements were made:
 - Add a drag-and-drop file uploader to allow easier upload of a chosen CSV file.
 - Display the chosen CSV file as an html table with options for choosing columns.
 - Allow the user to select a table column that contains target object identifiers.


Installation
============

This section assumes that an OMERO.web is already installed.

Installing from Pypi
--------------------

Install the app using [pip](<https://pip.pypa.io/en/stable/>) .

Ensure that you are running ``pip`` from the Python environment
where ``omero-web`` is installed. Depending on your install, you may need to
call ``pip`` with, for example: ``/path/to_web_venv/venv/bin/pip install ...``

::

    $ pip install -U omero-script-ui


Development mode
----------------

Install `omero-script-ui` in development mode as follows:

    # within your python venv:
    $ cd omero-script-ui
    $ pip install -e .

After installation either from [Pypi](https://pypi.org/) or in development mode, you need to configure the application.
To add the application to the `omero.web.apps` settings, run the following command:

Note the usage of single quotes around double quotes:

    $ omero config append omero.web.apps '"omero_script_ui"'

Optionally, add a link "Script UI" at the top of the webclient to
open the index page of this app:

    $ omero config append omero.web.ui.top_links '["Script UI", "omero_script_ui_index", {"title": "Open Script UI in new tab", "target": "_blank"}]'


Configure Open-with for individual scripts. Currently just one supported (requires https://github.com/ome/omero-scripts/pull/216)

    $ omero config append omero.web.open_with '["Import Annotations from CSV", "omero_script_ui_import_from_csv", {"supported_objects": ["projects", "datasets", "images", "screens", "plates"]}]'


Now restart your `omero-web` server and go to
<http://localhost:4080/omero_script_ui/> in your browser.


Further Info
============

1. This app was derived from [cookiecutter-omero-webapp](https://github.com/ome/cookiecutter-omero-webapp).
2. For further info on deployment, see [Deployment](https://docs.openmicroscopy.org/latest/omero/developers/Web/Deployment.html)


License
=======

This project, similar to many Open Microscopy Environment (OME) projects, is
licensed under the terms of the AGPL v3.


Copyright
=========

2024 University of Dundee


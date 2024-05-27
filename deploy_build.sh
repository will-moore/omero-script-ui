#!/bin/bash

echo "Deploying built resources..."

# output dir is static dir (js & css in correct place) - only need to move index.html
mkdir -p omero_script_ui/templates/omero_script_ui/
cp omero_script_ui/static/omero_script_ui/index.html omero_script_ui/templates/omero_script_ui/

#!/usr/bin/env python
#
# Copyright (c) 2024 University of Dundee.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.urls import re_path

from . import views

urlpatterns = [
    # index 'home page' of the app
    re_path(r"^$", views.index, name="omero_script_ui_index"),

    re_path(r"^import_from_csv/$", views.import_from_csv,
            name="omero_script_ui_import_from_csv"),

    re_path(r"^post_file_annotation/$", views.post_file_annotation,
            name="scriptui_post_file_annotation"),

    re_path(r"^read_csv_annotation/(?P<ann_id>[0-9]+)/$",
            views.read_csv_annotation,
            name="scriptui_read_csv_annotation"),
]

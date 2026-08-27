from __future__ import annotations

import os
from glob import glob

import importlib_resources
from tutor import hooks

########################################
# CONFIGURATION
########################################

hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        ("GOTENBERG_DOCKER_IMAGE", "gotenberg/gotenberg:8"),
        # The port Gotenberg responds to when calling it from within the LMS/CMS.
        # You probably don't need to change this.
        ("GOTENBERG_PORT", "3000"),
        # Used in docker-compose environments where 3000 is occupied, but you may
        # wish to access the service from the host.
        ("GOTENBERG_DC_HOST_PORT", "3000"),
    ]
)


########################################
# DOCKER IMAGE MANAGEMENT
########################################

hooks.Filters.IMAGES_BUILD.add_items(
    [
        (
            "gotenberg",
            ("plugins", "gotenberg", "build"),
            "{{ gotenberg_DOCKER_IMAGE }}",
            (),
        ),
    ]
)

hooks.Filters.IMAGES_PULL.add_items([("gotenberg", "{{ gotenberg_DOCKER_IMAGE }}")])


########################################
# TEMPLATE RENDERING
########################################

hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    [
        str(importlib_resources.files("tutorgotenberg") / "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("gotenberg/build", "plugins"),
        ("gotenberg/apps", "plugins"),
    ],
)


########################################
# PATCH LOADING
########################################

# For each file in tutorgotenberg/patches,
# apply a patch based on the file's name and contents.
for path in glob(str(importlib_resources.files("tutorgotenberg") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))

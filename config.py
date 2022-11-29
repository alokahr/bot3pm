#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "863a21ef-e8b1-4ef4-927d-22303ce545d9")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "1gc8Q~gxgtSXazccqOIelER0piWuzlcfWcCnJbcm")

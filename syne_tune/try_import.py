# Copyright 2021 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

def try_import_gpsearchers_message() -> str:
    return _try_import_message(
        "Gaussian process based searchers are not imported",
        tag="gpsearchers"
    )


def try_import_kde_message() -> str:
    return _try_import_message(
        "KDE searchers are not imported",
        tag="kde"
    )


def try_import_bore_message() -> str:
    return _try_import_message(
        "BORE searchers are not imported",
        tag="bore"
    )


def try_import_raytune_message() -> str:
    return _try_import_message(
        "Ray Tune schedulers and searchers are not imported",
        tag="raytune"
    )


def _try_import_message(
        message_text: str,
        tag: str
) -> str:
    return (
        message_text
        + " since dependencies are missing. You can install them with\n"
        + f"   pip install 'syne-tune[{tag}]'\n"
        + "or (for everything)\n"
        + "   pip install 'syne-tune[extra]'"
    )

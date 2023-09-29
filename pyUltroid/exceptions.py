# Akki - UserBot
# Copyright (C) 2021-2023 TeamAkki
#
# This file is a part of < https://github.com/TeamAkki/Akki/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamAkki/pyAkki/blob/main/LICENSE>.

"""
Exceptions which can be raised by py-Akki Itself.
"""


class pyUltroidError(Exception):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUltroidError):
    ...

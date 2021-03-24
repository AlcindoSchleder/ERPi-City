# -*- coding: utf-8 -*-

from erpicity import __version__


def erpicity_version(request):
    return {'versao': __version__}

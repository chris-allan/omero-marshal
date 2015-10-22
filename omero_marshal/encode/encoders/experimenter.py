#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Glencoe Software, Inc. All rights reserved.
#
# This software is distributed under the terms described by the LICENCE file
# you can find at the root of the distribution bundle.
# If the file is missing please request a copy by contacting
# jason@glencoesoftware.com.
#

from .. import Encoder
from omero.model import ExperimenterI


class ExperimenterEncoder(Encoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/OME/2015-01#Experimenter'

    def encode(self, obj):
        v = super(ExperimenterEncoder, self).encode(obj)
        if not obj.isLoaded():
            return v
        self.set_if_not_none(v, 'FirstName', obj.firstName)
        self.set_if_not_none(v, 'MiddleName', obj.middleName)
        self.set_if_not_none(v, 'LastName', obj.lastName)
        self.set_if_not_none(v, 'Email', obj.email)
        self.set_if_not_none(v, 'Institution', obj.institution)
        self.set_if_not_none(v, 'UserName', obj.omeName)
        return v

encoder = (ExperimenterI, ExperimenterEncoder)

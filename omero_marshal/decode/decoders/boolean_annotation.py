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

from .annotation import AnnotationDecoder
from omero.model import BooleanAnnotationI


class BooleanAnnotationDecoder(AnnotationDecoder):

    TYPE = 'http://www.openmicroscopy.org/Schemas/SA/2015-01#BooleanAnnotation'

    OMERO_CLASS = BooleanAnnotationI

    def decode(self, data):
        v = super(BooleanAnnotationDecoder, self).decode(data)
        v.boolValue = self.to_rtype(data.get('Value'))
        return v

decoder = (BooleanAnnotationDecoder.TYPE, BooleanAnnotationDecoder)

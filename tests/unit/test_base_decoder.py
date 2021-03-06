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

import json

from omero.model import RoiI
from omero_marshal import get_encoder, get_decoder


class TestBaseDecoder(object):

    def assert_roi(self, roi, has_annotations=False):
        assert roi.__class__ == RoiI
        assert roi.id.val == 1L
        assert roi.name.val == 'the_name'
        assert roi.description.val == 'the_description'
        if not has_annotations:
            assert not roi.annotationLinksLoaded

    def test_base_decoder(self, roi):
        encoder = get_encoder(roi.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(roi)
        v = decoder.decode(v)
        self.assert_roi(v)

    def test_base_decoder_from_string(self):
        data_as_string = """{
    "@type": "http://www.openmicroscopy.org/Schemas/ROI/2015-01#ROI",
    "@id": 1,
    "Name": "the_name",
    "Description": "the_description"
}"""
        data = json.loads(data_as_string)
        decoder = get_decoder(data['@type'])
        v = decoder.decode(data)
        self.assert_roi(v)


class TestPermissionsDecoder(object):

    def test_permissions(self, permissions):
        encoder = get_encoder(permissions.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(permissions)
        v = decoder.decode(v)
        assert v.canLink()
        assert v.canEdit()
        assert v.canDelete()
        assert v.canAnnotate()

    def test_permissions_cannot_link(self, permissions_cannot_link):
        encoder = get_encoder(permissions_cannot_link.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(permissions_cannot_link)
        v = decoder.decode(v)
        assert not v.canLink()
        assert v.canEdit()
        assert v.canDelete()
        assert v.canAnnotate()

    def test_permissions_cannot_edit(self, permissions_cannot_edit):
        encoder = get_encoder(permissions_cannot_edit.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(permissions_cannot_edit)
        v = decoder.decode(v)
        assert v.canLink()
        assert not v.canEdit()
        assert v.canDelete()
        assert v.canAnnotate()

    def test_permissions_cannot_delete(self, permissions_cannot_delete):
        encoder = get_encoder(permissions_cannot_delete.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(permissions_cannot_delete)
        v = decoder.decode(v)
        assert v.canLink()
        assert v.canEdit()
        assert not v.canDelete()
        assert v.canAnnotate()

    def test_permissions_cannot_annotate(self, permissions_cannot_annotate):
        encoder = get_encoder(permissions_cannot_annotate.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(permissions_cannot_annotate)
        v = decoder.decode(v)
        assert v.canLink()
        assert v.canEdit()
        assert v.canDelete()
        assert not v.canAnnotate()

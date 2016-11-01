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

from omero_marshal import get_encoder, get_decoder
from omero.model import LengthI
from omero.model.enums import UnitsLength


class TestProjectDecoder(object):

    def assert_project(self, project):
        assert project.name.val == 'the_name'
        assert project.description.val == 'the_description'

    def test_project_decoder(self, project):
        encoder = get_encoder(project.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project)
        v = decoder.decode(v)
        self.assert_project(v)
        assert v.sizeOfDatasetLinks() == 0

    def test_project_with_datasets_decoder(self, project_with_datasets):
        encoder = get_encoder(project_with_datasets.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(project_with_datasets)
        v = decoder.decode(v)
        assert v.id.val == 1L
        assert v.name.val == 'the_name'
        assert v.description.val == 'the_description'
        assert v.sizeOfDatasetLinks() == 2
        dataset_1, dataset_2 = v.linkedDatasetList()
        assert dataset_1.id.val == 1L
        assert dataset_1.name.val == 'dataset_name_1'
        assert dataset_1.description.val == 'dataset_description_1'
        assert dataset_2.id.val == 2L
        assert dataset_2.name.val == 'dataset_name_2'
        assert dataset_2.description.val == 'dataset_description_2'


class TestScreenDecoder(object):

    def assert_screen(self, screen):
        assert screen.name.val == 'the_name'
        assert screen.description.val == 'the_description'
        assert screen.protocolDescription.val == 'the_protocol_description'
        assert screen.protocolIdentifier.val == 'the_protocol_identifier'
        assert screen.reagentSetDescription.val == 'the_reagent_set_description'
        assert screen.reagentSetDescription.val == 'the_reagent_set_description'
        assert screen.reagentSetIdentifier.val == 'the_reagent_set_identifier'
        assert screen.type.val == 'the_type'

    def assert_plate(self, plate, plate_id):
        assert plate.id.val == plate_id
        assert plate.name.val == 'plate_name_%d' % plate_id
        assert plate.description.val == 'plate_description_%d' % plate_id
        assert plate.columnNamingConvention.val == 'number'
        assert plate.rowNamingConvention.val == 'letter'
        assert plate.columns.val == 12
        assert plate.rows.val == 8
        assert plate.defaultSample.val == 0
        assert plate.externalIdentifier.val == 'external_identifier_%d' % plate_id
        assert plate.status.val == 'status_%d' % plate_id
        assert plate.wellOriginX.__class__ is LengthI
        assert plate.wellOriginX.getUnit() == UnitsLength.REFERENCEFRAME
        assert plate.wellOriginX.getValue() == 0.1
        assert plate.wellOriginY.__class__ is LengthI
        assert plate.wellOriginY.getUnit() == UnitsLength.REFERENCEFRAME
        assert plate.wellOriginY.getValue() == 1.1

    def test_screen_decoder(self, screen):
        encoder = get_encoder(screen.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(screen)
        v = decoder.decode(v)
        self.assert_screen(v)
        assert v.sizeOfPlateLinks() == 0

    def test_screen_with_plates_decoder(self, screen_with_plates):
        encoder = get_encoder(screen_with_plates.__class__)
        decoder = get_decoder(encoder.TYPE)
        v = encoder.encode(screen_with_plates)
        v = decoder.decode(v)
        self.assert_screen(v)
        assert v.id.val == 4L
        assert v.sizeOfPlateLinks() == 2
        plate_1, plate_2 = v.linkedPlateList()
        self.assert_plate(plate_1, 5)
        self.assert_plate(plate_2, 6)

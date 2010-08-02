import unittest

from mopidy.backends.dummy import DummyBackend
from mopidy.mixers.dummy import DummyMixer
from mopidy.mpd import frontend

class AudioOutputHandlerTest(unittest.TestCase):
    def setUp(self):
        self.m = DummyMixer()
        self.b = DummyBackend(mixer=self.m)
        self.h = frontend.MpdFrontend(backend=self.b)

    def test_enableoutput(self):
        result = self.h.handle_request(u'enableoutput "0"')
        self.assert_(u'ACK [0@0] {} Not implemented' in result)

    def test_disableoutput(self):
        result = self.h.handle_request(u'disableoutput "0"')
        self.assert_(u'ACK [0@0] {} Not implemented' in result)

    def test_outputs(self):
        result = self.h.handle_request(u'outputs')
        self.assert_(u'outputid: 0' in result)
        self.assert_(u'outputname: DummyBackend' in result)
        self.assert_(u'outputenabled: 1' in result)
        self.assert_(u'OK' in result)

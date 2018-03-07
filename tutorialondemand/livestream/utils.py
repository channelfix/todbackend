from django.conf import settings
from opentok import OpenTok


class OpenTokResource(object):
    opentok = OpenTok(settings.APIKEY, settings.OPENTOKSECRETKEY)

    @classmethod
    def get_client(self):
        return self.opentok

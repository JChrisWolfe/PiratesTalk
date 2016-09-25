from configuration import settings
from network.singleton import Singleton
from urllib.request import urlopen
import urllib
import time


class PirateService(metaclass=Singleton):

    """
        A class which uses the webservice http://isithackday.com/arrpi.php to translate any given text
        to pirate idiom
    """
    def __init__(self):
        self.request_url = settings.network['request_url']
        self.max_retries = settings.network['max_retries']
        self.interval_between_retries = settings.network['interval_between_retries']


    """
        Given a text, communicates with the service and returns the translation
    """
    def send_pirate_request(self, text):

        counter = 1
        while not self.check_service_is_up():
            if counter <= self.max_retries:
                print("Service is down. Retrying again in " + str(self.interval_between_retries))
                counter += 1
                time.sleep(self.interval_between_retries)
            if counter > self.max_retries:
                print("The service is down for a long time now. Please try again later. Exiting...")
                exit(0)

        query_string = urllib.request.quote(text)
        response = urllib.request.urlopen(self.request_url + query_string)

        # Decode is used in order to remove the 'b' prefix from the output
        return response.read().decode('utf-8')

    def check_service_is_up(self):
        try:
            response_code = urllib.request.urlopen(self.request_url).getcode()
        except:
            return False

        if response_code == 200:
            return True
        else:
            return False
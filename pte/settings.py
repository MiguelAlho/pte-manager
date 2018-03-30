"""
Common configuration settings.

They are safe to commit, because essentially it doesn't make sense to have more
than one porto-tech-events instance with different settings, and besides,
there's nothing secret here.

All secret keys are stored in the .env file which is excluded from the repo.
"""
import os
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv())

MODEL_STORAGE_ROOT = '../porto-tech-events'
MEETUP_API_KEY = os.environ['MEETUP_API_KEY']
EVENTBRITE_API_TOKEN = os.environ['EVENTBRITE_API_TOKEN']

GCAL_ID = 'nldp40d05lh6muiv7mqh4crmno@group.calendar.google.com'
GCAL_OAUTH_REDIRECT_URI = 'http://127.0.0.1:5000/redirect'
GCAL_OAUTH_CLIENT_ID = os.environ['GCAL_OAUTH_CLIENT_ID']
GCAL_OAUTH_CLIENT_SECRET = os.environ['GCAL_OAUTH_CLIENT_SECRET']
GCAL_OAUTH_REFRESH_TOKEN_FILE = 'gcal_refresh_token.txt'


MEETUP_COMMUNITIES = [
    'pyporto',
    'Disruptive-Data-Science',
    'devopsporto',
    'portocodes',
    'datascienceportugal',
    'Merge-Porto',
    'Bitcoin-Altcoins-Blockchain',
    'Porto-Big-Data',
    'PortoStartupCoffee',
    'Docker-Porto',
    'Fullstack-Porto',
    'oposecurity',
    'Porto-i-o-events',
    'opo-js',
    'Lambda-PT',
    'drupal-porto',
    'PortoUX',
    'i-o-Sessions',
    '0xOPOSEC',
    'BrainsMeetup',
    'Agile-Connect-Porto',
    'WP-Porto',
    'GameDevMeetPorto',
    'GDG-Porto',
    'PHPorto',
    'Elastic-Portugal',
]

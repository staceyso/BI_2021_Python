import requests
from bs4 import BeautifulSoup as bs


def get_user_info(username):

    """
    :param username: string, username on GitHub
    :return: dict with name, organization, location, number of followers, number of repositories
    """

    req = requests.get(f'https://github.com/{username}/')
    soup = bs(req.content, features="html.parser")

    try:
        name = soup.find(class_='p-name vcard-fullname d-block overflow-hidden').getText().strip()
    except:
        name = None

    try:
        organization = soup.find(class_='p-org').getText()
    except:
        organization = None

    try:
        location = soup.find(class_='p-label').getText()
    except:
        location = None

    try:
        followers = soup.find(class_='text-bold color-fg-default').getText()
    except:
        followers = 0

    try:
        repositories = soup.find(class_='Counter').getText()
    except:
        repositories = 0

    dct = {'name': name,
           'organization': organization,
           'location': location,
           'number_of_followers': followers,
           'number_of_repositories': repositories}

    return dct

if name == __main__:
    print('Example:', get_user_info('staceyso'))
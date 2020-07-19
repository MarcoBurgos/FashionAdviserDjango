import json, re, requests

user = 'the.fashion.adviser'
profile = 'https://www.instagram.com/' + user
photos_from_instagram = []

with requests.session() as s:
    s.headers['user-agent'] = 'Mozilla/5.0'

    end_cursor = ''
    for count in range(1, 2):
        print('PAGE: ', count)

        r    = s.get(profile, params={'max_id': end_cursor})
        data = re.search(
            r'window._sharedData = (\{.+?});</script>', r.text).group(1)

        j = json.loads(data)
        
        media = j['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']

        for node in media:
            values = dict()
            values['display_url'] = node['node']['display_url']
            values['shortcode'] = node['node']['shortcode']
            photos_from_instagram.append(values)

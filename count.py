from datetime import datetime
from matplotlib import pylab as plt
from requests_cache import CachedSession

CACHE_EXPIRATION_SECS = 3600*24*356
YEAR_RANGE = range(2018, 2022)
MARKERS = ["o", "s", "d", "+", "*"]

RIRS = {
        'AFRINIC': {
            'url': 'https://ftp.ripe.net/ripe/rpki/afrinic.tal/',
            'marker': 'o',
            },
        'APNIC': {
            'url': 'https://ftp.ripe.net/ripe/rpki/apnic.tal/',
            'marker': 's',
            },
        'ARIN': {
            'url': 'https://ftp.ripe.net/ripe/rpki/arin.tal/',
            'marker': 'd'
            },
        'LACNIC': {
            'url': 'https://ftp.ripe.net/ripe/rpki/lacnic.tal/',
            'marker': '+',
            },
        'RIPE': {
            'url': 'https://ftp.ripe.net/ripe/rpki/ripencc.tal/',
            'marker': '*',
            }
        }

session = CachedSession(ExpirationTime = CACHE_EXPIRATION_SECS)
plt.figure(figsize=(7,4))

for rir, rir_info in RIRS.items():
    x = []
    y = []
    for year in YEAR_RANGE:
        for month in range(1,13):

            roa_count = -1 # skip the header
            parsed_url = f'{rir_info["url"]}/{year}/{month:02d}/15/roas.csv'
            csv = session.get( parsed_url )
            if csv.status_code != 200:
                print(parsed_url)
                print(csv.status_code)
                continue

            for line in csv.iter_lines(decode_unicode=True):
                roa_count += 1


            if roa_count > 0:
                x.append( datetime(year, month, 15) )
                y.append( roa_count )
            

    plt.plot(x, y, label=rir, marker=rir_info['marker'])

plt.grid( True )
plt.legend()
plt.ylabel('Number of ROAs')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(f'roa_count_{YEAR_RANGE[0]}_{YEAR_RANGE[-1]}.png')
plt.savefig(f'roa_count_{YEAR_RANGE[0]}_{YEAR_RANGE[-1]}.pdf')

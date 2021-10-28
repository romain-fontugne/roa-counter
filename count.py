from datetime import datetime
from matplotlib import pylab as plt
from requests_cache import CachedSession

CACHE_EXPIRATION_SECS = 3600*24*356
YEAR_RANGE = range(2018, 2022)

URLS = {
        'AFRINIC': 'https://ftp.ripe.net/ripe/rpki/afrinic.tal/',
        'APNIC': 'https://ftp.ripe.net/ripe/rpki/apnic.tal/',
        'ARIN': 'https://ftp.ripe.net/ripe/rpki/arin.tal/',
        'LACNIC': 'https://ftp.ripe.net/ripe/rpki/lacnic.tal/',
        'RIPE': 'https://ftp.ripe.net/ripe/rpki/ripencc.tal/',
        }

session = CachedSession(ExpirationTime = CACHE_EXPIRATION_SECS)
plt.figure()

for rir, url in URLS.items():
    x = []
    y = []
    for year in YEAR_RANGE:
        for month in range(1,13):

            roa_count = -1 # skip the header
            csv = session.get(f'{url}/{year}/{month:02d}/15/roa.csv')
            if csv.status_code != 200:
                continue

            for line in csv.iter_lines(decode_unicode=True):
                roa_count += 1


            if roa_count > 0:
                x.append( datetime(year, month, 15) )
                y.append( roa_count )
            

            plt.plot(x, y, legend=rir)

plt.grid( True )
plt.savefig(f'roa_count_{YEAR_RANGE[0]}_{YEAR_RANGE[-1]}.png')
plt.savefig(f'roa_count_{YEAR_RANGE[0]}_{YEAR_RANGE[-1]}.pdf')

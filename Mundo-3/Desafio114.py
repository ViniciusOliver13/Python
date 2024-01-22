import urllib
import urllib.request

print('==== DESAFIO 114 ====')

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except urllib.error.URLError:
    print('\033[1:31mO site que você tenteu acessar está indisponível!\033[m')
else:
    print('\033[1:32mO site está disponível!\033[m')

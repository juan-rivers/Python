print("Python")
#tab
print("\tPython")
#new line
print('Languages:\nPython\nC\nJavascript')

#stripping whitespace
favorite_language = ' python '
favorite_language.rstrip()
favorite_language.lstrip()
favorite_language.strip()

#removing prefixes
nostarch_url = 'https://nostarch.com'
nostarch_url.removeprefix('https://')
'nostarch.com'
simple_url = nostarch_url.removeprefix('https://')
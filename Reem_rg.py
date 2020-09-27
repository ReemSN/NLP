Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> string= "The emergence of COVID-19 we have seen instances of public stigmatization among specific populations, and the rise of harmful stereotypes. Stigmatization could potentially contribute to more severe health problems, ongoing transmission, and difficulties controlling infectious diseases during an epidemic. Please see the Subject in Focus section for more information on how to counter stigmatizing attitudes. New cases for today in Alexandria are 256 cases and 122 cases were registered as recovered. MOH thinking about major lockdown for 3 weeks. In Cairo there were registered 400 new cases and the recovered 350 but no lockdown is seen ahead."
>>> pattern="([Nn]ew.*cases|recovered.*)"
>>> match=re.search(pattern, string)
>>> print(match)
<re.Match object; span=(409, 592), match='New cases for today in Alexandria are 256 cases a>
>>> matchAll=re.findall(pattern, string)
>>> print(matchAll)
['New cases for today in Alexandria are 256 cases and 122 cases were registered as recovered. MOH thinking about major lockdown for 3 weeks. In Cairo there were registered 400 new cases', 'recovered 350 but no lockdown is seen ahead.']
>>> 
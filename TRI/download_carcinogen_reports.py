import pandas as pd
from urllib.request import urlopen

chems = pd.read_csv('chem_release 1990.csv', skiprows=1)
chems.drop(chems.index[0:3], axis=0, inplace=True)
chems.drop(chems.index[104:], axis=0, inplace=True)

carcinogen_no = chems[['CAS Number', 'Chemical']]
url = r"https://iaspub.epa.gov/triexplorer/release_fac?SAVEAS_=usch-releases.csv&p_view=USFA&trilib=TRIQ1&TAB_RPT=1&Fedcode=&LINESPP=&sort=_VIEW_&industry=ALL&FLD=AIRLBY&FLD=E1&FLD=E2&FLD=E3&FLD=E4&FLD=E5&FLD=E52&FLD=E53&FLD=E54&FLD=E51&FLD=TSFDSP&FLD=TSFDSP&FLD=m10&FLD=m41&FLD=m62&FLD=potwmetl&FLD=m71&FLD=m72&FLD=m73&FLD=m79&FLD=m90&FLD=m94&FLD=m99&FLD=RELLBY&FLD=RE_TOLBY&sort_fmt=1&TopN=ALL&STATE=All+states&COUNTY=All+counties&year=1990&report=&pOutput=CSV&pOutput=Download"

for n in carcinogen_no.iterrows():
  print(n[1])
  f = open(n[1][1] + "_" + "1990", 'wb')
  print("Downloading chemical {}, CAS number {}".format(n[1][1],n[1][0]))
  f.write(urlopen(url + "&chemical=" + n[1][0]).read())
  print("Saving chemical {}, CAS number {}".format(n[1][1], n[1][0]))
  f.close()

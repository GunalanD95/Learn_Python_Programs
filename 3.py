

import re
pattern = r"123"
string = "123zzb"
re.match(pattern, string) # Out: <_sre.SRE_Match object; span=(0, 3), match='123'>
match = re.match(pattern, string)
match.group( )

import re as re

html_code = '<div style="float:right;margin:0px 0px 20px 20px;" id="content_sys_div_msg"></div>2.0 125 KW Quattro, konkrētāk zvanot.<br><br><table cellpadding=0 cellspacing=0 border=0 width="100%" class="options_list"><tr><td width="50%" valign=top>'
text = re.search('div>[a-zāčēģīķļņšūžA-ZĀČĒĢĪĶĻŅŠŪŽ0-9QWY., ]+<br><br><table', html_code)
print(text)
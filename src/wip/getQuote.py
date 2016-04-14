import re
from urllib import urlopen
i = 224
while (i>1):
#	t = urlopen('http://www.theskepticsguide.org/archive/podcastinfo.aspx?mid=1&pid='+str(i)).read()
	fileObj = open("d:\sceptics\\"+str(i)+".txt","r")
	t=fileObj.read()
	fileObj.close()

	#namePattern = re.compile('</span>\s*</td>\s*<td style="vertical-align: top; text-align:left;">\s*\W+(.*?)</td>\s*</tr>\s*</table>', re.DOTALL | re.IGNORECASE)
	namePattern = re.compile('<td style="vertical-align: top; text-align:left;">\s*(.*?)\.\s*(.*?)\s*</td>', re.DOTALL | re.IGNORECASE)
	n = namePattern.search(t)
	if n:
		if len(n.group(1))>800:
			print str(i), 'ERROR'
		else:
			print str(i),n.group(1)+"#"+n.group(2)
	else:
		print str(i)
	i-=1

#fileObj = open("d","w")
#fileObj.write(text)

#fileObj = open("d","r")
#t=fileObj.read()





#quotes = open("quotes.txt","w")
#namePattern = re.compile('>\s*"(.*?)"\s*<br><br>\W+(.*?)<br>', re.DOTALL | re.IGNORECASE)
#n = namePattern.search(t)
#if n:
#	quotes.write(n.group(1)+n.group(2))
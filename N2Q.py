import urllib,json

charset="utf8"
banned_mark=["\\","/",":","*","?","\"","<",">","|"]
with open("plts.txt","r") as playlist_file:
	ss=playlist_file.readlines()
plts=[]
for s in ss:
	pos=s.find("playlist?id=");
	if(pos!=-1):
		pos+=12
		s=s.replace("\n","")
		plts.append("http://music.163.com/api/playlist/detail?id=%s"%(s[pos:]))
for plt in plts:
	f=urllib.urlopen(str(plt))
	html_file=f.read().decode("UTF-8")
	json_obj=json.loads(html_file)
	songs=json_obj["result"]["tracks"]
	
	file_name=json_obj["result"]["name"];
	for mark in banned_mark:
		file_name=file_name.replace(mark,"");

	with open("%s.txt"%(file_name),"w") as fp:
		fp.write("%s\n"%(u"\u6B4C\u66F2\u6807\u9898".encode(charset)))
		fp.write("%s\n"%(u"\u65F6\u957F".encode(charset)))
		fp.write("%s\n"%(u"\u6B4C\u624B".encode(charset)))
		fp.write("%s\n"%(u"\u4E13\u8F91".encode(charset)))
		count=1
		for song in songs:
			fp.write("%s\n"%(str(count)))
			fp.write("%s\n"%(song["name"].encode(charset)))
			fp.write("%s\n"%("05:67"))
			flag=False;
			for artist in song["artists"]:
				if(flag):
					fp.write("/")
				else:
					flag=True
				fp.write(artist["name"].encode(charset))
			fp.write("\n")
			fp.write("%s\n"%(song["album"]["name"].encode(charset)))
			count+=1;

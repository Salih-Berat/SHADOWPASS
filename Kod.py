print("""
Hoşgeldin Kullanıcı!
""")

enc={
"ı":"ü",
"I":"Ü",
"ü":"ı", 
"Ü":"I",
"B":"Z",
"b":"z",
"Z":"B",
"z":"b",
"i":"i",
"İ":"İ",
"A":"U",         
"a":"u",
"U":"A", 
"u":"a",
"c":"q",
"C":"Q",
"Q":"C",
"q":"c",
"ç":"v",
"Ç":"V",
"V":"Ç",
"v":"ç", 
"K":"T",
"k":"t",
"T":"K",
"t":"k",
"F":"Ş",
"f":"ş",
"Ş":"F",
"ş":"f",
"D":"Ğ",
"d":"ğ",
"Ğ":"D",
"ğ":"d",
"s":"n",
"S":"N",
"N":"S",
"n":"s",        
"H":"M",
"h":"m",
"M":"H",
"m":"h",
"p":"l",
"P":"L",
"L":"P",
"l":"p",
"J":"R", 
"j":"r",
"R":"J",
"r":"j",
"E":"Ö",
"e":"ö",
"Ö":"E", 
"ö":"e",
"O":"O",
"o":"o",
"G":"Y",
"g":"y",
"Y":"G",
"y":"g",
"W":"X",
"w":"x",
"X":"W",
"x":"w",
" ":" ",
"1":"0",
"0":"1",
"2":"8",
"8":"2",
"3":"7",
"7":"3",
"4":"6",
"6":"4",
"5":"9", 
"9":"5",
",":".",
".":",",
"?":"!",
"!":"?",
"_":"=",
"=":"_",
"<":">",
">":"<",
"+":"/",
"/":"+",
"*":"-",
"-":"*",
"(":")",
")":"(",
"@":"#",
"#":"@",
"'":"$",
"$":"'",
"^":"^",
":":"_",
"_":":",
"%":"&",
"&":"%",
"¹":"²",
"²":"²",
"{":"|",
"|":"{",
"[":"]",
"[":"]",
"}":"}",
'"':'÷',
"÷":'"'
}
print("""
         GÖLGE YAZICI V1.1\n
-Döngü Eklendi.
-Boşluk Bugu Düzeltildi.
-print(...) diye yazmanıza gerek kalmadı.\n
         GÖLGE YAZICI V1.15
-Büyük Harfler Kullanıma Açıldı.
-Bazı Özel Karakterler Kullanıma Açıldı (/*+-) gibi.
-Sayılar Kullanıma Açıldı.
-Bazı Şifreleme Metotları Değişti.
-Bazı Buglar ve Yazım Hataları Düzeltildi.\n
         GÖLGE YAZICI V1.16.1
-X ve x Harfi Kullanıma Açıldı.
-Büyük Harflerin Bugları Düzeltildi.
-Bazı Özel Karakterler Kullanıma Açıldı (/*+-) gibi.
-Bazı Şifreleme Metotları Değiştirildi.
-Bazı Yazım Hataları Düzeltildi.
-Çözülecek Buglar Kısmı Eklendi.\n
         GÖLGE YAZICI V1.16.11
-Önceki Sürümdeki Harf Bugu Kaldırıldı.\n         
         GÖLGE YAZICI V1.2
-İsim SHADOWPASS Yerine GÖLGE YAZICI olarak Değiştirildi.
-Bazı Özel Karakterler Kullanıma Açıldı.
-Kullanıcı Girişi Eklendi.
-Şifreleme Metotları Değişti.\n         """)
print("ŞİFRELER VE ÇÖZER\n")
print("""Programı kullanmak için\n
 Örnek Olarak:
 Şifrelenecek kelime yazın size şifreli haline vercektir.
 Programda Şifrelenmiş Kelimeyi Çözmek içinse
 Örnek Olarak:
 Çözülecek kelime yazın size çözülmüş halini verecektir
 NOT1= Yakında Linux ve Mac için Sürüm Desteği Gelecektir
 NOT2= İsteklerinizi Discord Sunucumdan Söyleyebilirsiniz:
 https://discord.gg/22evkyF \n""")
while 1:
	ف = input("Şifrele veya Çöz:")
	out=""
	oldlen=len(ف)
	ف=list(ف)
	while len(out)!=oldlen:
		for a,b in enc.items():
			if ف[0]==a:
				out+=b
				del ف[0]
				break
	ف=''.join(ف)
	print(out)

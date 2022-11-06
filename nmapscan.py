import nmap
ip=input("[+] IP Objetivo ==> ")
nm = nmap.PortScanner()

puertos_abiertos=""
results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4")
count=0


rep= open("Reporte de Escaneo.txt", "a")
rep.write("\nLa IP Host dada: %s" % ip)
rep.write("\nEl estado de la IP es: %s" % nm[ip].state())
print("\nLa IP Host dada: %s" % ip)
print("El estado de la IP es: %s" % nm[ip].state())
for proto in nm[ip].all_protocols():
	print("El protocolo es: %s" % proto)
	rep.write("\nEl protocolo es: %s" % proto)
	print()
	lport = nm[ip][proto].keys()
	sorted(lport)
	for port in lport:
		print ("port: %s\tstate: %s" % (port, nm[ip][proto][port]["state"]))
		rep.write("\nport: %s\tstate: %s" % (port, nm[ip][proto][port]["state"]))
		if count==0:
			puertos_abiertos=puertos_abiertos+str(port)
			count=1
		else:
			puertos_abiertos=puertos_abiertos+","+str(port)

print("\nLos puertos abiertos son: "+ puertos_abiertos)
rep.write("\nLos puertos abiertos son: "+ puertos_abiertos)
rep.close()

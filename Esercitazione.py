import requests

#response=requests.post(" http://192.168.1.231:8080/accreditamento",json={"nome":"Luca Bergognoni"})
#print (response)

#1
#res= requests.get("http://192.168.1.231:8080/esercizi/1", headers= {"x-data": "true"})
#print(res.json())
#
#c = res.json()
#h=c["data"]
#risposta=h.lower()
#
#
#a=requests.post(" http://192.168.1.231:8080/esercizi/1",json={"data":risposta})
#a=a.json()
#print(a)

#2



#res=requests.get("http://192.168.1.231:8080/esercizi/2", headers= {"x-data": "true"})
#print(res.json())
#
#c = res.json()
#h=c["data"]
#risposta= h*h
#
#
#a=requests.post(" http://192.168.1.231:8080/esercizi/2",json={"data":risposta})
#a=a.json()
#print(a)

#3


#res=requests.get("http://192.168.1.231:8080/esercizi/3", headers= {"x-data": "true"})
#print(res.json())
#
#c = res.json()
#h=c["data"]
#print(h)
#
#risposta= h["cognome"]
#
#
#a=requests.post(" http://192.168.1.231:8080/esercizi/3",json={"data":risposta})
#a=a.json()
#print(a)


#4


#res=requests.get("http://192.168.1.231:8080/esercizi/4", headers= {"x-data": "true"})
#print(res.json())
#
#c = res.json()
#h=c["data"]
#print(h)
#
#risposta= len(h)
#
#
#a=requests.post(" http://192.168.1.231:8080/esercizi/4",json={"data":risposta})
#a=a.json()
#print(a)



#5



#res=requests.get("http://192.168.1.231:8080/esercizi/5", headers= {"x-data": "true"})
#print(res.json())
#
#c = res.json()
#h=c["data"]
#print(h)
#
#risposta=[]
#for parola in h:
#	parola=parola.upper()
#	risposta.append(parola)
#
#
#a=requests.post(" http://192.168.1.231:8080/esercizi/5",json={"data":risposta})
#a=a.json()
#print(a)



#6

#res=requests.get("http://192.168.1.231:8080/esercizi/6", headers= {"x-data": "true"})
#print(res.json())
#
#c = res.json()
#h=c["data"]
#print(h)
#
#risposta=sum(h)
#
#
#
#a=requests.post(" http://192.168.1.231:8080/esercizi/6",json={"data":risposta})
#a=a.json()
#print(a)

#7
#res=requests.get("http://192.168.1.231:8080/esercizi/7", headers= {"x-data": "true"})
#print(res.json())
#
#c = res.json()
#h=c["data"]
#print(h)
#
#risposta=0
#for numero in h:
#	if numero>5:
#		risposta+=numero
#
#
#
#
#a=requests.post(" http://192.168.1.231:8080/esercizi/7",json={"data":risposta})
#a=a.json()
#print(a)


#8
res=requests.get("http://192.168.1.231:8080/esercizi/8", headers= {"x-data": "true"})
print(res.json())

c = res.json()
h=c["data"]
print(h)

risposta=0

for i in range(len(h)):
	if i%2==0:
		risposta+=h[i]


a=requests.post(" http://192.168.1.231:8080/esercizi/8",json={"data":risposta})
a=a.json()
print(a)


#9



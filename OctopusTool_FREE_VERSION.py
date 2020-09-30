
import os
import colorama
import sys
import socket
import mcstatus
import requests
import random
import threading
import nmap


from colorama import *
from mcstatus import *
from nmap import *

init()



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.2)

dedis = ["jouer","proxy","play","server","mc","dedi","bedwars","skywars","skyblock","creative","join","jogar","onya","buildteam","build","staff","dev","developer","serv11", "serv0", "serv10", "serv9", "serv8", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "premium", "login", "devteam"]
subdomains = ["www", "serieyt", "shop", "report", "apply", "youtube", "twitter", "st", "lost", "sg", "srvc1", "torneo", "serv11", "serv0", "serv10", "serv9", "serv8", "serv7", "serv6", "serv5", "serv4", "serv3", "serv2", "serv1", "serv", "mcp", "paysafe", "mu", "radio", "donate", "vps03", "vps02", "vps01", "xenon", "radio", "bans", "ns2", "ns1", "donar", "radio", "new", "appeals", "reports", "translations", "marketing", "staff", "bugs", "help", "render", "foro", "ts3", "git", "analytics", "coins", "votos", "docker-main", "main", "server3", "cdn", "server2", "creativo", "yt2", "yt", "factions", "solder", "test1", "test001", "testpene", "test", "panel", "apolo", "sv3", "sv2", "sv1", "backups", "zeus", "thor", "vps", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "games001", "games002", "game001", "game002", "game003", "sys001", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "render", "hcf", "grafana", "vote2", "file", "sentry", "enjin", "webserver", "xen", "mco", "monitor", "servidor2", "sadre", "gamehitodrh", "staff", "admin", "teamspeak"]



def pause():
	pause = input (" Press - Enter - to continue...")

class SConnect:
	def __init__(self, ip, port=None):
		self.ip = ip
		self.port = port
		self.address = (self.ip, self.port)
		self.s_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s_connection.settimeout(0.2)
	def portscan(self):
		return self.s_connection.connect_ex(self.address)


def banner():
    os.system("clear || cls")
    print(Fore.RED+" ╔═══════════════════════════════════════════════════════════════════════╗")            
    print(Fore.RED+" ║"+Fore.RED+" _____   ___  ____  _____  ____  __  __  ___  ____  _____  _____  __   "+Fore.RED+"║")
    print(Fore.RED+" ║"+Fore.RED+"(  _  ) / __)(_  _)(  _  )(  _ \(  )(  )/ __)(_  _)(  _  )(  _  )(  )  "+Fore.RED+"║")
    print(Fore.RED+" ║"+Fore.RED+" )(_)( ( (__   )(   )(_)(  )___/ )(__)( \__ \  )(   )(_)(  )(_)(  )(__ "+Fore.RED+"║")
    print(Fore.RED+" ║"+Fore.RED+"(_____) \___) (__) (_____)(__)  (______)(___/ (__) (_____)(_____)(____)"+Fore.RED+"║")
    print(Fore.RED+" ║"+Fore.RED+"Version 3.0                                                            "+Fore.RED+"║")
    print(Fore.RED+" ╚═══════════════════════════════════════════════════════════════════════╝")                                        
    print(Fore.RED+" ╔═════════════════════════════════════╗")
    print(Fore.RED+" ║"+Fore.BLUE+" Owner - ʍƦøc†øρu$ | [VB]#6161"+ Fore.RED+"             ║")                       
    print(Fore.RED+" ╚═════════════════════════════════════╝")




while True:
	os.system("cls")
	banner()
	print ()
	print (Fore.WHITE+" ("+Fore.BLUE+"1"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Dedicados (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"2"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Subdominios (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"3"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Port Scan Tracker (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"4"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Server Finder (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"5"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Guia comandos Grief (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"6"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Lista de servidores (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"7"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Whois (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"8"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Information Tool (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"9"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" Entrar a la MySQL (ONLINE)")
	print (Fore.WHITE+" ("+Fore.BLUE+"10"+Fore.WHITE+")"+Fore.LIGHTGREEN_EX+" NmapTracker (ONLINE)")

	print ()
	print (Fore.RED+" Selecciona tu opcion: "+Fore.WHITE, end='')
	x = input()

	if x == "0":
		sys.exit(1)

	# DEDICATEDS FINDER
	elif x == "1":
		print ()
		print (Fore.RED+" Domain: "+Fore.WHITE, end='')
		domain = input()
		print ()
		print (" Scanning... This may can take a long time....")
		print ()
		for subdomain in dedis:
			try:
				target = (subdomain)+"."+(domain)
				ipr = socket.gethostbyname(target)
				sock.connect_ex((ipr, 25565))
				server = MinecraftServer.lookup(ipr)
				status = server.status()
				print (Fore.GREEN+" Minecraft Server Found ! "+(ipr)+":25565 ["+Fore.MAGENTA+target+Fore.GREEN+"] ("+Fore.MAGENTA+str(status.version.name)+Fore.GREEN+")("+Fore.MAGENTA+str(status.players.online)+"/"+str(status.players.max)+Fore.GREEN+")"+Fore.WHITE)
			except:
				pass
		print ()
		pause()
	# SUBDOMAINS FINDER
	elif x == "2":
		print ()
		print (Fore.RED+" Domain: "+Fore.WHITE, end='')
		domain = input()
		print ()
		print (" Scanning... This may can take a long time....")
		print ()
		for subdomain in subdomains:
			try:
				target = (subdomain)+"."+(domain)
				ipr = socket.gethostbyname(target)
				print (Fore.GREEN+" Domain Found ! "+(ipr)+" [Domain: "+Fore.MAGENTA+target+Fore.GREEN+"]."+Fore.WHITE)
			except:
				pass
		print ()
		pause()
	# PORT SCANNER
	elif x == "3":
		print ()
		print (Fore.RED+" IP: "+Fore.WHITE, end='')
		domain = input()
		print ()
		print (" Scanning... This may can take a long time....")
		print ()
		for p in range(25565, 65535): 
			conn = SConnect(domain, p)
			if conn.portscan() == 0:
				try:
					server = MinecraftServer.lookup((domain)+":"+str(p))
					status = server.status()
					print (Fore.RED+" Port Found ! ("+Fore.MAGENTA+str(p)+Fore.RED+") ("+Fore.MAGENTA+str(status.version.name)+Fore.CYAN+")("+Fore.MAGENTA+str(status.players.online)+"/"+str(status.players.max)+Fore.CYAN+")"+Fore.WHITE)

				except:
					print (Fore.RED+" Port Found ! ("+Fore.MAGENTA+str(p)+Fore.RED+") ("+Fore.MAGENTA+"Can't found Minecraft"+Fore.CYAN+")"+Fore.WHITE)
		print ()
		pause()

	# SERVER FINDER
	elif x == "4":
		print ()
		print (Fore.RED+" IP: "+Fore.WHITE, end='')
		a1 = input().split(".")
		ip1 = a1[0]
		ip2 = a1[1]
		ip3 = a1[2]
		ip4 = a1[3]
		domain = (ip1)+"."+(ip2)+"."+(ip3)+"."
		print ()
		print (" Scanning... This may can take a long time....")
		print ()
		for r in range(0, 255):
			target = (domain)+str(r)
			c = SConnect(target, 25565)
			if c.portscan() == 0:
				try:
					server = MinecraftServer.lookup(target)
					status = server.status()
					print (Fore.CYAN+" Server Found ! ("+Fore.MAGENTA+str(target)+Fore.RED+") ("+Fore.MAGENTA+str(status.version.name)+Fore.RED+")("+Fore.MAGENTA+str(status.players.online)+"/"+str(status.players.max)+Fore.GREEN+")("+Fore.MAGENTA+str(status.latency)+"ms"+Fore.GREEN+")"+Fore.WHITE)
				except:
					print (Fore.CYAN+" Server Found ! ("+Fore.MAGENTA+str(target)+Fore.RED+") ("+Fore.MAGENTA+"Can't resolve server !"+Fore.RED+")"+Fore.WHITE)
		print ()



	# GuiaCommmandsGrief
	elif x == "5":
		print ()
		print (Fore.WHITE+"-------https://pastebin.com/DtbQCq46-------")
		GuiaCommmandsGrief = input()
		print ()

	# Lista De Servidores
	elif x == "6":
				from random import seed
				from random import randint
				for _ in range(1):
					value = randint(1, 150)
				if value == 1:
					print ("SkyCraft.es")
				if value == 2:
					print ("play.becto.net")
				if value == 3:
					print ("PLAY.ROYALLEGACY.NET")
				if value == 4:
					print ("pvp.desteria.com")
				if value == 5:
					print ("play.manacube.net")
				if value == 6:
					print ("play.extremecraft.net")
				if value == 7:
					print ("mc-central.net")
				if value == 8:
					print ("pixel.mc-complex.com")
				if value == 9:
					print ("mineheroes.net")
				if value == 10:
					print ("mc.snapcraft.net")
				if value == 11:
					print ("MC.Performium.net")
				if value == 12:
					print ("play.applecraft.org")
				if value == 13:
					print ("play.jartexnetwork.com")
				if value == 14:
					print ("play.thedestinymc.com")
				if value == 15:
					print ("play.vexedmc.com")
				if value == 16:
					print ("earthmc.net")
				if value == 17:
					print ("play.pixelmonrealms.com")
				if value == 18:
					print ("mc-gtm.net")
				if value == 19:
					print ("FadeCloud.com")
				if value == 20:
					print ("FadeCloud.com")
				if value == 21:
					print ("pvp.desteria.com")
				if value == 22:
					print ("pixel.rc-gamers.com")
				if value == 23:
					print ("eu.sonoyuncu.network")
				if value == 24:
					print ("PlayPokeNinjas.com")
				if value == 25:
					print ("DIRTCRAFT.GG")
				if value == 26:
					print ("jogar.gearfriends.net")
				if value == 27:
					print ("play.strongcraft.org")
				if value == 28:
					print ("play.pika-network.net")
				if value == 29:
					print ("mc.ecuacraft.com")
				if value == 30:
					print ("play.ggmc.me")
				if value == 31:
					print ("play.castiamc.com")
				if value == 32:
					print ("play.projectwonder.net")
				if value == 33:
					print ("play.mineville.org")
				if value == 34:
					print ("pixel.mc-blaze.com")
				if value == 35:
					print ("play.MuxMC.net")
				if value == 36:
					print ("jogar.rocketmc.com.br")
				if value == 37:
					print ("play.omegacraft.cl")
				if value == 38:
					print ("oyna.provanas.com")
				if value == 39:
					print ("play.uniocraft.com")
				if value == 40:
					print ("mineverse.com")
				if value == 41:
					print ("mc.minebox.es")
				if value == 42:
					print ("mc.ventureland.net")
				if value == 43:
					print ("Pokecentral.org")
				if value == 44:
					print ("play.azertumc.com")
				if value == 45:
					print ("mc.momentonetwork.net")
				if value == 46:
					print ("play.wildercraft.net")
				if value == 47:
					print ("play.mc-complex.com")
				if value == 48:
					print ("Play.Betacraft.Org")
				if value == 49:
					print ("play.wheelcraft-id.net")
				if value == 50:
					print ("smp.hometownmc.com")
				if value == 51:
					print ("mc.safesurvival.net")
				if value == 52:
					print ("play.cultivatemc.com")
				if value == 53:
					print ("play.alttd.com")
				if value == 54:
					print ("play.limitlessmc.net")
				if value == 55:
					print ("mc.clubobsidian.com")
				if value == 56:
					print ("play.pokeverse.org")
				if value == 57:
					print ("play.bulbacraft.com")
				if value == 58:
					print ("Play.Minecraft-Romania.Ro")
				if value == 59:
					print ("fun.multyplay.ro")
				if value == 60:
					print ("miningdead.com")
				if value == 61:
					print ("play.primemc.org")
				if value == 62:
					print ("jogar.luthcraft.com")
				if value == 63:
					print ("minelife.dk")
				if value == 64:
					print ("play.pokemayhem.com")
				if value == 65:
					print ("play.skyblocknetwork.com")
				if value == 66:
					print ("mc.PokeSmash.co")
				if value == 67:
					print ("play.ajgaming.net")
				if value == 68:
					print ("play.guildcraft.org")
				if value == 69:
					print ("mc.soulplex.net")
				if value == 70:
					print ("play.mineway.org")
				if value == 71:
					print ("mc.playdreamcraft.com.br")
				if value == 72:
					print ("mc.myftb.de")
				if value == 73:
					print ("mc.akarcraft.es")
				if value == 74:
					print ("jogar.pokelandia.com")
				if value == 75:
					print ("arefy.net")
				if value == 76:
					print ("mcm.datblock.com")
				if value == 77:
					print ("play.apeironmc.com")
				if value == 78:
					print ("mc.kingnw.com")
				if value == 79:
					print ("play.battleasya.com")
				if value == 80:
					print ("play.onlymc.net")
				if value == 81:
					print ("servicraft.org")
				if value == 82:
					print ("DBC.ApolloNetworkMC.net")
				if value == 83:
					print ("play.primemc.org")
				if value == 84:
					print ("mc.megaplanet.net")
				if value == 85:
					print ("play.skyblocknetwork.com")
				if value == 86:
					print ("mc.PokeSmash.co")
				if value == 87:
					print ("mc.akarcraft.es")
				if value == 88:
					print ("play.PrismForge.com")
				if value == 89:
					print ("mc.survival.pw")
				if value == 90:
					print ("play.potterworldmc.com")
				if value == 91:
					print ("play.journeygaming.com")
				if value == 92:
					print ("pixel.un-linked.com")
				if value == 93:
					print ("mc.kriptonpvp.com")
				if value == 94:
					print ("play.peacefulfarms.net")
				if value == 95:
					print ("tekkit.mc-complex.com")
				if value == 96:
					print ("mcmp.AspiriaMc.com")
				if value == 97:
					print ("play.breachpvp.com")
				if value == 98:
					print ("Pixelmon.HappyCloudMC.com")
				if value == 99:
					print ("play.minewonderland.net")
				if value == 100:
					print ("my.mineland.net")
				if value == 101:
					print ("mc.kgb-minecraft.info")
				if value == 102:
					print ("play.pokedash.org")
				if value == 103:
					print ("Play.DipCraft.Ro")
				if value == 151:
					print ("play.breakdowncraft.com")
				if value == 104:
					print ("play.pixelmonadventures.com")
				if value == 105:
					print ("play.mineswift.net")
				if value == 105:
					print ("omegarealm.com")
				if value == 106:
					print ("play.skybattle.net")
				if value == 106:
					print ("mc.ultranetwork.me")
				if value == 107:
					print ("jogar.craftsgp.net")
				if value == 108:
					print ("geoblock.es")
				if value == 109:
					print ("play.pixelmonharmony.com")
				if value == 110:
					print ("play.xenolithnetwork.com")
				if value == 111:
					print ("play.conspiracycraft.net")
				if value == 112:
					print ("play.creativefun.net")
				if value == 113:
					print ("play.phanaticmc.com")
				if value == 114:
					print ("tinetwork.net")
				if value == 115:
					print ("play.decimatepvp.com")
				if value == 116:
					print ("play.YomNetwork.ca")
				if value == 117:
					print ("play.silkycraft.net")
				if value == 118:
					print ("play.nytro.network")
				if value == 119:
					print ("mc.aminearserver.es")
				if value == 120:
					print ("play.lunarrisingmc.com")
				if value == 121:
					print ("InfinityCubedMC.com")
				if value == 122:
					print ("play.minelink.net")
				if value == 123:
					print ("SB-Central.com")
				if value == 124:
					print ("play.voidrealms.net")
				if value == 125:
					print ("play.ickcraft.nl")
				if value == 126:
					print ("play.hallowedfantasy.com")
				if value == 127:
					print ("mc.lotc.co")
				if value == 128:
					print ("play.poke-brawl.com")
				if value == 129:
					print ("play.feroxmc.net")
				if value == 130:
					print ("mc.pvpbulgaria.eu")
				if value == 131:
					print ("jogar.backmc.com.br")
				if value == 132:
					print ("play-pokecraft.com")
				if value == 133:
					print ("play.eminentmc.com")
				if value == 134:
					print ("play.dawnhaven.net")
				if value == 135:
					print ("massivecraft.com")
				if value == 136:
					print ("mc.divictusgaming.com")
				if value == 137:
					print ("play.acornmc.org")
				if value == 138:
					print ("vnlla.net")
				if value == 139:
					print ("play.shadownode.ca")
				if value == 140:
					print ("mc.calderaminecraft.com")
				if value == 141:
					print ("play.ghiblicraft.com")
				if value == 142:
					print ("diamond.voxmc.com")
				if value == 143:
					print ("server.proyecto40.es")
				if value == 144:
					print ("play.cursedcraft.com")
				if value == 145:
					print ("play.harvestmc.net")
				if value == 146:
					print ("play.harvestmc.net")
				if value == 147:
					print ("DangCap.Ga")
				if value == 148:
					print ("twerion.net")
				if value == 149:
					print ("play.poke-saga.com")
				if value == 150:
					print ("mc.feargames.it")
				ListaDeServidores = input()
				print ()



	# Whois
	elif x == "7":
		print ()
		print (Fore.WHITE+"Hola en esta intruduccion te dejare el link en el cual podras ver el whois de una ip, Si te preguntas que es whois pues WHOIS es un protocolo TCP basado en petición/respuesta que se utiliza para efectuar consultas en una base de datos que permite determinar el propietario de un nombre de dominio o una dirección IP en Internet")
		print (Fore.GREEN+"Aqui tienes el link https://elhacker.net/whois.html")
		print (Fore.RED+"Gracias al equipo administrativo de (elhacker.net) por la colaboracion")
		Whois = input()
		print ()

	# Information-Tool
	elif x == "8":
		print ()
		print (Fore.RED+"Bienvenidos a la GriefTool. En esta introduccion te mostrare de que se trata esta tools,")
		print (Fore.GREEN+"Actualizaciones : Lista de serves hecha ONLINE e incluso apartado de como entrar a la MySQL Proximamente]") 
		print (Fore.GREEN+"Proximamente tambien estara agregado el NmapTracker Sean Pacientes :D")
		print (Fore.GREEN+"La tool esta en beta tiene muchas funciones buenas asi que os pido que usen esta tool con buenas intenciones")
		print (Fore.RED+"---Creditos---")
		print (Fore.GREEN+" Owner - MrOctopus")
		print (Fore.GREEN+" Ayuda - WithZELXD")
		print (Fore.GREEN+" Distribuidor - Ninguno")
		Information = input()
		print ()


 #Entrar a la MySQL
	if x == "9":
		print ("Habre tu vps y pon:")
		print ("mysql -u root -h (Nombre de la mysql) -p (password)")
		DatabaseHacked = input()
		print ()

 	# NmapTracker
	if x == "10":
		os.system ("cls")
		a = input (Fore.YELLOW+"Set your first IP [1/4] (127) >> ")
		b = input (Fore.YELLOW+"Set your first IP [2/4] (0) >> ")
		c = input (Fore.YELLOW+"Set your first IP [3/4] (0) >> ")
		x = input (Fore.YELLOW+"Set your first IP [4/4] (1) >> ")
		y = int(1)
		z = int(x) - int(y)
		r = int(x) + int(y)
		ipresul = str(a)+"."+str(b)+"."+str(c)+"."+str(z)+"-"+str(r)
		print (Fore.MAGENTA+"")
		os.system ("nmap -p 1-12,1000-1010,20000-20005,25500-25700,28010-28015,30000-30005,40000-40010,65500-65535 -T5 -v -A -Pn "+ipresul)
		NmapTracker = input()
		print()

			

def InitPaquet() :

	"""Cette fonction sert à créer le paquet en début de partie. \nOn utilise une liste de tuples pour éviter au programme de calcul tout le temps l'équivalence d'un indice avec une couleur et un entryéro.\n"""

	from random import shuffle

	Paquet =[]
	#Ajoute d'abord les cartes bleues : 0, les chiffres, puis les spéciales.
	Paquet.append(("0", "Bleu"))
	for i in range (9) :
		Paquet.append((str(i+1), "Bleu"))
		Paquet.append((str(i+1), "Bleu"))
	Paquet.append(("+2", "Bleu"))
	Paquet.append(("+2", "Bleu"))
	Paquet.append(("Sens Interdit", "Bleu"))
	Paquet.append(("Sens Interdit", "Bleu"))
	Paquet.append(("Changement de Sens", "Bleu"))
	Paquet.append(("Changement de Sens", "Bleu"))

	#Puis les cartes rouges
	Paquet.append(("0", "Rouge"))
	for i in range (9) :
		Paquet.append((str(i+1), "Rouge"))
		Paquet.append((str(i+1), "Rouge"))
	Paquet.append(("+2", "Rouge"))
	Paquet.append(("+2", "Rouge"))
	Paquet.append(("Sens Interdit", "Rouge"))
	Paquet.append(("Sens Interdit", "Rouge"))
	Paquet.append(("Changement de Sens", "Rouge"))
	Paquet.append(("Changement de Sens", "Rouge"))

	#Puis les cartes jaunes
	Paquet.append(("0", "Jaune"))
	for i in range (9) :
		Paquet.append((str(i+1), "Jaune"))
		Paquet.append((str(i+1), "Jaune"))
	Paquet.append(("+2", "Jaune"))
	Paquet.append(("+2", "Jaune"))
	Paquet.append(("Sens Interdit", "Jaune"))
	Paquet.append(("Sens Interdit", "Jaune"))
	Paquet.append(("Changement de Sens", "Jaune"))
	Paquet.append(("Changement de Sens", "Jaune"))

	#Puis les cartes vertes
	Paquet.append(("0", "Vert"))
	for i in range (9) :
		Paquet.append((str(i+1), "Vert"))
		Paquet.append((str(i+1), "Vert"))
	Paquet.append(("+2", "Vert"))
	Paquet.append(("+2", "Vert"))
	Paquet.append(("Sens Interdit", "Vert"))
	Paquet.append(("Sens Interdit", "Vert"))
	Paquet.append(("Changement de Sens", "Vert"))
	Paquet.append(("Changement de Sens", "Vert"))

	#On termine par les cartes multicolores (Sans couleurs pour les tuples)
	for i in range(4) :
		Paquet.append(["+4", ""])
	for i in range(4) :
		Paquet.append(["Joker", ""])

	shuffle(Paquet)

	return Paquet

def Apparition_Fondu (imageDeFond, vitesse, width, height) :
	image = pygame.image.load(imageDeFond).convert()
	image = pygame.transform.scale(image, (width, height))
	for i in range(255,0,-4) :
		fenetre.blit(image,(0,0))
		fenetre.fill((i,i,i),special_flags=BLEND_RGB_SUB)
		sleep(vitesse)
		pygame.display.flip()

def Disparition_Fondu (vitesse) :
	for i in range(0,255,4):
		fenetre.fill(0x040404,special_flags=BLEND_RGB_SUB)
		sleep(vitesse)
		pygame.display.flip()

def Ecran_Chargement() :

	"""Permet d'afficher le texte de l'ecran titre et d'attendre une entree"""

	global fenetre, Paquet

	width, height = 1366, 768
	font = pygame.font.Font("Triforce.ttf", int(height/12))
	texte = font.render("Chargement", True, (255,255,255))
	position_texte = texte.get_rect(center = (width/2, height/2.1))

	affichage = True
	indice = 0
	dicoDesCartes = {}
	while affichage :
		for event in pygame.event.get() :
			if event.type == QUIT :
				quit()

		for i in range(255,0,-4):
			fenetre.blit(texte, (position_texte))
			fenetre.fill((i,i,i), special_flags=BLEND_RGB_SUB)
			sleep(0.005)
			pygame.display.flip()
		for j in range(indice, indice+len(Paquet)//4) :
			texteCarte = (" ").join(Paquet[j])
			if not tuple(Paquet[j]) in dicoDesCartes :
				dicoDesCartes[tuple(Paquet[j])] = pygame.image.load("Pics/Cartes/%s.png" %texteCarte)
		indice += len(Paquet)//4
		if indice >= len(Paquet) :
			affichage = False
		Disparition_Fondu(0.001)

	return width, height, dicoDesCartes

def Ecran_Titre(width, height) :

	"""Permet d'afficher le texte de l'ecran titre et d'attendre une entree"""

	global fenetre

	sonEcranTitre = pygame.mixer.music.load("Sounds/Title Sound.wav")
	click = pygame.mixer.Sound("Sounds/Click Start.wav")
	pygame.mixer.music.play()
	for event in pygame.event.get() :
		if event.type == VIDEORESIZE :
			width, height = event.w, event.h
	font = pygame.font.Font("Triforce.ttf", int(height/7))
	Titre = font.render("Appuyez sur espace...", True, (130,120,45))
	position_titre = Titre.get_rect(center = (width/2, height/2.1))
	for i in range(255,0,-4):
		fenetre.blit(Titre, (position_titre))
		fenetre.fill((i,i,i), special_flags=BLEND_RGB_SUB)
		sleep(0.05)
		pygame.display.flip()

	affichage = True
	fullscreen = True
	while affichage :
		for event in pygame.event.get() :
			if event.type == QUIT :
				quit()
			if event.type == KEYDOWN :
				if event.key == K_SPACE :
					click.play()
					affichage = False
			if event.type == VIDEORESIZE :
				width, height = event.w, event.h
				font = pygame.font.Font("Triforce.ttf", int(height/7))
				Titre = font.render("Appuyez sur espace...", True, (130,120,45))
				position_titre = Titre.get_rect(center = (width/2, height/2.1))
				fenetre.fill((0,0,0))
				fenetre.blit(Titre, (position_titre))
			if event.type == KEYDOWN :
				if event.key == K_F11 :
					if fullscreen == False :
						fenetre = pygame.display.set_mode((1366, 768), FULLSCREEN)
						font = pygame.font.Font("Triforce.ttf", int(height/7))
						Titre = font.render("Appuyez sur espace...", True, (130,120,45))
						position_titre = Titre.get_rect(center = (width/2, height/2.1))
						fenetre.fill((0,0,0))
						fenetre.blit(Titre, (position_titre))
						fullscreen = True
					else :
						fenetre = pygame.display.set_mode((1080, 607))
						font = pygame.font.Font("Triforce.ttf", int(height/7))
						Titre = font.render("Appuyez sur espace...", True, (130,120,45))
						position_titre = Titre.get_rect(center = (width/2, height/2.1))
						fenetre.fill((0,0,0))
						fenetre.blit(Titre, (position_titre))
						fullscreen = False
			if event.type == KEYDOWN :
				if event.key == K_ESCAPE and fullscreen == True :
					fenetre = pygame.display.set_mode((1080,607))
					font = pygame.font.Font("Triforce.ttf", int(height/7))
					Titre = font.render("Appuyez sur espace...", True, (130,120,45))
					position_titre = Titre.get_rect(center = (width/2, height/2.1))
					fenetre.fill((0,0,0))
					fenetre.blit(Titre, (position_titre))
					fullscreen = False
		pygame.display.flip()
	pygame.mixer.music.fadeout(800)
	Disparition_Fondu(0.015)
	return width, height, fullscreen


def InitNombreJoueurs (width, height, fullscreen) :

	"""Permet d'utiliser la fenetre graphique pour entrer le nombre de participants."""

	global backgroundMenu
	global fenetre
	pygame.time.Clock().tick(30)
	entry = ""
	apparition = 1
	backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
	backgroundMenu = pygame.transform.scale(backgroundMenu, (width, height))


	while True :
		for event in pygame.event.get() :
			if event.type == QUIT :
				quit()
			if event.type == KEYDOWN :
				if not (event.key == K_BACKSPACE or event.key == K_RETURN) :
						entry += event.unicode
					#La touche backspace efface simplement un caractère
				if event.key == K_BACKSPACE:
					entry = entry[:-1]
				#La touche entrée enregistre l'entrée
				if event.key == K_RETURN:
					try :
						nombre = int(entry)
						return nombre, width, height, fullscreen
					except ValueError :
						entry = ""
				if event.key == K_F11 :
					if fullscreen == False :
						fenetre = pygame.display.set_mode((1366, 768), FULLSCREEN)
						size = fenetre.get_size()
						backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
						backgroundMenu = pygame.transform.scale(backgroundMenu, size)
						fullscreen = True
					else :
						fenetre = pygame.display.set_mode((1080,607))
						size = fenetre.get_size()
						backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
						backgroundMenu = pygame.transform.scale(backgroundMenu, size)
						fullscreen = False
				if event.key == K_ESCAPE and fullscreen == True :
					fenetre = pygame.display.set_mode((1080,607))
					size = fenetre.get_size()
					backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
					backgroundMenu = pygame.transform.scale(backgroundMenu, size)
					entry = entry[:-1]
					fullscreen = False
			elif event.type == VIDEORESIZE :
				backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
				backgroundMenu = pygame.transform.scale(backgroundMenu, (event.w, event.h))
				#event.h et event.w correspondent aux nouvelles dimensions de la fenêtre
				width, height = event.w, event.h

		fontZelda = pygame.font.Font("triforce.ttf", int(height/10))
		fontZeldaOmbre = pygame.font.Font("triforce.ttf", int(height/10)+1)

		titreEntree = fontZelda.render("Combien de joueurs etes-vous ?", True, (110, 100, 40))
		entree = fontZelda.render(entry, True, (110, 100, 40))
		ombreTitre = fontZeldaOmbre.render("Combien de joueurs etes-vous ?", True, (30,25,10))
		ombreEntree = fontZeldaOmbre.render(entry, True, (30,25,10))

		#Definit les positions des rectangles avec les textes
		position_titre = titreEntree.get_rect(center = (width/2, height/4-(height/10+10)))
		position_entree = entree.get_rect(center = (width/2, height/4))
		position_ombreTitre = titreEntree.get_rect(center = (width/2, height/4-(height/10+10)))
		position_ombreEntree = entree.get_rect(center = (width/2, height/4))

		#Affiche le backgroundMenu, puis les textes par dessus, et actualise ensuite
		fenetre.blit(backgroundMenu, (0,0))
		fenetre.blit(ombreTitre, (position_ombreTitre))
		fenetre.blit(titreEntree, (position_titre))
		fenetre.blit(ombreEntree, (position_ombreEntree))
		fenetre.blit(entree, (position_entree))
		pygame.display.flip()

def InitNoms(Nombre_de_joueurs, width, height, fullscreen) :

	"""Initialise les Noms des joueurs en fonction du nombre de joueurs."""

	global backgroundMenu
	global fenetre
	pygame.time.Clock().tick(30)
	Noms = {}
	joueur = 1
	entry = ""

	pygame.key.set_repeat(150, 25)
	while joueur in range(1, Nombre_de_joueurs+1) :
		for event in pygame.event.get() :
			if event.type == KEYDOWN :
				if not (event.key == K_BACKSPACE or event.key == K_RETURN) :
					entry += event.unicode
				#La touche backspace efface simplement une lettre
				if event.key == K_BACKSPACE :
					entry = entry[:-1]
				#La touche entrée enregistre le nom qui a été écrit
				if event.key == K_RETURN :
					Noms[joueur] = entry
					joueur += 1 #J'incrémente l'indice qui me sert de clé dans mon dictionnaire, et j'associe le nom
					entry = ""
					#Le blit permet de poser un objet sur l'interface graphique, mais pas de l'affficher
					fenetre.blit(backgroundMenu, (0,0))
					#On utilise la fonction flip pour rafraichir l'écran et donc afficher les éléments ajoutés
					pygame.display.flip()
				if event.key == K_F11 :
					if fullscreen == False :
						fenetre = pygame.display.set_mode((1366, 768), FULLSCREEN)
						size = fenetre.get_size()
						backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
						backgroundMenu = pygame.transform.scale(backgroundMenu, size)
						fullscreen = True
					else :
						fenetre = pygame.display.set_mode((1080, 607))
						size = fenetre.get_size()
						backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
						backgroundMenu = pygame.transform.scale(backgroundMenu, size)
						fullscreen = False
				if event.key == K_ESCAPE and fullscreen == True :
					fenetre = pygame.display.set_mode((1080, 607))
					size = fenetre.get_size()
					backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
					backgroundMenu = pygame.transform.scale(backgroundMenu, size)
					fullscreen = False
			#L'événement VIDEORESIZE coreespond à un redimmensionnement de la fenêtre
			elif event.type == VIDEORESIZE :
				backgroundMenu = pygame.image.load("Pics/Arbre Mojo large.png").convert()
				backgroundMenu = pygame.transform.scale(backgroundMenu, (event.w, event.h))
				#event.h et event.w correspondent aux nouvelles dimensions de la fenêtre
				width, height = event.w, event.h
			elif event.type == QUIT :
				quit()

		#Définit la police à utiliser
		fontZelda = pygame.font.Font("triforce.ttf", int(height/10))
		fontZeldaOmbre = pygame.font.Font("triforce.ttf", int(height/10)+1)

		#Utilise render pour créer du texte
		titreEntree = fontZelda.render("Entrez le nom du joueur %s :" %str(joueur), True, (110, 100, 40))
		entree = fontZelda.render(entry, True, (110, 100, 40))
		ombreTitre = fontZeldaOmbre.render("Entrez le nom du joueur %s :"%str(joueur), True, (30,25,10))
		ombreEntree = fontZeldaOmbre.render(entry, True, (30,25,10))

		#Definit les positions des rectangles avec les textes
		position_titre = titreEntree.get_rect(center = (width/2, height/4-(height/10+10)))
		position_entree = entree.get_rect(center = (width/2, height/4))
		position_ombreTitre = titreEntree.get_rect(center = (width/2, height/4-(height/10+10)))
		position_ombreEntree = entree.get_rect(center = (width/2, height/4))

		#Affiche le backgroundMenu, puis les textes par dessus, et actualise ensuite
		fenetre.blit(backgroundMenu, (0,0))
		if joueur in range(1, Nombre_de_joueurs+1) :
			fenetre.blit(ombreTitre, (position_ombreTitre))
			fenetre.blit(ombreEntree, (position_ombreEntree))
			fenetre.blit(titreEntree, (position_titre))
			fenetre.blit(entree, (position_entree))

		pygame.display.flip()

	return Noms, width, height, fullscreen

def InitMains(Nombre_de_joueurs, source) :

	"""Initialise chaque main de joueur en fonction du nombre de joueurs."""

	mains = {}
	for joueur in range(Nombre_de_joueurs) :
		mains[joueur+1] = []
		for cartes in range(7) :		#Donne 7 cartes à chaque joueur
			mains[joueur+1].append(source.pop(0))

	return mains

def Piocher (Main_du_joueur, Nombre_cartes, source) :

	"""Permet de piocher une ou plusieurs cartes dans le paquet de cartes."""

	from time import sleep

	for i in range(Nombre_cartes) :
		Main_du_joueur.append(source.pop(0))
		sleep(0.5)
		if len(source) == 0 :	#Si la Paquet est vide, appelle la fonction qui la réinitialise
			Paquet_vide(Defausse, source)

def Affiche_cartes (imagesCartes, mains, joueur, width_carte, width_screen, height_screen, selectedCardID, cursX, cursY) :

	"""Affiche les cartes voulues, souvent celles de la main d'un joueur"""
	global Paquet
	i=0
	if len(mains[joueur]) > 7 :
		deltaX = 7*width_carte/len(mains[joueur])
	else :
		deltaX = width_carte
	positionPremiereCarte = (width_screen/2) - ((len(mains[joueur])-1)*deltaX + widthCarte)/2

	for indice, carte in enumerate(mains[joueur]) :
		carteDraw = imagesCartes[tuple(carte)]
		carteDraw = pygame.transform.scale(carteDraw, (widthCarte, heightCarte))
		if indice == selectedCardID :
			fenetre.blit(carteDraw,(positionPremiereCarte + i*deltaX + cursX, height_screen*0.75 + cursY))
		else :
			fenetre.blit(carteDraw,(positionPremiereCarte + i*deltaX, height_screen*0.75))
		i += 1

	return positionPremiereCarte, deltaX


def Paquet_vide(source, destination) :

	"""Reconstruit simplement le Paquet quand il est vide."""

	from random import shuffle

	while len(source) > 1 :
		destination.append(source.pop(1))
	shuffle(destination)

def cartesJouables(Main_du_joueur, destination, valeurMalus) :

	cartes_jouables = []				#Crée une liste avec toutes les cartes jouables, pour simplifier l'affichage
	for carte in Main_du_joueur : 			#Verifie si on peut jouer une carte
		if carte[0] == destination[0][0] or carte[1] == destination[0][1] or carte[1] == "" :		#Teste le entryero, puis la couleur, et ensuite si c'est une carte spéciale
			cartes_jouables.append(carte)

	return cartes_jouables

def preTour(Main_du_joueur, valeurMalus) :

	global Paquet, Defausse
	if Defausse[0][0] == "+2" and valeurMalus != 0 :
		Piocher(Main_du_joueur, 2, Paquet)
	valeurMalus = 0
	return valeurMalus

def consequences(destination, mains, valeurMalus, Sens_de_rotation, joueur, Nombre_joueurs, width, height) :

	global Paquet
	valeurMalus = 0
	couleur = destination[0][1]
	if couleur == "" :
		#On choisit la couleur de la carte modifiable, qui sera gardée jusqu'au tour suivant
		fenetre.blit(JokerRouge, (width/2-200, height/2-200))
		fenetre.blit(JokerVert, (width/2, height/2-200))
		fenetre.blit(JokerBleu, (width/2-200, height/2))
		fenetre.blit(JokerJaune, (width/2, height/2))
		pygame.display.flip()
		while couleur == "" :
			for event in pygame.event.get() :
				if event.type == MOUSEBUTTONDOWN and event.pos[0] in range(int(width/2 - 200), int(width/2 + 200)) and event.pos[1] in range(int(height/2 - 200), int(height/2 + 200)) :
					if event.pos[0] in range(int(width/2 - 200), int(width/2)) :
						if event.pos[1] in range(int(height/2 - 200), int(height/2)) :
							couleur = "Rouge"
						else :
							couleur = "Bleu"
					else :
						if event.pos[1] in range(int(height/2 - 200), int(height/2)) :
							couleur = "Vert"
						else :
							couleur = "Jaune"

	if destination[0][0] == "+4" :
		if joueur == Nombre_joueurs and Sens_de_rotation == 1 :
			joueur = 0
		if joueur == 1 and Sens_de_rotation == -1 :
			joueur = Nombre_joueurs + 1
		joueur += Sens_de_rotation
		Piocher(mains[joueur], 4, Paquet)
	elif destination[0][0] == "+2" :
		valeurMalus += 2
	elif destination[0][0] == "Changement de Sens" :
		Sens_de_rotation = -Sens_de_rotation
	elif destination[0][0] == "Sens Interdit" :
		if joueur == Nombre_joueurs and Sens_de_rotation == 1 :
			joueur = 0
		if joueur == 1 and Sens_de_rotation == -1 :
			joueur = Nombre_joueurs + 1
		joueur += Sens_de_rotation

	return valeurMalus, Sens_de_rotation, joueur, couleur #,blocage

if __name__ == "__main__" :

	#from FonctionsGraphiques import *
	from time import sleep
	from random import choice

	import pygame
	from pygame.locals import *

	pygame.init()

		#Initialisation de la fenetre principale
	fenetre = pygame.display.set_mode((1366, 768), FULLSCREEN)
	pygame.display.set_caption("UNO")
	#Chargement de l'icone de fenetre
	icone = pygame.image.load("Pics/Icone.png")
	pygame.display.set_icon(icone)

	#Initialise le paquet
	Paquet = InitPaquet()

	#On affiche l'écran de chragement, et width et height sont créées pour la première fois
	#dicoDesCartes est créé pendant l'écran de chargement
	width, height, dicoDesCartes = Ecran_Chargement()

	#Debut de l'affichage graphique
	#Fait apparaitre l'ecran titre et attend. Renvoie les nouvelles largeurs et hauteurs dns le cas d'un redimmensionnement
	width, height, fullscreen = Ecran_Titre(width, height)

	#Chargement de la musique du menu
	pygame.mixer.music.load("Sounds/Musics/SS-Main menu.wav")
	pygame.mixer.music.play()
	#Apparition du backgroundMenu grace au special_flags
	Apparition_Fondu("Pics/Arbre Mojo large.png", 0.025, width, height)
	sleep(0.125)

	#Initialisation des infos des joueurs
	Nombre_joueurs, width, height, fullscreen = InitNombreJoueurs(width, height, fullscreen)
	Noms, width, height, fullscreen = InitNoms(Nombre_joueurs, width, height, fullscreen)
	Mains = InitMains(Nombre_joueurs, Paquet)  #Cree les mains de chaque joueur, sous forme de dictionnaire
	sleep(1)
	Disparition_Fondu(0.025)
	pygame.mixer.music.fadeout(300)

	JokerRouge = pygame.image.load("Pics/Joker Rouge.png")
	JokerVert = pygame.image.load("Pics/Joker Vert.png")
	JokerBleu = pygame.image.load("Pics/Joker Bleu.png")
	JokerJaune = pygame.image.load("Pics/Joker Jaune.png")
	JokerRouge.set_colorkey((0,0,0))
	JokerVert.set_colorkey((0,0,0))
	JokerBleu.set_colorkey((0,0,0))
	JokerJaune.set_colorkey((0,0,0))
	backs = ["Pics/BackgroundJeu.png", "Pics/BackgroundJeu2.png", "Pics/BackgroundJeu3.png", "Pics/BackgroundJeu4.png"]
	Background = choice(backs)
	if Background in ["Pics/BackgroundJeu2.png", "Pics/BackgroundJeu4.png"] :
		Bouton = "Pics/BoutonTour2.png"
	else :
		Bouton = "Pics/BoutonTour.png"
	backgroundJeu = pygame.image.load(Background).convert()
	backgroundJeu = pygame.transform.scale(backgroundJeu, (width, height))
	boutonTour = pygame.image.load(Bouton).convert()
	boutonTour.set_colorkey((255,255,255))
	widthCarte = int(width*0.1)
	heightCarte = int(widthCarte*1.578)

	#Initialisation des variables du jeu
	#Choisit la première carte de la défausse
	i = 0
	while not Paquet[i][0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] :
		i += 1
	Defausse = [Paquet.pop(i)]	#Pioche la premiere carte, posee sur la table
	Joueur = 1 	#Definit le entryero du joueur qui doit jouer
	Pas = 1		#Definit le sens de rotation
	Malus = 0	#Nombre de cartes à piocher à chaque +4 ou +2
	FinPartie = False
	#blocage = False
	fullscreen = True
	cursorX = cursorY = 0
	carte_select = ()
	idSelect = -1
	positionDefausse = (int(width/2 - widthCarte/2), int(height/2 - heightCarte/2))

	pygame.mixer.music.load("Sounds/Musics/1 Hour Music.wav")
	pygame.mixer.music.play(-1)

	#Affiche le plateau en fondu
	carteDefausse = dicoDesCartes[tuple(Defausse[0])]
	carteDefausse = pygame.transform.scale(carteDefausse, (widthCarte, heightCarte))
	for i in range(255,0,-4):
			fenetre.blit(backgroundJeu, (0,0))
			fenetre.blit(boutonTour, (width*0.8, height/5-50))
			fenetre.blit(carteDefausse, positionDefausse)
			fenetre.fill((i,i,i), special_flags=BLEND_RGB_SUB)
			sleep(0.005)
			pygame.display.flip()

	while FinPartie == False :
		Malus = preTour(Mains[Joueur], Malus)
		cartes_jouables = cartesJouables(Mains[Joueur], Defausse, Malus)

		#if blocage == True :

		if len(cartes_jouables) != 0 :
			for event in pygame.event.get() :
				if event.type == QUIT :
					quit()

				if event.type == VIDEORESIZE :
					backgroundJeu = pygame.image.load(Background).convert()
					backgroundJeu = pygame.transform.scale(backgroundJeu, (event.w, event.h))
					#event.h et event.w correspondent aux nouvelles dimensions de la fenêtre
					width, height = event.w, event.h
					widthCarte = int(width*0.1)
					heightCarte = int(widthCarte*1.578)
					positionDefausse = (int(width/2 - widthCarte/2), int(height/2 - heightCarte/2))
				if event.type == KEYDOWN and event.key == K_F11 :
					if fullscreen == False :
						fenetre = pygame.display.set_mode((1366, 768), FULLSCREEN)
						fullscreen = True
					else :
						fenetre = pygame.display.set_mode((1080, 607))
						fullscreen = False
				if event.type == KEYDOWN and event.key == K_ESCAPE:
					fenetre = pygame.display.set_mode((1080, 607))
					fullscreen = False

				#Affichage du nom du joueur
				name = Noms[Joueur]
				font = pygame.font.Font("Triforce.ttf", int(height/12))
				NomDuJoueur = font.render("C'est le tour de %s" %name, True, (255,255,255))
				position_nom = NomDuJoueur.get_rect(center = (width/5, height/5))

				#Deplacement d'une carte
				if event.type == MOUSEMOTION and event.buttons[0] == 1 :
					if carte_select == () :
						if event.pos[1] in range(int(height*0.75), height) :
							for i in range(len(Mains[Joueur])-1) :
								if event.pos[0] in range(int(positionPremiereCarte + i*deltaX), int(positionPremiereCarte + (i+1)*deltaX)) :
									carte_select = Mains[Joueur][i]
									idSelect = i
							if event.pos[0] in range(int(positionPremiereCarte + (len(Mains[Joueur])-1)*deltaX), int(positionPremiereCarte + (len(Mains[Joueur])-1)*deltaX + widthCarte)) :
								carte_select = Mains[Joueur][-1]
								idSelect = len(Mains[Joueur])-1
					else :
						cursorX += event.rel[0]
						cursorY += event.rel[1]

				#Teste si la carte choisie est jouable ou non et si c'est le cas, effectue les actions en consequence
				if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[0] in range(positionDefausse[0], positionDefausse[0] + widthCarte) and event.pos[1] in range(positionDefausse[1], positionDefausse[1] + heightCarte) :
					if carte_select in cartes_jouables :
						Defausse.insert(0, Mains[Joueur].pop(idSelect))
						if len(Mains[Joueur]) == 0 :
							FinPartie = True
							break
						Malus, Pas, Joueur, couleurTemporaire = consequences(Defausse, Mains, Malus, Pas, Joueur, Nombre_joueurs, width, height)
						if Defausse[0][1] == "" :
							Defausse[0][1] = couleurTemporaire
						if Defausse[1][0] == "+4" or Defausse[1][0] == "Joker" :			#Si la carte est à couleur variable, réinitialise sa couleur
							Defausse[1][1] = ""
						if Joueur == Nombre_joueurs and Pas == 1 :
							Joueur = 0
						if Joueur == 1 and Pas == -1 :
							Joueur = Nombre_joueurs + 1
						Joueur += Pas
					carte_select = ()
					idSelect = -1
					cursorX = cursorY = 0
				if event.type == MOUSEBUTTONUP and not(event.pos[0] in range(positionDefausse[0], positionDefausse[0] + widthCarte) and event.pos[1] in range(positionDefausse[1], positionDefausse[1] + heightCarte)) :
					carte_select = ()
					idSelect = -1
					cursorX = cursorY = 0

				if event.type == MOUSEBUTTONDOWN and event.pos[0] in range(int(width*0.8), int(width*0.9)+200) and event.pos[1] in range(int(height/5-50), int(height/5+50)) :
					font = pygame.font.Font("Triforce.ttf", int(height/11))
					phrase = font.render("Vous piochez une carte", True, (0,0,0))
					position_titre = phrase.get_rect(center = (width/2, height/2.1))
					fenetre.blit(phrase, (position_titre))
					fenetre.blit(NomDuJoueur, position_nom)
					pygame.display.flip()
					sleep(0.75)
					Piocher(Mains[Joueur], 1, Paquet)
					if Joueur == Nombre_joueurs and Pas == 1 :
						Joueur = 0
					if Joueur == 1 and Pas == -1 :
						Joueur = Nombre_joueurs + 1
					Joueur += Pas

			#Affichage de tous les objets à l'écran
			#On commence par le background
			fenetre.blit(backgroundJeu, (0, 0))
			#Ensuite la carte du dessus du tas
			if Defausse[0][0] == "Joker" :
				carteDefausse = dicoDesCartes[("Joker", "")]
			elif Defausse[0][0] == "+4":
				carteDefausse = dicoDesCartes[("+4", "")]
			else :
				carteDefausse = dicoDesCartes[tuple(Defausse[0])]
			carteDefausse = pygame.transform.scale(carteDefausse, (widthCarte, heightCarte))
			fenetre.blit(carteDefausse, positionDefausse)
			#Puis le joueur dont c'est le tour
			fenetre.blit(NomDuJoueur, position_nom)
			#Puis on affiche toutes les cartes avec la fonction Affiche_cartes
			positionPremiereCarte, deltaX = Affiche_cartes(dicoDesCartes, Mains, Joueur, widthCarte, width, height, idSelect, cursorX, cursorY)

		if len(cartes_jouables) == 0 :
			font = pygame.font.Font("Triforce.ttf", int(height/11))
			phrase = font.render("Vous devez piocher une carte", True, (0,0,0))
			position_titre = phrase.get_rect(center = (width/2, height/2.1))
			fenetre.blit(phrase, (position_titre))
			fenetre.blit(NomDuJoueur, position_nom)
			pygame.display.flip()
			sleep(0.75)
			Piocher(Mains[Joueur], 1, Paquet)
			if Joueur == Nombre_joueurs and Pas == 1 :
				Joueur = 0
			if Joueur == 1 and Pas == -1 :
				Joueur = Nombre_joueurs + 1
			Joueur += Pas

		fenetre.blit(boutonTour, (width*0.8, height/5-50))
		pygame.display.flip()

	pygame.mixer.music.fadeout(250)
	Disparition_Fondu(0.025)
	#On charge la musique de fin
	creditMusic = pygame.mixer.music.load("Sounds/Musics/Minish Cap Credits.wav")

	#on utilise une police specifique aux credits de fin
	fontEnd = pygame.font.Font("The Wild Breath of Zelda.otf", int(height/10))
	End = fontEnd.render("%s a gagne, bravo !" %Noms[Joueur], True, (255,255,255))
	End2 = fontEnd.render("Merci d'avoir joue !", True, (255,255,255))
	#Le deuxieme texte n'a pas la meme taille de police
	fontCredits = pygame.font.Font("The Wild Breath of Zelda.otf", int(height/15))
	Credits = fontCredits.render("Jeu programme par Julie et Philippe", True, (255,255,255))
	#On centre les textes en utilisant les get_rect()
	position_end = End.get_rect(center = (width/2, height/4))
	position_credits = Credits.get_rect(center = (width/2, height/1.5))
	fenetre.fill((0,0,0))
	#On lance la musique
	pygame.mixer.music.play()
	#Et on affiche le dernier ecran
	for i in range(255,0,-4):
		fenetre.blit(End, position_end)
		fenetre.blit(End2, (position_end[0], position_end[1]+100))
		fenetre.blit(Credits, position_credits)
		fenetre.fill((i,i,i), special_flags=BLEND_RGB_SUB)
		sleep(0.05)
		pygame.display.flip()
	sleep(7)
	Disparition_Fondu(0.005)
	#Cet ecran ci-apres sert de generique
	Hyrule = pygame.image.load("Pics/HyrulePersos.jpg").convert()
	Hyrule = pygame.transform.scale(Hyrule, (width, height))
	for i in range(255,0,-4):
		fenetre.blit(Hyrule, (0,0))
		fenetre.fill((i,i,i), special_flags=BLEND_RGB_ADD)
		sleep(0.05)
		pygame.display.flip()
	SONG_END = pygame.USEREVENT + 1
	pygame.mixer.music.set_endevent(SONG_END)
	end = 0
	while end == 0 :
		for event in pygame.event.get() :
			if event.type == SONG_END or event.type == QUIT :
				end = 1
			if event.type == KEYDOWN and event.key == K_ESCAPE:
				fenetre = pygame.display.set_mode((1080, 607))
				Hyrule = pygame.transform.scale(Hyrule, (1080, 607))
				fenetre.blit(Hyrule, (0,0))
				pygame.display.flip()
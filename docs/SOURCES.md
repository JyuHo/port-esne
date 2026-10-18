# Sources du catalogue

## PortMaster

[PortMaster](https://github.com/PortsMaster/PortMaster-New) publie des ports prêts à jouer pour consoles portables
Linux. Sur ~1 450 ports, 93 ont une version x86_64. Gardés: ceux prêts à jouer (`rtr`), sans runtime PortMaster
(Love2D, Godot, GameMaker, Mono...), dont la licence est lisible dans l'archive et qui se lancent avec un simple
exécutable. `tools/check_portmaster.py --candidates` liste les suivants à étudier.

Écartés pour l'instant:

- démos et shareware: DevilutionX (Diablo shareware), OpenJazz, Commander Genius, Rise of the Triad, Blake Stone,
  Chocolate Keen, CorsixTH, Cosmo, DarkPlaces...
- jeux payants dont il faut ses propres fichiers mais dont le lanceur PortMaster prépare beaucoup de choses
  (Quake, Hexen 2, Morrowind, Jazz2, Dark Forces): à reprendre un par un, ou par Flathub;
- runtime PortMaster nécessaire (2048 Plus, Bugscraper, BYTEPATH, Mr. Rescue, Nova Pinball...): ES-NE ne fournit
  pas ces runtimes;
- lancement trop lié à PortMaster (OpenTTD et Rockbot décompressent un `.7z` au premier lancement, Xargon a trois
  épisodes, Tile World passe par un sélecteur, Ken's Labyrinth réécrit sa configuration): OpenTTD vient de Flathub;
- licence absente de l'archive ou incertaine: Doom 2D, Planet Merge, Xye, SkiFree, Stunt Car Racer.

## Ultimate Catalog of Web Game Ports

[Ultimate Catalog of Web Game Ports](https://github.com/Carter54git/Ultimate-Catalog-Of-Web-Game-Ports) (582 jeux,
octobre 2026) recense des jeux jouables dans un navigateur. Il a servi de liste d'idées, pas de source de fichiers:

- La plupart des entrées sont des portages web non autorisés de jeux commerciaux récents (Cuphead, Hollow Knight,
  Balatro, Undertale, Five Nights at Freddy's, Baldi's Basics...) hébergés sur des sites de « jeux débloqués ».
  Leur redistribution n'est pas permise: **aucune n'est reprise**.
- Les portages web de décompilations (Super Mario 64, Zelda: A Link to the Past, Animal Crossing, Golden Sun,
  Virtua Fighter...) demandent la ROM du jeu; leur version native n'est pas distribuée sur Flathub et leur
  compilation n'est pas faite ici. Pistes pour plus tard.
- Les jeux libres ou moteurs réécrits de la liste ont été repris dans leur **version Linux native**, depuis PortMaster
  ou Flathub: OpenTyrian, SDLPoP (Prince of Persia), OpenTTD, SuperTux, Neverball, Sonic Robo Blast 2, SRB2Kart,
  Mindustry, Chromium B.S.U., Abuse, Cro-Mag Rally, fheroes2, Julius (Caesar III), VCMI, RigelEngine (Duke Nukem II),
  DXX-Rebirth (Descent), Sonic 3 A.I.R., GZDoom. Les démos (« Demo ») sont exclues.
- OpenGGS (Giana Sisters) vient de PortMaster.

## Flathub

Identifiants vérifiés sur `github.com/flathub/<id>` (dépôt de construction de l'application) le 18 octobre 2026.

Ajouts du 18 octobre 2026 (Flathub, dépôts de construction actifs, aucun marqué « end-of-life »):

- Macintosh: les jeux Pangea Software remis en état par Iliyas Jorio (Nanosaur 1 et 2, Bugdom 1 et 2, Otto Matic,
  Mighty Mike), CC BY-NC-SA 4.0.
- Moteurs de jeux anciens (fichiers du jeu original à fournir): OpenRA (données de C&C téléchargées par OpenRA,
  rendues gratuites par EA), CorsixTH, Return to the Roots, Chocolate Doom, EDuke32 et Raze (licence Build, non
  commerciale), Augustus, OpenRCT2, JA2 Stracciatella (licence SFI, non commerciale), Yamagi Quake II, iortcw,
  OpenMW, doukutsu-rs.
- Jeux libres: SuperTuxKart, Extreme Tux Racer, Speed Dreams, Hedgewars, Wesnoth, 0 A.D., Flare, Shattered Pixel
  Dungeon, Frozen Bubble, Taisei, AstroMenace, Open Surge, Teeworlds, DDNet, Xonotic, OpenArena, Red Eclipse,
  Sauerbraten, Endless Sky, Naev, Luanti, Veloren, Cataclysm: DDA. Ceux qui demandent clavier et souris le disent
  dans leur description.
- Écartés: Pingus, Tuxemon et l'ancien OpenArena (fin de vie sur Flathub), Freeciv, Warzone 2100 et MegaGlest
  (dépôt Flathub inactif depuis plus d'un an), Space Cadet Pinball (données Microsoft téléchargées par le paquet).

## Révision du 18 octobre 2026: rien à fournir

Retirés: tous les jeux qui demandaient les fichiers du jeu original ou une ROM (fheroes2, RigelEngine, DXX-Rebirth,
The Force Engine, GZDoom, Chocolate Doom, CorsixTH, Return to the Roots, EDuke32, Raze, Julius, Augustus, VCMI,
OpenRCT2, JA2 Stracciatella, Yamagi Quake II, iortcw, OpenMW, doukutsu-rs, Sonic 3 A.I.R.), ainsi que deux cas
douteux: SDLPoP (données de Prince of Persia © Jordan Mechner / Ubisoft redistribuées sans licence) et Trogdor
Reburninated (reprise par un fan d'un jeu © Videlectrix). Gardés parce que les ayants droit ont rendu les données
gratuites: OpenTyrian (Tyrian 2.1), OpenOMF (One Must Fall 2097), OpenRA (Command & Conquer, Red Alert), Abuse
(domaine public). Les listes « Ajouts » ci-dessus sont donc en partie caduques.

## Jeux Solarus (18 octobre 2026)

Dépôts de [gitlab.com/solarus-games](https://gitlab.com/solarus-games) et quêtes listées par le projet Solarus:

- Ajouté: Word Breaker (Llamazing, GPL-3.0, polices SIL OFL, musiques Soundimage), fichier `.solarus` publié dans
  son dépôt GitLab.
- Écartés: les jeux Zelda de fans (Mystery of Solarus DX, XD, Return of the Hylian SE, Oni-Link Begins SE, Mercuris'
  Chest, Tunics, The Only One) qui reprennent l'univers et des graphismes de Nintendo; Yarntown (hommage à Bloodborne,
  univers © Sony/FromSoftware, graphismes « tous droits réservés »); Children of Solarus (libre, mais encore en
  cours, sans version publiée); Hallow's Eve (itch.io seulement), Red Rain et Tombwater (commerciaux).

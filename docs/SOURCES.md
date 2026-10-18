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

# SPDX-License-Identifier: GPL-3.0-or-later
"""Source du catalogue: liste tenue à la main, écrite dans ``catalog.json`` par ``tools/build_catalog.py``.

Chaque port a une ``source``:
  portmaster  archive du catalogue PortMaster (https://github.com/PortsMaster/PortMaster-New), téléchargée depuis
              les releases de PortMaster; seul le dossier ``dir`` est gardé et ES-NE écrit son propre lanceur
              (``launch``: ``binary`` reçoit le suffixe ``.<arch>``, ``args``, ``cwd``, ``env`` avec ``$GAMEDIR``,
              ``gptk`` = correspondance manette -> clavier lue par esne-padkeys)
  flatpak     application Flathub installée pour l'utilisateur (``flatpak install --user``), lancée par ``flatpak run``

``requires``: ce que le joueur doit fournir (fichiers du jeu original). Aucune démo ni version shareware.
"""

CATEGORIES = [
    ("pc-dos", "PC (DOS)"),
    ("amiga", "Amiga"),
    ("macintosh", "Macintosh"),
    ("windows", "Windows"),
    ("unix", "Unix"),
    ("megadrive", "Mega Drive"),
    ("libres", "Jeux libres"),
]


def pm(zip_name, binary, *, dir=None, args=(), gptk=None, cwd="", env=None):
    name = zip_name[:-4]
    launch = {"binary": binary}
    if args:
        launch["args"] = list(args)
    if gptk:
        launch["gptk"] = gptk
    if cwd:
        launch["cwd"] = cwd
    if env:
        launch["env"] = env
    return {"type": "portmaster", "zip": zip_name, "dir": dir or name}, launch, f"https://portmaster.games/detail.html?name={name}"


def fp(app_id):
    return {"type": "flatpak", "id": app_id}, None, f"https://flathub.org/apps/{app_id}"


PORTS = [
    # --- PC (DOS)
    ("digger", "Digger", "pc-dos", "Arcade", "Creuse des galeries et ramasse les émeraudes (Windmill Software, 1983).",
     "GPL-2.0 (Digger Remastered)", None, pm("digger.zip", "digger", gptk="digger.gptk")),
    ("opentyrian", "OpenTyrian", "pc-dos", "Shoot'em up", "Shoot'em up vertical d'Epic MegaGames (1995), version 2.1 devenue gratuite.",
     "GPL-2.0 (moteur), données Tyrian 2.1 gratuites (Epic MegaGames)", None,
     pm("opentyrian.zip", "opentyrian", args=["--data=data"], gptk="opentyrian.gptk")),
    ("sdlpop", "Prince of Persia (SDLPoP)", "pc-dos", "Plates-formes", "Le premier Prince of Persia (1990) sur un moteur libre.",
     "GPL-3.0 (moteur SDLPoP); données du jeu © Jordan Mechner / Ubisoft, fournies par PortMaster", None,
     pm("sdlpop.zip", "prince", gptk="prince.gptk")),
    ("openomf", "One Must Fall 2097 (OpenOMF)", "pc-dos", "Combat", "Combat de robots géants (Diversions Entertainment, 1994), gratuit depuis 1999.",
     "MIT (moteur OpenOMF), données gratuites (Epic MegaGames)", None,
     pm("openomf.zip", "openomf", gptk="openomf.gptk",
        env={"OPENOMF_RESOURCE_DIR": "$GAMEDIR/gamedata", "OPENOMF_PLUGIN_DIR": "$GAMEDIR/plugins"})),
    ("openttd", "OpenTTD", "pc-dos", "Gestion", "Gestion de compagnie de transport, d'après Transport Tycoon Deluxe (1995).",
     "GPL-2.0, graphismes, sons et musiques libres (OpenGFX, OpenSFX, OpenMSX)", None, fp("org.openttd.OpenTTD")),
    ("abuse", "Abuse", "pc-dos", "Action", "Run and gun de Crack dot Com (1995), code et données rendus publics.",
     "domaine public et GPL-2.0", None, fp("com.github.Xenoveritas.abuse")),
    ("fheroes2", "Heroes of Might and Magic II (fheroes2)", "pc-dos", "Stratégie", "Moteur libre de Heroes of Might and Magic II (1996).",
     "GPL-2.0 (moteur)", "fichiers du jeu original (GOG ou CD)", fp("io.github.ihhub.Fheroes2")),
    ("rigelengine", "Duke Nukem II (RigelEngine)", "pc-dos", "Plates-formes", "Moteur libre de Duke Nukem II (Apogee, 1993).",
     "GPL-2.0 (moteur)", "fichiers du jeu complet (GOG ou Steam)", fp("io.github.lethal_guitar.RigelEngine")),
    ("dxx-rebirth", "Descent (DXX-Rebirth)", "pc-dos", "Action", "Moteur libre de Descent et Descent 2 (Parallax, 1995).",
     "GPL-3.0 et licence Parallax (moteur)", "fichiers du jeu complet (GOG ou Steam)", fp("io.github.dxx_rebirth.DXX-Rebirth")),
    ("theforceengine", "Star Wars: Dark Forces (The Force Engine)", "pc-dos", "FPS", "Moteur libre de Dark Forces (LucasArts, 1995).",
     "GPL-2.0 (moteur)", "fichiers du jeu complet (GOG ou Steam)", fp("io.github.theforceengine.tfe")),
    ("gzdoom", "Doom (GZDoom)", "pc-dos", "FPS", "Moteur de Doom, Doom II, Heretic et Hexen.",
     "GPL-3.0 (moteur)", "fichiers WAD du jeu (DOOM.WAD, DOOM2.WAD...) ou un jeu libre comme Freedoom", fp("org.zdoom.GZDoom")),
    # --- Amiga
    ("openggs", "Open Great Giana Sisters", "amiga", "Plates-formes", "Remake libre de The Great Giana Sisters (1987).",
     "GPL-2.0", None, pm("openggs.zip", "openggs", gptk="openggs.gptk")),
    ("supermethanebros", "Super Methane Brothers", "amiga", "Plates-formes", "Plates-formes à la Bubble Bobble, sorti sur Amiga en 1993.",
     "GPL-2.0", None, pm("supermethanebros.zip", "methane", gptk="methane.gptk")),
    ("mirrormagic", "Mirror Magic", "amiga", "Réflexion", "Miroirs et rayons lasers, d'après le jeu Amiga de 1989.",
     "GPL-2.0", None, pm("mirrormagic.zip", "mirrormagic", gptk="mirrormagic.gptk")),
    # --- Macintosh
    ("cromagrally", "Cro-Mag Rally", "macintosh", "Course", "Course de karts à l'âge de pierre (Pangea Software, 2000).",
     "CC BY-NC-SA 4.0", None, pm("cromagrally.zip", "CroMagRally")),
    # --- Windows
    ("julius", "Caesar III (Julius)", "windows", "Gestion", "Moteur libre de Caesar III (Impressions Games, 1998).",
     "AGPL-3.0 (moteur)", "fichiers du jeu original (GOG ou Steam)", fp("com.github.bvschaik.julius")),
    ("vcmi", "Heroes of Might and Magic III (VCMI)", "windows", "Stratégie", "Moteur libre de Heroes of Might and Magic III (1999).",
     "GPL-2.0 (moteur)", "fichiers du jeu original (GOG ou CD)", fp("eu.vcmi.VCMI")),
    # --- Unix
    ("minesofmoria", "Mines of Moria", "unix", "Rogue-like", "Moria (1983), l'ancêtre des rogue-likes, dans sa version Umoria.",
     "GPL-3.0", None, pm("minesofmoria.zip", "minesofmoria", cwd="saves")),
    # --- Mega Drive
    ("sonic3air", "Sonic 3 A.I.R.", "megadrive", "Plates-formes", "Sonic 3 & Knuckles (1994) refait en écran large.",
     "gratuit, usage non commercial (Eukaryot)", "ROM Sonic 3 & Knuckles (Sega Mega Drive Classics sur Steam)",
     fp("org.sonic3air.Sonic3AIR")),
    # --- Jeux libres
    ("abbayedesmorts", "L'Abbaye des Morts", "libres", "Plates-formes", "Un cathare fuit les croisés dans une abbaye maudite (Locomalito, 2010).",
     "GPL-3.0", None, pm("abbayedesmorts.zip", "abbayev2", gptk="abbayev2.gptk")),
    ("abes_adventure", "Abe's Amazing Adventure", "libres", "Plates-formes", "Exploration de pyramides à clés, à la manière du Commodore Plus/4.",
     "GPL-2.0", None, pm("abes_adventure.zip", "abe", gptk="abe.gptk")),
    ("blockamokremix", "Blockamok Remix", "libres", "Action", "Évite les blocs qui foncent sur toi.",
     "MIT", None, pm("blockamokremix.zip", "blockamokremix", gptk="blockamokremix.gptk")),
    ("davegnukem", "Dave Gnukem", "libres", "Plates-formes", "Parodie libre de Duke Nukem 1.",
     "GPL-2.0", None, pm("davegnukem.zip", "davegnukem", gptk="davegnukem.gptk")),
    ("defendguin", "Defendguin", "libres", "Arcade", "Clone de Defender avec un manchot.",
     "ISC", None, pm("defendguin.zip", "defendguin", args=["--fullscreen"], gptk="defendguin.gptk")),
    ("harmonist", "Harmonist", "libres", "Rogue-like", "Rogue-like d'infiltration: un singe sauve ses amis de la Mine.",
     "ISC", None, pm("harmonist.zip", "harmonist", args=["-F"], gptk="harmonist.gptk")),
    ("shamogu", "Shamogu", "libres", "Rogue-like", "Rogue-like tactique: un chaman et ses esprits totems.",
     "ISC", None, pm("shamogu.zip", "shamogu", args=["-F"], gptk="shamogu.gptk")),
    ("miceamaze", "MiceAmaze", "libres", "Réflexion", "Guide les souris vers ta maison avec des flèches, gare aux serpents.",
     "BSD-3-Clause", None, pm("miceamaze.zip", "miceamaze", args=["-f"], gptk="miceamaze2.gptk")),
    ("minesector", "MineSector", "libres", "Réflexion", "Démineur revisité.",
     "MIT", None, pm("minesector.zip", "minesector", gptk="minesector.gptk")),
    ("openmrac", "OpenMRac", "libres", "Course", "Course automobile en 3D vue de dessus.",
     "BSD-2-Clause", None, pm("openmrac.zip", "openmrac-es2", args=["./openmrac.dat", "--skip-settings"], gptk="openmrac.gptk")),
    ("rlone", "Rlone: A Rogue Clone", "libres", "Rogue-like", "Clone de Rogue.",
     "GPL-3.0 (code), CC BY-SA 3.0 et CC0 (sons et images)", None, pm("rlone.zip", "rlone", gptk="rlone.gptk")),
    ("scavenger", "Scavenger", "libres", "Réflexion", "Jeu à la Lode Runner, 196 tableaux.",
     "GPL-1.0", None, pm("scavenger.zip", "sdlscav", gptk="sdlscav.gptk")),
    ("sip2", "Space Invaders Part 2", "libres", "Shoot'em up", "Hommage à Space Invaders Part II.",
     "MIT", None, pm("sip2.zip", "si", gptk="si.gptk")),
    ("sudokul", "SuDokuL", "libres", "Réflexion", "Sudoku.", "MIT", None, pm("sudokul.zip", "sdkl")),
    ("trogdorrb", "Trogdor Reburninated", "libres", "Action", "Recréation du Trogdor de Homestar Runner par un fan.",
     "MIT (code); jeu original © Videlectrix", None, pm("trogdorrb.zip", "tdrb", gptk="tdrb.gptk")),
    ("supertux", "SuperTux", "libres", "Plates-formes", "Plates-formes en 2D avec Tux, la mascotte de Linux.",
     "GPL-3.0", None, fp("org.supertuxproject.SuperTux")),
    ("neverball", "Neverball", "libres", "Adresse", "Incline le plateau pour guider la bille.", "GPL-2.0", None, fp("org.neverball.Neverball")),
    ("srb2", "Sonic Robo Blast 2", "libres", "Plates-formes", "Jeu de fans Sonic en 3D sur un moteur Doom.",
     "GPL-2.0", None, fp("org.srb2.SRB2")),
    ("srb2kart", "SRB2Kart", "libres", "Course", "Karting de fans Sonic.", "GPL-2.0", None, fp("org.srb2.SRB2Kart")),
    ("mindustry", "Mindustry", "libres", "Stratégie", "Tower defense et chaînes de production.", "GPL-3.0", None,
     fp("com.github.Anuken.Mindustry")),
    ("chromium-bsu", "Chromium B.S.U.", "libres", "Shoot'em up", "Shoot'em up vertical en 3D.", "Clarified Artistic License", None,
     fp("net.sourceforge.chromium-bsu")),
]

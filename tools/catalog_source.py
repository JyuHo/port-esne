# SPDX-License-Identifier: GPL-3.0-or-later
"""Source du catalogue: liste tenue à la main, écrite dans ``catalog.json`` par ``tools/build_catalog.py``.

Chaque port a une ``source``:
  portmaster  archive du catalogue PortMaster (https://github.com/PortsMaster/PortMaster-New), téléchargée depuis
              les releases de PortMaster; seul le dossier ``dir`` est gardé et ES-NE écrit son propre lanceur
              (``launch``: ``binary`` reçoit le suffixe ``.<arch>``, ``args``, ``cwd``, ``env`` avec ``$GAMEDIR``,
              ``gptk`` = correspondance manette -> clavier lue par esne-padkeys)
  flatpak     application Flathub installée pour l'utilisateur (``flatpak install --user``), lancée par ``flatpak run``

Règle: un jeu s'installe et se joue sans rien fournir (pas de fichiers du jeu original, de ROM ni de dump), sans démo ni
version shareware, et sa licence permet la redistribution par sa source.
"""

CATEGORIES = [
    ("pc-dos", "PC (DOS)"),
    ("amiga", "Amiga"),
    ("macintosh", "Macintosh"),
    ("windows", "Windows"),
    ("unix", "Unix"),
    ("libres", "Jeux libres"),
]

KM = " Se joue au clavier et à la souris."


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
    ("openomf", "One Must Fall 2097 (OpenOMF)", "pc-dos", "Combat", "Combat de robots géants (Diversions Entertainment, 1994), gratuit depuis 1999.",
     "MIT (moteur OpenOMF), données gratuites (Epic MegaGames)", None,
     pm("openomf.zip", "openomf", gptk="openomf.gptk",
        env={"OPENOMF_RESOURCE_DIR": "$GAMEDIR/gamedata", "OPENOMF_PLUGIN_DIR": "$GAMEDIR/plugins"})),
    ("openttd", "OpenTTD", "pc-dos", "Gestion", "Gestion de compagnie de transport, d'après Transport Tycoon Deluxe (1995).",
     "GPL-2.0, graphismes, sons et musiques libres (OpenGFX, OpenSFX, OpenMSX)", None, fp("org.openttd.OpenTTD")),
    ("abuse", "Abuse", "pc-dos", "Action", "Run and gun de Crack dot Com (1995), code et données rendus publics.",
     "domaine public et GPL-2.0", None, fp("com.github.Xenoveritas.abuse")),
    ("openra", "Command & Conquer (OpenRA)", "pc-dos", "Stratégie", "Command & Conquer, Red Alert et Dune 2000 sur un moteur libre; les données des jeux, rendus gratuits par EA, sont téléchargées au premier lancement.",
     "GPL-3.0 (moteur)", None, fp("net.openra.OpenRA")),
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
    ("nanosaur", "Nanosaur", "macintosh", "Action", "Un dinosaure du futur sauve les œufs de son espèce (Pangea Software, 1998).",
     "CC BY-NC-SA 4.0", None, fp("io.jor.nanosaur")),
    ("nanosaur2", "Nanosaur 2", "macintosh", "Action", "Un ptérodactyle armé contre les voleurs d'œufs (Pangea Software, 2004).",
     "CC BY-NC-SA 4.0", None, fp("io.jor.nanosaur2")),
    ("bugdom", "Bugdom", "macintosh", "Plates-formes", "Rollie le cloporte libère le royaume des insectes (Pangea Software, 1999).",
     "CC BY-NC-SA 4.0", None, fp("io.jor.bugdom")),
    ("bugdom2", "Bugdom 2", "macintosh", "Plates-formes", "Skip la sauterelle court après son sac à dos volé (Pangea Software, 2002).",
     "CC BY-NC-SA 4.0", None, fp("io.jor.bugdom2")),
    ("ottomatic", "Otto Matic", "macintosh", "Plates-formes", "Un robot sauve les humains d'une invasion martienne (Pangea Software, 2001).",
     "CC BY-NC-SA 4.0", None, fp("io.jor.ottomatic")),
    ("mightymike", "Mighty Mike", "macintosh", "Action", "Action vue de dessus dans un magasin de jouets (Pangea Software, 1995).",
     "CC BY-NC-SA 4.0", None, fp("io.jor.mightymike")),
    # --- Windows
    # --- Unix
    ("minesofmoria", "Mines of Moria", "unix", "Rogue-like", "Moria (1983), l'ancêtre des rogue-likes, dans sa version Umoria.",
     "GPL-3.0", None, pm("minesofmoria.zip", "minesofmoria", cwd="saves")),
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
    ("supertuxkart", "SuperTuxKart", "libres", "Course", "Karting avec Tux et les mascottes du logiciel libre.", "GPL-3.0", None,
     fp("net.supertuxkart.SuperTuxKart")),
    ("extremetuxracer", "Extreme Tux Racer", "libres", "Course", "Tux dévale les pentes enneigées sur le ventre.", "GPL-2.0-or-later", None,
     fp("net.sourceforge.ExtremeTuxRacer")),
    ("speed-dreams", "Speed Dreams", "libres", "Course", "Simulation de course automobile.", "GPL-2.0-or-later", None,
     fp("org.speed_dreams.SpeedDreams")),
    ("hedgewars", "Hedgewars", "libres", "Stratégie", "Combats de hérissons au tour par tour, à la Worms.", "GPL-2.0", None, fp("org.hedgewars.Hedgewars")),
    ("wesnoth", "La Bataille pour Wesnoth", "libres", "Stratégie", "Stratégie au tour par tour dans un monde de fantasy." + KM,
     "GPL-2.0-or-later", None, fp("org.wesnoth.Wesnoth")),
    ("0ad", "0 A.D.", "libres", "Stratégie", "Stratégie en temps réel dans l'Antiquité." + KM, "GPL-2.0-or-later (code), CC BY-SA 3.0 (données)", None,
     fp("com.play0ad.zeroad")),
    ("flare", "Flare", "libres", "RPG", "Action-RPG à la Diablo.", "GPL-3.0 (moteur), CC BY-SA 3.0 (données)", None, fp("org.flarerpg.Flare")),
    ("shatteredpd", "Shattered Pixel Dungeon", "libres", "Rogue-like", "Rogue-like en pixel art.", "GPL-3.0", None,
     fp("com.shatteredpixel.shatteredpixeldungeon")),
    ("frozen-bubble", "Frozen Bubble", "libres", "Réflexion", "Lance des bulles et fais-les éclater par trois.", "GPL-2.0", None,
     fp("org.frozen_bubble.frozen-bubble")),
    ("taisei", "Taisei", "libres", "Shoot'em up", "Shoot'em up à la Touhou.", "MIT (code), licences libres variées (données)", None,
     fp("org.taisei_project.Taisei")),
    ("astromenace", "AstroMenace", "libres", "Shoot'em up", "Shoot'em up spatial en 3D.", "GPL-3.0", None, fp("com.viewizard.AstroMenace")),
    ("opensurge", "Open Surge", "libres", "Plates-formes", "Plates-formes rapide dans l'esprit des Sonic 16 bits.", "GPL-3.0", None,
     fp("org.opensurge2d.OpenSurge")),
    ("teeworlds", "Teeworlds", "libres", "Action", "Action en 2D multijoueur.", "Zlib (code), CC BY-SA 3.0 (données)", None, fp("com.teeworlds.Teeworlds")),
    ("ddnet", "DDraceNetwork", "libres", "Plates-formes", "Course d'obstacles coopérative, d'après Teeworlds.", "Zlib", None, fp("tw.ddnet.ddnet")),
    ("xonotic", "Xonotic", "libres", "FPS", "FPS d'arène rapide.", "GPL-3.0-or-later", None, fp("org.xonotic.Xonotic")),
    ("openarena", "OpenArena", "libres", "FPS", "FPS d'arène dans l'esprit de Quake III.", "GPL-2.0-or-later", None, fp("io.github.ec_.Quake3e.OpenArena")),
    ("redeclipse", "Red Eclipse", "libres", "FPS", "FPS d'arène avec parkour.", "Zlib (code), CC BY-SA 3.0 (données)", None, fp("net.redeclipse.RedEclipse")),
    ("sauerbraten", "Cube 2: Sauerbraten", "libres", "FPS", "FPS rapide et éditeur de cartes intégré.", "Zlib", None, fp("org.sauerbraten.Sauerbraten")),
    ("endless-sky", "Endless Sky", "libres", "Simulation", "Commerce et combats spatiaux à la Escape Velocity." + KM, "GPL-3.0", None,
     fp("io.github.endless_sky.endless_sky")),
    ("naev", "Naev", "libres", "Simulation", "Exploration spatiale, commerce et combats." + KM, "GPL-3.0", None, fp("org.naev.Naev")),
    ("luanti", "Luanti", "libres", "Bac à sable", "Jeu de construction en cubes (ex-Minetest).", "LGPL-2.1-or-later (moteur)", None, fp("org.luanti.luanti")),
    ("veloren", "Veloren", "libres", "RPG", "RPG en monde ouvert multijoueur en voxels." + KM, "GPL-3.0", None, fp("net.veloren.veloren")),
    ("cataclysm-dda", "Cataclysm: Dark Days Ahead", "libres", "Rogue-like", "Survie post-apocalyptique au tour par tour." + KM, "CC BY-SA 3.0", None,
     fp("org.cataclysmdda.CataclysmDDA")),
]

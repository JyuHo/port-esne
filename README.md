# port-esne

Catalogue des **ports** proposés au téléchargement par [ES-NE](https://github.com/JyuHo/ES-NE), dans le menu
**MISES À JOUR ET TÉLÉCHARGEMENTS > TÉLÉCHARGEMENT DE CONTENU** d'EmulationStation.

Un port est un jeu qui tourne nativement sous Linux: remake libre, moteur réécrit d'un jeu ancien ou jeu libre.
Les jeux sont classés par machine d'origine (PC (DOS), Amiga, Macintosh, Windows, Unix, Mega Drive) et une
catégorie **Jeux libres** regroupe les créations originales. Pas de démo ni de version shareware.

## Ce que contient le dépôt

| Fichier | Rôle |
|---|---|
| `catalog.json` | le catalogue lu par ES-NE (`esctl store`) |
| `LICENSES.md` | licence de chaque jeu et ce que le joueur doit fournir |
| `docs/SOURCES.md` | d'où viennent les jeux, ce qui a été écarté et pourquoi |
| `tools/catalog_source.py` | la liste tenue à la main |
| `tools/build_catalog.py` | écrit `catalog.json` et `LICENSES.md` |
| `tools/check_portmaster.py` | vérifie les entrées PortMaster (`--deep`: contenu des archives, `--candidates`: pistes d'ajout) |

**Aucun jeu n'est hébergé ici.** Chaque jeu est téléchargé sur la machine du joueur depuis sa source:

- **PortMaster**: archive publiée dans les releases de [PortMaster](https://github.com/PortsMaster/PortMaster-New),
  somme md5 vérifiée. ES-NE ne garde que le dossier du jeu et écrit son propre lanceur (le script PortMaster n'est
  pas utilisé); les jeux qui n'acceptent que le clavier se jouent à la manette grâce à `esne-padkeys` et au fichier
  `.gptk` du port.
- **Flathub**: application installée pour l'utilisateur (`flatpak install --user flathub ...`) et lancée par
  `flatpak run`. Les moteurs de jeux anciens (fheroes2, Julius, VCMI, RigelEngine...) demandent les fichiers du jeu
  original, que le joueur doit posséder: c'est indiqué dans la description du jeu.

## Format de `catalog.json`

```json
{
 "schema": 1,
 "categories": [{"id": "pc-dos", "name": "PC (DOS)"}],
 "ports": [
  {
   "id": "opentyrian",
   "title": "OpenTyrian",
   "category": "pc-dos",
   "genre": "Shoot'em up",
   "description": "Shoot'em up vertical d'Epic MegaGames (1995)...",
   "license": "GPL-2.0 (moteur), données Tyrian 2.1 gratuites",
   "homepage": "https://portmaster.games/detail.html?name=opentyrian",
   "source": {"type": "portmaster", "zip": "opentyrian.zip", "dir": "opentyrian"},
   "launch": {"binary": "opentyrian", "args": ["--data=data"], "gptk": "opentyrian.gptk", "cwd": "", "env": {}}
  }
 ]
}
```

- `requires` (facultatif): ce que le joueur doit fournir, par exemple les fichiers du jeu original.
- `source.type`: `portmaster` (`zip`, `dir`) ou `flatpak` (`id`).
- `launch` (PortMaster seulement): `binary` reçoit le suffixe de l'architecture (`opentyrian.x86_64`), `args`,
  `cwd` (sous-dossier de lancement), `env` (`$GAMEDIR` = dossier du jeu), `gptk` (correspondance manette -> clavier).
- Un champ inconnu est ignoré par ES-NE; un changement incompatible augmente `schema`.

## Ajouter un jeu

1. Vérifier la licence (fichiers `LICENSE`/`COPYING` de l'archive, page du projet). Pas de démo, pas de shareware,
   pas de jeu commercial redistribué sans autorisation.
2. Ajouter une ligne dans `tools/catalog_source.py`.
3. `python3 tools/build_catalog.py && python3 tools/check_portmaster.py --deep`
4. Committer `catalog.json` et `LICENSES.md` avec la source.

ES-NE relit le catalogue au plus une fois par jour, ou tout de suite avec **ACTUALISER** dans le menu.

## Licence

Le catalogue et les scripts sont sous [GPL-3.0-or-later](LICENSE), comme ES-NE. Les jeux gardent leur propre
licence (voir [LICENSES.md](LICENSES.md)); les noms et marques citées appartiennent à leurs détenteurs.

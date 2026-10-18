#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Vérifie les entrées PortMaster de ``catalog.json`` contre le catalogue PortMaster du moment.

Sans option: archive présente, version x86_64, pas de démo. ``--deep`` télécharge aussi chaque archive et vérifie
que le dossier, l'exécutable ``<binary>.x86_64`` et le fichier ``.gptk`` y sont. ``--candidates`` liste les jeux
PortMaster x86_64 prêts à jouer, sans démo ni runtime, absents du catalogue (pistes d'ajout, à vérifier à la main).
"""
from __future__ import annotations

import io
import json
import sys
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PORTS_JSON = "https://github.com/PortsMaster/PortMaster-New/releases/latest/download/ports.json"


def fetch(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "port-esne"}), timeout=300) as r:
        return r.read()


def main(argv: list[str]) -> int:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    pm = json.loads(fetch(PORTS_JSON))["ports"]
    errors = 0
    used = set()
    for port in catalog["ports"]:
        src = port["source"]
        if src["type"] != "portmaster":
            continue
        used.add(src["zip"])
        entry = pm.get(src["zip"])
        if entry is None:
            print(f"{port['id']}: {src['zip']} absent de PortMaster"); errors += 1; continue
        attr = entry["attr"]
        if "x86_64" not in attr.get("arch", []):
            print(f"{port['id']}: pas de version x86_64"); errors += 1
        if (attr.get("availability") or "").lower() == "demo":
            print(f"{port['id']}: démo"); errors += 1
        if "--deep" in argv:
            names = set(zipfile.ZipFile(io.BytesIO(fetch(entry["source"]["url"]))).namelist())
            launch = port["launch"]
            wanted = [f"{src['dir']}/{launch['binary']}.x86_64"]
            if launch.get("gptk"):
                wanted.append(f"{src['dir']}/{launch['gptk']}")
            for path in wanted:
                if path not in names:
                    print(f"{port['id']}: {path} absent de l'archive"); errors += 1
    if "--candidates" in argv:
        for name, entry in sorted(pm.items()):
            attr = entry["attr"]
            if (name not in used and "x86_64" in attr.get("arch", []) and attr.get("rtr") and not attr.get("runtime")
                    and (attr.get("availability") or "").lower() not in ("demo", "paid")):
                print(f"candidat: {name} ({attr.get('title')})")
    print(f"{errors} erreur(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
"""Écrit ``catalog.json`` et ``LICENSES.md`` à partir de ``tools/catalog_source.py``, puis vérifie le résultat."""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from catalog_source import CATEGORIES, PORTS  # noqa: E402

SCHEMA = 1


def build() -> dict:
    categories = dict(CATEGORIES)
    ports = []
    seen = set()
    for key, title, category, genre, description, license_, requires, (source, launch, homepage) in PORTS:
        if key in seen:
            raise SystemExit(f"{key}: identifiant en double")
        if category not in categories:
            raise SystemExit(f"{key}: catégorie inconnue {category}")
        seen.add(key)
        entry = {"id": key, "title": title, "category": category, "genre": genre, "description": description,
                 "license": license_, "homepage": homepage, "source": source}
        if requires:
            entry["requires"] = requires
        if launch:
            entry["launch"] = launch
        ports.append(entry)
    return {"schema": SCHEMA, "updated": datetime.date.today().isoformat(),
            "categories": [{"id": k, "name": v} for k, v in CATEGORIES], "ports": ports}


def licenses_md(catalog: dict) -> str:
    names = {c["id"]: c["name"] for c in catalog["categories"]}
    lines = ["# Licences des jeux", "",
             "Ce dépôt ne contient aucun jeu: seulement le catalogue. Chaque jeu est téléchargé par ES-NE depuis sa source",
             "(releases de [PortMaster](https://github.com/PortsMaster/PortMaster-New) ou [Flathub](https://flathub.org)),",
             "avec les fichiers de licence fournis par cette source. Licences relevées dans les archives PortMaster",
             "(fichiers `LICENSE`, `COPYING`...) ou sur la page du projet.", "",
             "| Jeu | Catégorie | Source | Licence | À fournir |", "|---|---|---|---|---|"]
    for p in catalog["ports"]:
        src = p["source"]
        where = f"PortMaster `{src['zip']}`" if src["type"] == "portmaster" else f"Flathub `{src['id']}`"
        lines.append(f"| [{p['title']}]({p['homepage']}) | {names[p['category']]} | {where} | {p['license']} | {p.get('requires', '')} |")
    return "\n".join(lines) + "\n"


def main() -> int:
    catalog = build()
    (ROOT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (ROOT / "LICENSES.md").write_text(licenses_md(catalog), encoding="utf-8")
    print(f"catalog.json: {len(catalog['ports'])} jeux")
    return 0


if __name__ == "__main__":
    sys.exit(main())

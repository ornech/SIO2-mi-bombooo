const carte = {
  "salles": [
    {
      "id": "hall-principal",
      "description": "Un hall d'entrée aux murs lambrissés. Deux portes s'ouvrent de part et d'autre.",
      "objets": [],
      "mobilier": [],
      "portes": [
        { "vers": "us02-salon-est", "description": "Une porte à double battant" },
        { "vers": "us03-cuisine", "description": "Une porte basse en bois" }
      ]
    },
    {
      "id": "us02-salon-est",
      "description": "Un salon poussiéreux, les rideaux tirés.",
      "objets": [
        { "nom": "chandelier en argent", "visible": true },
        { "nom": "clé rouillée", "visible": false }
      ],
      "mobilier": [
        { "nom": "commode en chêne", "fouillable": true, "contient": ["clé rouillée"] }
      ],
      "portes": [
        { "vers": "hall-principal", "description": "Une porte à double battant" }
      ]
    },
    {
      "id": "us03-cuisine",
      "description": "Une cuisine vide, les placards ouverts.",
      "objets": [],
      "mobilier": [],
      "portes": [
        { "vers": "hall-principal", "description": "Une porte basse en bois" }
      ]
    }
  ]
};

const salles = {};
carte.salles.forEach(salle => {
  salles[salle.id] = salle;
});

let salleActuelleId = "hall-principal";

const sortie = document.getElementById("sortie");
const champCommande = document.getElementById("commande");

ecrire("Tapez 'aller <élément>' pour vous déplacer, 'fouiller <meuble>' pour fouiller, 'aide' pour revoir la salle.");
decrireSalle(salleActuelleId);

champCommande.addEventListener("keydown", function (e) {
  if (e.key === "Enter") {
    const texte = champCommande.value.trim();
    champCommande.value = "";
    if (texte.length > 0) {
      ecrire("> " + texte);
      traiterCommande(texte);
    }
  }
});

function ecrire(texte) {
  sortie.textContent += texte + "\n";
  sortie.scrollTop = sortie.scrollHeight;
}

function decrireSalle(id) {
  const salle = salles[id];
  if (!salle) {
    ecrire("Erreur : la salle '" + id + "' n'existe pas.");
    return;
  }

  salleActuelleId = id;

  ecrire("");
  ecrire(salle.description);

  const objetsVisibles = salle.objets.filter(o => o.visible);
  if (objetsVisibles.length > 0) {
    ecrire("Objets visibles : " + objetsVisibles.map(o => o.nom).join(", "));
  }

  if (salle.mobilier.length > 0) {
    ecrire("Mobilier : " + salle.mobilier.map(m => m.nom).join(", "));
  }

  if (salle.portes.length > 0) {
    ecrire("Portes : " + salle.portes.map(p => p.description).join(" / "));
  }
}

function traiterCommande(texte) {
  const mots = texte.toLowerCase().split(" ");
  const verbe = mots[0];
  const cible = mots.slice(1).join(" ");
  const salle = salles[salleActuelleId];

  if (verbe === "aide" || verbe === "regarder") {
    decrireSalle(salleActuelleId);
    return;
  }

  if (verbe === "aller") {
    const porte = salle.portes.find(p =>
      p.description.toLowerCase().includes(cible) || p.vers.toLowerCase().includes(cible)
    );
    if (porte) {
      decrireSalle(porte.vers);
    } else {
      ecrire("Aucune porte ne correspond à '" + cible + "'.");
    }
    return;
  }

  if (verbe === "fouiller") {
    const meuble = salle.mobilier.find(m => m.nom.toLowerCase().includes(cible));
    if (!meuble) {
      ecrire("Aucun meuble ne correspond à '" + cible + "'.");
    } else if (!meuble.fouillable) {
      ecrire("Rien d'intéressant à fouiller là-dedans.");
    } else {
      const contenu = meuble.contient || [];
      ecrire(contenu.length > 0 ? "Vous trouvez : " + contenu.join(", ") : "Rien d'intéressant.");
    }
    return;
  }

  ecrire("Commande non reconnue. Essayez 'aller ...', 'fouiller ...' ou 'aide'.");
}

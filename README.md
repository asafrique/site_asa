# Site web — Association Sciences pour l'Afrique (ASA)

Site statique (HTML / CSS / JavaScript, sans dépendance ni build). Il se publie tel quel sur GitHub Pages.

## Structure

```
index.html          Accueil
activites.html      Vue d'ensemble des activités + soutiens
seminaires.html     ASA Séminaire, années 2021 → 2027
journal.html        Journal de vulgarisation des sciences + mini-cours
adhesion.html       Comment adhérer
contact.html        Courriel, formulaires, réseaux sociaux
bureau.html         Le bureau exécutif (absente du menu, liée depuis l'accueil et le pied de page)
404.html            Page d'erreur
CNAME               Nom de domaine personnalisé (GitHub Pages)
.nojekyll           Désactive le traitement Jekyll de GitHub Pages
assets/
  css/style.css     Feuille de style unique
  js/app.js         Menu, accordéons des séances, filtres du journal
  data/             Contenu éditable (JSON)
  posters/          Affiches des séances
  slides/           Diapositives PDF
  docs/             Mini-cours, modèle LaTeX du journal
  img/              Logos utilisés par le site
  logo/             Logo source (PDF vectoriel, JPEG, PNG transparent)
```

## Ajouter une séance de séminaire

Tout se passe dans `assets/data/seminars-<année>.json`. Chaque séance est un objet :

```json
{
  "date": "2026-09-13",
  "dateLabel": "13 septembre 2026",
  "title": "Titre de l'exposé",
  "speaker": "Prénom Nom",
  "affiliation": "Laboratoire, ville, pays",
  "abstract": "Résumé. Un saut de ligne double crée un nouveau paragraphe.",
  "bio": "Quelques lignes sur l'orateur ou l'oratrice.",
  "website": "https://…",
  "poster": "assets/posters/2026-09-13-nom.jpg",
  "slides": "assets/slides/2026-09-13-nom-slides.pdf",
  "video": "https://www.youtube.com/watch?v=…"
}
```

Seuls `dateLabel`, `title` et `speaker` sont obligatoires. Tout champ vide peut être supprimé :
le site n'affiche que ce qui existe. Les séances apparaissent dans l'ordre du fichier.

Convention de nommage des fichiers : `AAAA-MM-JJ-nom.jpg` pour les affiches,
`AAAA-MM-JJ-nom-slides.pdf` pour les diapositives.

## Changer les affiches de l'accueil

`assets/data/vitrine.json` alimente à la fois le carrousel du haut de page et la mosaïque
« Six ans de séances ». Chaque entrée demande `poster`, `speaker`, `date`, `sujet` et
`annee` (l'année sert à ouvrir le bon onglet de la page séminaires). Six entrées donnent
une mosaïque de deux rangées ; trois ou neuf fonctionnent aussi bien.

## Modifier le bureau exécutif

La liste est dans `build_pages.py`, variable `MEMBRES` : initiales, nom, fonction et une
phrase de présentation. Le site étant statique, il faut relancer `python3 build_pages.py`
après modification, ou éditer directement `bureau.html`.

## Ajouter une entrée au journal

Dans `assets/data/journal.json`. Le champ `genre` doit valoir `article`, `cours` ou `modele` —
ce sont les valeurs utilisées par les filtres de la page.

## Développer en local

```bash
python3 -m http.server 8000
# puis http://localhost:8000
```

Un simple double-clic sur `index.html` ne suffit pas : les fichiers JSON sont chargés en `fetch`,
ce qui exige un serveur HTTP.

## Héberger un fichier lourd hors du dépôt

Tous les champs de fichier (`poster`, `slides`, `doc` dans les séances, `url` dans le
journal) acceptent aussi bien un chemin local qu'une adresse complète. Pour un support
volumineux qu'on ne veut pas mettre dans le dépôt, il suffit donc de le déposer sur
Google Drive et de coller son lien :

1. Déposez le fichier dans Drive, clic droit, **Partager**, puis « Tous les utilisateurs
   disposant du lien » en **Lecteur**.
2. Copiez le lien, de la forme `https://drive.google.com/file/d/IDENTIFIANT/view?usp=sharing`.
3. Dans le JSON, écrivez soit ce lien tel quel (ouverture dans l'aperçu Drive), soit
   `https://drive.google.com/uc?export=download&id=IDENTIFIANT` pour un téléchargement direct.

```json
"slides": "https://drive.google.com/file/d/1AbCdEf.../view?usp=sharing"
```

Le bouton s'affiche exactement comme pour un fichier local. Faites-le seulement quand
c'est nécessaire : un fichier dans le dépôt reste plus rapide et ne dépend de personne.

## Publication

GitHub Pages, dépôt `asafrique/site_asa`, branche `main`, dossier racine. Le fichier `CNAME` fixe le domaine personnalisé.
Toute modification poussée sur `main` est en ligne en une à deux minutes.

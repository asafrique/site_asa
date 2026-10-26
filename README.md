# Site web — Association Sciences pour l’Afrique (ASA)

Site **Jekyll** publié par GitHub Pages sur https://asafrique.org, éditable avec **Pages CMS** (https://app.pagescms.org).
Mode d’emploi pour les membres : **GUIDE.md**.

## Structure

```
_seminaires/        Une fiche .md par séance (date, orateur, affiche, résumé, PDF…)
_posts/             Actualités (AAAA-MM-JJ-titre.md)
_bibliotheque/      Fiches du journal : articles, mini-cours, modèles
_bureau/            Membres du bureau exécutif
_data/site.yml      Coordonnées, formulaires, réseaux, clé Web3Forms
_data/navigation.yml Menu
_includes/, _layouts/  Gabarits (en-tête, pied, carte de séance, article…)
index.html, seminaires.html, journal.html, activites.html, adhesion.html,
contact.html, bureau.html, actualites.html, 404.html   Pages
assets/css/style.css   Charte ASA (inchangée) · assets/css/ajouts.css  nouveaux composants
assets/js/app.js       Carrousel, onglets, recherche, prochaine séance, agenda .ics, formulaire
assets/posters, slides, docs, actualites, bureau   Fichiers déposés
.pages.yml             Formulaires de Pages CMS
```

## Prévisualiser en local (facultatif)

```
bundle install
bundle exec jekyll serve
```

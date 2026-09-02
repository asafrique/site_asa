# Notes de contenu — à traiter par le bureau

Ce fichier récapitule ce qui a été reconstitué depuis les archives, ce qui reste à vérifier
et ce qui manque. Il n'est pas publié sur le site : supprimez-le quand tout est traité.

## 0. À faire en priorité

**Corriger les dates fausses sur les affiches Canva.** Cinq séances portent une date
erronée dans les archives (tableau ci-dessous). Les affiches Canva de ces séances, quand
elles existent, doivent être régénérées avec la bonne date, puis réexportées en PNG et
reversées dans `assets/posters/`.

## 1. Dates corrigées (à répercuter sur les affiches et les archives)

Ces cinq séances étaient rattachées à la mauvaise année dans l'ancien site. Les dates
retenues ici viennent des annonces WhatsApp reproduites dans
« Séminaire Asa Titre et Resume.docx », qui donnent le jour exact.

| Orateur·rice | Ancienne mention | Date retenue |
|---|---|---|
| Emmanuel Zongo | 2021 | 11 septembre 2022 |
| Lucie Baudouin | 2023 (mois à confirmer) | 9 octobre 2022 |
| Swann Marx | 2023 (mois à confirmer) | 4 décembre 2022 |
| Ousmane Koutou | 2023 (mois à confirmer) | 11 décembre 2022 |
| Ismaïla Balogoun | 2023 (mois à confirmer) | novembre 2022 — **jour à confirmer** |

## 2. Séances ajoutées, absentes de l'ancien site

| Séance | Date | Source |
|---|---|---|
| Baparou Danhane — Ensemble-contrôlabilité des systèmes linéaires | février 2023, jour à confirmer | docx des résumés |
| Didi Kala Agbo Bidi — Sterile Insect Technique | 9 juin 2024 | AgboLink1.png + Abstract_AGBO.pdf |
| Adnane Saoud — Learning-based control of cyber-physical systems | 14 juillet 2024 | SeminarySaoud.pdf |
| Aulan Zahoundo — Quantum error correction codes and decoders | 12 janvier 2025 | Aulan_seminary.pdf |
| Oumarou Asso — nonlocal (N, N/s)-Laplacian | 11 janvier 2026 | main_ASSO.pdf (Porto-Novo) |

Aulan Zahoundo et Oumarou Asso ont donc donné **deux** exposés chacun·e ; les deux
séances figurent au programme, ce n'est pas un doublon.

## 3. Points à vérifier

- **Séances 2021 sans date.** Zodji (Navier-Stokes), Adote, Godeme, Assogba et Addogbo
  n'ont ni jour ni mois dans aucune archive : seulement un titre. Elles sont affichées
  avec la mention « Date à confirmer ».
- **Enregistrements vidéo.** Les liens Zoom des archives ne fonctionnent plus et ont été
  retirés du site. Le champ `video` reste géré par le code : dès qu'une séance est mise en
  ligne sur YouTube, ajoutez `"video": "https://www.youtube.com/watch?v=…"` dans le JSON
  et le bouton « Voir l'enregistrement » réapparaît automatiquement sur la séance.
- **Rattachement des diapositives.** Les PDF ont été associés aux séances d'après les noms
  de dossiers et les pages de titre. Deux cas méritaient une vérification et ont été
  tranchés ainsi : `AssoOumarouJanvier2026/main.pdf` va à la séance du 11 janvier 2026 (la
  page de titre indique « Porto-Novo, January 11, 2026 ») ; `Jan2026Boubacar/…` va à la
  séance du 7 février 2026 (date de l'affiche).
- **Affiches.** Les dix-sept affiches sont les exports Canva d'origine, en 1080 × 1080,
  converties en JPEG pour alléger le dépôt. Elles ont été relues une à une : le nom de l'orateur·rice,
  le titre et la date lus sur chaque affiche correspondent bien à la séance à laquelle
  elle est rattachée.

## 4. Résumés manquants

Ces séances ont un titre, une affiche et parfois des diapositives, mais pas de résumé.
Un paragraphe suffit — champ `abstract` dans `assets/data/seminars-<année>.json`.

- 2024 : Guilherme Mazanti, Oumarou Asso, Olga Yufereva
- 2025 : Ikram El Haskouki, Mohammad Akil
- 2026 : Oumarou Asso, Boubacar Diallo, Cyprien Tamekue, Clotilde Djuikem,
  N. K. David Adenyo, Arnauld Tuyaba

## 5. À compléter

- Confirmer le titre et la date de la séance de **Nana Téwendé Emmanuel** (Université
  Nazi Boni), actuellement affichée en « prochainement ».
- Publier le **premier article du journal de vulgarisation** : la page existe et le modèle
  LaTeX est en ligne, mais le catalogue ne contient encore aucun article publié.
- Mettre à jour le compteur « 36 séances archivées » de l'accueil quand le programme
  s'étoffe.

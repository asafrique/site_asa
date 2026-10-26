# Guide du site ASA (asafrique.org)

Le site est désormais **dynamique** : les séances, les actualités, la bibliothèque du journal et le bureau
sont de simples fiches que l’on remplit dans un formulaire en ligne (**Pages CMS**). GitHub reconstruit le site
tout seul en 1 à 2 minutes après chaque enregistrement. Aucune connaissance technique n’est nécessaire.

---

## 1. Mise en ligne (une seule fois)

1. Décompressez `asa-site-dynamique.zip` sur votre ordinateur.
2. Sur GitHub, ouvrez le dépôt **asafrique/site_asa** → **Add file** → **Upload files**.
3. Ouvrez le dossier décompressé, **sélectionnez tout son contenu** (y compris les dossiers qui commencent par `_` et le
   fichier `.pages.yml`) et glissez-le dans la page GitHub.
   - Sur Mac, `.pages.yml` est caché : appuyez sur **Cmd + Maj + .** dans le Finder pour l’afficher.
4. En bas, cliquez sur **Commit changes**. Les fichiers existants sont remplacés, les affiches et PDF déjà en ligne sont conservés.
5. Onglet **Actions** : attendez la coche verte (1 à 2 min), puis ouvrez https://asafrique.org.
   Astuce : rechargez avec **Ctrl + F5** (ou Cmd + Maj + R) pour vider le cache.

> Rien à changer chez Zoho ni dans **Settings → Pages** : le domaine reste `asafrique.org`, branche `main`, dossier `/ (root)`.

**Facultatif (ménage)** : ces anciens fichiers ne servent plus et peuvent être supprimés sur GitHub
(ouvrir le fichier → icône **…** → *Delete file*) : `build_pages.py`, le dossier `assets/data/`. Les laisser ne gêne pas.

---

## 2. Formulaire de contact → boîte contact@asafrique.org (5 minutes)

1. Allez sur **https://web3forms.com** → **Create your Access Key**.
2. Saisissez **contact@asafrique.org** (l’adresse qui recevra les messages) → la clé arrive par e-mail.
3. Dans Pages CMS → **Réglages du site** → champ **Clé Web3Forms** : collez la clé → **Enregistrer**.

Tant que la clé est vide, le bouton « Envoyer » ouvre simplement la messagerie du visiteur : rien n’est cassé.
Les messages arrivent avec l’objet `[Site ASA] Sujet — Nom` ; il suffit de cliquer **Répondre**.

---

## 3. Modifier le site avec Pages CMS

1. Ouvrez **https://app.pagescms.org** → **Sign in with GitHub** (compte qui gère `asafrique`).
2. Autorisez l’accès au dépôt **site_asa**, puis ouvrez-le. Le menu de gauche propose :

| Menu | Pour quoi faire |
|---|---|
| **Actualités** | Publier une nouvelle : titre, date, catégorie, résumé, image, PDF joint, texte. |
| **Séminaires** | Ajouter une séance : orateur, titre, date, heure, affiche, résumé, diapositives, vidéo. |
| **Bibliothèque du journal** | Ajouter un article, un mini-cours ou un modèle, avec ses PDF. |
| **Bureau exécutif** | Changer un membre, sa fonction, ajouter une photo. |
| **Réglages du site** | E-mail, RNA, siège, liens des formulaires Google, réseaux sociaux, clé Web3Forms. |
| **Menu du site** | Libellés et ordre du menu. |

### Ajouter une séance (le plus fréquent)
**Séminaires → Add an entry** : remplissez *Orateur·rice*, *Titre*, *Affiliation*, *Date*, *Heure* → déposez l’affiche
→ collez le résumé → **Save**.
- La séance apparaît automatiquement dans l’archive (bonne année), dans le compteur de l’accueil, et dans le
  bloc **« Prochaine séance »** de l’accueil avec compte à rebours et bouton **Ajouter à mon agenda**.
- Date pas encore fixée ? Mettez une date approximative, cochez **Séance à venir** et écrivez
  « Prochainement (date à confirmer) » dans **Date affichée**.
- Après la séance : décochez *Séance à venir*, ajoutez les diapositives (PDF) et le lien YouTube.
- Cochez **Montrer l’affiche en page d’accueil** pour la faire défiler dans le carrousel.

### Publier une actualité
**Actualités → Add an entry** → titre, date, catégorie, résumé → image (facultative) → texte → **Save**.
Les 3 dernières actualités s’affichent sur l’accueil ; toutes sont sur `/actualites/`, avec boutons de partage
WhatsApp, LinkedIn, Facebook et flux RSS.

### Déposer un PDF
Dans n’importe quel champ « fichier » (diapositives, annonce, PDF joint, fichier de la bibliothèque) :
cliquez, puis **Upload** et choisissez le PDF. Il est rangé automatiquement dans le bon dossier.

---

## 4. Donner l’accès aux autres membres (sans compte GitHub)

Dans Pages CMS, ouvrez le dépôt → **Settings → Collaborators** → saisissez l’e-mail du membre → **Invite**.
Il reçoit un lien de connexion par e-mail et peut ajouter séances et actualités immédiatement.

---

## 5. Petites nouveautés du site

- Bloc **Prochaine séance** sur l’accueil (compte à rebours, ajout à l’agenda Google / Outlook / Apple).
- **Recherche** dans toute l’archive des séminaires (nom, sujet, institution, sans tenir compte des accents).
- Lien direct vers une séance : `asafrique.org/seminaires.html#s-2024-06-09-…` (ouvre la séance et la surligne).
- Page **Actualités** avec filtres par catégorie, partage et flux RSS.
- **Formulaire de contact** avec sujet pré-rempli (ex. le bouton du journal arrive sur « Proposition d’article JVS »).
- Compteurs (séances, années) calculés automatiquement ; bouton « haut de page ».
- Sitemap et balises de partage (aperçu sur WhatsApp / LinkedIn) générés automatiquement.

---

## 6. En cas de souci

- **Le site n’a pas changé** : onglet **Actions** sur GitHub. Une croix rouge indique une erreur ; cliquez dessus,
  le message cite le fichier en cause (souvent un guillemet ou une date mal saisie). Corrigez-le dans Pages CMS.
- **Annuler une modification** : sur GitHub, ouvrez le fichier → **History** → copiez l’ancienne version.

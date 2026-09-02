#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère les pages HTML statiques du site ASA."""
import os

SITE = os.path.dirname(os.path.abspath(__file__))
DOMAINE = "https://asafrique.org"

FORM_ADHESION = "https://forms.gle/nd3MrV9NQJDFcSuC6"
FORM_SEMINAIRE = "https://forms.gle/T9jEudFH7i3tUBnf6"
LINKEDIN = "https://www.linkedin.com/company/association-sciences-pour-l-afrique/"
INSTAGRAM = "https://www.instagram.com/sci4africa/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61581832300614"
WHATSAPP = "https://chat.whatsapp.com/Fy2bQDI7ddjBXvCgywHk6Q"
TIOH = "https://tioh-academy.github.io/bourse.html"
MAIL = "contact@asafrique.org"

NAV = [
    ("index.html", "Accueil"),
    ("activites.html", "Activités"),
    ("journal.html", "Journal"),
    ("contact.html", "Contact"),
]


def entete(actif):
    liens = ""
    for href, libelle in NAV:
        cur = ' aria-current="page"' if href == actif else ""
        liens += f'\n      <a href="{href}"{cur}>{libelle}</a>'
    return f"""<a class="skip" href="#contenu">Aller au contenu</a>
<header class="entete">
  <div class="wrap entete-int">
    <a class="marque" href="index.html" aria-label="ASA, Association Sciences pour l’Afrique, accueil">
      <img src="assets/img/asa-logo.png" alt="Association Sciences pour l’Afrique" width="1200" height="590">
    </a>
    <button class="burger" aria-expanded="false" aria-controls="menu-principal" aria-label="Ouvrir le menu">☰</button>
    <nav class="menu" id="menu-principal" aria-label="Navigation principale">{liens}
      <a class="cta" href="adhesion.html">Adhérer</a>
    </nav>
  </div>
</header>"""


def suivant(titre, cartes):
    items = "".join(f'<a href="{h}"><b>{t}</b><span>{d}</span></a>' for h, t, d in cartes)
    return f"""<section class="bloc suivant">
  <div class="wrap">
    <h2>{titre}</h2>
    <div class="suivant-grille">{items}</div>
  </div>
</section>"""


PIED = f"""<footer class="pied">
  <div class="wrap">
    <div class="pied-grille">
      <div>
        <a class="pied-logo" href="index.html">
          <img src="assets/img/asa-logo.png" alt="Association Sciences pour l’Afrique">
        </a>
        <p class="baseline">Association loi 1901, apolitique et à but non lucratif, qui contribue à la promotion et au développement des sciences en Afrique.</p>
      </div>
      <div>
        <h4>Activités</h4>
        <ul>
          <li><a href="seminaires.html">ASA Séminaire</a></li>
          <li><a href="journal.html">Journal de vulgarisation</a></li>
          <li><a href="journal.html#mini-cours">Mini-cours</a></li>
          <li><a href="activites.html#soutiens">Ce que nous soutenons</a></li>
        </ul>
      </div>
      <div>
        <h4>Participer</h4>
        <ul>
          <li><a href="adhesion.html">Adhérer</a></li>
          <li><a href="{FORM_SEMINAIRE}" target="_blank" rel="noopener">Proposer un exposé</a></li>
          <li><a href="journal.html#publier">Publier un article</a></li>
          <li><a href="contact.html">Nous écrire</a></li>
          <li><a href="bureau.html">Le bureau exécutif</a></li>
        </ul>
      </div>
      <div>
        <h4>Suivre</h4>
        <ul>
          <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
          <li><a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a></li>
          <li><a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a></li>
          <li><a href="{WHATSAPP}" target="_blank" rel="noopener">Groupe WhatsApp</a></li>
        </ul>
      </div>
    </div>
    <div class="pied-bas">
      <span>© <span id="annee">2026</span> Association Sciences pour l’Afrique, RNA W941020769</span>
      <span><a href="mailto:{MAIL}">{MAIL}</a></span>
    </div>
  </div>
</footer>
<script src="assets/js/app.js" defer></script>"""


def page(fichier, titre, description, corps, actif):
    html = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titre} | ASA, Association Sciences pour l’Afrique</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#6E5A33">
<link rel="canonical" href="{DOMAINE}/{fichier}">
<meta property="og:type" content="website">
<meta property="og:title" content="{titre} | ASA">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{DOMAINE}/{fichier}">
<meta property="og:image" content="{DOMAINE}/assets/img/asa-og.jpg">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/asa-logo-small.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,400;1,9..144,600&family=Karla:ital,wght@0,400;0,500;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
{entete(actif)}
<main id="contenu">
{corps}
</main>
{PIED}
</body>
</html>
"""
    with open(os.path.join(SITE, fichier), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit :", fichier)


VALEURS = """    <div class="valeurs">
      <div class="valeur">
        <h3>Rassembler</h3>
        <span class="devise">Personne ne cherche seul.</span>
        <p>Relier le monde scientifique africain à celui de l’extérieur : partager des expériences, des méthodes et des contacts, et donner la parole en priorité aux jeunes chercheuses et chercheurs.</p>
      </div>
      <div class="valeur">
        <h3>Transmettre</h3>
        <span class="devise">Une idée ne vaut que comprise.</span>
        <p>Rendre les sciences lisibles pour la jeunesse africaine : exposés accessibles, articles de vulgarisation, mini-cours et jeux-concours scientifiques.</p>
      </div>
      <div class="valeur">
        <h3>Enraciner</h3>
        <span class="devise">Chercher ici, pour ici.</span>
        <p>Bâtir sur le continent, jusqu’à un centre de recherche, et nouer des partenariats avec universités, laboratoires et organismes de financement pour y parvenir.</p>
      </div>
    </div>"""


# =====================================================================  ACCUEIL
accueil = f"""
<section class="hero">
  <div class="wrap hero-int-2col">
    <div class="hero-texte">
      <img class="hero-logo" src="assets/img/asa-logo.png" alt="Association Sciences pour l’Afrique" width="1200" height="590">
      <h1>Une séance par mois, <em>partout où l’Afrique cherche</em>.</h1>
      <p>ASA réunit en ligne chercheuses et chercheurs africains et leurs collègues du monde entier. Depuis 2021, chaque mois, un exposé d’une heure, ouvert à tous.</p>
      <div class="hero-actions">
        <a class="btn btn-or" href="seminaires.html">Voir les séminaires</a>
        <a class="btn btn-ligne" href="adhesion.html">Rejoindre l’association</a>
      </div>
      <div class="compteurs">
        <div><b data-compte="36">0</b><span>séances archivées</span></div>
        <div><b data-compte="12">0</b><span>rendez-vous par an</span></div>
        <div><b data-compte="5">0</b><span>années de séminaire</span></div>
      </div>
    </div>
    <figure class="vitrine hero-vitrine">
      <div class="vitrine-cadre" id="vitrine-cadre"></div>
      <figcaption id="vitrine-legende"></figcaption>
      <div class="vitrine-points" id="vitrine-points" aria-label="Choisir une affiche"></div>
    </figure>
  </div>
</section>

<section class="bloc">
  <div class="wrap">
    <div class="intro-bloc">
      <h2>Ce qui nous tient</h2>
      <p>Trois engagements, tirés de nos statuts, qui décident de ce que nous faisons et de ce que nous refusons de faire.</p>
    </div>
{VALEURS}
  </div>
</section>

<section class="bloc bloc-blanc">
  <div class="wrap">
    <div class="intro-bloc">
      <h2>Six ans de séances</h2>
      <p>Chaque mois, une affiche, un thème et une nouvelle voix. Voici quelques rendez-vous récents ; l’archive complète remonte à 2021.</p>
    </div>
    <div class="mosaique" id="mosaique"></div>
    <p style="margin-top:var(--pas-4)"><a class="btn btn-ligne" href="seminaires.html">Parcourir toute l’archive</a></p>
  </div>
</section>

<section class="bloc bloc-ivoire">
  <div class="wrap">
    <div class="intro-bloc">
      <h2>Trois façons d’entrer</h2>
      <p>Écouter, lire, ou prendre la parole. Tout est gratuit et en ligne.</p>
    </div>
    <div class="grille-3">
      <a class="carte" href="seminaires.html">
        <h3>ASA Séminaire</h3>
        <p>Un exposé par mois depuis 2021, en visioconférence. Résumés, affiches et diapositives des séances passées.</p>
        <span class="suite">Parcourir 2021 à 2027</span>
      </a>
      <a class="carte" href="journal.html">
        <h3>Journal de vulgarisation</h3>
        <p>Notre revue en cinq pages maximum, écrite pour un lectorat non spécialiste. Le modèle LaTeX est prêt, l’appel à contributions est ouvert.</p>
        <span class="suite">Lire et publier</span>
      </a>
      <a class="carte" href="adhesion.html">
        <h3>Adhérer</h3>
        <p>Docteur·es, doctorant·es et étudiant·es en master sont particulièrement encouragé·es, sans que l’association soit réservée à personne.</p>
        <span class="suite">Rejoindre l’association</span>
      </a>
    </div>
  </div>
</section>

<section class="bloc">
  <div class="wrap">
    <div class="encadre">
      <div>
        <h2>Le prochain exposé est peut-être le vôtre</h2>
        <p>Thèse en cours, résultat récent, sujet que vous voulez faire connaître : le séminaire ASA accueille les travaux à tous les stades. Une heure, en ligne, devant un public venu de plusieurs continents.</p>
        <div class="hero-actions">
          <a class="btn btn-or" href="{FORM_SEMINAIRE}" target="_blank" rel="noopener">Proposer un exposé</a>
          <a class="btn btn-ligne" href="seminaires.html">Voir les séances passées</a>
        </div>
      </div>
      <ol>
        <li>Vous remplissez le formulaire ASA Séminaire.</li>
        <li>Nous fixons la date et préparons l’affiche.</li>
        <li>L’annonce part sur l’ensemble de nos réseaux.</li>
        <li>La séance est archivée sur cette page.</li>
      </ol>
    </div>
  </div>
</section>

<section class="bloc bloc-blanc" id="qui-sommes-nous">
  <div class="wrap">
    <div class="intro-bloc">
      <h2>Qui nous sommes</h2>
      <p>L’Association Sciences pour l’Afrique est une association loi 1901, apolitique, non syndicale et à but non lucratif. Son objet : contribuer à la promotion et au développement des sciences en Afrique.</p>
    </div>
    <div class="grille-2" style="margin-top:var(--pas-4)">
      <div>
        <h3>Comment l’association fonctionne</h3>
        <ul class="liste-nue">
          <li><b>Bureau exécutif</b> : présidence, deux vice-présidences (communication et affaires extérieures ; organisation et numérique), secrétariat général, trésorerie et conseillers. Élu chaque année.</li>
          <li><b>Assemblée générale</b> : organe suprême, une session ordinaire par trimestre.</li>
          <li><b>Membres</b> : fondateurs, bienfaiteurs et actifs.</li>
          <li><b>Ressources</b> : cotisations des adhérents, dons, subventions et produits des activités.</li>
        </ul>
        <p style="margin-top:var(--pas-3)"><a class="btn btn-ligne" href="bureau.html">Voir le bureau exécutif</a></p>
      </div>
      <div>
        <h3>Repères</h3>
        <ul class="liste-nue">
          <li><b>Nom</b> : Association Sciences pour l’Afrique (ASA)</li>
          <li><b>Régime</b> : loi du 1<sup>er</sup> juillet 1901</li>
          <li><b>Numéro RNA</b> : W941020769</li>
          <li><b>Déclaration</b> : préfecture du Val-de-Marne, 3 novembre 2025</li>
          <li><b>Publication</b> : Journal officiel des associations, 11 novembre 2025</li>
          <li><b>Siège</b> : Maisons-Alfort, France</li>
        </ul>
      </div>
    </div>
  </div>
</section>

{suivant("Continuer", [
    ("activites.html", "Nos activités", "Séminaire, journal, mini-cours et soutiens"),
    ("adhesion.html", "Adhérer", "Rejoindre l’association en quelques minutes"),
    ("contact.html", "Nous écrire", "Courriel et réseaux sociaux"),
])}
"""

# =====================================================================  ACTIVITÉS
activites = f"""
<section class="bloc">
  <div class="wrap">
    <div class="intro-bloc">
      <h1>Nos activités</h1>
      <p>Tout ce que fait ASA tient en une phrase de ses statuts : faire circuler les sciences entre l’Afrique et le reste du monde, et les rendre accessibles à celles et ceux qui n’en font pas métier.</p>
    </div>
    <div class="grille-3" style="margin-top:var(--pas-4)">
      <a class="carte" href="seminaires.html">
        <h3>ASA Séminaire</h3>
        <p>Le rendez-vous mensuel de l’association depuis 2021 : mathématiques appliquées, contrôle, épidémiologie, calcul quantique, apprentissage automatique, santé publique. Chaque séance est archivée avec son affiche et son résumé.</p>
        <span class="suite">Voir la programmation</span>
      </a>
      <a class="carte" href="journal.html">
        <h3>Journal de vulgarisation des sciences</h3>
        <p>Une revue écrite par les membres pour un public large. Format court de cinq pages, modèle LaTeX fourni, relecture par le comité éditorial.</p>
        <span class="suite">Découvrir le journal</span>
      </a>
      <a class="carte" href="journal.html#mini-cours">
        <h3>Mini-cours</h3>
        <p>Des séries courtes sur un thème technique, pensées pour les niveaux master et début de thèse. Premier cycle disponible : la quantification, en deux parties.</p>
        <span class="suite">Ouvrir les supports</span>
      </a>
    </div>
  </div>
</section>

<section class="bloc bloc-ivoire" id="soutiens">
  <div class="wrap">
    <div class="intro-bloc">
      <h2>Ce que nous soutenons</h2>
      <p>Au-delà de nos propres activités, ASA appuie des initiatives qui ouvrent des portes aux étudiantes et étudiants du continent.</p>
    </div>
    <div class="grille-3" style="margin-top:var(--pas-3)">
      <a class="carte" href="{TIOH}" target="_blank" rel="noopener">
        <h3>Bourse Tioh Academy</h3>
        <p>ASA soutient la bourse portée par Tioh Academy, qui accompagne financièrement des élèves et étudiants dans la poursuite de leur parcours scientifique.</p>
        <span class="suite">Voir la bourse</span>
      </a>
      <div class="carte">
        <h3>Un centre de recherche en Afrique</h3>
        <p>C’est notre horizon de long terme : faire exister sur le continent un lieu de recherche qui réponde à ses enjeux industriels et contribue à une formation de qualité. Chaque partenariat noué nous en rapproche.</p>
        <span class="suite">Projet en construction</span>
      </div>
      <a class="carte" href="contact.html">
        <h3>Partenariats</h3>
        <p>Universités, laboratoires, fondations et organismes de financement : nous cherchons des partenaires pour les séminaires, le journal et les projets de formation.</p>
        <span class="suite">Nous contacter</span>
      </a>
    </div>
  </div>
</section>

{suivant("Continuer", [
    ("seminaires.html", "ASA Séminaire", "36 séances archivées depuis 2021"),
    ("journal.html", "Le journal", "Modèle d’article et appel à contributions"),
    ("adhesion.html", "Adhérer", "Rejoindre l’association"),
])}
"""

# =====================================================================  SÉMINAIRES
seminaires = f"""
<section class="bloc" style="padding-bottom:var(--pas-3)">
  <div class="wrap">
    <div class="intro-bloc">
      <h1>ASA Séminaire</h1>
      <p>Une séance par mois, en visioconférence, ouverte à tous. Cliquez sur un titre pour lire le résumé, voir l’affiche et retrouver les diapositives quand elles existent.</p>
      <div class="hero-actions">
        <a class="btn btn-bronze" href="{FORM_SEMINAIRE}" target="_blank" rel="noopener">Proposer un exposé</a>
        <a class="btn btn-ligne" href="contact.html">Suivre les annonces</a>
      </div>
    </div>
  </div>
</section>

<section class="bloc" style="padding-top:var(--pas-3)">
  <div class="wrap">
    <div class="rail" id="rail-annees" role="tablist" aria-label="Choisir une année">
      <button type="button" role="tab" data-annee="2021" aria-selected="false">2021</button>
      <button type="button" role="tab" data-annee="2022" aria-selected="false">2022</button>
      <button type="button" role="tab" data-annee="2023" aria-selected="false">2023</button>
      <button type="button" role="tab" data-annee="2024" aria-selected="false">2024</button>
      <button type="button" role="tab" data-annee="2025" aria-selected="false">2025</button>
      <button type="button" role="tab" data-annee="2026" aria-selected="false" data-defaut="1">2026</button>
      <button type="button" role="tab" data-annee="2027" aria-selected="false">2027</button>
    </div>
    <div id="panneau-seances" role="region" aria-live="polite">Chargement des séances…</div>
  </div>
</section>

{suivant("Continuer", [
    ("journal.html", "Le journal", "Publier un article de vulgarisation"),
    ("adhesion.html", "Adhérer", "Devenir membre de l’association"),
    ("contact.html", "Nous écrire", "Une question sur une séance ?"),
])}
"""

# =====================================================================  JOURNAL
journal = f"""
<section class="bloc bandeau">
  <div class="wrap">
    <div class="intro-bloc">
      <h1>Journal de vulgarisation des sciences</h1>
      <p>La revue d’ASA : cinq pages maximum, écrites pour quelqu’un qui n’est pas du métier. Une idée de recherche, une méthode, un objet du quotidien, expliqués sans jargon, avec une figure et un exemple.</p>
    </div>
    <div class="meta-revue">
      <div><b>5 pages</b>format maximum</div>
      <div><b>Français ou anglais</b>langues acceptées</div>
      <div><b>LaTeX</b>modèle fourni</div>
      <div><b>Ouvert</b>appel à contributions</div>
    </div>
  </div>
</section>

<section class="bloc">
  <div class="wrap">
    <h2 id="bibliotheque">La bibliothèque</h2>
    <p>Articles publiés, mini-cours et outils de rédaction, réunis au même endroit.</p>
    <div class="filtres" id="filtres" style="margin-top:var(--pas-3)">
      <button type="button" data-genre="tout" aria-pressed="true">Tout</button>
      <button type="button" data-genre="article" aria-pressed="false">Articles</button>
      <button type="button" data-genre="cours" aria-pressed="false">Mini-cours</button>
      <button type="button" data-genre="modele" aria-pressed="false">Modèles</button>
    </div>
    <div class="catalogue" id="catalogue">Chargement du catalogue…</div>
  </div>
</section>

<section class="bloc bloc-ivoire" id="publier">
  <div class="wrap">
    <div class="encadre">
      <div>
        <h2>Écrire pour le journal</h2>
        <p>Vous travaillez sur un sujet que personne n’arrive à vous faire expliquer en dîner de famille ? C’est exactement l’article que nous cherchons. Le comité éditorial relit, commente et accompagne jusqu’à la publication.</p>
        <div class="hero-actions">
          <a class="btn btn-or" href="assets/docs/ASA-JVS-Template.zip">Télécharger le modèle LaTeX</a>
          <a class="btn btn-ligne" href="mailto:{MAIL}?subject=Proposition%20d%27article%20JVS">Envoyer une proposition</a>
        </div>
      </div>
      <ol>
        <li>Choisissez un sujet et écrivez-en le résumé en cinq lignes.</li>
        <li>Envoyez-le nous : nous répondons avec un avis et un calendrier.</li>
        <li>Rédigez avec la classe <code>asa-jvs</code> : encadrés, lettrines et figures sont prévus.</li>
        <li>Deux relectures, une mise en page, publication dans le numéro.</li>
      </ol>
    </div>
  </div>
</section>

<section class="bloc" id="mini-cours">
  <div class="wrap">
    <div class="intro-bloc">
      <h2>Mini-cours</h2>
      <p>Plus techniques que les articles, plus courts qu’un cours de master : les mini-cours ASA traitent un thème en deux ou trois séances, supports téléchargeables.</p>
    </div>
    <div class="grille-3" style="margin-top:var(--pas-3)">
      <a class="carte" href="assets/docs/mini-cours-quantification-1.pdf" target="_blank" rel="noopener">
        <h3>Quantification, partie 1</h3>
        <p>Introduction et premiers outils.</p>
        <span class="suite">Ouvrir le PDF</span>
      </a>
      <a class="carte" href="assets/docs/mini-cours-quantification-2.pdf" target="_blank" rel="noopener">
        <h3>Quantification, partie 2</h3>
        <p>Approfondissements et exemples travaillés.</p>
        <span class="suite">Ouvrir le PDF</span>
      </a>
      <a class="carte" href="{FORM_SEMINAIRE}" target="_blank" rel="noopener">
        <h3>Proposer un mini-cours</h3>
        <p>Vous maîtrisez un sujet et voulez le transmettre ? Décrivez-le nous avec le formulaire du séminaire.</p>
        <span class="suite">Remplir le formulaire</span>
      </a>
    </div>
  </div>
</section>

{suivant("Continuer", [
    ("seminaires.html", "ASA Séminaire", "Les séances mois par mois, depuis 2021"),
    ("adhesion.html", "Adhérer", "Participer au comité éditorial"),
    ("contact.html", "Nous écrire", "Questions éditoriales et partenariats"),
])}
"""

# =====================================================================  ADHÉSION
adhesion = f"""
<section class="bloc">
  <div class="wrap">
    <div class="intro-bloc">
      <h1>Adhérer à ASA</h1>
      <p>Un formulaire, quelques minutes, et vous rejoignez une communauté de chercheuses et chercheurs répartis entre l’Afrique, l’Europe et l’Amérique du Nord.</p>
      <div class="hero-actions">
        <a class="btn btn-or" href="{FORM_ADHESION}" target="_blank" rel="noopener">Remplir le formulaire d’adhésion</a>
        <a class="btn btn-ligne" href="contact.html">Nous poser une question</a>
      </div>
    </div>
  </div>
</section>

<section class="bloc bloc-blanc">
  <div class="wrap">
    <div class="intro-bloc">
      <h2>Qui peut adhérer</h2>
      <p>Toute personne qui adhère aux objectifs de l’association et dont la candidature est acceptée par le bureau exécutif. Les docteur·es, doctorant·es et étudiant·es en master sont vivement encouragé·es, mais l’association n’est réservée à personne.</p>
    </div>
    <div class="grille-3" style="margin-top:var(--pas-3)">
      <div class="carte">
        <h3>Membre actif</h3>
        <p>Vous participez aux activités et à l’assemblée générale, vous votez et vous pouvez être élu·e au bureau exécutif. Une cotisation régulière est demandée ; son montant vous est indiqué à la validation de votre candidature.</p>
      </div>
      <div class="carte">
        <h3>Membre bienfaiteur</h3>
        <p>Personne physique ou morale qui soutient l’association par un don ou un service important, sur décision du bureau et approbation de l’assemblée générale.</p>
      </div>
      <div class="carte">
        <h3>Simplement présent·e</h3>
        <p>Les séminaires sont ouverts à tous, sans adhésion. Suivez les annonces sur nos réseaux et venez écouter.</p>
      </div>
    </div>
  </div>
</section>

<section class="bloc bloc-ivoire">
  <div class="wrap">
    <div class="encadre">
      <div>
        <h2>Trois minutes, pas plus</h2>
        <p>Le formulaire demande votre identité, votre statut académique et votre domaine. Le bureau exécutif examine les candidatures au fil de l’eau et vous répond par courriel.</p>
        <div class="hero-actions">
          <a class="btn btn-or" href="{FORM_ADHESION}" target="_blank" rel="noopener">Adhérer maintenant</a>
        </div>
      </div>
      <ol>
        <li>Vous remplissez le formulaire d’adhésion.</li>
        <li>Le bureau examine et valide la candidature.</li>
        <li>Vous recevez les informations pratiques et l’accès aux canaux internes.</li>
        <li>Vous êtes convié·e à la prochaine assemblée générale.</li>
      </ol>
    </div>
  </div>
</section>

{suivant("Continuer", [
    ("seminaires.html", "ASA Séminaire", "Le rendez-vous mensuel de l’association"),
    ("journal.html", "Le journal", "Publier votre premier article"),
    ("index.html#qui-sommes-nous", "Qui nous sommes", "Objet, gouvernance et repères"),
])}
"""

# =====================================================================  CONTACT
contact = f"""
<section class="bloc">
  <div class="wrap">
    <div class="grille-2">
      <div>
        <h1>Nous écrire</h1>
        <p>Une question sur une séance, une proposition d’exposé ou d’article, un projet de partenariat : écrivez-nous, nous répondons.</p>
        <p><a class="btn btn-bronze" href="mailto:{MAIL}">{MAIL}</a></p>

        <h2 style="margin-top:var(--pas-4)">Participer directement</h2>
        <ul class="liste-nue">
          <li><a href="{FORM_ADHESION}" target="_blank" rel="noopener">Formulaire d’adhésion à l’association</a></li>
          <li><a href="{FORM_SEMINAIRE}" target="_blank" rel="noopener">Formulaire ASA Séminaire, proposer un exposé</a></li>
          <li><a href="journal.html#publier">Proposer un article au journal de vulgarisation</a></li>
        </ul>

        <h2 style="margin-top:var(--pas-4)">Siège</h2>
        <p>Association Sciences pour l’Afrique<br>Maisons-Alfort, France<br>Association loi 1901, RNA W941020769</p>
      </div>
      <div>
        <h2>Nos réseaux</h2>
        <p>Les annonces de séminaire, les appels à contributions et les actualités de l’association sont publiés sur l’ensemble de nos réseaux.</p>
        <div class="reseaux">
          <a class="reseau" href="{LINKEDIN}" target="_blank" rel="noopener">
            <span><b>LinkedIn</b><span class="desc">Page de l’association</span></span><span class="fleche">↗</span>
          </a>
          <a class="reseau" href="{INSTAGRAM}" target="_blank" rel="noopener">
            <span><b>Instagram</b><span class="desc">@sci4africa</span></span><span class="fleche">↗</span>
          </a>
          <a class="reseau" href="{FACEBOOK}" target="_blank" rel="noopener">
            <span><b>Facebook</b><span class="desc">Actualités et affiches</span></span><span class="fleche">↗</span>
          </a>
          <a class="reseau" href="{WHATSAPP}" target="_blank" rel="noopener">
            <span><b>WhatsApp</b><span class="desc">Groupe général de l’association</span></span><span class="fleche">↗</span>
          </a>
        </div>
      </div>
    </div>
  </div>
</section>

{suivant("Continuer", [
    ("seminaires.html", "ASA Séminaire", "Toutes les séances depuis 2021"),
    ("journal.html", "Le journal", "Bibliothèque et modèle d’article"),
    ("adhesion.html", "Adhérer", "Rejoindre l’association"),
])}
"""


# =====================================================================  BUREAU
MEMBRES = [
    ("BD", "Baparou Danhane", "Président",
     "Enseignant-chercheur, il préside l’association et la représente dans tous les actes de la vie civile."),
    ("FK", "Mahuklo Florent Koudohode", "Co-président",
     "Chercheur postdoctorant, il anime le séminaire mensuel et coordonne le site et les outils numériques."),
    ("KD", "Kokou Michaelis Dotse", "Co-président",
     "Chercheur, il appuie la présidence sur la programmation et les relations avec les laboratoires."),
    ("IB", "Ismaïla Balogoun", "Secrétaire général",
     "Docteur en mathématiques, il instruit les demandes d’adhésion et tient les comptes rendus de l’association."),
    ("BG", "Branda Goncalves", "Trésorière",
     "Maîtresse de conférences, elle tient les comptes, prépare le budget et présente le rapport financier annuel."),
    ("EZ", "Emmanuel Zongo", "Trésorier adjoint",
     "Chercheur, il seconde la trésorerie et suit les ressources liées aux activités."),
]

cartes_membres = "".join(
    f'''<article class="membre">
        <span class="monogramme" aria-hidden="true">{ini}</span>
        <div>
          <h3>{nom}</h3>
          <p class="role">{role}</p>
          <p>{texte}</p>
        </div>
      </article>'''
    for ini, nom, role, texte in MEMBRES
)

bureau = f"""
<section class="bloc">
  <div class="wrap">
    <div class="intro-bloc">
      <h1>Le bureau exécutif</h1>
      <p>Six personnes élues par l’assemblée générale, réparties entre la France, la Grèce et les réseaux de recherche du continent. Le bureau est renouvelé chaque année.</p>
    </div>
    <div class="bureau">
      {cartes_membres}
    </div>
  </div>
</section>

<section class="bloc bloc-ivoire">
  <div class="wrap">
    <div class="grille-2">
      <div>
        <h2>Comment le bureau est élu</h2>
        <p>Le bureau sortant constitue un comité électif impartial qui organise les élections avant la fin de son mandat. Le vote a lieu en assemblée générale, à main levée, à bulletin secret ou par voie électronique selon l’occasion.</p>
        <p>Le bureau délibère valablement dès que la moitié de ses membres est réunie et statue à la majorité des présents ou représentés.</p>
      </div>
      <div>
        <h2>Rejoindre l’équipe</h2>
        <p>Les postes de conseiller·ère et les responsabilités opérationnelles (communication, journal, programmation, partenariats) sont ouverts aux membres actifs. Si vous voulez y contribuer, dites-le nous.</p>
        <div class="hero-actions">
          <a class="btn btn-or" href="{FORM_ADHESION}" target="_blank" rel="noopener">Adhérer à l’association</a>
          <a class="btn btn-ligne" href="contact.html">Écrire au bureau</a>
        </div>
      </div>
    </div>
  </div>
</section>

{suivant("Continuer", [("index.html#qui-sommes-nous", "Qui nous sommes", "Objet, valeurs et repères"), ("activites.html", "Nos activités", "Séminaire, journal et mini-cours"), ("contact.html", "Nous écrire", "Courriel et réseaux")])}
"""

# =====================================================================  404
notfound = """
<section class="bloc">
  <div class="wrap">
    <div class="etat-vide" style="max-width:640px;margin-inline:auto">
      <h1>Cette page n’existe pas</h1>
      <p>Le lien est peut-être ancien. Reprenez par l’accueil, ou allez directement aux séances du séminaire.</p>
      <div class="hero-actions" style="justify-content:center">
        <a class="btn btn-bronze" href="index.html">Retour à l’accueil</a>
        <a class="btn btn-ligne" href="seminaires.html">Voir les séminaires</a>
      </div>
    </div>
  </div>
</section>
"""

page("index.html", "Accueil",
     "ASA, Association Sciences pour l’Afrique : un séminaire scientifique mensuel en ligne depuis 2021, un journal de vulgarisation et des mini-cours ouverts à tous.",
     accueil, "index.html")
page("activites.html", "Nos activités",
     "Séminaire mensuel, journal de vulgarisation des sciences, mini-cours et soutien à la bourse Tioh Academy : les activités de l’association ASA.",
     activites, "activites.html")
page("seminaires.html", "ASA Séminaire",
     "Toutes les séances du séminaire ASA de 2021 à 2027 : résumés, affiches et diapositives.",
     seminaires, "activites.html")
page("journal.html", "Journal de vulgarisation",
     "Le journal de vulgarisation des sciences d’ASA : bibliothèque, mini-cours, modèle LaTeX et appel à contributions.",
     journal, "journal.html")
page("adhesion.html", "Adhérer",
     "Rejoindre l’Association Sciences pour l’Afrique : qui peut adhérer et comment candidater.",
     adhesion, "index.html")
page("contact.html", "Contact",
     "Contacter l’Association Sciences pour l’Afrique : courriel, formulaires et réseaux sociaux.",
     contact, "contact.html")
page("bureau.html", "Le bureau exécutif",
     "Les six membres du bureau exécutif de l’Association Sciences pour l’Afrique et le mode d’élection de l’équipe.",
     bureau, "index.html")
page("404.html", "Page introuvable",
     "La page demandée n’existe pas sur le site de l’Association Sciences pour l’Afrique.",
     notfound, "index.html")

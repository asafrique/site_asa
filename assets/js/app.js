/* ASA — comportements du site (aucune dépendance externe).
   Le contenu est produit par Jekyll ; ce script n'ajoute que l'interactivité. */
(function () {
  "use strict";

  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var lent = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
    "septembre", "octobre", "novembre", "décembre"];
  var JOURS = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"];

  /* ---------------------------------------------------------- menu mobile */
  var burger = $(".burger");
  var menu = document.getElementById("menu-principal");
  if (burger && menu) {
    burger.addEventListener("click", function () {
      var ouvert = menu.classList.toggle("ouvert");
      burger.setAttribute("aria-expanded", ouvert ? "true" : "false");
    });
  }

  /* ---------------------------------------------------------- année pied */
  var an = document.getElementById("annee");
  if (an) an.textContent = new Date().getFullYear();

  /* ---------------------------------------------------------- compteurs */
  var compteurs = $$("[data-compte]");
  if (compteurs.length && "IntersectionObserver" in window) {
    var obs = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (e) {
        if (!e.isIntersecting) return;
        obs.unobserve(e.target);
        var cible = parseInt(e.target.dataset.compte, 10);
        if (lent) { e.target.textContent = cible; return; }
        var debut = null;
        (function pas(t) {
          if (t === undefined) return requestAnimationFrame(pas);
          if (debut === null) debut = t;
          var p = Math.min((t - debut) / 900, 1);
          e.target.textContent = Math.round(cible * (1 - Math.pow(1 - p, 3)));
          if (p < 1) requestAnimationFrame(pas);
        })();
      });
    }, { threshold: .1, rootMargin: "0px 0px -40px 0px" });
    compteurs.forEach(function (c) { obs.observe(c); });
  } else {
    compteurs.forEach(function (c) { c.textContent = c.dataset.compte; });
  }

  /* ---------------------------------------------------------- vitrine (accueil) */
  var cadre = document.getElementById("vitrine-cadre");
  if (cadre) {
    var images = $$("img", cadre);
    var points = $$("#vitrine-points button");
    var legende = document.getElementById("vitrine-legende");
    var courant = 0, minuteur = null;
    var montrer = function (i) {
      if (!images.length) return;
      courant = (i + images.length) % images.length;
      images.forEach(function (im, k) { im.classList.toggle("actif", k === courant); });
      points.forEach(function (b, k) { b.setAttribute("aria-current", String(k === courant)); });
      var im = images[courant];
      legende.innerHTML = "";
      var l = document.createElement("div"); l.className = "vitrine-legende";
      var b = document.createElement("b"); b.textContent = im.dataset.orateur;
      var d = document.createElement("span"); d.textContent = im.dataset.date;
      l.appendChild(b); l.appendChild(d);
      var p = document.createElement("p"); p.className = "vitrine-sujet"; p.textContent = im.dataset.sujet;
      legende.appendChild(l); legende.appendChild(p);
    };
    var relancer = function () {
      if (lent || images.length < 2) return;
      clearInterval(minuteur);
      minuteur = setInterval(function () { montrer(courant + 1); }, 5200);
    };
    points.forEach(function (b, k) { b.addEventListener("click", function () { montrer(k); relancer(); }); });
    cadre.addEventListener("mouseenter", function () { clearInterval(minuteur); });
    cadre.addEventListener("mouseleave", relancer);
    relancer();
  }

  /* ---------------------------------------------------------- données des séances */
  var donnees = [];
  var bloc = document.getElementById("donnees-seances");
  if (bloc) { try { donnees = JSON.parse(bloc.textContent); } catch (e) { donnees = []; } }

  var dateLocale = function (iso) { var p = iso.split("-"); return new Date(+p[0], +p[1] - 1, +p[2]); };
  var aujourdhui = new Date(); aujourdhui.setHours(0, 0, 0, 0);
  var dateLongue = function (d) {
    var j = d.getDate();
    return JOURS[d.getDay()] + " " + (j === 1 ? "1er" : j) + " " + MOIS[d.getMonth()] + " " + d.getFullYear();
  };

  /* Fichier .ics universel (Google Agenda, Outlook, Apple Calendrier) */
  var telechargerIcs = function (s) {
    var d = s.date.replace(/-/g, "");
    var h = (s.heure || "").match(/^(\d{1,2})[:h](\d{2})?/);
    var debut, fin;
    if (h) {
      var hh = ("0" + h[1]).slice(-2), mm = h[2] || "00";
      var hf = ("0" + (parseInt(h[1], 10) + 1)).slice(-2);
      debut = "DTSTART;TZID=Europe/Paris:" + d + "T" + hh + mm + "00";
      fin = "DTEND;TZID=Europe/Paris:" + d + "T" + hf + mm + "00";
    } else {
      var lendemain = dateLocale(s.date); lendemain.setDate(lendemain.getDate() + 1);
      var dl = lendemain.getFullYear() + ("0" + (lendemain.getMonth() + 1)).slice(-2) + ("0" + lendemain.getDate()).slice(-2);
      debut = "DTSTART;VALUE=DATE:" + d;
      fin = "DTEND;VALUE=DATE:" + dl;
    }
    var esc = function (t) { return String(t || "").replace(/[\\,;]/g, "\\$&").replace(/\n/g, "\\n"); };
    var page = location.origin + "/seminaires.html#" + s.id;
    var ics = [
      "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//ASA//Seminaire//FR", "CALSCALE:GREGORIAN",
      "BEGIN:VEVENT",
      "UID:" + s.id + "@asafrique.org",
      "DTSTAMP:" + new Date().toISOString().replace(/[-:]/g, "").replace(/\.\d+/, ""),
      debut, fin,
      "SUMMARY:" + esc("Séminaire ASA : " + s.titre),
      "DESCRIPTION:" + esc(s.orateur + (s.affiliation ? " (" + s.affiliation + ")" : "") + "\n" + (s.lien || page)),
      "LOCATION:" + esc(s.lien || "En ligne (lien envoyé avant la séance)"),
      "URL:" + (s.lien || page),
      "END:VEVENT", "END:VCALENDAR"
    ].join("\r\n");
    var a = document.createElement("a");
    a.href = URL.createObjectURL(new Blob([ics], { type: "text/calendar;charset=utf-8" }));
    a.download = "seminaire-asa-" + s.date + ".ics";
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  };

  /* ---------------------------------------------------------- prochaine séance (accueil) */
  var prochaineBloc = document.getElementById("prochaine-seance");
  if (prochaineBloc && donnees.length) {
    var futures = donnees.filter(function (s) { return !s.approx && dateLocale(s.date) >= aujourdhui; });
    var annoncees = donnees.filter(function (s) { return s.approx && s.a_venir; });
    var prochaine = futures[0] || annoncees[0];
    if (prochaine) {
      var champ = function (n) { return prochaineBloc.querySelector("[data-prochaine-" + n + "]"); };
      var dt = dateLocale(prochaine.date);
      champ("date").textContent = prochaine.approx ? prochaine.approx :
        dateLongue(dt).replace(/^./, function (c) { return c.toUpperCase(); }) + (prochaine.heure ? " · " + prochaine.heure : "");
      champ("titre").textContent = prochaine.titre;
      champ("orateur").textContent = prochaine.orateur + (prochaine.affiliation ? " (" + prochaine.affiliation + ")" : "");
      if (prochaine.affiche) {
        var img = document.createElement("img");
        img.src = prochaine.affiche; img.alt = "Affiche du séminaire de " + prochaine.orateur; img.loading = "lazy";
        champ("affiche").appendChild(img);
      } else {
        champ("affiche").classList.add("sans-affiche");
        champ("affiche").innerHTML = '<span aria-hidden="true">ASA</span>';
      }
      champ("lien").href = "seminaires.html#" + prochaine.id;
      var compte = champ("compte");
      var agenda = champ("agenda");
      if (prochaine.approx) {
        compte.textContent = "Date communiquée très bientôt sur nos réseaux.";
        agenda.hidden = true;
      } else {
        var jours = Math.round((dt - aujourdhui) / 86400000);
        compte.textContent = jours === 0 ? "C’est aujourd’hui !" : jours === 1 ? "C’est demain !" : "Dans " + jours + " jours";
        agenda.addEventListener("click", function () { telechargerIcs(prochaine); });
      }
      prochaineBloc.hidden = false;
    }
  }

  /* ---------------------------------------------------------- archive des séminaires */
  var rail = document.getElementById("rail-annees");
  var panneau = document.getElementById("panneau-seances");
  if (rail && panneau) {
    var onglets = $$("button", rail);
    var annees = $$(".annee-seances", panneau);
    var champRecherche = document.getElementById("recherche-seance");
    var statut = document.getElementById("recherche-statut");
    var videRecherche = document.getElementById("recherche-vide");
    var anneeActive = null;

    var ouvrirAnnee = function (annee, sansHash) {
      anneeActive = annee;
      onglets.forEach(function (o) { o.setAttribute("aria-selected", String(o.dataset.annee === annee)); });
      annees.forEach(function (p) { p.hidden = p.dataset.annee !== annee; });
      if (!sansHash) history.replaceState(null, "", "#y" + annee);
    };

    onglets.forEach(function (b) {
      b.addEventListener("click", function () {
        if (champRecherche && champRecherche.value) { champRecherche.value = ""; filtrer(); }
        ouvrirAnnee(b.dataset.annee);
      });
    });

    $$(".seance-tete", panneau).forEach(function (b) {
      b.addEventListener("click", function () {
        var art = b.closest(".seance");
        var ouvert = art.classList.toggle("ouvert");
        b.setAttribute("aria-expanded", ouvert ? "true" : "false");
        if (ouvert && art.id) history.replaceState(null, "", "#" + art.id);
      });
    });

    var sansAccents = function (t) { return t.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase(); };
    var filtrer = function () {
      var q = sansAccents((champRecherche.value || "").trim());
      if (!q) {
        rail.classList.remove("estompe");
        $$(".seance", panneau).forEach(function (s) { s.hidden = false; });
        $$(".annee-seances .etat-vide", panneau).forEach(function (e) { e.hidden = false; });
        videRecherche.hidden = true; statut.textContent = "";
        ouvrirAnnee(anneeActive || rail.querySelector("[data-defaut]").dataset.annee, true);
        return;
      }
      rail.classList.add("estompe");
      var mots = q.split(/\s+/), n = 0;
      annees.forEach(function (p) {
        var visibles = 0;
        $$(".seance", p).forEach(function (s) {
          var texte = sansAccents(s.dataset.recherche || "");
          var ok = mots.every(function (m) { return texte.indexOf(m) !== -1; });
          s.hidden = !ok; if (ok) visibles++;
        });
        $$(".etat-vide", p).forEach(function (e) { e.hidden = true; });
        p.hidden = visibles === 0; n += visibles;
      });
      videRecherche.hidden = n > 0;
      statut.textContent = n ? n + " séance" + (n > 1 ? "s" : "") + " trouvée" + (n > 1 ? "s" : "") + ", toutes années confondues" : "";
    };
    if (champRecherche) champRecherche.addEventListener("input", filtrer);

    /* Ouverture initiale : #y2024, #s-2024-06-09-nom… ou année par défaut */
    var h = decodeURIComponent(location.hash.slice(1));
    var cibleSeance = h && h.indexOf("s-") === 0 ? document.getElementById(h) : null;
    var anneeHash = (h.match(/^y(\d{4})$/) || [])[1];
    if (cibleSeance) {
      ouvrirAnnee(cibleSeance.closest(".annee-seances").dataset.annee, true);
      cibleSeance.classList.add("ouvert", "surligne");
      $(".seance-tete", cibleSeance).setAttribute("aria-expanded", "true");
      setTimeout(function () { cibleSeance.scrollIntoView({ behavior: lent ? "auto" : "smooth", block: "start" }); }, 80);
    } else if (anneeHash && rail.querySelector('[data-annee="' + anneeHash + '"]')) {
      ouvrirAnnee(anneeHash, true);
    } else {
      ouvrirAnnee((rail.querySelector("[data-defaut]") || onglets[0]).dataset.annee, true);
    }
  }

  /* ---------------------------------------------------------- filtres (journal, actualités) */
  var brancherFiltres = function (groupe, elements, attrBouton, attrElement, vide) {
    var boutons = $$("button", groupe);
    boutons.forEach(function (b) {
      b.addEventListener("click", function () {
        boutons.forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
        var val = b.dataset[attrBouton], n = 0;
        elements.forEach(function (el) {
          var ok = val === "tout" || el.dataset[attrElement] === val;
          el.hidden = !ok; if (ok) n++;
        });
        if (vide) vide.hidden = n > 0;
      });
    });
  };
  var filtresJournal = document.getElementById("filtres");
  if (filtresJournal) brancherFiltres(filtresJournal, $$("#catalogue .fiche"), "genre", "genre", document.getElementById("catalogue-vide"));
  var filtresActus = document.getElementById("filtres-actus");
  if (filtresActus) brancherFiltres(filtresActus, $$(".actu-item"), "filtre", "categorie", null);

  /* ---------------------------------------------------------- copier le lien (articles) */
  $$(".copier-lien").forEach(function (b) {
    b.addEventListener("click", function () {
      var fait = function () { var t = b.textContent; b.textContent = "Lien copié ✓"; setTimeout(function () { b.textContent = t; }, 1800); };
      if (navigator.clipboard) navigator.clipboard.writeText(b.dataset.url).then(fait, function () { prompt("Copiez ce lien :", b.dataset.url); });
      else prompt("Copiez ce lien :", b.dataset.url);
    });
  });

  /* ---------------------------------------------------------- formulaire de contact */
  var form = document.getElementById("formulaire-contact");
  if (form) {
    var statutF = document.getElementById("formulaire-statut");
    var sujet = (new URLSearchParams(location.search)).get("sujet");
    var choix = document.getElementById("champ-sujet");
    if (sujet && choix) {
      var existe = $$("option", choix).some(function (o) { return o.value === sujet; });
      if (!existe) { var o = document.createElement("option"); o.textContent = sujet; choix.insertBefore(o, choix.firstChild); }
      choix.value = sujet;
    }
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var donneesF = new FormData(form);
      /* Sans clé Web3Forms : on ouvre la messagerie du visiteur */
      if (!form.dataset.cle) {
        var corps = donneesF.get("message") + "\n\n" + donneesF.get("nom") + " — " + donneesF.get("email");
        location.href = "mailto:" + form.dataset.email + "?subject=" + encodeURIComponent("[Site ASA] " + donneesF.get("sujet")) + "&body=" + encodeURIComponent(corps);
        return;
      }
      donneesF.set("subject", "[Site ASA] " + donneesF.get("sujet") + " — " + donneesF.get("nom"));
      donneesF.set("replyto", donneesF.get("email"));
      var bouton = form.querySelector("button[type=submit]");
      bouton.disabled = true; statutF.className = "formulaire-statut"; statutF.textContent = "Envoi en cours…";
      fetch(form.action, { method: "POST", body: donneesF, headers: { Accept: "application/json" } })
        .then(function (r) { return r.json(); })
        .then(function (r) {
          if (!r.success) throw new Error(r.message);
          form.reset();
          statutF.className = "formulaire-statut ok";
          statutF.textContent = "Merci ! Votre message est bien parti, nous vous répondrons rapidement.";
        })
        .catch(function () {
          statutF.className = "formulaire-statut erreur";
          statutF.innerHTML = "L’envoi a échoué. Écrivez-nous directement à <a href=\"mailto:" + form.dataset.email + "\">" + form.dataset.email + "</a>.";
        })
        .then(function () { bouton.disabled = false; });
    });
  }

  /* ---------------------------------------------------------- bouton « haut de page » */
  var haut = document.createElement("button");
  haut.type = "button"; haut.className = "haut-de-page"; haut.setAttribute("aria-label", "Revenir en haut de la page");
  haut.textContent = "↑";
  haut.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: lent ? "auto" : "smooth" }); });
  document.body.appendChild(haut);
  var majHaut = function () { haut.classList.toggle("visible", window.scrollY > 700); };
  window.addEventListener("scroll", majHaut, { passive: true }); majHaut();
})();

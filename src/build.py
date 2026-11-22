# -*- coding: utf-8 -*-
import os, json, html, re, shutil, sys
from urllib.parse import quote_plus
sys.path.insert(0, os.path.dirname(__file__))
from content import CHECKLIST, PRIO, GUIDES, MESSAGES, FAQ_HOME
from extra_m import EXTRA
from longtail_m import PRINTLIST
import neutre_m
from auto_articles import AUTO_META
from tools_m import TOOLS
import ogimg

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'docs')
# Sans domaine pour l'instant (plus tard : LMM_BASE=https://domaine.fr et CUSTOM_DOMAIN)
BASE = os.environ.get('LMM_BASE', 'https://malistedemariage.fr')
CUSTOM_DOMAIN = os.environ.get('LMM_DOMAIN', 'malistedemariage.fr')
CUSTOM = bool(CUSTOM_DOMAIN) and CUSTOM_DOMAIN in BASE
PATH0 = '/' + BASE.split('://', 1)[1].split('/', 1)[1] + '/' if BASE.count('/') > 2 else '/'
DOMAIN = CUSTOM_DOMAIN if CUSTOM else 'Ma liste mariage'
SITE = 'Ma liste mariage'
LLMS_INTRO = "Ma liste mariage aide les futurs mariés à préparer leur liste de mariage et l'organisation du jour J : idées de cadeaux pour la maison, guides pour bien choisir l'électroménager et les arts de la table, comparatifs de produits vendus en France, checklist d'organisation. Les liens vers Amazon sont des liens d'affiliation."
TAG = 'malistemariage-21'   # identifiant Amazon Partenaires
CONTACT = 'contact@cvlibre.com'
YEAR = 2026
AMZ_LIST = 'https://www.amazon.fr/wedding?tag=' + TAG   # prime liste de mariage
BABY_SITE = 'https://malistebebe.fr/'
DISCLOSURE = "En tant que Partenaire Amazon, nous réalisons un bénéfice sur les achats remplissant les conditions requises."

def amz(q):
    return 'https://www.amazon.fr/s?k=' + quote_plus(q) + '&tag=' + TAG

def esc(s): return html.escape(s, quote=True)

# Couleur et emoji de chaque guide
META = {
  'liste-de-mariage-amazon/': ('🎁', 'peche'),
  'que-mettre-dans-une-liste-de-mariage/': ('📝', 'ciel'),
  'liste-de-mariage-quand-on-vit-deja-ensemble/': ('🏡', 'menthe'),
  'liste-de-mariage-originale/': ('✨', 'miel'),
  'liste-de-mariage-petit-budget/': ('🪙', 'menthe'),
  'liste-de-mariage-ou-cagnotte/': ('💶', 'lilas'),
  'quand-faire-sa-liste-de-mariage/': ('📅', 'ciel'),
  'message-liste-de-mariage/': ('💌', 'peche'),
  'combien-donner-pour-un-mariage/': ('🤔', 'miel'),
  'idees-cadeau-de-mariage/': ('🎀', 'lilas'),
  'remerciements-mariage/': ('🙏', 'menthe'),
  'liste-de-pacs/': ('💞', 'peche'),
  'acheter-sur-une-liste-de-mariage-amazon/': ('🛒', 'ciel'),
  'trouver-une-liste-de-mariage-amazon/': ('🔎', 'menthe'),
  'modifier-supprimer-liste-de-mariage-amazon/': ('⚙️', 'lilas'),
  'liste-de-mariage-a-imprimer/': ('🖨️', 'ciel'),
  'liste-de-mariage-mariage-civil/': ('🏛️', 'miel'),
  'liste-de-mariage-et-bebe-en-route/': ('🍼', 'peche'),
  'faut-il-faire-une-liste-de-mariage/': ('❓', 'menthe'),
}
META.update(AUTO_META)
CAT_TINT = ['lilas', 'ciel', 'peche', 'menthe', 'miel', 'lilas', 'ciel']

CTA = ('<aside class="tag"><span class="tag-hole" aria-hidden="true"></span><div class="tag-tx">'
       '<strong>Prêts à créer votre liste en ligne ?</strong>'
       '<span>Notre choix : la liste Amazon, gratuite et simple pour vos invités. <a href="{R}ou-faire-sa-liste-de-mariage/">Comparer les solutions</a></span></div>'
       '<a class="btn" href="' + AMZ_LIST + '" rel="sponsored nofollow noopener" target="_blank">Créer notre liste</a></aside>')

NAV = [('checklist/', 'Checklist'), ('ou-faire-sa-liste-de-mariage/', 'Où faire sa liste'),
       ('outils/', 'Outils'), ('guides/', 'Guides')]

FONTS = ('<link rel="preload" href="@R@assets/fonts/bricolage-grotesque-latin-800-normal.woff2" as="font" type="font/woff2" crossorigin>'
         '<link rel="preload" href="@R@assets/fonts/figtree-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>')

AUTHOR_NAME = 'Jérémy Dacier-Jury'
AUTHOR_LD = {"@type": "Person", "name": AUTHOR_NAME, "url": BASE + '/a-propos/'}
PUBLISHER_LD = {"@type": "Organization", "name": SITE, "url": BASE + '/', "logo": {"@type": "ImageObject", "url": BASE + '/assets/apple-touch-icon.png'}}



# Boutons de partage (22 nov 2026, demande de Jeremy)
SHARE_SKIP = ('a-propos/', 'mentions-legales/', 'confidentialite/', 'contact/', 'publicite/', 'partenariats/', '404-tmp/')
def share_html(url, title):
    from urllib.parse import quote
    import json as _j
    t = title.split(' | ')[0]
    u, tq = quote(url, safe=''), quote(t, safe='')
    return ('<style>.share{margin:28px 0 8px;padding:14px 0 0;border-top:1px solid var(--line,var(--trait,#ddd))}'
      '.share-t{font-weight:700;margin:0 0 8px}.share-b{display:flex;flex-wrap:wrap;gap:8px}'
      '.sh{display:inline-flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;border:1.5px solid var(--brand,var(--framboise,#2F6B57));'
      'background:#fff;color:var(--brand,var(--framboise,#2F6B57));font:inherit;font-size:.92em;font-weight:700;text-decoration:none;cursor:pointer}'
      '.sh:hover,.sh:focus-visible{background:var(--brand,var(--framboise,#2F6B57));color:#fff}.sh[hidden]{display:none}</style>'
      '<div class="share"><p class="share-t">Partager cette page</p><div class="share-b">'
      '<button type="button" class="sh sh-n" hidden>Partager</button>'
      f'<a class="sh" href="https://wa.me/?text={tq}%20{u}" target="_blank" rel="noopener nofollow">WhatsApp</a>'
      f'<a class="sh" href="https://www.facebook.com/sharer/sharer.php?u={u}" target="_blank" rel="noopener nofollow">Facebook</a>'
      f'<a class="sh" href="mailto:?subject={tq}&amp;body={u}">E-mail</a>'
      '<button type="button" class="sh sh-c">Copier le lien</button></div></div>'
      '<script>(function(){var s=document.currentScript.previousElementSibling,u=' + _j.dumps(url) + ',t=' + _j.dumps(t) + ';'
      'var n=s.querySelector(".sh-n");if(navigator.share){n.hidden=false;n.onclick=function(){navigator.share({title:t,url:u}).catch(function(){})}}'
      'var c=s.querySelector(".sh-c");c.onclick=function(){var ok=function(){c.textContent="Lien copié"};'
      'if(navigator.clipboard){navigator.clipboard.writeText(u).then(ok,function(){})}else{var i=document.createElement("input");i.value=u;document.body.appendChild(i);i.select();try{document.execCommand("copy");ok()}catch(e){}i.remove()}}})()</script>')

def page(path, title, desc, body, schema=None, crumbs=None, extra_head='', cls='', noindex=False, og=None):
    depth = path.count('/')
    R = '../' * depth
    url = BASE + '/' + path
    if path not in SHARE_SKIP:
        if body.count('</article>') == 1: body = body.replace('</article>', share_html(url, title) + '</article>')
        else: body += '<div class="wrap">' + share_html(url, title) + '</div>'
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE + '/', "inLanguage": "fr", "publisher": PUBLISHER_LD}]
    if path == '': ld.append(dict({"@context": "https://schema.org"}, **PUBLISHER_LD))
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Accueil", "item": BASE + '/'}]
        for i, (n, p) in enumerate(crumbs):
            items.append({"@type": "ListItem", "position": i + 2, "name": n, "item": BASE + '/' + p})
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if schema: ld += schema
    nav = ''.join('<a href="%s%s"%s>%s</a>' % (R, p, ' aria-current="page"' if p == path else '', n) for p, n in NAV)
    bc = ''
    if crumbs:
        bc = '<nav class="bc" aria-label="Fil d\'Ariane"><a href="%s">Accueil</a>' % R + ''.join(
            ' / <a href="%s%s">%s</a>' % (R, p, esc(n)) for n, p in crumbs[:-1]) + ' / <span>%s</span></nav>' % esc(crumbs[-1][0])
    doc = f'''<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">{'<meta name="robots" content="noindex">' if noindex else ''}
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/{og or "assets/og.png"}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{esc(title)}">
<meta property="og:site_name" content="Ma liste mariage">
<meta name="twitter:image" content="{BASE}/{og or "assets/og.png"}">
<meta property="og:locale" content="fr_FR">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#F1F4F0">
<meta name="google-site-verification" content="8W3sIwH_eiI687C-pNBPh9q22AMJyMqlmjN3iID2_k8" />
<link rel="icon" href="{R}assets/favicon.ico" sizes="32x32"><link rel="icon" href="{R}assets/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="{R}assets/apple-touch-icon.png">
{FONTS.replace('@R@', R)}
<link rel="stylesheet" href="{R}assets/style.css?v=26">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{extra_head}</head>
<body class="{cls}">
<a class="skip" href="#main">Aller au contenu</a>
<header class="top"><div class="wrap top-in">
<a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">💍</span>Ma liste mariage</a>
<nav class="menu" aria-label="Menu">{nav}</nav>
</div></header>
<main id="main">
{('<div class="wrap">' + bc + '</div>') if bc else ''}
{body.replace('{R}', R)}
</main>
<div class="wave-foot"><svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C 240 70 480 0 720 25 C 960 50 1200 10 1440 30 L1440 60 L0 60 Z"/></svg></div><footer class="foot"><div class="wrap foot-in">
<div><a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">💍</span>Ma liste mariage</a>
<p>La checklist gratuite pour composer votre liste de mariage, pièce par pièce.</p></div>
<nav aria-label="Pied de page"><a href="{R}checklist/">Checklist</a><a href="{R}guides/">Guides</a><a href="{R}outils/">Outils</a><a href="{R}a-propos/">À propos</a><a href="{R}mentions-legales/">Mentions légales</a><a href="{R}confidentialite/">Confidentialité</a><a href="mailto:{CONTACT}">Contact</a></nav>
<p class="wed">🍼 Un bébé en route ? <a href="{BABY_SITE}">Préparez votre liste de naissance sur Ma liste bébé</a></p>
<nav class="sites" aria-label="Nos autres sites"><p class="sites-t">Découvrez aussi nos autres sites</p><div class="sites-g"><a href="https://vieillir-chez-soi.fr/"><img src="https://vieillir-chez-soi.fr/assets/favicon.svg" alt="" width="40" height="40" loading="lazy"><span><strong>Vieillir chez soi</strong><small>Rester autonome à la maison</small></span></a><a href="https://lesoiseauxdujardin.fr/"><img src="https://lesoiseauxdujardin.fr/assets/favicon.svg" alt="" width="40" height="40" loading="lazy"><span><strong>Les oiseaux du jardin</strong><small>Nourrir et observer les oiseaux</small></span></a><a href="https://malistebebe.fr/"><img src="https://malistebebe.fr/assets/favicon.svg" alt="" width="40" height="40" loading="lazy"><span><strong>Ma liste bébé</strong><small>Préparer l'arrivée de bébé</small></span></a></div></nav>
<p class="disc">{DISCLOSURE} Les prix et les conditions d'Amazon peuvent changer : vérifiez-les avant d'acheter. © {YEAR} {DOMAIN}</p>
</div></footer>
<script src="{R}assets/track.js?v=1" defer></script>
</body>
</html>
'''
    if '—' in doc:
        raise SystemExit('Tiret long interdit dans ' + path)
    d = os.path.join(OUT, path)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(doc)
    if len(title) > 65: print('Titre long :', path, len(title))
    if not noindex: PAGES.append(path)

PAGES = []

def ogfor(name, title, kicker, emoji, tint):
    rel = 'og/' + name + '.png'
    ogimg.make(os.path.join(OUT, rel), title, kicker, emoji, tint)
    return rel

def faq_block(faq):
    if not faq: return '', []
    h = '<h2 id="faq">Questions fréquentes</h2><div class="faq">' + ''.join(
        '<details><summary>%s</summary><p>%s</p></details>' % (esc(q), esc(a)) for q, a in faq) + '</div>'
    s = [{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]
    return h, s

def gcard(x, long=False):
    e, t = META.get(x['slug'], ('📄', 'ciel'))
    d = x['desc'] if long else x['desc'][:96].rsplit(' ', 1)[0] + '...'
    return ('<a class="gcard t-%s" href="{R}%s"><span class="gcard-e" aria-hidden="true">%s</span>'
            '<strong>%s</strong><span class="gcard-d">%s</span></a>') % (t, x['slug'], e, esc(x['short'] if not long else x['h1']), esc(d))

def related(cur):
    i = [x['slug'] for x in GUIDES].index(cur)
    links = [GUIDES[(i + k) % len(GUIDES)] for k in range(1, 4)]
    return '<section class="wrap rel"><h2>À lire ensuite</h2><div class="grid3">' + ''.join(gcard(x) for x in links) + '</div></section>'

def slugify(t):
    import unicodedata
    t = unicodedata.normalize('NFD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')[:50]

def add_toc(body):
    heads = []
    def rep(m):
        txt = re.sub('<[^>]+>', '', m.group(1)); sid = slugify(txt); heads.append((sid, txt))
        return '<h2 id="%s">%s</h2>' % (sid, m.group(1))
    body = re.sub(r'<h2>(.*?)</h2>', rep, body)
    if len(heads) < 3: return body, ''
    toc = '<nav class="toc" aria-label="Sommaire"><strong>Dans ce guide</strong><ol>' + ''.join(
        '<li><a href="#%s">%s</a></li>' % (i, esc(t)) for i, t in heads) + '</ol></nav>'
    return body, toc

def messages_html():
    out = '<div class="msgs">'
    for i, (t, m) in enumerate(MESSAGES):
        m = m.replace('\\n', '\n')
        out += '<div class="msg"><h3>%s</h3><p class="mtext" id="m%d">%s</p><button class="btn ghost sm copy" data-t="m%d">Copier le message</button></div>' % (
            esc(t), i, esc(m).replace('\n', '<br>'), i)
    out += '</div><script src="{R}assets/msg.js?v=2" defer></script>'
    return out

HERO_TAG = """<div class="hero-tag" aria-hidden="true"><span class="tag-hole"></span>
<p class="ht-title">Notre liste de mariage</p>
<ul>
<li class="on" style="--d:.2s">Cocotte en fonte</li>
<li class="on" style="--d:.6s">Service pour 12</li>
<li class="on" style="--d:1s">Valises cabine</li>
<li style="--d:1.4s">Robot pâtissier</li>
<li style="--d:1.8s">Parure de lit en lin</li>
</ul>
<p class="ht-foot">3 sur 49 cochés</p></div>"""
# Guide « comment choisir » associé à un article de la checklist (affiché seulement si le guide existe)
GUIDE_MAP = [('Batterie de casseroles', 'comment-choisir-batterie-de-casseroles/'), ('Cocotte', 'comment-choisir-cocotte-en-fonte/'), ('Couteaux', 'comment-choisir-couteaux-de-cuisine/'), ('Robot pâtissier', 'quel-robot-patissier-pour-une-liste-de-mariage/'), ('Robot multifonction', 'comment-choisir-blender/'), ('Machine à café', 'comment-choisir-machine-a-cafe-grain/'), ('Service de vaisselle', 'comment-choisir-service-de-table/'), ('Couette', 'comment-choisir-couette/'), ('Aspirateur balai', 'comment-choisir-aspirateur-balai/'), ('Robot aspirateur', 'comment-choisir-robot-aspirateur/'), ('Fer ou centrale', 'comment-choisir-centrale-vapeur/'), ('Valises cabine', 'comment-choisir-valise-cabine/'), ('Grande valise', 'comment-choisir-valise-cabine/'), ('Barbecue ou plancha', 'comment-choisir-plancha/'), ('Parure de lit', 'linge-de-maison-liste-de-mariage/'), ('Serviettes de bain', 'linge-de-maison-liste-de-mariage/')]
def guide_for(name):
    have = {x['slug'] for x in GUIDES}
    for key, slug in GUIDE_MAP:
        if name.startswith(key) and slug in have:
            return slug
    return None

REL = 'rel="sponsored nofollow noopener" target="_blank"'
def top_pick(body):
    """Produit n°1 d'un top : (nom, raison, ancre, requête Amazon) ou None.
    Premier intertitre (« 1. » en priorité) suivi, avant l'intertitre suivant, d'un lien « Voir ... Amazon »."""
    if not re.search(r'Comment (?:nous avons|on a) fait cette sélection', body): return None
    heads = list(re.finditer(r'<h([23])(?: id="([^"]*)")?>\s*(.+?)</h\1>', body))
    order = [h for h in heads if re.match(r'1\.\s', h.group(3))] + heads
    for k, h in enumerate(order):
        nxt = next((x.start() for x in heads if x.start() > h.start()), len(body))
        a = re.search(r'href="\{AMZ:([^}]+)\}"[^>]*>\s*Voir[^<]*Amazon', body[h.end():nxt])
        if not a: continue
        title = re.sub(r'^1\.\s*', '', re.sub('<[^>]+>', '', h.group(3)))
        name, _, why = title.partition(' : ')
        why = re.sub(r'\s*\((?:notre|mon) choix[^)]*\)\s*$', '', why.strip(), flags=re.I)
        return name.strip(), (why[:1].upper() + why[1:]) if why else '', h.group(2), a.group(1)
    return None

def buy_buttons(body):
    """Tops : le lien « Voir sur Amazon » de fin de fiche devient un bouton « Voir le prix sur Amazon »."""
    if not re.search(r'Comment (?:nous avons|on a) fait cette sélection', body): return body
    return re.sub(r'<p><a href="(\{AMZ:[^}]+\})"[^>]*>\s*Voir sur Amazon\s*</a></p>',
                  lambda m: '<p class="buy"><a class="btn" href="%s" %s>Voir le prix sur Amazon</a></p>' % (m.group(1), REL), body)

def pick_box(body):
    """Encadré « Notre choix » juste après l'intro : produit n°1 des tops, ou n°1 du comparatif lié pour les guides."""
    if '{CTA}' not in body or 'class="pick"' in body: return body
    p = top_pick(body)
    if p:
        name, why, anchor, q = p
        more = ('<a class="pick-more" href="#%s">Pourquoi ce choix</a>' % anchor) if anchor else ''
        box = ('<aside class="pick"><div><span class="pick-tag">⭐ Notre choix n°1</span><strong>%s</strong><span>%s</span>%s</div>'
               '<a class="btn" href="{AMZ:%s}" %s>Voir sur Amazon</a></aside>') % (esc(name), esc(why or 'Notre recommandation n°1 dans ce comparatif.'), more, q, REL)
        return body.replace('{CTA}', box + '\n{CTA}', 1)
    return body

def pick_box_guide(body, slug):
    """Pour un guide : n°1 du comparatif lié qui parle du même produit (mots communs dans l'adresse)."""
    if '{CTA}' not in body or 'class="pick"' in body or slug.startswith('meilleur'): return body
    stop = {'a', 'd', 'l', 'au', 'aux', 'des', 'en', 'et', 'un', 'une', 'par', 'sa', 'son', 'ses', 'ma', 'mon', 'mes', 'ta', 'ton', 'tes', 'noces', 'annee', 'ans', 'bebe', 'mariage', 'liste', 'naissance', 'cadeau', 'livre', 'livres', 'meilleur', 'meilleure', 'meilleurs', 'comment', 'choisir', 'senior', 'personne', 'agee', 'de', 'du', 'la', 'le', 'les', 'pour', 'bien', 'quel', 'quelle'}
    if re.search(r'aide|rembours|prix|retraite', slug): return body
    words = [w for w in slug.strip('/').split('-') if w not in stop]
    if not words: return body
    mine = set(words)
    best, score = None, 0
    cands = list(dict.fromkeys(re.findall(r'href="\{R\}(meilleur[a-z0-9-]*/)"', body))) + [gd['slug'] for gd in GUIDES if gd['slug'].startswith('meilleur')]
    for cand in cands:
        cw = set(cand.strip('/').split('-')) - stop
        sc = len(mine & cw) if words[0] in cw else 0
        if sc > score: best, score = cand, sc
    if not best or score < min(2, len(mine)): return body
    top = next((gd for gd in GUIDES if gd['slug'] == best), None)
    p = top_pick(top['body']) if top else None
    if not p: return body
    name, why, anchor, q = p
    box = ('<aside class="pick"><div><span class="pick-tag">⭐ Notre n°1</span><strong>%s</strong><span>%s</span>'
           '<a class="pick-more" href="{R}%s">Voir tout le comparatif</a></div>'
           '<a class="btn" href="{AMZ:%s}" %s>Voir sur Amazon</a></aside>') % (esc(name), esc(why or ('Extrait de notre comparatif « %s ».' % top['short'])), best, q, REL)
    return body.replace('{CTA}', box + '\n{CTA}', 1)

def build():
    if os.path.exists(OUT):
        for n in os.listdir(OUT):
            p = os.path.join(OUT, n)
            if n == 'assets' or (n.endswith('.txt') and len(n) == 36): continue
            shutil.rmtree(p) if os.path.isdir(p) else os.remove(p)
    os.makedirs(OUT, exist_ok=True)

    # Image de partage par défaut
    ogimg.make(os.path.join(OUT, 'assets', 'og.png'), 'Votre liste de mariage, prête en 10 minutes', 'Checklist gratuite', '💍', 'miel')
    # Données de la checklist
    data = []
    for cat, emo, items in CHECKLIST:
        data.append({"c": cat, "e": emo, "i": [dict({"n": n, "u": amz(q), "p": p, "t": t}, **({"g": guide_for(n)} if guide_for(n) else {})) for n, q, p, t in items]})
    total = sum(len(c['i']) for c in data)
    js = 'window.LDN_DATA=' + json.dumps(data, ensure_ascii=False) + ';window.LDN_PRIO=' + json.dumps({str(k): v for k, v in PRIO.items()}, ensure_ascii=False) + ';window.LDN_LIST=' + json.dumps(AMZ_LIST) + ';window.LDN_TAG=' + json.dumps(TAG) + ';'
    with open(os.path.join(OUT, 'assets', 'data.js'), 'w', encoding='utf-8') as f:
        f.write(js)

    tool = ('<div id="ck" class="ck"><noscript>Active JavaScript pour cocher les articles.</noscript></div>'
            '<script src="{R}assets/data.js?v=3"></script><script src="{R}assets/checklist.js?v=9b" defer></script>')

    # Accueil
    cats = ''.join('<a class="cat-chip t-%s" href="{R}checklist/#cat%d"><span aria-hidden="true">%s</span>%s<small>%d articles</small></a>' % (
        CAT_TINT[i % len(CAT_TINT)], i, e, esc(c), len(it)) for i, (c, e, it) in enumerate(CHECKLIST))
    fh, fs = faq_block(FAQ_HOME)
    home = f'''<section class="hero"><span class="blob b1" aria-hidden="true"></span><span class="blob b2" aria-hidden="true"></span><span class="spark s1" aria-hidden="true">✦</span><span class="spark s2" aria-hidden="true">✦</span><span class="spark s3" aria-hidden="true">✦</span><div class="wrap hero-in">
<div class="hero-tx">
<h1>Votre liste de mariage, prête en 10 minutes</h1>
<p class="hero-p">{total} idées de cadeaux triées par pièce, de la cocotte aux valises du voyage de noces. Vous cochez, vous comparez les modèles en un clic, et vous remplissez votre liste en ligne sans rien oublier.</p>
<div class="hbtn"><a class="btn big" href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">Créer notre liste</a>
<a class="btn ghost big" href="{{R}}checklist/">Voir la checklist</a></div>
<p class="hero-note"><strong>1.</strong> Créez votre liste de mariage sur Amazon, c'est gratuit (<a href="{{R}}ou-faire-sa-liste-de-mariage/">pourquoi Amazon ?</a>). <strong>2.</strong> Remplissez-la avec notre checklist, pièce par pièce.</p>
</div>
{HERO_TAG}
</div></section>
<section class="wrap block">
<h2>Pièce par pièce</h2>
<p class="sub">Ouvrez une catégorie pour voir les cadeaux qui comptent vraiment.</p>
<div class="chips">{cats}</div>
</section>
<div class="wave-top"><svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C 240 70 480 0 720 25 C 960 50 1200 10 1440 30 L1440 60 L0 60 Z"/></svg></div><section class="band"><div class="wrap block">
<h2>Comment ça marche</h2>
<ol class="steps">
<li><strong>Créez votre liste</strong><span>sur Amazon, gratuitement : <a href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">créer notre liste</a>.</span></li>
<li><strong>Remplissez-la</strong><span>avec la <a href="{{R}}checklist/">checklist</a> : pour chaque article, « Voir » vous montre les modèles à ajouter.</span></li>
<li><strong>Partagez-la</strong><span>avec vos invités grâce à nos <a href="{{R}}message-liste-de-mariage/">textes tout prêts</a>.</span></li>
</ol></div></section><div class="wave-bot"><svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C 240 70 480 0 720 25 C 960 50 1200 10 1440 30 L1440 60 L0 60 Z"/></svg></div>
<section class="wrap block">
<h2>Les guides des futurs mariés</h2>
<div class="grid3">{''.join(gcard(x) for x in GUIDES[:6])}</div>
<p class="more"><a href="{{R}}guides/">Voir les {len(GUIDES)} guides</a></p>
</section>
<section class="wrap block">
<h2>Nos outils gratuits</h2>
<div class="grid3">{''.join(('<a class="gcard t-%s" href="{R}%s"><span class="gcard-e" aria-hidden="true">%s</span><strong>%s</strong><span class="gcard-d">%s</span></a>') % (x['tint'], x['slug'], x['emoji'], esc(x['h1']), esc(x['desc'])) for x in TOOLS)}</div>
</section>
<section class="wrap block narrow"><div class="prose">
<h2>Préparer sa liste de mariage sereinement</h2>
<p>Une liste de mariage rend service à tout le monde : vos invités savent quoi offrir, et vous recevez des cadeaux qui vous serviront vraiment. La plupart des couples la créent trois à quatre mois avant le jour J, en même temps que les faire-part. Notre <a href="{{R}}quand-faire-sa-liste-de-mariage/">calendrier</a> détaille chaque étape.</p>
<p>Le secret d'une bonne liste, c'est l'équilibre : des essentiels pour la maison, quelques coups de cœur qui vous ressemblent, et des cadeaux à tous les prix. Prévoyez un tiers d'articles à moins de 40 €, pour que chaque invité trouve son bonheur, et quelques gros cadeaux que vos amis offriront ensemble. Vous vivez déjà ensemble ? Misez sur le <a href="{{R}}liste-de-mariage-quand-on-vit-deja-ensemble/">renouvellement et le voyage de noces</a>.</p>
<p>Pour la liste en ligne, plusieurs solutions existent : site marchand, liste multi-boutiques, grand magasin. Notre comparatif <a href="{{R}}ou-faire-sa-liste-de-mariage/">où faire sa liste de mariage</a> vous aide à choisir. Vous hésitez avec une cagnotte ? Notre comparatif <a href="{{R}}liste-de-mariage-ou-cagnotte/">liste ou cagnotte</a> vous aide à choisir, et nos <a href="{{R}}message-liste-de-mariage/">textes tout prêts</a> vous aident à l'annoncer avec tact.</p>
</div></section>
<section class="wrap block narrow">{fh}</section>'''
    page('', 'Liste de mariage : checklist et %d idées de cadeaux (%d)' % (total, YEAR),
         'Composez votre liste de mariage en 10 minutes : checklist gratuite de %d idées de cadeaux triées par pièce, conseils et comparatif des listes en ligne.' % total,
         home, schema=fs, cls='home', og=ogfor('accueil', 'Votre liste de mariage, prête en 10 minutes', 'Checklist gratuite', '💍', 'miel'))

    # Checklist
    ck = f'''<section class="wrap pagehead"><h1>Checklist liste de mariage</h1>
<p class="lead">{total} idées de cadeaux triées par pièce. Cochez ce que vous voulez mettre dans votre liste : vos choix restent enregistrés sur cet appareil.</p></section>
<div class="wrap"><div class="ck-first"><strong>Comment ajouter un article à votre liste</strong><ol><li>Pas encore de liste ? <a href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">Créez-la sur Amazon</a>, c'est gratuit.</li><li>Ici, cliquez sur <strong>« Voir »</strong> à côté d'un article : Amazon s'ouvre avec des modèles.</li><li>Choisissez un modèle, puis appuyez sur <strong>« Ajouter à la liste de mariage »</strong>, sous « Ajouter au panier ». Sur l'appli, il peut se trouver dans le menu « Ajouter à une liste ».</li><li>Revenez ici : l'article est déjà coché, passez au suivant.</li></ol></div></div>
<div class="wrap">{tool}
{CTA}
<div class="prose">
<h2>Comment utiliser cette checklist ?</h2>
<p>Commencez par filtrer sur <strong>Essentiel</strong> : ce sont les cadeaux les plus utiles pour une maison bien équipée. Ajoutez ensuite les articles <strong>Utile</strong>, puis quelques <strong>Coups de cœur</strong> qui vous ressemblent. Gardez des cadeaux à tous les prix pour que chaque invité trouve son bonheur.</p>
<p>Pour chaque article, le bouton « Voir » vous montre des modèles : choisissez celui qui vous plaît et ajoutez-le à votre liste en ligne. Une fois la liste remplie, partagez-la avec nos <a href="{{R}}message-liste-de-mariage/">textes tout prêts</a>.</p>
</div></div>'''
    schema = [{"@context": "https://schema.org", "@type": "WebApplication", "name": "Checklist liste de mariage",
               "applicationCategory": "LifestyleApplication", "operatingSystem": "Tous", "url": BASE + '/checklist/',
               "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}]
    page('checklist/', 'Checklist liste de mariage gratuite (%d idées)' % total,
         'Checklist interactive pour votre liste de mariage : %d idées de cadeaux triées par pièce (cuisine, table, linge, voyage de noces), avec des conseils.' % total,
         ck, schema=schema, crumbs=[('Checklist', 'checklist/')], cls='tool', og=ogfor('checklist', 'Checklist liste de mariage : %d idées' % total, 'Gratuit', '✅', 'menthe'))

    # Guides
    for x in GUIDES:
        ex_html, ex_faq = EXTRA.get(x['slug'], ('', []))
        fh, fs = faq_block(x['faq'] + ex_faq)
        body = pick_box_guide(pick_box(buy_buttons(x['body'] + ex_html)), x['slug']).replace('{CTA}', CTA).replace('{PRINTLIST}', PRINTLIST).replace('{MSGS}', messages_html())
        body = re.sub(r'\{AMZ:([^}]+)\}', lambda m: amz(m.group(1)), body)
        body, toc = add_toc(body)
        words = len(re.sub('<[^>]+>', ' ', body).split())
        mins = max(2, round(words / 200))
        e, t = META.get(x['slug'], ('📄', 'ciel'))
        ogp = ogfor(x['slug'].strip('/'), x['h1'], 'Guide', e, t)
        art = [{"@context": "https://schema.org", "@type": "Article", "headline": x['h1'], "description": x['desc'],
                "inLanguage": "fr-FR", "datePublished": "2026-11-14", "dateModified": "2026-11-14",
                "author": AUTHOR_LD, "publisher": PUBLISHER_LD, "image": BASE + '/' + ogp, "mainEntityOfPage": BASE + '/' + x['slug']}]
        b = ('<header class="cover t-%s"><span class="cover-dots" aria-hidden="true"></span><div class="wrap cover-in"><span class="cover-e" aria-hidden="true">%s</span>'
             '<div><h1>%s</h1><p class="cover-d">%s</p><p class="cover-m">%d min de lecture, mis à jour en novembre %d, par <a href="/a-propos/" rel="author">Jérémy</a></p></div></div></header>'
             '<div class="wrap art-wrap"><article class="prose">%s%s%s%s</article></div>%s') % (
            t, e, esc(x['h1']), esc(x['desc']), mins, YEAR, toc, body, CTA, fh, related(x['slug']))
        page(x['slug'], x['title'], x['desc'], b, schema=art + fs,
             crumbs=[('Guides', 'guides/'), (x['short'], x['slug'])], cls='guide',
             og=ogp)

    idx = ('<section class="wrap pagehead"><h1>Guides liste de mariage</h1><p class="lead">Tout pour composer votre liste, l\'annoncer à vos invités et les remercier.</p></section>'
           '<section class="wrap block"><div class="grid3">' + ''.join(gcard(x, True) for x in GUIDES) + '</div></section>')
    page('guides/', 'Guides liste de mariage : idées, textes et conseils',
         'Tous nos guides pour votre liste de mariage : que mettre, liste Amazon, petits prix, cagnotte, textes pour le faire-part, combien donner et remerciements.',
         idx, crumbs=[('Guides', 'guides/')], og=ogfor('guides', 'Tous les guides pour votre liste de mariage', 'Guides', '📚', 'ciel'))

    # Outils gratuits
    for x in TOOLS:
        fh, fs = faq_block(x['faq'])
        body, toc = add_toc(x['body'])
        app = [{"@context": "https://schema.org", "@type": "WebApplication", "name": x['h1'], "description": x['desc'],
                "applicationCategory": "UtilitiesApplication", "operatingSystem": "Tous", "url": BASE + '/' + x['slug'],
                "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}}]
        ogp = ogfor(x['slug'].strip('/'), x['h1'], 'Outil gratuit', x['emoji'], x['tint'])
        b = ('<header class="cover t-%s"><span class="cover-dots" aria-hidden="true"></span><div class="wrap cover-in"><span class="cover-e" aria-hidden="true">%s</span>'
             '<div><h1>%s</h1><p class="cover-d">%s</p><p class="cover-m">Outil gratuit, sans inscription</p></div></div></header>'
             '<div class="wrap art-wrap"><div class="tool-box">%s</div><article class="prose">%s%s%s%s</article></div>'
             '<script src="{R}assets/tools.js?v=1" defer></script>') % (
            x['tint'], x['emoji'], esc(x['h1']), esc(x['desc']), x['tool'], toc, body, CTA, fh)
        page(x['slug'], x['title'], x['desc'], b, schema=app + fs,
             crumbs=[('Outils', 'outils/'), (x['short'], x['slug'])], cls='guide', og=ogp)
    tcards = ''.join(('<a class="gcard t-%s" href="{R}%s"><span class="gcard-e" aria-hidden="true">%s</span>'
                      '<strong>%s</strong><span class="gcard-d">%s</span></a>') % (x['tint'], x['slug'], x['emoji'], esc(x['h1']), esc(x['desc'])) for x in TOOLS)
    page('outils/', 'Outils gratuits mariage : rétroplanning, budget, liste', "Outils gratuits pour organiser votre mariage : rétroplanning personnalisé, calculateur de budget et nombre d'articles pour votre liste de mariage.",
         '<section class="wrap pagehead"><h1>Outils gratuits pour futurs mariés</h1><p class="lead">Rétroplanning, budget et taille de la liste : organisez votre mariage en quelques clics.</p></section><section class="wrap block"><div class="grid3">' + tcards + '</div></section>',
         crumbs=[('Outils', 'outils/')], og=ogfor('outils', 'Outils gratuits pour futurs mariés', 'Gratuit', '🧰', 'menthe'))

    # Compte


    # Pages légales
    ml = f'''<div class="wrap art-wrap"><article class="prose"><h1>Mentions légales</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay, France. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub Inc., 88 Colin P Kelly Jr St, San Francisco, CA 94107, États-Unis.</p>
<h2>Affiliation</h2><p>{DISCLOSURE} Les liens vers Amazon.fr sont des liens d'affiliation : si vous achetez après avoir cliqué, nous touchons une commission, sans surcoût pour vous. Le choix des articles reste indépendant.</p>
<h2>Responsabilité</h2><p>Les conseils de ce site sont donnés à titre informatif. Les conditions des offres Amazon peuvent changer à tout moment.</p></article></div>'''
    page('a-propos/', 'À propos | ' + SITE, "Qui écrit " + SITE + ", d'où viennent nos conseils et comment le site est financé.", f'''<div class="wrap art-wrap"><article class="prose"><h1>À propos</h1>
<p>Ma liste mariage aide les futurs mariés à composer leur liste de mariage et leurs invités à choisir un cadeau : guides, idées et outils gratuits. Le site est édité par Jérémy Dacier-Jury.</p>
<h2>Qui écrit</h2><p>Les guides sont rédigés et relus par Jérémy, avec l'aide d'outils de rédaction. Chaque page indique sa date de mise à jour.</p>
<h2>Notre méthode</h2><ul><li><strong>Des critères de choix expliqués</strong> pour chaque article : sécurité, normes, usage réel, entretien.</li>
<li><strong>Pas de faux tests</strong> : nous ne testons pas tous les produits nous-mêmes. Les sélections s'appuient sur les fiches des fabricants, les normes et les avis d'utilisateurs.</li>
<li><strong>Aucun prix inventé</strong> : les prix changent, nous renvoyons vers la fiche du produit.</li>
<li><strong>Des corrections rapides</strong> : une erreur ? Écris-nous à <a href="mailto:{CONTACT}">{CONTACT}</a>.</li></ul>
<h2>Comment le site est financé</h2><p>{DISCLOSURE} Si tu achètes après avoir cliqué sur un lien Amazon, nous touchons une commission, sans surcoût pour toi. Le choix des articles reste indépendant.</p></article></div>''', crumbs=[('À propos', 'a-propos/')])
    page('mentions-legales/', 'Mentions légales | Ma liste mariage', 'Mentions légales du site Ma liste mariage.', ml, crumbs=[('Mentions légales', 'mentions-legales/')])
    cf = f'''<div class="wrap art-wrap"><article class="prose"><h1>Confidentialité</h1>
<p>La checklist fonctionne sans inscription. Aucun compte n'est nécessaire.</p>
<h2>Votre checklist</h2><p>Les articles que vous cochez sont enregistrés uniquement dans votre navigateur (stockage local). Rien n'est envoyé sur un serveur. Vider les données du navigateur efface votre checklist.</p>
<h2>Mesure d'audience</h2><p>Nous comptons les pages vues et les clics vers Amazon de façon anonyme : page visitée, site d'origine, type d'appareil (mobile ou ordinateur) et un identifiant aléatoire stocké dans votre navigateur. Ces données ne permettent pas de vous identifier, ne sont ni vendues ni utilisées pour de la publicité, et sont hébergées par Supabase dans l'Union européenne.</p>
<h2>Amazon</h2><p>Quand vous cliquez sur un lien vers Amazon.fr, Amazon peut déposer des cookies pour attribuer la commission. Consultez la politique de confidentialité d'Amazon pour en savoir plus.</p>
<h2>Contact</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p></article></div>'''
    page('confidentialite/', 'Confidentialité | Ma liste mariage', 'Politique de confidentialité de Ma liste mariage : checklist sans inscription, sans inscription ni compte.', cf, crumbs=[('Confidentialité', 'confidentialite/')])

    # 404
    page('404-tmp/', 'Page introuvable | Ma liste mariage', 'Page introuvable.',
         '<div class="wrap art-wrap prose"><h1>Page introuvable</h1><p>Cette page n\'existe pas ou a changé d\'adresse. <a href="/checklist/">Ouvrez la checklist</a> ou revenez à <a href="/">l\'accueil</a>.</p></div>')
    shutil.move(os.path.join(OUT, '404-tmp', 'index.html'), os.path.join(OUT, '404.html'))
    shutil.rmtree(os.path.join(OUT, '404-tmp')); PAGES.remove('404-tmp/')
    with open(os.path.join(OUT, '404.html'), encoding='utf-8') as f: t = f.read()
    with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
        f.write(t.replace('href="../', 'href="' + PATH0).replace('src="../', 'src="' + PATH0).replace('href="/checklist/', 'href="' + PATH0 + 'checklist/').replace('href="/">', 'href="' + PATH0 + '">').replace('<head>', '<head>\n<meta name="robots" content="noindex">')
            .replace('<link rel="canonical" href="' + BASE + '/404-tmp/">\n', ''))

    # sitemap, robots, CNAME
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(
        '<url><loc>%s/%s</loc><lastmod>2026-11-14</lastmod></url>\n' % (BASE, p) for p in PAGES) + '</urlset>\n'
    open(os.path.join(OUT, 'sitemap.xml'), 'w').write(sm)
    open(os.path.join(OUT, 'robots.txt'), 'w').write('User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % BASE)
    # llms.txt : résumé du site pour les IA (généré à chaque build)
    try:
        import html as _h
        _out = ['# ' + SITE, '', '> ' + LLMS_INTRO, '', 'Site : ' + BASE + '/', 'Langue : français', '', '## Pages']
        for _loc in re.findall(r'<loc>([^<]+)</loc>', sm):
            _rel = _loc[len(BASE):].strip('/')
            _f = os.path.join(OUT, _rel, 'index.html') if _rel else os.path.join(OUT, 'index.html')
            if not os.path.exists(_f): continue
            _t = open(_f, encoding='utf-8').read()
            _ti = re.search(r'<title>(.*?)</title>', _t, re.S)
            _de = re.search(r'<meta name="description" content="([^"]*)"', _t)
            if not _ti or 'http-equiv="refresh"' in _t: continue
            _out.append('- [%s](%s)%s' % (_h.unescape(_ti.group(1)).strip(), _loc, (': ' + _h.unescape(_de.group(1)).strip()) if _de else ''))
        open(os.path.join(OUT, 'llms.txt'), 'w', encoding='utf-8').write('\n'.join(_out) + '\n')
    except Exception as _e:
        print('llms.txt non généré :', _e)
    cn = os.path.join(OUT, 'CNAME')
    if CUSTOM: open(cn, 'w').write(DOMAIN + '\n')
    elif os.path.exists(cn): os.remove(cn)
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    open(os.path.join(OUT, 'da4540821acf4048569bad7fbedc3ee1.txt'), 'w').write('da4540821acf4048569bad7fbedc3ee1')
    print(len(PAGES), 'pages,', total, 'articles')

if __name__ == '__main__':
    build()

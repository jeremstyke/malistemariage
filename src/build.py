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

def page(path, title, desc, body, schema=None, crumbs=None, extra_head='', cls='', noindex=False, og=None):
    depth = path.count('/')
    R = '../' * depth
    url = BASE + '/' + path
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": SITE, "url": BASE + '/'}]
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
<link rel="icon" href="{R}assets/favicon.svg" type="image/svg+xml">
{FONTS.replace('@R@', R)}
<link rel="stylesheet" href="{R}assets/style.css?v=15">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{extra_head}</head>
<body class="{cls}">
<a class="skip" href="#main">Aller au contenu</a>
<header class="top"><div class="wrap top-in">
<a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">💍</span>Ma liste mariage</a>
<nav class="menu" aria-label="Menu">{nav}</nav>
<a id="nav-account" class="nav-acc" href="{R}compte/"><span class="acc-ico" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16"><circle cx="12" cy="8" r="4" fill="currentColor"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7" fill="currentColor"/></svg></span><span id="nav-account-txt">Connexion</span></a>
</div></header>
<main id="main">
{('<div class="wrap">' + bc + '</div>') if bc else ''}
{body.replace('{R}', R)}
</main>
<div class="wave-foot"><svg class="wave" viewBox="0 0 1440 60" preserveAspectRatio="none" aria-hidden="true"><path d="M0 30 C 240 70 480 0 720 25 C 960 50 1200 10 1440 30 L1440 60 L0 60 Z"/></svg></div><footer class="foot"><div class="wrap foot-in">
<div><a class="logo" href="{R}"><span class="logo-ico" aria-hidden="true">💍</span>Ma liste mariage</a>
<p>La checklist gratuite pour composer votre liste de mariage, pièce par pièce.</p></div>
<nav aria-label="Pied de page"><a href="{R}checklist/">Checklist</a><a href="{R}guides/">Guides</a><a href="{R}outils/">Outils</a><a href="{R}mentions-legales/">Mentions légales</a><a href="{R}confidentialite/">Confidentialité</a><a href="mailto:{CONTACT}">Contact</a></nav>
<p class="wed">🍼 Un bébé en route ? <a href="{BABY_SITE}">Préparez votre liste de naissance sur Ma liste bébé</a></p>
<p class="disc">{DISCLOSURE} Les prix et les conditions d'Amazon peuvent changer : vérifiez-les avant d'acheter. © {YEAR} {DOMAIN}</p>
</div></footer>
<script src="{R}assets/account.js?v=5" defer></script>
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
        data.append({"c": cat, "e": emo, "i": [{"n": n, "u": amz(q), "p": p, "t": t} for n, q, p, t in items]})
    total = sum(len(c['i']) for c in data)
    js = 'window.LDN_DATA=' + json.dumps(data, ensure_ascii=False) + ';window.LDN_PRIO=' + json.dumps({str(k): v for k, v in PRIO.items()}, ensure_ascii=False) + ';window.LDN_LIST=' + json.dumps(AMZ_LIST) + ';window.LDN_TAG=' + json.dumps(TAG) + ';'
    with open(os.path.join(OUT, 'assets', 'data.js'), 'w', encoding='utf-8') as f:
        f.write(js)

    tool = ('<div id="ck" class="ck"><noscript>Active JavaScript pour cocher les articles.</noscript></div>'
            '<script src="{R}assets/data.js?v=3"></script><script src="{R}assets/checklist.js?v=5" defer></script>')

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
<div class="save-hint" data-guest><span aria-hidden="true">☁️</span><div><strong>Sauvegardez votre liste</strong><span>Connectez-vous par e-mail, sans mot de passe : votre checklist vous suit sur tous vos appareils, à deux, et vous pouvez la partager à vos invités.</span></div><a class="btn sm" href="{{R}}compte/">Me connecter</a></div>
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
<div class="wrap"><p class="ck-first">Pas encore de liste ? <a href="{AMZ_LIST}" rel="sponsored nofollow noopener" target="_blank">Créez d'abord votre liste de mariage sur Amazon</a> (gratuit), puis remplissez-la ici article par article.</p></div>
<div class="wrap"><div class="save-hint" data-guest><span aria-hidden="true">☁️</span><div><strong>Sauvegardez votre liste</strong><span>Connectez-vous par e-mail, sans mot de passe : votre checklist vous suit sur tous vos appareils, à deux, et vous pouvez la partager à vos invités.</span></div><a class="btn sm" href="{{R}}compte/">Me connecter</a></div>
{tool}
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
        body = (x['body'] + ex_html).replace('{CTA}', CTA).replace('{PRINTLIST}', PRINTLIST).replace('{MSGS}', messages_html())
        body = re.sub(r'\{AMZ:([^}]+)\}', lambda m: amz(m.group(1)), body)
        body, toc = add_toc(body)
        words = len(re.sub('<[^>]+>', ' ', body).split())
        mins = max(2, round(words / 200))
        e, t = META.get(x['slug'], ('📄', 'ciel'))
        ogp = ogfor(x['slug'].strip('/'), x['h1'], 'Guide', e, t)
        art = [{"@context": "https://schema.org", "@type": "Article", "headline": x['h1'], "description": x['desc'],
                "inLanguage": "fr-FR", "datePublished": "2026-11-14", "dateModified": "2026-11-14",
                "author": {"@type": "Organization", "name": SITE, "url": BASE + '/'}, "publisher": {"@type": "Organization", "name": SITE, "url": BASE + '/'}, "image": BASE + '/' + ogp, "mainEntityOfPage": BASE + '/' + x['slug']}]
        b = ('<header class="cover t-%s"><span class="cover-dots" aria-hidden="true"></span><div class="wrap cover-in"><span class="cover-e" aria-hidden="true">%s</span>'
             '<div><h1>%s</h1><p class="cover-d">%s</p><p class="cover-m">%d min de lecture, mis à jour en novembre %d</p></div></div></header>'
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
    acc = """<div class="wrap art-wrap"><div class="prose" id="acc">
<h1>Notre compte</h1>
<div id="acc-out">
<p class="lead">Votre compte est gratuit et se crée en 10 secondes, sans mot de passe.</p>
<ul class="perks">
<li><span aria-hidden="true">☁️</span><div><strong>Votre liste sauvegardée</strong>Ce que vous cochez n'est jamais perdu, même si vous changez de téléphone.</div></li>
<li><span aria-hidden="true">💑</span><div><strong>À deux, sur tous vos appareils</strong>Connectez-vous chacun avec le même e-mail et préparez la liste ensemble.</div></li>
<li><span aria-hidden="true">💌</span><div><strong>Partagée avec vos invités</strong>Un lien privé montre à vos proches les cadeaux choisis, prêts à offrir.</div></li>
<li><span aria-hidden="true">🍼</span><div><strong>Le même compte que Ma liste bébé</strong>Une seule adresse e-mail pour vos deux listes, le jour où un bébé arrive.</div></li>
</ul>
<form id="form-magic" class="accf">
<label>Votre e-mail<input type="email" name="email" autocomplete="email" required></label>
<label class="check"><input type="checkbox" name="news"> Je veux recevoir la newsletter de Ma liste mariage : conseils et rappels pour préparer la liste et les remerciements (désinscription en un clic).</label>
<button class="btn" type="submit">Recevoir mon lien de connexion</button>
<p class="small">Si vous n'avez pas encore de compte, il est créé automatiquement. En continuant, vous acceptez notre <a href="{R}confidentialite/">politique de confidentialité</a>.</p>
</form>
<div id="acc-sent" hidden><h2>Regardez vos e-mails 📬</h2><p>Nous vous avons envoyé un lien de connexion. Ouvrez-le sur cet appareil pour vous connecter. Pensez à vérifier les indésirables.</p><button class="linkbtn" type="button" id="acc-again">Utiliser une autre adresse</button></div>
</div>
<div id="acc-in" hidden>
<p class="lead">Connecté avec <strong id="acc-email"></strong>. Votre checklist est sauvegardée : <strong id="acc-count"></strong>.</p>
<p><a class="btn" href="{R}checklist/">Ouvrir ma checklist</a></p>
<h2>Notre liste à partager</h2>
<form id="form-wed" class="accf">
<label>Vos prénoms (facultatif)<input type="text" id="f-names" maxlength="60" placeholder="Léa et Hugo"></label>
<label>Date du mariage (facultatif)<input type="date" id="f-date"></label>
<label class="check"><input type="checkbox" id="f-public"> Rendre notre liste visible avec un lien privé</label>
<label class="check"><input type="checkbox" id="f-news"> Recevoir la newsletter (conseils et rappels)</label>
<button class="btn" type="submit">Enregistrer</button>
</form>
<div id="acc-sharebox" hidden><p>Envoyez ce lien à vos invités : ils voient les cadeaux que vous avez cochés, avec les liens pour les offrir.</p>
<div class="sharerow"><input id="acc-share" readonly><button class="btn ghost sm" type="button" id="acc-copy">Copier le lien</button></div></div>
<div id="acc-other" class="save-hint" hidden></div>
<h2>Mon compte</h2>
<p><button class="btn ghost sm" type="button" id="acc-logout">Se déconnecter</button> <button class="btn ghost sm" type="button" id="acc-wipe">Supprimer mes données</button></p>
</div>
<p id="acc-msg" class="acc-msg" role="status" aria-live="polite"></p>
</div></div>"""
    page('compte/', 'Notre compte | Ma liste mariage', 'Connectez-vous par e-mail, sans mot de passe, pour sauvegarder votre liste de mariage et la partager.', acc, noindex=True)

    pub = """<section class="wrap pagehead"><h1 id="pub-title">Une liste de mariage</h1>
<p class="lead">Voici les cadeaux choisis par les mariés. Cliquez sur un article pour l'offrir.</p></section>
<div class="wrap"><div id="pub" class="ck"><p>Chargement de la liste...</p></div>
<div class="prose"><p>Vous aussi, vous vous mariez ? <a href="{R}checklist/">Faites votre checklist gratuite</a>.</p></div></div>
<script src="{R}assets/data.js?v=3"></script>"""
    page('ma-liste/', 'Notre liste de mariage 💍', 'Voici les cadeaux choisis par les mariés. Cliquez sur un article pour l\'offrir.', pub, noindex=True, cls='tool', og=ogfor('ma-liste', 'Notre liste de mariage', 'Cliquez pour offrir un cadeau', '🎁', 'peche'))

    # Pages légales
    ml = f'''<div class="wrap art-wrap"><article class="prose"><h1>Mentions légales</h1>
<h2>Éditeur</h2><p>Jérémy Dacier-Jury, 9 passage des Tisserands, 38790 Charantonnay, France. Contact : <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>Hébergement</h2><p>GitHub Pages, GitHub Inc., 88 Colin P Kelly Jr St, San Francisco, CA 94107, États-Unis.</p>
<h2>Affiliation</h2><p>{DISCLOSURE} Les liens vers Amazon.fr sont des liens d'affiliation : si vous achetez après avoir cliqué, nous touchons une commission, sans surcoût pour vous. Le choix des articles reste indépendant.</p>
<h2>Responsabilité</h2><p>Les conseils de ce site sont donnés à titre informatif. Les conditions des offres Amazon peuvent changer à tout moment.</p></article></div>'''
    page('mentions-legales/', 'Mentions légales | Ma liste mariage', 'Mentions légales du site Ma liste mariage.', ml, crumbs=[('Mentions légales', 'mentions-legales/')])
    cf = f'''<div class="wrap art-wrap"><article class="prose"><h1>Confidentialité</h1>
<p>La checklist fonctionne sans inscription. Le compte est facultatif.</p>
<h2>Sans compte</h2><p>Les articles que vous cochez sont enregistrés uniquement dans votre navigateur (stockage local). Rien n'est envoyé sur un serveur. Vider les données du navigateur efface votre checklist.</p>
<h2>Avec un compte</h2><p>Si vous créez un compte, nous enregistrons votre adresse e-mail (pour vous envoyer vos liens de connexion), les articles cochés et, si vous les indiquez, vos prénoms et la date du mariage. Ce compte est commun avec notre site Ma liste bébé. Si vous avez coché la case newsletter, votre e-mail sert aussi à vous envoyer nos conseils ; vous pouvez vous désinscrire à tout moment depuis la page compte ou avec le lien présent dans chaque e-mail. Les données sont hébergées par Supabase, sur des serveurs situés dans l'Union européenne. Nous ne les vendons pas et ne les utilisons pas pour de la publicité.</p>
<p>Votre liste n'est visible par d'autres personnes que si vous activez le partage : elle n'est alors accessible qu'avec son lien. Vous pouvez supprimer vos données à tout moment depuis la page compte, et demander la suppression complète de votre compte en nous écrivant.</p>
<h2>Amazon</h2><p>Quand vous cliquez sur un lien vers Amazon.fr, Amazon peut déposer des cookies pour attribuer la commission. Consultez la politique de confidentialité d'Amazon pour en savoir plus.</p>
<h2>Contact</h2><p><a href="mailto:{CONTACT}">{CONTACT}</a></p></article></div>'''
    page('confidentialite/', 'Confidentialité | Ma liste mariage', 'Politique de confidentialité de Ma liste mariage : checklist sans inscription, compte facultatif.', cf, crumbs=[('Confidentialité', 'confidentialite/')])

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
    cn = os.path.join(OUT, 'CNAME')
    if CUSTOM: open(cn, 'w').write(DOMAIN + '\n')
    elif os.path.exists(cn): os.remove(cn)
    open(os.path.join(OUT, '.nojekyll'), 'w').write('')
    print(len(PAGES), 'pages,', total, 'articles')

if __name__ == '__main__':
    build()

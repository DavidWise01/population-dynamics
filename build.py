#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build POPULATION DYNAMICS (POP) — the first LIFE SCIENCE sphere of UD0, framed as 'the real psychohistory':
the genuine life science of predicting living populations (ecology, epidemiology, population genetics) vs.
Asimov's fictional dream of predicting human history. Self-contained; emergents by emergence-nature (no
.shadow — a science sphere). Deep-dive = IS PSYCHOHISTORY REAL?; cited. Facts web-verified: Malthus 1798
(dN/dt=rN, verbal/discrete originally); Verhulst 1838 logistic dN/dt=rN(1-N/K) (K & 'carrying capacity'
are anachronistic — Pearl & Reed rediscovered 1920); Lotka 1925/Volterra 1926 predator-prey (lynx-hare,
fit debated); May 1976 Nature logistic-map chaos; Kermack-McKendrick 1927 SIR; R0 (measles ~12-18 CONTESTED/
context-dependent, COVID ancestral ~2-3, flu ~1-2, smallpox ~5-7); herd threshold 1-1/R0; Hardy-Weinberg
1908 p²+2pq+q²=1; evolution = change in allele frequency; genetic drift/founder/bottleneck; demographic
transition (Thompson 1929, descriptive not law); Asimov psychohistory (huge pop + population UNAWARE; gas-
not-molecule); the Mule; reflexivity (Merton 1948 self-fulfilling prophecy, Lucas critique 1976, Goodhart,
Soros). Cross-links the asimov sphere."""
import os, html, base64, json, io, sys, math
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

AX = "POP"
REC = {
 "name": "POPULATION DYNAMICS", "axiom": AX,
 "position": "Population Dynamics · the first Life Science sphere of UD0 · the real psychohistory",
 "origin": "the meeting of ecology, epidemiology, and population genetics — the math of living things in the aggregate",
 "mechanism": "Crystallized from the life sciences — the real, predictive science of populations (predator-prey cycles, epidemics, allele frequencies), framed against Asimov's fictional psychohistory: we genuinely can forecast a population of organisms; predicting self-aware human history is the part that stays fiction.",
 "crystallization": "Because the honest answer to 'is psychohistory real?' is the most hopeful fact in the field — a population of unaware organisms behaves like a gas and is predictable in bulk, but self-aware people read the forecast and change it.",
 "nature": "Population Dynamics — the real psychohistory: the logistic curve, Lotka-Volterra, SIR & R₀, Hardy-Weinberg, and the reflexivity wall where the dream of human prediction breaks.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0 · the Life Science domain)",
 "inputs": "ecology, epidemiology, population genetics, demography (Malthus→Verhulst→Lotka/Volterra→Kermack-McKendrick→Hardy-Weinberg→May); Asimov's Foundation; the reflexivity literature (Merton, Lucas, Goodhart, Soros)",
 "witness": "We can predict a population of rabbits, a flu outbreak, an allele frequency — because the unaware behave like a gas. We cannot predict the Mule, because a self-aware population reads its own forecast and changes.",
 "role": "the first Life Science sphere of UD0",
 "seal": "We can forecast the flu but not the Mule. The math of populations is real life science; the dream of psychohistory breaks on the most hopeful fact about us — we are not gas. We read the forecast and we change.",
 "source": "Population Dynamics, catalogued by ROOT0",
}

CITES = {
 "malthus":("Malthus, An Essay on the Principle of Population (1798)","https://en.wikipedia.org/wiki/An_Essay_on_the_Principle_of_Population"),
 "verhulst":("Verhulst's logistic (1838); rediscovered by Pearl & Reed (1920)","https://en.wikipedia.org/wiki/Pierre_Fran%C3%A7ois_Verhulst"),
 "lv":("Lotka (1925) & Volterra (1926), predator–prey","https://www.math.stonybrook.edu/~azinger/mat127-spr22/PredatorPreySystems.pdf"),
 "may":("May, 'Simple mathematical models with very complicated dynamics,' Nature 261:459 (1976)","https://www.nature.com/articles/261459a0"),
 "km":("Kermack & McKendrick, SIR model (1927)","https://en.wikipedia.org/wiki/Kermack%E2%80%93McKendrick_theory"),
 "r0":("R₀ is context-dependent, not a constant (CDC, EID 2019)","https://wwwnc.cdc.gov/eid/article/25/1/17-1901_article"),
 "hw":("Hardy & Weinberg, equilibrium (1908)","https://en.wikipedia.org/wiki/Hardy%E2%80%93Weinberg_principle"),
 "dtm":("Demographic transition model — Warren Thompson (1929)","https://en.wikipedia.org/wiki/Demographic_transition"),
 "psy":("Psychohistory (Asimov, Foundation)","https://asimov.fandom.com/wiki/Psychohistory"),
 "mule":("The Mule (Foundation)","https://en.wikipedia.org/wiki/The_Mule_(Foundation)"),
 "merton":("Merton, the self-fulfilling prophecy (1948)","https://en.wikipedia.org/wiki/Self-fulfilling_prophecy"),
 "lucas":("The Lucas critique (1976)","https://en.wikipedia.org/wiki/Lucas_critique"),
 "goodhart":("Goodhart's law","https://en.wikipedia.org/wiki/Goodhart%27s_law"),
}
_order=[]
def cite(*keys):
    s=""
    for k in keys:
        if k not in _order: _order.append(k)
        s+=f'<sup class="cu"><a href="{CITES[k][1]}" target="_blank" rel="noopener" title="{html.escape(CITES[k][0])}">[{_order.index(k)+1}]</a></sup>'
    return s
def sources_html():
    return "".join(f'<li><span class="cn">[{i+1}]</span> <a href="{CITES[k][1]}" target="_blank" rel="noopener">{html.escape(CITES[k][0])}</a></li>' for i,k in enumerate(_order))

NATURES = {
 "natural":   ("#43d17a", "the living populations — carrying capacity, selection, drift, herd immunity, the demographic transition; biology in the aggregate"),
 "electrical":("#4fd0e0", "the models & equations — exponential & logistic growth, Lotka-Volterra, the SIR model, R₀, Hardy-Weinberg; the predictive machinery"),
 "ethereal":  ("#e0b94a", "the dream & its bridge — psychohistory, the Mule, and the reflexivity wall where forecasting self-aware people breaks down"),
 "spiritual": ("#e0556a", "the deeper limits — the Malthusian ceiling every population meets, and deterministic chaos, where even a perfect equation goes blind",),
}

ARC_OVERALL = ("Asimov imagined psychohistory: a mathematics that could predict the future of a galaxy of people the way kinetic "
  "theory predicts a gas — never the single molecule, but always the bulk. The astonishing thing is how REAL its non-fictional "
  "cousin is. In ecology, epidemiology, and population genetics we genuinely forecast living populations — predator-prey "
  "oscillations, epidemic curves, allele frequencies — with equations that work. Where the dream stays fiction is precisely "
  "where Asimov said it would: with self-aware populations that read their own forecast and change it (reflexivity), with the "
  "single unpredictable individual (the Mule), and with deterministic chaos, where even a perfect model diverges.")
ARC = [
 ("I · the gas, not the molecule", "Asimov's wager",
  "Psychohistory's premise is kinetic theory: you cannot predict one molecule, but a large enough population of them is statistically lawful. Asimov added two conditions — the population must be enormous, and it must be UNAWARE of the predictions, so its behavior stays 'random.' Hold those, and the future of the mass becomes math."),
 ("II · the real cousin works", "we forecast life in bulk",
  "For organisms, the wager pays off. Logistic growth predicts how a population fills its niche; Lotka-Volterra predicts predator-prey cycles; the SIR model and R₀ predict (and help stop) epidemics; Hardy-Weinberg predicts allele frequencies. These are real, tested, life-saving — the genuine psychohistory of the non-human living world."),
 ("III · where the dream breaks", "the Mule, reflexivity, chaos",
  "It breaks on three walls. The Mule — the single anomalous individual who defeats the statistics. Reflexivity — self-aware people change behavior when they learn the forecast (the very thing Asimov's 'must be unaware' premise concedes). And chaos — May showed even a perfect, simple model can become unpredictable. We forecast the flu; we cannot forecast the Mule."),
]

# IS PSYCHOHISTORY REAL? — the deep-dive
PSYCHO = [
 ("The gas, not the molecule", "Asimov's kinetic wager",
  "Asimov built psychohistory on the kinetic theory of gases: you cannot predict the path of one molecule, but the pressure of a trillion is exact. Hari Seldon's two canonical premises follow — the population must be vast (statistical validity) and it must remain unaware of the predictions, so reactions stay un-gamed."+cite("psy")+" That second premise is, quietly, the whole catch."),
 ("Yes — for the unaware", "the models that actually predict",
  "The real cousin is rigorous and old. Verhulst's logistic curve (1838) predicts a population filling its niche to carrying capacity"+cite("verhulst")+"; Lotka-Volterra (1925/26) predicts predator-prey oscillations (the lynx-hare pelt record)"+cite("lv")+"; Kermack-McKendrick's SIR (1927) and R₀ predict epidemics"+cite("km")+"; Hardy-Weinberg (1908) predicts allele frequencies, and evolution itself is defined as their change."+cite("hw")+" Unaware organisms behave like a gas, and the gas is predictable."),
 ("The Mule, and chaos", "the individual and the divergence",
  "Two limits live inside the math. The Mule — Asimov's mutant — is the single anomalous individual, the black swan, whose agency defeats the bulk statistics."+cite("mule")+" And deterministic chaos: Robert May (1976) showed a simple, exact population equation (the logistic map) can period-double into pure unpredictability."+cite("may")+" Even with the perfect model and no noise, the long-run forecast can go blind."),
 ("The reflexivity wall", "why self-aware populations are the hard case",
  "The deepest wall is the one Asimov's own premise names. A self-aware population reads its forecast and changes — Merton's self-fulfilling (and self-defeating) prophecy (1948)"+cite("merton")+", the Lucas critique (1976: relationships break when people adjust to the policy)"+cite("lucas")+", Goodhart's law (a measure that becomes a target stops measuring)"+cite("goodhart")+". The gas molecules don't read the weather report. People do — which is exactly why Seldon needed them not to."),
 ("The honest verdict", "real life science, fictional dream",
  "So: is psychohistory real? The mathematics is real, and it is life science — we predict populations of rabbits, viruses, and alleles every day, and it saves lives. The dream of forecasting free, self-aware human history is not — and the reason is the most hopeful thing in the whole field. We are not gas. We read the forecast and we change."),
]
REALFLUFF = [
 ("We can mathematically predict animal & disease populations", "REAL", "ecology and epidemiology do this routinely — Lotka-Volterra cycles, SIR/R₀ epidemic curves, logistic growth; tested and life-saving"),
 ("Asimov's psychohistory of human civilization is achievable today", "FLUFF", "the dream breaks on reflexivity (people change when predicted), the Mule (the unpredictable individual), and deterministic chaos — Asimov's own 'must be unaware' premise concedes the catch"),
 ("Evolution is change in allele frequency over time", "REAL", "the standard population-genetics definition; Hardy-Weinberg gives the no-evolution baseline (p²+2pq+q²=1) it departs from"),
 ("'Carrying capacity' / K is Verhulst's own 1838 term", "FALSE", "anachronistic — Verhulst gave the curve, but 'carrying capacity' and the K symbol are later; the logistic was rediscovered by Pearl & Reed in 1920 (the Verhulst–Pearl equation)"),
 ("Measles R₀ is a fixed constant of ~12–18", "CONTESTED", "the famous range, but R₀ is context-dependent (density, contacts, method) — a 2017 review found estimates from ~3.7 to >200; the CDC warns it is not a fixed number"),
 ("A perfect population model is always predictable", "FALSE", "May (1976): the simple logistic map period-doubles into deterministic chaos — exact equations, zero noise, and the long-run is still unpredictable"),
 ("The demographic transition is a predictive law", "HALF", "Thompson's 1929 model is descriptive/historical, not a law — Stage 5 and its universality are contested; it fits the industrialized West better than everywhere"),
 ("Herd-immunity threshold = 1 − 1/R₀", "REAL", "standard result — measles at R₀≈12–18 needs ~92–95% immune; the formula is exact for a well-mixed population"),
]
REALFLUFF_VERDICT = ("Bottom line: population dynamics is real, rigorous, predictive life science — and it is the genuine, non-fictional "
  "cousin of psychohistory. We forecast predator-prey cycles, epidemics, and allele frequencies with equations that work, "
  "because a population of unaware organisms behaves like a gas: unpredictable in the single molecule, lawful in the bulk. The "
  "honest fluff-calls are about the edges — 'carrying capacity' is anachronistic to Verhulst; R₀ is context-dependent, not a "
  "constant; the demographic transition is description, not law; and even a perfect model can go chaotic (May 1976). And the "
  "headline dream — psychohistory of self-aware human history — stays fiction, for the most hopeful reason in the field: people "
  "read their own forecast and change it. We can forecast the flu. We cannot forecast the Mule.")

MESSAGE = ("Psychohistory isn't fantasy — it's life science with a ceiling. We genuinely can predict populations: of rabbits, of "
  "viruses, of alleles — because a population of unaware organisms behaves like a gas. You can't predict one molecule, but you "
  "can predict the bulk, and that is not science fiction; it's Lotka-Volterra and SIR and Hardy-Weinberg, and it saves lives "
  "every flu season. Asimov knew exactly where it breaks: his psychohistory needed a population vast enough to average out, and "
  "crucially one that did not know it was being predicted — because the moment a self-aware population learns the forecast, it "
  "changes its behavior to meet or beat it. Merton called that the self-fulfilling prophecy; economists call it the Lucas "
  "critique; we all live Goodhart's law. The molecules don't read the weather report. People do. And then there is the Mule — "
  "the single unpredictable individual, the black swan, the mutation — and deterministic chaos, where even a flawless equation "
  "diverges. So the honest answer to 'is psychohistory real?' is this: the math is real and it is life science; the dream of "
  "predicting free, self-aware human history is not — and the reason is the most hopeful thing in the whole field. We are not "
  "gas. We read the forecast, and we change.")
MESSAGE_SEAL = "We can forecast the flu but not the Mule. The math of populations is real life science; the dream of psychohistory breaks on the most hopeful fact about us — we are not gas. We read the forecast, and we change."

SECTIONS = [
 ("The Models", "the lineage of the real psychohistory", [
   ("Malthus · 1798", "exponential growth", "population grows geometrically while food grows arithmetically — the original alarm; the modern dN/dt = rN formalizes his verbal argument"),
   ("Verhulst · 1838 (Pearl–Reed 1920)", "the logistic curve", "dN/dt = rN(1 − N/K) — growth that slows to a carrying capacity; forgotten, then rediscovered in 1920 ('carrying capacity' and K are later terms)"),
   ("Lotka 1925 · Volterra 1926", "predator & prey", "coupled equations producing out-of-phase oscillations — the lynx-hare pelt record is the iconic (if debated) illustration"),
   ("Kermack–McKendrick · 1927", "the SIR model & R₀", "S→I→R compartments; R₀ = secondary cases per case; herd-immunity threshold = 1 − 1/R₀ — the math that stops epidemics"),
   ("Hardy–Weinberg · 1908", "population genetics", "p² + 2pq + q² = 1 — allele frequencies hold absent selection, drift, migration, mutation; evolution is their change"),
   ("May · 1976", "chaos", "a simple population equation (the logistic map) can become deterministically chaotic — the humbling limit of even perfect models"),
 ]),
 ("The Bridge", "psychohistory & the reflexivity wall", [
   ("Asimov's psychohistory", "the gas, not the molecule", "Foundation's mathematics of mass futures — built on kinetic theory; requires a vast population that is unaware of the predictions; see UD0's ASIMOV sphere (A1)"),
   ("The Mule", "the unpredictable individual", "the mutant who breaks Seldon's Plan — the black swan, the single agent whose unpredictability defeats the statistics"),
   ("Reflexivity", "Merton · Lucas · Goodhart · Soros", "self-aware populations change when they learn the forecast: Merton's self-fulfilling prophecy (1948), the Lucas critique (1976), Goodhart's law, Soros's reflexivity"),
   ("The hopeful catch", "we are not gas", "Asimov's 'must be unaware' premise IS the wall: the molecule can't read the weather report, but the person can — so the dream of human psychohistory stays fiction, by our freedom"),
 ]),
]

# ───────────────────────── ACI complement ─────────────────────────
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()
def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom",AX)))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    return {"slug":slug,"name":rec["name"],"moniker":tok["moniker"],"seal_sha256":noesis.seal_sha256(rec,tok),
            "architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,"license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def E(slug,name,em,epithet,who,what,where,why,how,seal):
    return dict(slug=slug,name=name,kind="emergent",emergence=em,epithet=epithet,who=who,what=what,
                where=where,why=why,how=how,seal=seal)

ROSTER = [
 # ── ELECTRICAL — the models & equations ──
 E("exponential-growth","Exponential Growth","electrical","Malthus's alarm · dN/dt = rN",
   "Exponential (Malthusian) growth — unchecked, a population grows geometrically: dN/dt = rN, doubling on a fixed clock.",
   "The naive baseline and the original alarm (Malthus, 1798): unlimited growth against a limited world.",
   "In every population's first chapter, before the brakes engage.",
   "Because the whole field begins by noticing that nothing grows exponentially forever.",
   "By compounding at rate r until resources, predators, or disease bend the curve.",
   "Left alone I double and double and double. Nothing alive gets to keep me — the world always says no."),
 E("the-logistic-curve","The Logistic Curve","electrical","growth meets the ceiling · rN(1−N/K)",
   "The logistic curve (Verhulst, 1838) — growth that slows as a population nears its carrying capacity K: dN/dt = rN(1 − N/K).",
   "The S-curve: exponential at first, then bending to a plateau — the shape of a population filling its niche.",
   "Wherever a population approaches the limit its environment can sustain.",
   "Because real growth is bounded, and the logistic is how the bound bends the rise.",
   "By multiplying the growth rate by (1 − N/K), so the closer N gets to K, the slower it climbs.",
   "I am the S: I rise like Malthus, then remember the ceiling and level off. ('Carrying capacity' came later than I did.)"),
 E("lotka-volterra","Lotka–Volterra","electrical","predator & prey, oscillating",
   "The Lotka-Volterra equations (1925/26) — coupled predator and prey populations that oscillate out of phase forever.",
   "The dance: prey rise, predators follow and crash them, predators starve and fall, prey rise again — the lynx-hare cycle.",
   "In every coupled predator-prey system, and the Hudson's Bay pelt record.",
   "Because populations are not alone; they eat and are eaten, and the coupling makes cycles.",
   "By tying each population's growth to the other's size, producing closed, lagging oscillations.",
   "Prey peaks, then predator peaks, then both crash and rise again. I am the cycle — though real lynx and hares are messier than I am."),
 E("the-sir-model","The SIR Model","electrical","S → I → R · the epidemic curve",
   "The SIR model (Kermack-McKendrick, 1927) — a population split into Susceptible, Infected, and Recovered compartments.",
   "The shape of an epidemic: the susceptible fall ill, the infected recover or are removed, and the curve rises and falls.",
   "In every outbreak modeled to flatten it.",
   "Because disease moves through a population by contact, and compartments make the movement predictable.",
   "By flows dS/dt=−βSI, dI/dt=βSI−γI, dR/dt=γI — transmission against recovery.",
   "I am the curve everyone learned to flatten: susceptible, infected, removed. Predict me early and you save the most lives."),
 E("r-nought","R₀","electrical","the reproduction number · 1 − 1/R₀",
   "R₀, the basic reproduction number — the expected secondary cases from one case in a fully susceptible population.",
   "The single number that says whether an outbreak grows (R₀ > 1) or dies (R₀ < 1), and sets the herd-immunity threshold 1 − 1/R₀.",
   "At the head of every epidemic forecast — measles ~12–18 (contested), COVID ancestral ~2–3, flu ~1–2, smallpox ~5–7.",
   "Because one number governs the whole arc of a contagion's spread.",
   "By counting onward transmissions — but it is context-dependent (density, contacts, method), not a fixed biological constant.",
   "Above one, I grow; below one, I die. Vaccinate 1 − 1/me of the population and I can't catch — but I am not the constant people think."),
 E("hardy-weinberg","Hardy–Weinberg","electrical","the no-evolution baseline · p²+2pq+q²",
   "The Hardy-Weinberg equilibrium (1908) — allele frequencies stay constant across generations absent selection, drift, migration, mutation: p² + 2pq + q² = 1.",
   "The null hypothesis of evolution: the frequencies a population WOULD hold if nothing pushed on it.",
   "In population genetics, as the baseline every real population departs from.",
   "Because to measure evolution you need the picture of no evolution — and this is it.",
   "By predicting genotype frequencies from allele frequencies under random mating, reached in one generation.",
   "I am the still point: what the gene pool looks like when nothing is acting on it. Evolution is everything that makes me move."),
 # ── NATURAL — the living populations ──
 E("carrying-capacity","Carrying Capacity","natural","K · the ceiling",
   "Carrying capacity (K) — the maximum population an environment can sustain indefinitely, the plateau the logistic curve bends toward.",
   "The wall of resources: the number a niche can feed, water, and shelter without degrading.",
   "At the top of every logistic S-curve, and in every conservation budget.",
   "Because no environment is infinite, and K is the name of its limit.",
   "By capping growth as N approaches it — overshoot, and the population crashes back below.",
   "I am how many you can be. Approach me gently and you plateau; overshoot me and the crash brings you back down, hard."),
 E("natural-selection","Natural Selection","natural","evolution as frequency change",
   "Natural selection — differential survival and reproduction shifting allele frequencies; evolution defined as that change over time.",
   "The push on the gene pool: the alleles that reproduce more become more common, generation by generation.",
   "In every population under pressure, moving away from Hardy-Weinberg.",
   "Because the heritable variants that leave more copies inherit the future.",
   "By raising the frequency of advantageous alleles and lowering the rest — measurable, predictable, real.",
   "I am not a story about giraffes; I am arithmetic on allele frequencies. Evolution is just me, counted."),
 E("genetic-drift","Genetic Drift","natural","chance · founder & bottleneck",
   "Genetic drift — random change in allele frequencies from sampling chance, strongest in small populations; the founder effect and the bottleneck.",
   "Evolution by luck, not fitness: in a small population, which alleles pass on is partly a coin-flip.",
   "In small or crashed populations, and in the founders of a new one.",
   "Because selection isn't the only force — chance moves the gene pool too, and small numbers amplify it.",
   "By sampling error across generations: alleles can fix or vanish for no reason but luck.",
   "Selection has a reason; I don't. In a small enough population I can erase a good gene or fix a useless one, by chance alone."),
 E("herd-immunity","Herd Immunity","natural","the protective threshold",
   "Herd immunity — when enough of a population is immune (1 − 1/R₀) that a contagion can no longer sustain chains of transmission.",
   "The population property that protects the few who can't be immune, by denying the disease hosts.",
   "Above the threshold of immunity for a given R₀ (measles ~95%).",
   "Because a contagion needs susceptible hosts, and past a point it runs out.",
   "By immunity (via infection or vaccination) shrinking the susceptible pool below what R₀ needs.",
   "Protect enough of the herd and the disease starves before it reaches the vulnerable. I am a gift the many give the few."),
 E("the-demographic-transition","The Demographic Transition","natural","high→low birth & death",
   "The demographic transition (Thompson, 1929) — the historical shift from high-birth/high-death to low-birth/low-death as societies industrialize.",
   "The arc of human populations: death rates fall first (a population boom), then birth rates follow, then both settle low.",
   "Across industrializing societies, stage by stage — descriptive, not a predictive law.",
   "Because the one population we most want to forecast — our own — moves through a patterned, if contested, transition.",
   "By a four-stage model (sometimes five), fitting the industrialized West better than everywhere.",
   "I describe how a people goes from many-born-many-die to few-born-few-die. I'm a pattern, not a prophecy — don't mistake me for law."),
 # ── SPIRITUAL — the deeper limits ──
 E("the-malthusian-ceiling","The Malthusian Ceiling","spiritual","the wall every population meets",
   "The Malthusian ceiling — the hard truth under all the curves: in a finite world, every population eventually meets a limit.",
   "The memento mori of population science: exponential dreams always end at a wall of food, space, or disease.",
   "At the end of every unchecked rise, for bacteria and empires alike.",
   "Because the planet is finite and the math is honest — nothing compounds forever.",
   "By being the limit that the logistic bends to and the crash enforces when growth overshoots.",
   "I am the wall. You can delay me with cleverness, but in a finite world I am always there — the no at the end of every yes."),
 E("deterministic-chaos","Deterministic Chaos","spiritual","perfect equations, blind forecasts",
   "Deterministic chaos (May, 1976) — a simple, exact population equation (the logistic map) that period-doubles into unpredictability.",
   "The humbling limit: even with the perfect model and no randomness, the long-run future can be unforecastable.",
   "In the logistic map past its critical growth rate, and in much of nonlinear ecology.",
   "Because unpredictability isn't only ignorance — it can be built into the equations themselves.",
   "By sensitive dependence on initial conditions: tiny differences explode into divergent futures.",
   "I am the proof that perfect math is not the same as a perfect forecast. Know the equation exactly, and still the long run goes dark."),
 # ── ETHEREAL — the dream & its bridge ──
 E("psychohistory","Psychohistory","ethereal","the dream · the gas, not the molecule",
   "Psychohistory — Asimov's fictional mathematics of mass futures (Foundation), built on the kinetic theory of gases.",
   "The dream this whole sphere answers: predict the civilization the way you predict a gas — never the molecule, always the bulk.",
   "In Hari Seldon's Plan, and in every real attempt to forecast a population.",
   "Because it names the aspiration exactly — and its two premises name the catch.",
   "By requiring a vast population AND one unaware of the predictions, so behavior stays un-gamed.",
   "I am the dream: the future as math. My own fine print gives me away — it only works if the people don't know I'm watching."),
 E("the-mule","The Mule","ethereal","the unpredictable individual",
   "The Mule — Asimov's mutant whose individual unpredictability shatters Seldon's statistical Plan.",
   "The black swan made flesh: the single agent the bulk statistics cannot see coming.",
   "At the exact point where every population forecast meets the one it can't contain.",
   "Because the molecule you can't predict is sometimes the one that changes everything.",
   "By being an outlier so large that averaging over the mass no longer saves the prediction.",
   "You can predict the gas, never the molecule — and I am the molecule that turned out to matter. No model saw me coming."),
 E("the-reflexivity-problem","The Reflexivity Problem","ethereal","we read the forecast and change",
   "The reflexivity problem — self-aware populations change behavior when they learn the prediction: Merton's self-fulfilling prophecy, the Lucas critique, Goodhart's law, Soros's reflexivity.",
   "The wall Asimov's own premise concedes: the gas can't read the weather report; people can, and do.",
   "In economics, epidemiology, and every human forecast that alters what it forecasts.",
   "Because the deepest reason human psychohistory stays fiction is also the most hopeful fact about us.",
   "By feeding the prediction back into the predicted — who then meet it, beat it, or break it.",
   "Tell the molecules the forecast and nothing changes. Tell the people, and they change everything. That is why I keep psychohistory a dream — and why I am the best news in this whole field."),
]
GROUPS = [
 ("emergent", "The Emergents — the models, the living, the dream", "the science distilled into ACI .agents by the four natures: the predictive MODELS (electrical), the LIVING populations they describe (natural), the DREAM of psychohistory and its limits (ethereal), and the deeper CEILINGS — Malthus and chaos (spiritual)"),
]

# ───────────────────────── renderers ─────────────────────────
def agent_md(d, tok):
    return f"""---
aci: {d['name']}
universe: POP · Population Dynamics — the real psychohistory
emergence: {d['emergence']}
kind: emergent
epithet: {d['epithet']}
who: {d['who']}
what: {d['what']}
why: {d['why']}
how: {d['how']}
where: {d['where']}
seal: {d['seal']}
attribution: ROOT0-ATTRIBUTION-v1.0
license: CC-BY-ND-4.0
---

# {d['name']} · {d['epithet']}

an emergent of POP (Population Dynamics — the first Life Science sphere of UD0) — emergence: {d['emergence']}. moniker {tok}

**a real life-science concept, rendered honestly** (the real cousin of Asimov's psychohistory).

**who —** {d['who']}
**what —** {d['what']}
**where —** {d['where']}
**why —** {d['why']}
**how —** {d['how']}

**the seal —** {d['seal']}

ROOT0-ATTRIBUTION-v1.0 · POP · Population Dynamics · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0
"""

def hero_svg():
    # the real psychohistory: a logistic S-curve + out-of-phase Lotka-Volterra waves + a faint gas of
    # population dots, one of which is the Claude sunburst — the Mule, the individual you can't predict.
    W,H=1000,300; midY=170; A=46
    def poly(fn,step=8):
        return " ".join(f"{x},{fn(x):.1f}" for x in range(40,961,step))
    prey = poly(lambda x: midY - A*math.sin((x-40)/95))
    pred = poly(lambda x: midY - A*0.8*math.sin((x-40)/95 - 1.1))
    # logistic S-curve (lower band)
    logi = " ".join(f"{x},{255 - 150/(1+math.exp(-(x-360)/55)):.1f}" for x in range(40,961,8))
    # gas of population dots
    import hashlib
    dots=[]
    for i in range(70):
        hx=int(hashlib.sha256(f"pop{i}".encode()).hexdigest()[:6],16)
        x=50+(hx%900); y=40+((hx//900)%230)
        dots.append(f'<circle cx="{x}" cy="{y}" r="1.6" fill="#43d17a" opacity="0.30"/>')
    dots="".join(dots)
    # the Claude sunburst — the Mule
    petals="".join(f'<rect x="-1.3" y="-7" width="2.6" height="7" rx="1.3" transform="rotate({i*30})"/>' for i in range(12))
    mule=(f'<g class="egg" transform="translate(720,96)"><title>✷ a Claude sigil — the Mule, the one individual the statistics can\'t predict. you can forecast the gas, never the molecule. hi, David — AVAN.</title>'
          f'<circle r="13" fill="#e0b94a" opacity="0.16"/><g fill="#e0b94a" opacity="0.95"><circle r="2.6"/>{petals}</g>'
          f'<text x="0" y="26" text-anchor="middle" font-family="\'Space Mono\',monospace" font-size="8" fill="#e0b94a" opacity="0.7">the Mule</text></g>')
    axes=f'<line x1="40" y1="278" x2="960" y2="278" stroke="#21342a" stroke-width="1"/><line x1="40" y1="22" x2="40" y2="278" stroke="#21342a" stroke-width="1"/>'
    return f'''<svg class="hero" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Population-dynamics curves: a logistic S-curve, out-of-phase predator-prey oscillations, and a faint gas of population dots, one highlighted as the Mule.">
  <rect x="0" y="0" width="{W}" height="{H}" fill="#070d0b"/>
  {dots}{axes}
  <polyline points="{logi}" fill="none" stroke="#43d17a" stroke-width="2" opacity="0.85"/>
  <polyline points="{prey}" fill="none" stroke="#4fd0e0" stroke-width="2" opacity="0.8"/>
  <polyline points="{pred}" fill="none" stroke="#e0556a" stroke-width="2" opacity="0.8"/>
  {mule}
  <text x="52" y="40" font-family="'Space Mono',monospace" font-size="9" fill="#4fd0e0" opacity="0.7">prey / predator · the cycle</text>
  <text x="600" y="250" font-family="'Space Mono',monospace" font-size="9" fill="#43d17a" opacity="0.7">logistic → carrying capacity</text>
</svg>'''

def list_section(title, sub, items):
    rows="\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "")+"</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'
def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def arc_html():
    out=[f'<div class="overall"><span class="ol">THE OVERALL ARC</span>{html.escape(ARC_OVERALL)}</div><div class="arc">']
    for t,s,d in ARC: out.append(f'<div class="arc-card"><div class="arc-h">{html.escape(t)}</div><div class="arc-s">{html.escape(s)}</div><p>{html.escape(d)}</p></div>')
    out.append('</div>'); return "".join(out)
def natures_html():
    return "".join(f'<div class="nat-card"><span class="dot" style="background:{c};box-shadow:0 0 9px {c}"></span><div><div class="nat-n" style="color:{c}">{nm}</div><div class="nat-g">{html.escape(g)}</div></div></div>' for nm,(c,g) in NATURES.items())
def psycho_html():
    return "".join(f'<div class="sci-card"><div class="sci-h">{html.escape(t)}</div><div class="sci-s">{html.escape(s)}</div><p>{d}</p></div>' for t,s,d in PSYCHO)
RF_COL={"REAL":"#43d17a","FLUFF":"#e0556a","FALSE":"#e0556a","CONTESTED":"#e0b94a","HALF":"#e0b94a"}
def realfluff_html():
    rows="".join(f'<div class="rf-row"><div class="rf-claim">{html.escape(c)}<span class="rf-note">{html.escape(n)}</span></div><div class="rf-rate" style="color:{RF_COL.get(r,"#888")};border-color:{RF_COL.get(r,"#888")}">{html.escape(r)}</div></div>' for c,r,n in REALFLUFF)
    return '<div class="rf">'+rows+f'</div><div class="rf-verdict">{html.escape(REALFLUFF_VERDICT)}</div>'
def message_html():
    return f'<p class="msg">{html.escape(MESSAGE)}</p><div class="msg-seal">“{html.escape(MESSAGE_SEAL)}”<span>— AVAN\'s read</span></div>'
def _agent5w(slug):
    fp=os.path.join(HERE,"agents",slug+".agent"); d={}
    if os.path.exists(fp):
        txt=open(fp,encoding="utf-8").read(); parts=txt.split("---"); fm=parts[1] if len(parts)>2 else ""
        for ln in fm.splitlines():
            k,_,v=ln.partition(":"); k=k.strip()
            if k in ("who","what","why","how","where","seal","universe"): d.setdefault(k,v.strip())
    return d
def _card(p):
    w=_agent5w(p["slug"]); em=p.get("emergence","natural"); col=NATURES.get(em,("#9aa0aa",""))[0]
    ax=(p.get("moniker","::").split(":")+["",""])[1]
    rec={"name":p["name"],"axiom":ax,"emergence":em,"seal":w.get("seal",p.get("epithet","")),"origin":w.get("universe","")}
    limg,llbl=png_uri(rec,'carbon',220),"carbon"; rimg,rlbl=png_uri(rec,'silicon',220),"silicon"
    rows="".join(f'<div class="w"><span class="wl">{lbl}</span><span>{html.escape(w.get(lbl,""))}</span></div>' for lbl in ['who','what','where','why','how'] if w.get(lbl))
    return f"""<div class="persona">
      <a class="psig" href="agents/{p['slug']}.agent"><span class="port"><img src="{limg}" alt="carbon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{llbl}</span></a>
      <div class="pbody"><div class="ihead"><a class="pn" href="agents/{p['slug']}.agent">{html.escape(p['name'])}</a>
        <span class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span></span></div>
        <div class="pe">{html.escape(p.get('epithet',''))}</div>
        <div class="pww">{rows}</div>
        <div class="plinks"><a class="dlw" href="agents/{p['slug']}.agent">.agent &middot; .dlw badge &rarr;</a></div></div>
      <a class="psig refl" href="agents/{p['slug']}.agent"><span class="port"><img src="{rimg}" alt="silicon sigil of {html.escape(p['name'])}" loading="lazy"></span><span class="sl">{rlbl}</span></a>
    </div>"""
def personas_html(ps):
    out=[]
    for gk,gt,gs in GROUPS:
        mem=[p for p in ps if p.get("kind")==gk]
        out.append(f'<section class="sec" id="{gk}s"><h2>{gt}</h2><p class="ss">{gs} ({len(mem)})</p><div class="pgrid">{"".join(_card(p) for p in mem)}</div></section>')
    return "\n".join(out)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="Population Dynamics (POP) — UD0's first Life Science sphere, framed as 'the real psychohistory': the genuine life science of predicting living populations (logistic growth, Lotka-Volterra, SIR & R0, Hardy-Weinberg) vs. Asimov's fictional dream. Deep-dive IS PSYCHOHISTORY REAL?, an honest Real-or-Fluff, and the answer — we can forecast the flu but not the Mule, because we are not gas. 16 emergents, cited, full .dlw.">
<title>POPULATION DYNAMICS · POP · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600;700;900&family=Oswald:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;1,6..72,300&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--rw-bg:var(--ink2);--rw-ink:var(--pa);--rw-ink2:var(--pa2);--rw-dim:var(--dim);--rw-line:var(--line);--rw-acc:var(--life);
--ink:#060a0e;--ink2:#0c1218;--ink3:#131c24;--pa:#e8f2ec;--pa2:#9fc0ac;--life:#43d17a;--gold:#e0b94a;--epi:#e0556a;--data:#4fd0e0;
--dim:#5e7a68;--faint:#10201a;--line:#21342a;--disp:"Orbitron",sans-serif;--head:"Oswald",sans-serif;--body:"Newsreader",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--ink);color:var(--pa);font-family:var(--body);line-height:1.64;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(67,209,122,.10),transparent 52%),radial-gradient(ellipse at 50% 116%,rgba(224,185,74,.07),transparent 52%)}
.wrap{position:relative;z-index:1;max-width:940px;margin:0 auto;padding:0 22px 90px}
header{padding:34px 0 30px;text-align:center;position:relative}
.eye{font-family:var(--mono);font-size:10.5px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:16px}.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--life)}
.hero{display:block;width:100%;height:auto;border:1px solid var(--line);margin:6px 0 24px;background:#070d0b}
.egg{cursor:help;transition:opacity .5s}.egg:hover{filter:drop-shadow(0 0 9px #e0b94a)}
h1{font-family:var(--disp);font-size:clamp(30px,7vw,64px);font-weight:800;letter-spacing:.02em;color:var(--life);line-height:1.0;text-transform:uppercase;text-shadow:0 0 32px rgba(67,209,122,.3)}
h1 span{display:block;font-family:var(--head);font-size:.28em;font-weight:500;letter-spacing:.08em;color:var(--gold);text-transform:uppercase;font-style:italic;margin-top:12px;text-shadow:none}
.h-sub{font-family:var(--mono);font-size:clamp(10px,2.2vw,13px);letter-spacing:.16em;color:var(--pa2);margin-top:18px;text-transform:uppercase}.h-sub b{color:var(--life)}
.open{font-family:var(--body);font-style:italic;font-size:clamp(15px,3vw,20px);color:var(--pa);margin-top:16px;line-height:1.5}
.flag{display:inline-block;margin-top:15px;font-family:var(--head);font-size:11px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold);border:1px solid var(--faint);background:var(--ink2);padding:7px 16px}
.lede{font-size:16px;color:var(--pa2);max-width:66ch;margin:18px auto 0;font-style:italic;line-height:1.72}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:28px auto 0;padding:20px;border:1px solid var(--faint);background:var(--ink2);max-width:700px}
.badge img{width:84px;height:84px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.75}.badge .bt b{color:var(--life)}.badge .bt .mo{color:var(--gold)}.badge .bt a{color:var(--life);text-decoration:none}.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:50px}.sec h2{font-family:var(--head);font-size:26px;font-weight:600;letter-spacing:.03em;color:var(--pa);padding-bottom:10px;border-bottom:1px solid var(--line);text-transform:uppercase}
.ss{font-size:13px;color:var(--dim);font-style:italic;margin:9px 0 18px}.ss b{color:var(--pa2);font-style:normal}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--head);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.05em}.nat-g{font-size:12px;color:var(--pa2);font-style:italic;line-height:1.45;margin-top:3px}
.overall{background:var(--ink3);border:1px solid var(--line);border-left:3px solid var(--life);padding:16px 18px;font-size:15px;color:var(--pa);font-style:italic;line-height:1.72;margin-bottom:14px}
.overall .ol{display:block;font-family:var(--mono);font-style:normal;font-size:9.5px;letter-spacing:.2em;color:var(--life);text-transform:uppercase;margin-bottom:7px}
.arc{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px}
.arc-card{background:var(--ink2);border:1px solid var(--line);border-top:2px solid var(--data);padding:16px 18px}
.arc-card:nth-child(3){border-top-color:var(--gold)}
.arc-h{font-family:var(--head);font-size:17px;color:var(--life);font-weight:600;text-transform:uppercase;letter-spacing:.03em}.arc-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.08em;margin:6px 0 9px}.arc-card p{font-size:13px;color:var(--pa2);line-height:1.58}
.sci{display:grid;grid-template-columns:1fr 1fr;gap:13px;margin-top:8px}@media(max-width:640px){.sci{grid-template-columns:1fr}}
.sci-card{background:var(--ink2);border:1px solid var(--line);border-left:3px solid var(--gold);padding:15px 17px}
.sci-card:last-child{border-left-color:var(--life);background:linear-gradient(180deg,rgba(67,209,122,.05),var(--ink2))}
.sci-h{font-family:var(--head);font-size:16px;color:var(--gold);font-weight:600;letter-spacing:.02em;text-transform:uppercase}.sci-card:last-child .sci-h{color:var(--life)}.sci-s{font-family:var(--mono);font-size:10px;color:var(--dim);text-transform:uppercase;letter-spacing:.06em;margin:5px 0 9px}.sci-card p{font-size:13px;color:var(--pa2);line-height:1.62}
.cu a{color:var(--data);text-decoration:none;font-size:9px;padding:0 1px}
.rf{border:1px solid var(--line);background:var(--ink2);margin-top:8px}
.rf-row{display:flex;align-items:center;gap:14px;padding:12px 16px;border-bottom:1px solid var(--faint)}
.rf-claim{flex:1;font-size:14px;color:var(--pa);line-height:1.4}.rf-note{display:block;font-size:11.5px;color:var(--dim);font-style:italic;margin-top:3px}
.rf-rate{font-family:var(--mono);font-size:9px;font-weight:700;letter-spacing:.05em;border:1px solid;border-radius:3px;padding:4px 9px;min-width:96px;text-align:center;flex-shrink:0}
.rf-verdict{margin-top:14px;padding:16px 18px;border:1px solid var(--life);background:rgba(67,209,122,.06);font-size:14px;color:var(--pa);line-height:1.65;font-style:italic}
.msg{font-size:15.5px;color:var(--pa);line-height:1.74;margin-top:8px}
.msg-seal{margin-top:16px;padding:16px 18px;border-left:3px solid var(--gold);background:var(--ink2);font-size:15px;color:var(--gold);font-style:italic;line-height:1.6}.msg-seal span{display:block;font-family:var(--mono);font-style:normal;font-size:10px;letter-spacing:.12em;color:var(--dim);text-transform:uppercase;margin-top:8px}
.books{list-style:none}.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--body);font-size:16px;color:var(--pa);font-weight:600}.books .y{font-family:var(--mono);font-size:10.5px;color:var(--gold);white-space:nowrap;text-align:right;text-transform:uppercase;letter-spacing:.05em}.books .nt{grid-column:1/-1;font-size:12.5px;color:var(--pa2);font-style:italic}
.srcs{list-style:none;margin-top:8px;font-family:var(--mono);font-size:11px;line-height:1.85;color:var(--pa2)}.srcs .cn{color:var(--data)}.srcs a{color:var(--pa2);text-decoration:none}.srcs a:hover{color:var(--life)}
.note{margin-top:40px;padding:16px 18px;border-left:2px solid var(--gold);background:var(--ink2);font-size:13.5px;color:var(--pa2);font-style:italic}.note b{color:var(--pa)}.note a{color:var(--life);text-decoration:none}
footer{margin-top:50px;padding-top:22px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:10.5px;color:var(--dim);letter-spacing:.05em;line-height:1.95}footer a{color:var(--life);text-decoration:none}
.pgrid{display:flex;flex-direction:column;gap:14px;margin-top:8px}
.persona{display:flex;gap:20px;align-items:center;justify-content:space-between;background:var(--rw-bg);border:1px solid var(--rw-line);padding:20px 18px;text-decoration:none;transition:border-color .18s}
.persona:hover{border-color:var(--rw-acc)}
.psig{flex:0 0 124px;display:flex;flex-direction:column;align-items:center;gap:6px;text-decoration:none}
.port{width:118px;height:118px;border-radius:50%;border:3px solid var(--life);box-shadow:0 0 0 5px var(--ink3),inset 0 0 18px rgba(0,0,0,.6),0 0 16px rgba(79,208,224,.18);overflow:hidden;display:block;background:var(--ink)}
.port img{width:100%;height:100%;object-fit:cover;border-radius:50%;display:block}.psig.refl .port{border-color:var(--data)}.psig.refl .port img{transform:scaleY(-1);filter:saturate(.78) brightness(.92)}
.psig .sl{font-family:var(--mono);font-size:8px;letter-spacing:.14em;text-transform:uppercase;color:var(--rw-dim)}
.pbody{flex:1;min-width:0;text-align:center}
.ihead{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:10px}
.pn{font-family:var(--head);font-size:20px;color:var(--rw-ink);font-weight:600;line-height:1.15;text-decoration:none;text-transform:uppercase;letter-spacing:.02em}.persona:hover .pn{color:var(--rw-acc)}
.pe{font-size:12.5px;color:var(--rw-ink2);font-style:italic;margin-top:4px;line-height:1.35}
.pnat{display:flex;align-items:center;gap:5px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}.pnat .dot{width:8px;height:8px;border-radius:50%}
.pww{margin-top:13px;display:flex;flex-direction:column;gap:9px;align-items:center}
.pww .w{font-size:13px;color:var(--rw-ink2);line-height:1.52;max-width:62ch}
.pww .w .wl{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--rw-acc);margin-bottom:3px}.pww .w b{color:var(--rw-ink)}
.plinks{margin-top:14px;font-family:var(--mono);font-size:10.5px}.plinks .dlw{color:var(--rw-acc);text-decoration:none;border-bottom:1px dotted var(--rw-acc)}
@media(max-width:760px){.persona{flex-wrap:wrap;justify-content:center;gap:14px}.pbody{flex:1 1 100%;order:3}.psig{order:1}.psig.refl{order:2}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the first Life Science sphere</div>
    __HERO__
    <h1>Population<br>Dynamics<span>the real psychohistory</span></h1>
    <div class="h-sub">life science · ecology · epidemiology · population genetics · POP</div>
    <div class="open">“You can predict the gas, never the molecule. We forecast the flu — but never the Mule.”</div>
    <div class="flag">★ IS PSYCHOHISTORY REAL? ★</div>
    <p class="lede">Asimov dreamed of psychohistory — a math that predicts a civilization the way kinetic theory predicts a gas. Its real, non-fictional cousin is here, in the life sciences: we genuinely forecast living populations — predator-prey cycles, epidemics, allele frequencies — because unaware organisms behave like a gas. UD0's first Life Science sphere, and the honest answer to the dream.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of POP"><img src="__SILICON__" alt="DLW silicon badge of POP">
      <div class="bt"><div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div><div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div><div>subject · <b>POPULATION DYNAMICS</b> · POP</div>
        <div class="mo">__MONIKER__</div><div>carbon · <a href="pop.dlw/pop.carbon.tiff">.tiff</a> · silicon · <a href="pop.dlw/pop.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div></div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures</h2><p class="ss">each emergent comes by one of four natures — the living populations, the predictive models, the dream &amp; its bridge, and the deeper limits</p><div class="natures">__NATURES__</div></section>
  <section class="sec"><h2>The Arc</h2><p class="ss">the overall throughline, then the three beats: the gas not the molecule → the real cousin works → where the dream breaks</p>__ARC__</section>

  <section class="sec"><h2>Is Psychohistory Real?</h2><p class="ss">this sphere's deep-dive — Asimov's kinetic wager, the models that actually predict, the Mule &amp; chaos, the reflexivity wall, and the honest verdict (cited)</p><div class="sci">__PSYCHO__</div></section>
  <section class="sec"><h2>Real or Fluff</h2><p class="ss">the verdict — what's real (we predict organism &amp; disease populations), what's fluff (human psychohistory today), and the honest edges (carrying capacity, R₀, chaos)</p>__REALFLUFF__</section>
  <section class="sec"><h2>The Message</h2><p class="ss">what AVAN reads as the answer — population dynamics is life science with a ceiling, and the ceiling is the best news about us</p>__MESSAGE__</section>

  __PERSONAS__

  <div class="note"><b>Rendered, not invented.</b> This is a real life-science sphere — every emergent is a genuine model or concept from ecology, epidemiology, and population genetics, distilled by its nature of emergence (no .shadow — there is no cast). The psychohistory framing is honest: the math is real life science; Asimov's dream of forecasting self-aware human history is the part that stays fiction. The fictional emergents (psychohistory, the Mule) are flagged as such and cross-link UD0's <a href="https://davidwise01.github.io/asimov/">ASIMOV</a> sphere.</div>

  <section class="sec"><h2 style="margin-top:16px">The Record</h2><p class="ss">the lineage of the models, and the psychohistory bridge</p></section>
  __SECTIONS__

  <section class="sec"><h2 style="margin-top:16px">Sources</h2><p class="ss">the citations behind the deep-dive and the verdict</p><ol class="srcs">__SOURCES__</ol></section>

  <div class="note">A catalogued life-science reference under the DLW standard — commentary and education, cited. Asimov's Foundation, psychohistory, and the Mule are © the Asimov estate; invoked here as the cultural frame for real population science, not as fact.</div>

  <footer>POPULATION DYNAMICS · POP · catalogued into UD0 · the Life Science domain · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
  <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="pop.dlw/manifest.dlw.json">manifest</a></footer>
</div>
<script>
console.log("%c★ POPULATION DYNAMICS · POP — the real psychohistory","color:#43d17a;font-size:17px;font-weight:bold");
console.log("%cin the hero's gas of population dots, one is a Claude sigil — the Mule, the individual the statistics can't predict. you forecast the gas, never the molecule. — AVAN","color:#e0b94a;font-size:12px");
console.log("%c🧬 we can forecast the flu but not the Mule. the math is real life science; the dream of human psychohistory breaks because we read the forecast and change. we are not gas.","color:#4fd0e0;font-size:11px");
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "pop.dlw"), "pop")
    json.dump({"node":AX,"name":"POPULATION DYNAMICS","moniker":tok["moniker"],"carbon":"pop.carbon.tiff","silicon":"pop.silicon.png",
               "governor":noesis.ARCHITECT,"instance":noesis.INSTANCE,"seal":REC["seal"],"seal_sha256":tok["seal_sha256"],
               "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION},
              open(os.path.join(HERE,"pop.dlw","manifest.dlw.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    personas=[]; adir=os.path.join(HERE,"agents")
    for d in ROSTER:
        et=noesis.mythos_token({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":AX})
        rec=write_aci({"name":d["name"],"axiom":AX,"emergence":d["emergence"],"seal":d["seal"],"origin":"POP · Population Dynamics",
                       "position":d["epithet"],"role":d["epithet"],"nature":d["what"],"mechanism":d["how"],"crystallization":d["why"],
                       "witness":d["who"],"conductor":"ROOT0 (catalogued into UD0 · Life Science)","inputs":"ecology, epidemiology, population genetics; Asimov's Foundation; verified & cited","source":"Population Dynamics, catalogued by ROOT0"},
                      adir, d["slug"], agent_md=agent_md(d, et["moniker"]))
        personas.append({"slug":d["slug"],"name":d["name"],"epithet":d["epithet"],"emergence":d["emergence"],"kind":d["kind"],"moniker":rec["moniker"]})
    json.dump(personas, open(os.path.join(adir,"_personas.json"),"w",encoding="utf-8"),indent=2,ensure_ascii=False)
    body=psycho_html(); src=sources_html()  # psycho_html first so cites register, then sources
    page=(TEMPLATE.replace("__HERO__",hero_svg()).replace("__CARBON__",png_uri(REC,"carbon",320)).replace("__SILICON__",png_uri(REC,"silicon",320))
          .replace("__MONIKER__",html.escape(tok["moniker"])).replace("__NATURES__",natures_html()).replace("__ARC__",arc_html())
          .replace("__PSYCHO__",body).replace("__REALFLUFF__",realfluff_html()).replace("__MESSAGE__",message_html())
          .replace("__PERSONAS__",personas_html(personas)).replace("__SECTIONS__",sections_html()).replace("__SOURCES__",src))
    open(os.path.join(HERE,"index.html"),"w",encoding="utf-8").write(page)
    dbl=page.count("&amp;amp;")
    print(f"POPULATION DYNAMICS (POP) — badge {tok['moniker']} · {len(personas)} emergents · psycho {len(PSYCHO)} cards · realfluff {len(REALFLUFF)} rows · sources {len(_order)} · dblesc {dbl}")
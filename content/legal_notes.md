# Note Giuridiche — DPIA e Sistemi di Intelligenza Artificiale

## Nota 1 — Ambito di applicazione dell'art. 35 GDPR

La DPIA non è richiesta per ogni trattamento, ma solo quando è **probabile** (not certain) che il trattamento comporti un rischio elevato. La valutazione della probabilità deve essere svolta **ex ante**, prima dell'inizio del trattamento.

Il Considerando 91 GDPR chiarisce che la DPIA è opportuna quando si trattano dati su larga scala con finalità di profilazione o quando si monitora sistematicamente una zona pubblica. Il termine "larga scala" non è definito nel GDPR ma le linee guida WP248 indicano criteri orientativi: numero di interessati, volume di dati, durata, estensione geografica.

---

## Nota 2 — DPIA e sistemi AI: il quadro normativo in evoluzione

### GDPR (2016/679)
Già l'art. 35 GDPR impone la DPIA per trattamenti automatizzati con effetti significativi. L'art. 22 GDPR limita le decisioni esclusivamente automatizzate.

### AI Act (Reg. UE 2024/1689)
Il Regolamento sull'Intelligenza Artificiale dell'UE introduce il concetto di **sistemi AI ad alto rischio** (Allegato III), che include:
- sistemi AI per l'accesso a servizi pubblici essenziali (incluso l'alloggio)
- sistemi AI per il controllo delle frontiere e l'applicazione della legge
- sistemi AI per la valutazione del credito e la selezione del personale

Per i sistemi ad alto rischio, l'AI Act prevede obblighi di:
- valutazione della conformità (Conformity Assessment)
- registrazione nel database EU AI
- trasparenza e documentazione tecnica
- supervisione umana effettiva
- robustezza e accuratezza

> **Interazione con GDPR**: la DPIA ex art. 35 GDPR e la valutazione di conformità ex AI Act sono atti distinti ma complementari. Nella pratica, una DPIA ben condotta può soddisfare in parte i requisiti documentali dell'AI Act.

---

## Nota 3 — Il ruolo del DPO nella DPIA

Il Responsabile della Protezione dei Dati (DPO) nominato ex artt. 37-39 GDPR **deve essere consultato** prima di procedere alla DPIA (art. 35 par. 2 GDPR).

Il DPO:
- fornisce consulenza sul processo di DPIA
- verifica se la DPIA è necessaria
- monitora l'esecuzione della DPIA
- può essere coinvolto nella valutazione dei rischi

La consultazione del DPO deve essere documentata. Non è necessario che il DPO approvi la DPIA, ma il titolare deve tenere conto del suo parere.

> Nota pratica: le amministrazioni pubbliche (come i Comuni) sono generalmente obbligate a nominare un DPO ex art. 37 par. 1 lett. a) GDPR.

---

## Nota 4 — Consultazione preventiva dell'Autorità (art. 36 GDPR)

Se la DPIA evidenzia un **rischio residuo elevato** che non può essere mitigato con misure ragionevoli, il titolare è obbligato a **consultare preventivamente** il Garante per la protezione dei dati personali prima di iniziare il trattamento.

La consultazione preventiva è una misura eccezionale e non deve essere confusa con la semplice comunicazione al Garante. L'Autorità, ricevuta la richiesta, può:
- fornire consulenza entro 8 settimane (prorogabile di 6 settimane)
- autorizzare il trattamento con condizioni
- vietare il trattamento

Il Garante italiano ha pubblicato linee guida e provvedimenti specifici su trattamenti ad alto rischio (disponibili su www.garanteprivacy.it).

---

## Nota 5 — Riesame della DPIA (art. 35 par. 11)

La DPIA non è un documento statico. Il titolare deve riesaminarla periodicamente e in ogni caso:
- quando cambiano le circostanze del trattamento
- quando emergono nuovi rischi
- quando vengono adottate nuove tecnologie
- quando si verificano incidenti di sicurezza rilevanti

Le linee guida EDPB raccomandano un riesame periodico (tipicamente annuale per trattamenti ad alto rischio).

---

## Nota 6 — Privacy by Design e by Default (art. 25 GDPR)

La DPIA è strettamente connessa al principio di **privacy by design**: il titolare deve integrare la protezione dei dati nelle fasi di progettazione del trattamento, non come adempimento successivo.

Gli elementi di privacy by design rilevanti per i sistemi AI:
- minimizzazione dei dati (usare solo i dati strettamente necessari)
- pseudonimizzazione e anonimizzazione dove possibile
- limitazione della conservazione
- architetture che minimizzano l'esposizione dei dati
- accesso basato sul principio del minimo privilegio

---

## Nota 7 — Responsabile del trattamento esterno (art. 28 GDPR)

Quando il sistema AI è fornito da un soggetto esterno, questo agisce tipicamente come **responsabile del trattamento** ex art. 28 GDPR. È obbligatorio:
- stipulare un contratto scritto che disciplini il trattamento
- il contratto deve prevedere le garanzie elencate all'art. 28 par. 3 GDPR
- il responsabile non può sub-appaltare senza autorizzazione del titolare
- il responsabile deve cancellare o restituire i dati al termine del contratto

Il titolare rimane **responsabile in ultima istanza** anche per il trattamento effettuato dal responsabile.

---

## Nota 8 — Principio di accountability (art. 5 par. 2 e art. 24 GDPR)

Il titolare del trattamento deve essere in grado di **dimostrare** la conformità al GDPR. La DPIA è uno strumento fondamentale di accountability:
- documenta le decisioni di design
- evidenzia i rischi identificati
- registra le misure adottate
- costituisce prova della diligenza del titolare

In caso di controllo da parte del Garante o di contenzioso, la DPIA può essere richiesta come documento probatorio.

---

## Nota 9 — Casistica italiana rilevante

Il Garante per la protezione dei dati personali ha adottato provvedimenti rilevanti in materia di:
- sistemi di scoring e profilazione (es. provvedimento su Lendix, sistemi di credit scoring)
- videosorveglianza e riconoscimento facciale (es. provvedimento di Lecce 2023)
- trattamenti da parte di pubbliche amministrazioni (es. utilizzo di AI nei servizi sociali)

Il Garante ha pubblicato le **liste delle tipologie di trattamenti soggetti a DPIA** obbligatoria (disponibili sul sito del Garante).

---

*Note giuridiche elaborate a fini didattici — Clinica Legale AI & DPIA*
*Ultimo aggiornamento: 2025 — verificare gli aggiornamenti normativi successivi*

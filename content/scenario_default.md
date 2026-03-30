# Scenario di Default — Comune e sistema AI per l'alloggio di emergenza

## Titolo del caso
**Comune di [X] — Sistema automatizzato di prioritizzazione delle domande di alloggio di emergenza**

---

## Descrizione del trattamento

Il Comune di [X] ha adottato un sistema di intelligenza artificiale sviluppato da un fornitore esterno (SocietàTech Srl) per la **gestione e prioritizzazione automatica delle domande di alloggio di emergenza**.

Il sistema riceve in input le informazioni fornite dai richiedenti attraverso il portale comunale e le integra con dati provenienti da banche dati pubbliche (anagrafe, INPS, Agenzia delle Entrate, servizi sociali). Sulla base di questi dati, l'algoritmo assegna un **punteggio di priorità** a ciascun richiedente, determinando l'ordine di assegnazione degli alloggi disponibili.

---

## Finalità dichiarata

Ottimizzare l'allocazione delle risorse abitative pubbliche, garantire equità nelle assegnazioni, ridurre i tempi di istruttoria, e supportare gli operatori dei servizi sociali nelle decisioni allocative.

---

## Categorie di dati trattati

- **Dati anagrafici**: nome, cognome, data di nascita, codice fiscale, indirizzo di residenza
- **Dati familiari**: composizione del nucleo familiare, presenza di minori, anziani, disabili
- **Dati economici**: ISEE, reddito dichiarato, situazione lavorativa
- **Dati abitativi**: situazione abitativa attuale, eventuali sfratti, coabitazioni forzate
- **Dati territoriali**: zona di residenza, prossimità a servizi, storico degli spostamenti nel territorio comunale
- **Dati sociali**: segnalazioni dei servizi sociali, eventuali fragilità certificate
- **Potenzialmente**: dati di origine etnica o nazionalità (indirettamente derivabili da nome/luogo di nascita)

---

## Categorie di interessati

- Cittadini richiedenti alloggio di emergenza
- Nuclei familiari in condizione di fragilità o vulnerabilità
- Minori (componenti del nucleo familiare)
- Persone con disabilità
- Persone in condizioni di povertà estrema

---

## Base giuridica

Art. 6 par. 1 lett. e) GDPR (esecuzione di un compito di interesse pubblico)
Legge regionale in materia di edilizia residenziale pubblica (normativa di riferimento da specificare)

---

## Sistema AI utilizzato

Modello di machine learning supervisionato, addestrato su dati storici delle assegnazioni precedenti, che calcola un **punteggio composito di urgenza e priorità** basato su variabili ponderate.

Il sistema è stato fornito da SocietàTech Srl, che mantiene il codice sorgente riservato (black box parziale). La documentazione tecnica è disponibile per il Comune ma non per i richiedenti.

---

## Processo decisionale

1. Il richiedente compila il modulo digitale sul portale
2. Il sistema interroga le banche dati esterne
3. L'algoritmo elabora i dati e assegna il punteggio
4. La graduatoria generata dal sistema viene trasmessa agli operatori sociali
5. **Gli operatori possono teoricamente modificare il punteggio**, ma nella pratica raramente lo fanno (controllo umano formalmente presente, ma sostanzialmente debole)
6. La graduatoria viene approvata dall'ufficio competente e pubblicata

---

## Criticità identificabili

### Rischio di discriminazione algoritmica
Il modello è stato addestrato su dati storici che potrebbero riflettere bias preesistenti nell'allocazione degli alloggi (es. sotto-rappresentazione di determinate aree geografiche o categorie demografiche).

### Opacità
I richiedenti non ricevono spiegazione del punteggio ricevuto né dei fattori che lo hanno determinato.

### Controllo umano nominale
Il margine di intervento degli operatori è formalmente previsto ma scarsamente esercitato, rendendo di fatto il processo decisionale automatizzato.

### Dati territoriali come proxy
L'uso di dati di localizzazione può costituire un proxy per l'origine etnica o il background socioeconomico, con potenziali effetti discriminatori indiretti.

### Dati di soggetti vulnerabili
Tutti gli interessati sono per definizione in condizione di vulnerabilità. I minori e i disabili sono indirettamente coinvolti.

### Fornitore esterno
SocietàTech Srl agisce come responsabile del trattamento. Il contratto ex art. 28 GDPR deve essere verificato. Il codice del modello non è auditabile dall'esterno.

---

## Domande guida per la DPIA

1. Il trattamento rispetta il principio di non discriminazione?
2. Il meccanismo di scoring è spiegabile e contestabile?
3. Esiste un meccanismo di revisione individuale del punteggio?
4. I richiedenti sono informati dell'uso del sistema AI?
5. Il fornitore garantisce il rispetto del GDPR?
6. Il sistema è stato testato per rilevare bias?
7. Esiste una procedura di contestazione accessibile?
8. L'algoritmo è stato validato da soggetti indipendenti?

---

## Esito atteso della DPIA (scenario critico)

- **Precheck**: DPIA necessaria (AI + profilazione + effetti significativi + soggetti vulnerabili + larga scala)
- **Necessità/proporzionalità**: parzialmente giustificata ma con profili critici
- **Livello di rischio**: ALTO (discriminazione, opacità, controllo umano debole)
- **Misure raccomandate**: explainability, audit esterno, meccanismo di contestazione, informativa rafforzata, revisione del controllo umano
- **Esito**: rischio elevato ma mitigabile — si può procedere solo con misure ulteriori

---

*Scenario elaborato a fini didattici — Clinica Legale AI & DPIA*

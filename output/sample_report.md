# DPIA — Valutazione d'Impatto sulla Protezione dei Dati
## Ai sensi dell'art. 35 del Regolamento (UE) 2016/679 (GDPR)

---

**Documento:** DPIA-2025-001
**Data di redazione:** [data]
**Versione:** 1.0
**Stato:** Bozza / Approvato
**Redatto da:** [nome referente]
**Validato da:** [DPO, se nominato]

---

## 1. Descrizione del Trattamento

### 1.1 Titolare del trattamento
Comune di [X] — Servizio Politiche Abitative
Via [indirizzo], [Comune]
P.IVA / C.F.: [codice]
Referente: [nome, qualifica]

### 1.2 Finalità del trattamento
Il trattamento ha la finalità di **prioritizzare automaticamente le domande di alloggio di emergenza** presentate dai cittadini, al fine di ottimizzare l'allocazione delle risorse abitative pubbliche e ridurre i tempi di istruttoria.

Il sistema assegna un punteggio composito di urgenza a ciascun richiedente, tenendo conto di variabili socioeconomiche, familiari e abitative, al fine di determinare l'ordine di assegnazione degli alloggi disponibili.

### 1.3 Categorie di dati trattati
| Categoria | Tipo di dato | Fonte |
|-----------|-------------|-------|
| Dati anagrafici | Nome, cognome, data di nascita, codice fiscale, residenza | Dichiarazione richiedente / Anagrafe |
| Dati familiari | Composizione nucleo, presenza minori/anziani/disabili | Dichiarazione richiedente |
| Dati economici | ISEE, reddito, situazione lavorativa | INPS / Agenzia Entrate |
| Dati abitativi | Situazione attuale, sfratti, coabitazioni | Dichiarazione richiedente / Ufficio tecnico |
| Dati territoriali | Zona di residenza, storico spostamenti | Anagrafe / Sistema interno |
| Dati sociali | Segnalazioni servizi sociali, fragilità certificate | Servizi sociali comunali |

**Dati particolari ex art. 9 GDPR presenti:** Sì (dati su disabilità; potenzialmente dati idonei a rivelare l'origine etnica attraverso proxy).

### 1.4 Categorie di interessati
- Cittadini richiedenti alloggio di emergenza
- Nuclei familiari in condizione di fragilità o vulnerabilità
- Minori (componenti del nucleo familiare)
- Persone con disabilità

**Nota:** tutti gli interessati sono per definizione in condizione di vulnerabilità socioeconomica.

### 1.5 Base giuridica
Art. 6 par. 1 lett. e) GDPR — esecuzione di un compito di interesse pubblico
Legge regionale n. [X] in materia di edilizia residenziale pubblica

Per i dati particolari: art. 9 par. 2 lett. g) GDPR (interesse pubblico rilevante).

### 1.6 Sistema AI utilizzato
**Tipo di sistema:** Modello di machine learning supervisionato (algoritmo di ranking)
**Fornitore:** SocietàTech Srl (responsabile del trattamento ex art. 28 GDPR)
**Trasparenza:** Il modello produce output (punteggio) ma la logica interna è parzialmente opaca
**Dati di addestramento:** Storico assegnazioni precedenti del Comune (dati anonimizzati)
**Output:** Punteggio numerico (0-100) e posizione in graduatoria

### 1.7 Processo decisionale
1. Il richiedente compila il modulo digitale sul portale comunale
2. Il sistema interroga le banche dati esterne (INPS, Anagrafe, Agenzia Entrate)
3. L'algoritmo elabora i dati e assegna il punteggio di priorità
4. La graduatoria viene trasmessa agli operatori dei servizi sociali
5. Gli operatori possono modificare il punteggio con motivazione
6. La graduatoria viene approvata dall'ufficio competente e pubblicata

**Grado di automazione:** Alto — il controllo umano è formalmente previsto ma raramente esercitato nella pratica.

### 1.8 Fornitori esterni
SocietàTech Srl agisce come **responsabile del trattamento** ai sensi dell'art. 28 GDPR. Il contratto ex art. 28 [è stato stipulato / deve essere stipulato]. Il codice sorgente dell'algoritmo è proprietario ma la documentazione tecnica è disponibile per il Comune.

---

## 2. Necessità e Proporzionalità

### 2.1 Necessità del trattamento
Il trattamento è **parzialmente giustificato** rispetto alla finalità dichiarata. L'uso del sistema AI accelera i tempi di istruttoria e mira a standardizzare i criteri di valutazione, riducendo la discrezionalità soggettiva degli operatori.

Tuttavia, **non risulta documentata una valutazione di alternative meno invasive** (es. sistema a punteggio trasparente senza componente ML, graduatorie manuali con criteri standardizzati).

### 2.2 Proporzionalità dei dati
I dati raccolti sono in parte pertinenti alle finalità, ma si evidenziano **profili di eccedenza** riguardo ai dati territoriali (storico spostamenti) che potrebbero non essere strettamente necessari per la prioritizzazione.

### 2.3 Informativa agli interessati
L'informativa agli interessati [è/non è] adeguata. In particolare, [deve essere integrata con] informazioni specifiche sull'uso del sistema AI e sul meccanismo di scoring, come richiesto dall'art. 22 par. 3 GDPR e dal Considerando 71.

### 2.4 Controllo umano
Il controllo umano è **formalmente presente ma sostanzialmente debole**. Gli operatori raramente modificano il punteggio algoritmico. Questa situazione non soddisfa il requisito di "intervento umano significativo" richiesto dall'art. 22 GDPR.

### 2.5 Spiegabilità
La logica dell'algoritmo è **parzialmente spiegabile**. Il Comune è in grado di descrivere le variabili utilizzate ma non il loro peso relativo né le interazioni interne al modello. Questo non soddisfa il requisito di spiegazione "significativa" della logica dell'elaborazione.

### 2.6 Sintesi della valutazione di necessità e proporzionalità
Il trattamento persegue una finalità legittima di interesse pubblico, ma presenta **significativi profili di criticità** riguardo alla proporzionalità, al controllo umano effettivo e alla spiegabilità. **Sono necessarie misure correttive** prima di procedere o nel breve periodo successivo all'avvio del trattamento.

---

## 3. Rischi Individuati

### 3.1 Matrice dei rischi

| # | Rischio | Probabilità | Gravità | Punteggio | Livello |
|---|---------|-------------|---------|-----------|---------|
| R1 | Discriminazione algoritmica | Alta | Alta | 9 | ALTO |
| R2 | Errore decisionale | Media | Alta | 6 | ALTO |
| R3 | Opacità e mancanza di spiegabilità | Alta | Media | 6 | ALTO |
| R4 | Esclusione o pregiudizio ingiustificato | Media | Alta | 6 | ALTO |
| R5 | Impossibilità di contestazione | Alta | Alta | 9 | ALTO |
| R6 | Violazione della riservatezza | Bassa | Media | 2 | BASSO |
| R7 | Uso improprio dei dati | Bassa | Bassa | 1 | BASSO |
| R8 | Vulnerabilità di sicurezza | Bassa | Media | 2 | BASSO |
| R9 | Effetti su soggetti vulnerabili | Alta | Alta | 9 | ALTO |

### 3.2 Rischi critici — descrizione

**R1 — Discriminazione algoritmica (CRITICO)**
Il modello è stato addestrato su dati storici che potrebbero riflettere bias preesistenti. L'uso di variabili territoriali come proxy di caratteristiche demografiche può produrre discriminazione indiretta. Il modello non è stato sottoposto a test specifici di fairness.

**R5 — Impossibilità di contestazione (CRITICO)**
I richiedenti non ricevono spiegazione del punteggio assegnato. Non esiste un meccanismo formale di contestazione della posizione in graduatoria basato su ragioni algoritmiche. Questo viola il diritto previsto dall'art. 22 par. 3 GDPR.

**R9 — Effetti su soggetti vulnerabili (CRITICO)**
Tutti gli interessati si trovano in condizione di vulnerabilità. Le decisioni del sistema incidono direttamente sulla possibilità di accedere a un alloggio di emergenza, con conseguenze potenzialmente gravi e irreversibili.

### 3.3 Valutazione aggregata del rischio
**RISCHIO AGGREGATO: ELEVATO**

Motivazione: 5 rischi su 9 presentano un punteggio alto (≥ 6), con tre rischi al livello massimo (9/9). Il trattamento ha potenziale di ledere in modo grave i diritti fondamentali di persone in situazioni di vulnerabilità.

---

## 4. Misure Previste

### 4.1 Misure adottate o in corso di adozione

| Misura | Stato | Note |
|--------|-------|------|
| Minimizzazione dei dati | Da implementare | Rivedere la raccolta dei dati territoriali |
| Limitazione della finalità | Parzialmente | Verificare contratto con SocietàTech |
| Controllo umano effettivo | Da rafforzare | Procedura operativa da ridefinire |
| Logging e tracciabilità | Presente | Sistema di log già attivo |
| Audit periodici | Da pianificare | Prevedere audit annuale |
| Explainability | Da implementare | Sistema di spiegazione individuale da sviluppare |
| Informativa rafforzata | Da aggiornare | Aggiungere sezione su AI e scoring |
| Controlli di accesso | Presenti | Verificare segmentazione degli accessi |
| Misure di sicurezza tecniche | Presenti | Conformi agli standard attuali |
| Revisione periodica DPIA | Da pianificare | Cadenza annuale |
| Canali di contestazione | Da istituire | Procedura di reclamo algoritmico da definire |
| Consultazione DPO | In corso | DPO consultato nella presente DPIA |
| Test per bias e fairness | Da eseguire | Affidare a soggetto terzo indipendente |
| Contratto ex art. 28 con SocietàTech | Da verificare/stipulare | Verificare conformità all'art. 28 GDPR |

### 4.2 Misure prioritarie

Le seguenti misure sono **prioritarie** e devono essere adottate prima dell'avvio o entro 30 giorni:

1. **Istituire un meccanismo di contestazione** del punteggio accessibile a tutti i richiedenti
2. **Aggiornare l'informativa agli interessati** con sezione specifica sull'uso dell'AI
3. **Rafforzare il controllo umano** con procedura operativa che preveda revisione obbligatoria per i casi borderline
4. **Commissionare un audit di fairness** del modello a soggetto terzo indipendente
5. **Verificare/stipulare il contratto ex art. 28** con SocietàTech Srl

---

## 5. Esito Finale

### 5.1 Semaforo di rischio
**GIALLO — Rischio elevato ma mitigabile**

### 5.2 Valutazione conclusiva

Il trattamento presenta **rischi elevati** per i diritti e le libertà degli interessati, in particolare riguardo alla discriminazione algoritmica, alla spiegabilità delle decisioni e alla possibilità di contestazione.

Le misure di mitigazione previste, se integralmente implementate, possono ridurre il rischio residuo a un livello accettabile. Tuttavia, **il trattamento non dovrebbe proseguire senza l'adozione delle misure prioritarie** indicate nella sezione 4.2.

### 5.3 Decisione del titolare
☐ Si può procedere con il trattamento adottando le misure previste
☐ Non si può procedere — rischio residuo non accettabile
☐ Si procede con riserva — misure da implementare entro [data]

**Motivazione della decisione:**
[da compilare]

---

## 6. Promemoria e Obblighi Successivi

### 6.1 Consultazione del DPO
> Il Responsabile della Protezione dei Dati (DPO), se nominato, **deve essere consultato** ai sensi dell'art. 35 par. 2 GDPR prima di procedere con il trattamento.
>
> DPO del Comune di [X]: [nome, contatti]
> Data di consultazione: [data]
> Parere del DPO: [allegare]

### 6.2 Aggiornamento della DPIA
> La DPIA deve essere **riesaminata** ai sensi dell'art. 35 par. 11 GDPR in caso di:
> - variazione delle modalità del trattamento
> - adozione di nuove versioni del sistema AI
> - cambiamento significativo del contesto normativo
> - verificarsi di incidenti di sicurezza o anomalie rilevanti
>
> **Data del prossimo riesame previsto:** [data — si raccomanda annuale]

### 6.3 Consultazione preventiva del Garante
> Qualora il rischio residuo rimanga elevato nonostante le misure adottate, il titolare è **obbligato** a consultare preventivamente il Garante per la protezione dei dati personali ai sensi dell'art. 36 GDPR prima di avviare il trattamento.

---

## Allegati

- [ ] Allegato A — Documentazione tecnica del sistema AI
- [ ] Allegato B — Contratto ex art. 28 GDPR con SocietàTech Srl
- [ ] Allegato C — Parere del DPO
- [ ] Allegato D — Informativa agli interessati (versione aggiornata)
- [ ] Allegato E — Risultati del test di fairness

---

*DPIA redatta a fini didattici — Clinica Legale AI & DPIA*
*Il presente documento è una bozza generata automaticamente dalla web app DPIA-Path. Deve essere revisionata e validata dal titolare del trattamento e dal DPO prima dell'uso in contesti reali.*

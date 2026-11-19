# ADR Identification and Preliminary Pharmacovigilance Analysis

**Workora PV Remote Internship — Task 1**  
**Project type:** Educational pharmacovigilance / synthetic case-data analysis  
**Dataset:** 18 synthetic case records (SYN-PV-001 to SYN-PV-018)

## Project overview
This repository documents a structured review of 18 fictional patient case scenarios. For each record, the listed suspected medicinal product and reported adverse drug reaction (ADR) are captured, onset after treatment initiation is recorded, concomitant medicines are kept separate, and the supplied expectedness, seriousness, dechallenge and rechallenge fields are summarised.

The project is a preliminary ADR-identification exercise. It does **not** establish causality and is not a substitute for clinical review or regulatory case processing.

## Objectives
- Identify the suspected medicinal product and reported ADR in each synthetic case.
- Record the reported time to onset after treatment initiation.
- Distinguish suspected products from concomitant medicines.
- Summarise expectedness, seriousness, dechallenge and rechallenge as supplied.
- Perform basic descriptive analysis and flag source-data quality issues.

## Repository structure
```text
adr_identification_pharmacovigilance_task1/
├── data/
│   └── adr_cases.csv
├── docs/
│   └── source_report.pdf
├── outputs/
│   ├── summary_statistics.csv
│   └── figures/
│       ├── adr_frequency_by_drug.png
│       ├── seriousness_distribution.png
│       └── onset_by_case.png
├── src/
│   └── analyse_adr_data.py
├── .gitignore
├── LICENSE
├── requirements.txt
└── README.md
```

## Dataset fields
| Field | Description |
|---|---|
| `case_id` | Synthetic case identifier |
| `age_years`, `sex` | Demographic details as supplied |
| `suspected_drug` | Product named as suspected in the source report |
| `dose_as_reported`, `route` | Dose and route reproduced as supplied |
| `indication_as_reported` | Indication reproduced as supplied |
| `reported_adr` | Reaction recorded in the source |
| `onset_days` | Days after treatment initiation, as supplied |
| `concomitant_medicine` | Co-medication or “None reported” |
| `expectedness_as_reported` | “Known” or “Unexpected” from the source |
| `seriousness_as_reported` | Seriousness category from the source |
| `dechallenge`, `rechallenge` | Source-recorded assessment fields |

## Key descriptive findings
The source report records:
- **18** synthetic cases
- **8** unique suspected medicines
- **8** unique reported reactions
- **16** cases marked “Known” and **2** marked “Unexpected”
- Seriousness: **10** medically important, **5** hospitalisation, **3** not serious
- **4** positive dechallenge records and **7** positive rechallenge records

These are descriptive counts only. The source's categories have not been independently verified.

## Run the analysis
Python 3.9 or later is recommended.

```bash
pip install -r requirements.txt
python src/analyse_adr_data.py
```

The script reads `data/adr_cases.csv`, validates basic structure, writes summary tables to `outputs/`, and generates three figures in `outputs/figures/`.

## Interpretation and pharmacovigilance notes
- The source report identifies one suspected product per case. Concomitant medicines are recorded separately and are not automatically considered causal.
- A temporal relationship may support further assessment, but **time to onset alone does not prove causality**.
- Positive/negative/unknown dechallenge and rechallenge values are reproduced from the source. The detailed chronology needed to independently verify these values is not available.
- A definitive WHO–UMC causality category must not be inferred from this dataset alone.
- “Known” and “Unexpected” are reproduced as supplied; product labels/reference documents were not included for independent expectedness verification.
- Seriousness categories are reproduced as supplied; detailed supporting criteria are not available.

## Data-quality observations
The source contains values that require verification against original clinical records. Examples include:
- Amlodipine recorded as **500 mg twice daily** (SYN-PV-004).
- Atorvastatin recorded as **500 mg twice daily** (SYN-PV-018).
- Several medicine–indication combinations appear unusual in the source (for example, Amoxicillin or Atorvastatin with “Anxiety”).

All values are intentionally preserved exactly as reported. No dose or indication has been silently corrected. These are **data-verification flags**, not clinical recommendations.

## Limitations
The source is explicitly synthetic and does not include complete medical history, laboratory results, allergy history, exact start/stop dates, confirmed diagnoses, treatment details or detailed outcome narratives. It must not be treated as a real patient dataset or submitted to a regulatory reporting system.

## Ethical and educational statement
This repository is intended solely for educational demonstration of basic pharmacovigilance data organisation and descriptive analysis. It contains fictional case records and no real patient personal data.

## Source
Prepared from the user-provided document: *ADR Identification Report — ADR Identification Basics | Analysis of Synthetic Patient Case Scenarios* (3 pages).

# Explaining this project and describing it on a CV

## Short explanation to practise in your own words

I analyzed 41,188 historical banking campaign records in Excel to compare term-deposit subscription performance across customer profiles and contact patterns. I kept the published source data intact, documented unknown values and repeated rows, and added four calculated fields. I created 10 native PivotTables and 10 charts, checking every comparison against the same overall totals. The main lesson was to compare conversion rates with group size and subscription volume, while avoiding causal claims from descriptive historical data.

## Questions you should be able to answer

**Why is the average of a 1/0 indicator a subscription rate?**

The sum counts the 1s, and the average divides that sum by the number of valid outcomes. This is the share that subscribed.

**Why can students have the highest occupation rate while administrative workers produce more subscriptions?**

There are 875 student records and 10,422 administrative-worker records. Students convert at 31.43%, producing 275 subscriptions. Administrative workers convert at 12.97%, producing 1,352. The much larger group produces more subscriptions despite a lower rate.

**Why retain the 12 exact repeats?**

There is no customer or event identifier. Identical published attributes are not conclusive evidence that a row was duplicated by mistake. I recorded the issue and retained the full published sample.

**Does the channel comparison prove cellular contact is better?**

No. Cellular records have a higher observed rate, but clients, timing, economic conditions and campaign selection may differ. A controlled comparison or a suitable adjusted design would be needed to estimate an effect.

**Why not average the displayed rates to get the overall rate?**

Groups have different sizes. I use total subscriptions divided by total records, which is equivalent to weighting each group rate by its record count.

**Why not conclude that more calls reduce conversion?**

Clients who have not converted may receive more calls. The aggregate association does not isolate the effect of an additional call, and no call-level sequence is provided.

**What is the problem with duration in a pre-call model?**

The duration of the call is unavailable before the call takes place. Using it for a pre-call decision would leak information from later in the process.

**Why is the monthly chart not proof of seasonality?**

The year is absent from the row-level file, and campaign composition changes over time. Month groups pool available years. January and February have no records.

**What would you do with more data?**

Request permitted customer/event identifiers, full timestamps, contact sequences, campaign costs and newer observations. Investigate selection differences and test specific contact-policy changes prospectively. Do not claim improved revenue or conversion until measured.

## Suggested CV entry after reviewing the project

### English

**Bank Marketing Campaign Analysis — Independent Portfolio Project**  
October 2026

- Prepared and analyzed 41,188 public banking campaign records in Excel, documenting data-quality decisions and adding four calculated analysis fields.
- Built 10 PivotTables and 10 dashboard charts to compare subscription rates, group sizes and campaign contact patterns; validated summaries against independent source-data calculations.

### German

**Bank-Marketing-Analyse — Eigenständiges Portfolio-Projekt**  
Oktober 2026

- Aufbereitung und Analyse von 41.188 öffentlich verfügbaren Bank-Marketing-Datensätzen in Excel, einschließlich dokumentierter Datenqualitätsprüfungen und vier berechneter Analysefelder.
- Erstellung von 10 PivotTables und 10 Dashboard-Diagrammen zum Vergleich von Abschlussquoten, Gruppengrößen und Kontaktmustern; Abgleich der Ergebnisse mit unabhängigen Kontrollberechnungen.

Add the actual repository link after publication. Use the date the portfolio project was built. This entry should not be described as work for Arab Bank or as a project completed in 2025.

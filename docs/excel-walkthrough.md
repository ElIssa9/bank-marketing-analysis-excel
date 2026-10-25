# Reproduce the project in Excel for Mac

This guide explains how to rebuild the project rather than only present its final charts. Microsoft 365 for Mac is the intended application.

## 1. Understand the source

The business outcome is `y`: whether a term deposit was subscribed. One row is a campaign record. A customer identifier and transaction amounts are absent, so do not claim unique-customer counts or revenue.

Import `data/raw/bank-additional-full.csv` using Excel's Text/CSV import. Select **semicolon** as the delimiter. Check that `age`, `duration`, `campaign`, `pdays`, `previous` and the economic indicators are numeric. If your locale uses decimal commas, verify the decimal-point indicators were interpreted correctly.

Keep the header in row 5 of `Bank_Data`, original columns A:U, and the 41,188 data rows in rows 6:41193. Add the source citation above the table. Preserve the original categories and row order.

## 2. Inspect data quality

Expected checks:

- Rows: 41,188; original columns: 21.
- `y`: 4,640 yes and 36,548 no.
- No empty fields; there are explicit `unknown` categories.
- 12 excess exact repeated rows, retained and documented.
- `pdays=999`: 39,673 records, meaning not previously contacted.
- Ages range from 17 to 98; unusual ages are not deleted without evidence of error.

Do not use Remove Duplicates automatically. Identical published attributes are not enough to prove two records refer to the same event or client.

## 3. Add four calculated fields

Enter these headers in V5:Y5: `subscribed`, `age_band`, `contact_band`, `prior_contact`.

In row 6, enter:

```excel
V6: =IF(U6="yes",1,IF(U6="no",0,NA()))
W6: =IF(A6<30,"Under 30",IF(A6<40,"30-39",IF(A6<50,"40-49",IF(A6<60,"50-59","60+"))))
X6: =IF(L6=1,"1 contact",IF(L6<=3,"2-3 contacts",IF(L6<=5,"4-5 contacts","6+ contacts")))
Y6: =IF(M6=999,"Not previously contacted","Previously contacted")
```

Fill these formulas through row 41193. Depending on the regional Excel settings, semicolons may be needed between formula arguments. Convert `A5:Y41193` to an Excel Table named **BankData**. Keep the four derived columns visually distinguishable from the original data.

Why average works: for 1/0 outcomes, `SUM(subscribed)` counts subscriptions, while `AVERAGE(subscribed)` divides subscriptions by the number of valid outcomes. For example, 1, 0, 1, 0 has an average of 0.5, meaning 50% subscribed.

## 4. Calculate the baseline

On `Analysis`, use:

```excel
B6: =COUNTA(BankData[y])
B7: =SUM(BankData[subscribed])
B8: =B7/B6
B9: =AVERAGE(BankData[campaign])
```

Expected results: 41,188; 4,640; 11.27%; and 2.57 contacts. Format counts as whole numbers and rates as percentages. The overall rate is the ratio of totals, not an unweighted average of the displayed group rates.

## 5. Create the first native PivotTable

Select a cell in BankData, choose **Insert > PivotTable**, and place it on `Analysis` at A13. Name it **SubscriptionsByJob**.

- Rows: `job`.
- Values: `y`, summarized by **Count**, caption **Records**.
- Values: `subscribed`, summarized by **Sum**, caption **Subscriptions**.
- Values again: `subscribed`, summarized by **Average**, caption **Subscription rate**, number format `0.00%`.

Use tabular layout, with no row subtotals and with grand totals. Verify the grand total equals the baseline. Students should have 875 records, 275 subscriptions and a 31.43% rate. Administrative workers should have 10,422 records, 1,352 subscriptions and a 12.97% rate.

## 6. Build the other nine comparisons

Repeat the same three value aggregations, changing only the row field and destination:

| PivotTable name | Row field | Destination |
|---|---|---|
| OutcomeCounts | y | A60 |
| AgePerformance | age_band | A82 |
| EducationPerformance | education | A104 |
| ChannelPerformance | contact | A126 |
| MonthPerformance | month | A148 |
| WeekdayPerformance | day_of_week | A170 |
| ContactFrequencyPerformance | contact_band | A192 |
| PreviousOutcomePerformance | poutcome | A214 |
| HousingPerformance | housing | A236 |

All ten PivotTables use **BankData** as their source. Each comparison must reconcile to 41,188 records and 4,640 subscriptions. Do not count only the yes rows when calculating a group's denominator.

## 7. Connect chart data with GETPIVOTDATA

Ordered chart helpers sit beside each PivotTable in columns F:I on `Analysis`. These columns are Group, Chart label, Rate or Records, and Records. For the occupation helper, the first category is in F14:

```excel
G14: =F14&" (n="&TEXT(I14,"#,##0")&")"
H14: =GETPIVOTDATA("Subscription rate",$A$13,"job",F14)
I14: =GETPIVOTDATA("Records",$A$13,"job",F14)
```

Point charts to the corresponding G:H range, including its header. Using GETPIVOTDATA means rates remain connected even when a PivotTable reorders its rows. Captions such as `Subscription rate` must exactly match the PivotTable value captions.

The outcome chart uses **Records**, not the outcome-group average (which would simply be 0% or 100%). Display months March–December in calendar order and weekdays Monday–Friday. Age and contact-frequency bands also follow their natural order. The ranked occupation and education orders reflect this original sample.

## 8. Assemble the Dashboard

Use two columns and five chart rows. Dashboard metrics link to the baseline calculations on Analysis. Create editable bar charts for categorical comparisons and column charts for month and weekday. Exclude PivotTable grand totals from chart categories.

For every rate chart, set the value-axis bounds to **minimum 0, maximum 0.7**, major unit 0.1, and percentage number format. The overall outcome-count chart uses 0–40,000. Keep chart titles and group labels readable and explain small groups beside the chart.

## 9. Refresh and verify

Changing source values recalculates formulas immediately, but PivotTables need refresh. Use **Data > Refresh All**, or refresh each of the ten PivotTables from its Analyze ribbon. The formula-linked chart data updates after refresh. Filtering the source Excel Table alone does not filter the dashboard.

Compare each PivotTable to `results/group_metrics.csv`. Check all totals, representative group rates, chart category counts, percentage axes and formula errors. New source categories require extending helper lists and chart ranges; simply adding rows does not configure new categories automatically.

## 10. Explain the result

Read the findings and limitations in the README. Be prepared to explain the difference between volume and rate, why unknown values and repeated rows were retained, why call duration is unsuitable for pre-call targeting, and why a historical association is not a causal effect.

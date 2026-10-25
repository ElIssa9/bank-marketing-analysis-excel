# Verification record

Verified in the connected Microsoft Excel for Mac workbook on 25 October 2026:

- Source: 41,188 records in a native Excel Table, BankData, at `Bank_Data!A5:Y41193`.
- Original source columns A:U preserved, with four formula-derived columns V:Y.
- Native object inventory: 10 PivotTables sourced from BankData and 10 editable charts on Dashboard.
- Overall totals: 41,188 records, 4,640 subscriptions, 11.2654171117801% subscription rate and 2.56759250267068 mean campaign contacts.
- Each of the ten PivotTable comparisons reconciled to the overall record and subscription totals.
- All 54 group counts, subscription counts and rates were programmatically compared with independent calculations from the original semicolon-delimited CSV. Counts matched exactly; rates agreed within 1e-12.
- Workbook formula-error scan returned no matches for the standard reference, value, division, name, numeric, missing, spill or calculation errors.
- All ten chart layouts were visually reviewed. Rate axes use 0–70%; the count chart uses 0–40,000. Category lists, source helpers and chart counts were checked.
- Native refresh check: temporarily changing the first source outcome from no to yes increased subscriptions from 4,640 to 4,641. Refreshing the occupation PivotTable increased housemaid subscriptions from 106 to 107 and its rate from 10.00% to 10.09%. The GETPIVOTDATA chart helper updated as expected.
- The original no outcome was restored, the PivotTable refreshed, and the baseline and housemaid results rechecked. No temporary test data remains.
- The included Python validation checks source schema, numeric validity, original totals, repeated-row count, band boundaries and group reconciliation. Its generated outputs are in results/.

The screenshots are native range captures of the Excel dashboard. The tests above establish live workbook behavior. They do not prove that the final workbook has been saved to disk or published; those handoff steps are tracked separately in workbook/README.md.

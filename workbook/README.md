# Native Excel workbook

**[Download Bank_Marketing_Analysis.xlsx](Bank_Marketing_Analysis.xlsx)**

Built and saved in Microsoft Excel for Mac with four worksheets, 10 native PivotTables, 10 editable charts and all 41,188 source records.

Open the Dashboard sheet for the charts and headline metrics. Analysis contains the native PivotTables and formula-linked chart data. Bank_Data preserves the original 21 columns, with four derived formula columns added separately. Data_Dictionary explains all fields.

Expected baseline: 41,188 records, 4,640 subscriptions, 11.27% subscription rate and 2.57 average campaign contacts. The underlying rate is 4,640 / 41,188; displayed percentages are rounded.

After source-data edits, refresh all 10 PivotTables. The GETPIVOTDATA helpers and chart values update after refresh. Source-table filters do not filter the dashboard. New categories require extending the chart helper lists and chart ranges.

This historical analysis uses no macros, external workbook links or predictive model. Read the project README for sampling, missing-category, repeated-row and causal-interpretation limitations.

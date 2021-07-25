<%* // Template generates generate test cases from selection by splitting comma-separated strings. String in clipboard is used as a  beginning part of the case summary

clip = await tp.system.clipboard(); %>

<%* tc_description = "\n- " + tp.file.selection() + ","; %>
<%* generated = ("," + clip).split(',').join( tc_description); %>
<%* tR += generated; %>


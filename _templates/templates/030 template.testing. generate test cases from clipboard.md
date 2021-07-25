<%* <%* // Template generates generate test cases from clipboard by splitting comma-separated strings
clip = await tp.system.clipboard(); %>

<%* tc_description = "\n- " + await tp.system.prompt("Please enter a test case description") + ","; _%>
<%* generated = ("," + clip).split(',').join( tc_description); %>
<%* tR += generated; _%>


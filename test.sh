#!/bin/bash

# URL to check
URL="https://example.com"

# Check the status of the URL
STATUS=$(curl -o /dev/null -s -w "%{http_code}" $URL)

# Create or overwrite the HTML file with the status result
HTML_FILE="url_status.html"
cat <<EOL > $HTML_FILE
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Status</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        h1 { color: green; }
        .error { color: red; }
    </style>
</head>
<body>
    <h1>URL Status Checker</h1>
    <p>URL: <a href="$URL">$URL</a></p>
EOL

# Display status code and corresponding message
if [ $STATUS -eq 200 ]; then
    echo "<p>Status: <span class='success'>Online (HTTP $STATUS)</span></p>" >> $HTML_FILE
else
    echo "<p>Status: <span class='error'>Offline or Error (HTTP $STATUS)</span></p>" >> $HTML_FILE
fi

# Close the HTML tags
cat <<EOL >> $HTML_FILE
</body>
</html>
EOL

# Output a message to the terminal
echo "HTML report generated: $HTML_FILE"









echo > SL0G echo "<ht=l>" >> $06 echo "chead) >> 5L0G echo "<atyle>" >> $L0G echo table, th, td border: lpx solid black, porder-collapse: collapser )" >> $L0G echo " th, td I font-size: l0pti padding: 8xn) >> $L0G echo "alert ( font-s1ze: l0pt; font-family: verdana, padding: 5pxi background-color: blacki background-size: 50" echo "</style>- >> $10G autoi color: white;) echo -</head>" >> $L0G echo " <BODY text -black link-yellow vlink-white>" >> $10G echo • div class-"alert"> <otrong>< B>Current Capacity of App Nodos in 4. x 01 cluster as of $DATE </B></atrong></div>" >> SL0G echo" (bE> >> $L0G echo <br> >> SL0G echo " <font size-"2" face="verdana" J >> 5L0G echo <table>- >> $10G echo " <tr>" >> SL0G echo <table BORDER-I"2\">" >> SLOG eCho " <tr bgcolor- D0DoDo> >> $L0G echo <th> QA APP Node</th>" >> $L0G echo <th>CpU Request (Core) </th>" >> $LOG echo <th>CrU Limits (Core)</th> >> $10G echo <th>Mamory Requests (GB) </th>" >> 5L0G echo <th>Momory Limits (GB) </th>" >> $L0G echo <th>CpU Available (Core) </th>" >> $L0G echo <th>Memory Available (GB) </th>" >> $L0G echo <th>Total Pod Count</th>" >> $L0G echo <ItE> >> SL0G echo" trX" >> SL0G
 14 login into clustert
cd_logout-"oc4 logout" echo "logout from current logged cluster'

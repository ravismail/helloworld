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

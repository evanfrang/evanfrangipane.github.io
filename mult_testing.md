<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mult Testing</title>
  <script src="https://unpkg.com/marked@4.0.12/lib/marked.min.js"></script>

</head>
<body>

  <div id="markdown-container">Loading content...</div> <!-- Placeholder for content -->

  <script>
    // GitHub API URL to fetch the file (base64 encoded content)
    const url = 'https://api.github.com/repos/evanfrang/mult_testing/contents/README.md';

    // Fetch the file using the GitHub API
    fetch(url)
      .then(response => response.json())  // Parse the JSON response
      .then(data => {
        // Decode the base64 content of the markdown file
        const markdownContent = atob(data.content); // Base64 decode
        // Render the Markdown content as HTML using Marked.js
        document.getElementById('markdown-container').innerHTML = marked(markdownContent);
      })
      .catch(error => {
        // Handle errors and show a fallback message
        document.getElementById('markdown-container').innerText = 'Failed to load content.';
        console.error('Error fetching content:', error);
      });
  </script>

</body>
</html>
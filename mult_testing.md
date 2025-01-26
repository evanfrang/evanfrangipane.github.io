<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mult Testing</title>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
</head>
<body>

  <div id="markdown-container">Loading content...</div>

  <script>
    const url = 'https://cdn.jsdelivr.net/gh/evanfrang/mult_testing/main/README.md'; // The jsDelivr URL

    fetch(url)
      .then(response => {
        if (!response.ok) throw new Error('Failed to load content');
        return response.text();
      })
      .then(markdown => {
        // Render Markdown as HTML using Marked.js
        document.getElementById('markdown-container').innerHTML = marked(markdown);
      })
      .catch(error => {
        // Handle errors and show a fallback message
        document.getElementById('markdown-container').innerText = 'Failed to load content.';
        console.error('Error fetching content:', error);
      });
  </script>

</body>
</html>

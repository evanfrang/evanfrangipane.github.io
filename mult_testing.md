<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
  fetch('https://cdn.jsdelivr.net/gh/evanfrang/mult_testing/README.md')
    .then(response => {
      if (!response.ok) throw new Error('Network response was not ok');
      return response.text();
    })
    .then(markdown => {
      document.getElementById('dynamic-markdown-content').innerHTML = marked(markdown);
    })
    .catch(error => {
      document.getElementById('dynamic-markdown-content').innerText = "Failed to load content.";
      console.error('There was a problem fetching the content:', error);
    });
</script>

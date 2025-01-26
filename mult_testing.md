---
layout: page
title: Multiple Testing
permalink: /mult_test/
---
<div id="dynamic-markdown-content">Loading content...</div>

<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
  fetch('https://raw.githubusercontent.com/evanfrang/mult_testing/README.md')
    .then(response => response.text())
    .then(markdown => {
      document.getElementById('dynamic-markdown-content').innerHTML = marked(markdown);
    })
    .catch(error => {
      document.getElementById('dynamic-markdown-content').innerText = "Failed to load content.";
      console.error(error);
    });
</script>

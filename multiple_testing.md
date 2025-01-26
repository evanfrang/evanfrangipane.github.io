---
layout: page
title: Multiple Testing
---

{% include_relative mult_testing/README.md %}
<script>
    document.querySelectorAll('img').forEach(img => {
        if (img.src.includes('README_files')) {
            img.src = img.src.replace('README_files', '/mult_testing/README_files');
        }
    });
</script>

---
layout: page
title: Multiple Testing
---

{% include_relative mult_testing/README.md %}

<script>
    document.addEventListener("DOMContentLoaded", function () {
        // Select all images within the rendered README content
        document.querySelectorAll('img').forEach(img => {
            if (img.src.includes('README_files') && !img.src.includes('/mult_testing/')) {
                img.src = img.src.replace('README_files', '/mult_testing/README_files');
            }
        });
    });
</script>

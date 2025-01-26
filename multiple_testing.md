---
layout: page
title: Multiple Testing
---

{% include_relative mult_testing/README.md %}

<script>
    // Ensure the script runs after the DOM has loaded
    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll('img').forEach(img => {
            if (img.src.includes('README_files')) {
                // Update image path to point to submodule
                img.src = img.src.replace('README_files', '/mult_testing/README_files');
            }
        });
    });
</script>

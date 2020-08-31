# Thredup_Sort

**8/18/2020 Update:**
**This project has migrated and merged with a larger project called "thredup-scraper-api". Please check out that repository instead**


Thredup is an online consignment store with thousands of options but their filtering system could be better. Due to environmental reasons, I only purchase clothing made of natural materials (wool, cotton, silk, etc.) and avoid polyester and any clothing where the fabric content is unknown.

The following code filters out clothing by removing search results with the words: "Polyester”, “Fabric details not available" and "No Fabric Content". A URL is input as a variable and all results (that don't contain the forbidden words) are opened in a new tab for viewing.

“url” – (line 11) the only input into the file. Take the current URL from the thredup page and replace the current default.

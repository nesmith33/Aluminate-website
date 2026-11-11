# Aluminate v1.14 — SEO and migration checklist

## Implemented
- Unique titles and meta descriptions for six primary pages and Industry Insights
- Canonical tags, Open Graph metadata, Organization schema, sitemap.xml, robots.txt
- Industry Insights index linked in footer, absent from main navigation
- Two legacy article URLs represented by staging placeholders
- Responsive baseline stylesheet and common navigation/footer JavaScript rebuilt because v1.13 archive omitted them
- GHL form integration retained

## BLOCKERS — do not publish without resolving
1. Original WordPress article bodies, images, dates and metadata must be exported from DreamHost and inserted into both placeholder article pages.
2. Original v1.13 CSS, JS, Finishes art assets were absent from supplied archive; this package includes rebuilt approximations and fallback images. Visually compare every page to approved design before deployment.
3. Confirm the two latest approved v1.14 hero revision images and tactile icon are the exact intended files.
4. Validate redirects for all other indexed WordPress URLs using Search Console crawl export.
5. Confirm production domain canonical handling, slash conventions, analytics IDs, Search Console verification and GHL form submission events.
6. Run Lighthouse and mobile browser QA after deploying to a Vercel preview.
7. Add article schema with factual author, publication and modification dates only after original articles are imported.

No search-ranking or performance outcomes are claimed without measurement.

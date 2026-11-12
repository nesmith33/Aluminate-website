# Aluminate v2.0 SEO launch checklist

## Required before DNS cutover

- **BLOCKER: migrate the full original content and media** for `/how-to-create-a-nutrition-facts-label-for-a-beverage/` and `/choosing-the-right-aluminum-can-liner/` from DreamHost/WordPress into Vercel at exactly those paths. They are intentionally NOT included in this package; URL preservation alone does not move content.
- Do not publish the Industry Insights index until both article pages return HTTP 200 with original substance, headings, images, publication details and self-referencing canonicals.
- Add the two article URLs to sitemap.xml once migrated, with valid Article structured data and verified author/date fields.
- Verify Vercel clean URL routing for all six primary pages and the blog index; check 200 statuses and no redirect loops.
- Export and compare existing indexed URLs and backlinks; map all changed URLs using permanent 301 redirects only where needed.
- Confirm Google Search Console and Bing Webmaster Tools ownership; submit sitemap after cutover.
- Verify robots.txt, canonicals, title/description, Open Graph preview, mobile navigation, GHL contact form and accessibility.
- Run PageSpeed Insights/Core Web Vitals and check image compression/widths and CLS.
- Monitor 404s, indexing, traffic and rankings for 4-8 weeks after cutover.

## Implementation notes

- Existing website visuals, text and assets were retained; metadata was improved and a footer-only Industry Insights link added.
- Article index previews are original summaries, not copied article text.
- Sitemap excludes unmigrated article paths to avoid asserting that they exist on Vercel.
- No SEO outcome/ranking guarantee is implied.

## Industry Insights migration (v2.0)
- Both supplied Word articles have been converted into full HTML articles at their existing URLs, with embedded images.
- Confirm original publication dates and any historical author attribution in WordPress; these were not supplied and have not been invented.
- Editorial review recommended for the original epoxy/BPANI article: its health, California regulatory, liner availability and 99.9% compatibility claims are preserved from the supplied document, but may need current legal/technical validation before public launch.
- Nutrition labeling requirements should also be checked against current FDA rules.
- After Vercel deployment, test both URLs directly, images, sitemap, mobile layout, and Google Search Console indexing.

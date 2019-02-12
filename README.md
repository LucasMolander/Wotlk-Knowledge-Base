# Wrath of the Lich King Knowledge Base
This README (along with this project) is a work in progress.

## Design Decisions and Explanations
Explanations for some weird design decisions.

### Including Everything in `_layouts/default.html`
Explanation for this messiness!
It's really because linking to other files doesn't really work.
Therefore, just use the 'page' `GET` argument and set the HTML dynamically.


## Development Workflow
Asdf

### Adding a New Page
If you've developed or generate some nice HTML and want to add it to the website,
you must edit `_layouts/default.html`:
  1) Add a div in `<div id="pages">`
  2) Add its entry to `getDirectory()`
  3) Add a `btn` link to it in the `#main-banner` banner


## Asdf


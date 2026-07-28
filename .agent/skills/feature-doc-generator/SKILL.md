---
name: feature-doc-generator
description: Generate feature documentation from user descriptions using the standard project template and naming conventions. Use this skill whenever the user asks to create or generate a "feature doc", "feature documentation", or add a feature to the backlog.
context: fork
---

# Feature Document Generator

This skill defines the standard procedure for creating feature documentation in the project.

## Rules & Conventions

When the user asks to generate a feature doc based on a description, absolutely follow these rules:

1. **Template Locator:** 
   - Use the isolated template file bundled with this skill: `assets/feature_template.md`. Always base the new document on this template.
   
2. **Format:** 
   - Feature docs must be created in Markdown format.

3. **Storage Location:** 
   - Feature docs must be stored in the `features backlog` directory, located inside the directory with the stream name (e.g., `PUC/features backlog/` or `E2E VC/features backlog/`).
   - If the `features backlog` directory does not exist for the stream, explicitly create it.
   - The stream name can be inferred from the directory where the `features backlog` folder is or will be placed.

4. **Feature ID Format:** 
   - The Feature ID must be composed exactly as follows: 
     `{stream name}-{feature order number in the folder, with two leading zeroes}-{up-to-three-words-summary-of-feature-description}`
   - *Note on Order Number:* Check the existing files in the stream's `features backlog` to determine the next sequential number. For example, if `PUC-001` exists, the next is `PUC-002`. First file is `001`.
   - *Note on Summary:* Take the core essence of the feature description and summarize it in up to 3 words, separated by dashes (e.g., `inventory-levels-visibility`).

5. **Filename:** 
   - The file name of the feature doc must be the exact Feature ID with a `.md` extension.
   - Example: `PUC-001-inventory-levels-visibility.md`

6. **Prefilling Content:** 
   - When creating the document, prefill the template fields (e.g., Summary, User Story, Acceptance Criteria) based on the feature description provided.
   - Do not omit comments with possible values in the metadata section, propagate them to the resulting document along with fields values.
   - Where inference is not possible (e.g., Technical Notes, missing prerequisites), keep the placeholder lines exactly as they are in the template. Do not invent information that wasn't provided or easily inferred.

## Process

1. Identify the requested stream and the feature description(s) from the user's prompt.
2. Locate the stream directory and its `features backlog` subfolder.
3. List the existing contents of the `features backlog` to determine the next `feature order number`.
4. Generate the Feature ID(s) and corresponding `.md` filename(s).
5. Read the bundled template at `assets/feature_template.md`.
6. Create the new feature doc(s) and notify the user once completed.

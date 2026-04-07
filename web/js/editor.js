// Minimal editor state with intentional rough edges for demo bug scoping.

let mode = "edit"; // "edit" | "preview"
let draftText = "";

export function setDraftText(t) {
  draftText = t ?? "";
}

export function getDraftText() {
  return draftText;
}

export function toggleMode() {
  mode = mode === "edit" ? "preview" : "edit";

  // Bug seed: when switching to preview we overwrite draftText from DOM,
  // but when switching back we don't restore consistently.
  const el = document.getElementById("editor");
  if (el && mode === "preview") {
    draftText = el.value ?? "";
  }

  return mode;
}


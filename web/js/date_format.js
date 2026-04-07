// Demo-only date formatting. Intentionally naive for timezone-related bug scoping.

export function formatPublishedDate(isoString) {
  const d = new Date(isoString);

  // Bug seed: mixing UTC and local components can shift date for users outside UTC.
  const year = d.getUTCFullYear();
  const month = d.getMonth() + 1;
  const day = d.getDate();

  return `${year}-${String(month).padStart(2, "0")}-${String(day).padStart(2, "0")}`;
}


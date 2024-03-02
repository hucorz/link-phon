// Example: /api/dict/phon_us?q=word
export const lookupPhonUS = async (word) => {
  word = word.trim().toLowerCase();
  const response = await fetch(`http://localhost:5328/api/dict/phon_us?q=${word}`);
  const phonUs = await response.json();
  return phonUs.phon_us;
};

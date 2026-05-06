(() => {
  const dataEl = document.getElementById('problem-data');
  const form = document.getElementById('cloze-form');
  if (!dataEl || !form) return;

  const problem = JSON.parse(dataEl.textContent);
  const storageKey = `problem:${problem.id}`;
  const submitBtn = document.getElementById('btn-submit');
  const resetBtn = document.getElementById('btn-reset');
  const readout = document.getElementById('score-readout');

  const shuffle = (arr) => {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };

  // Build a <select> + (hidden) explanation slot for every blank span.
  const blankSpans = form.querySelectorAll('.cloze-blank');
  blankSpans.forEach((span) => {
    const name = span.dataset.blank;
    const def = problem.blanks[name];
    if (!def) return;

    const select = document.createElement('select');
    select.className = 'cloze-select';
    select.name = name;
    select.dataset.blank = name;

    const placeholder = document.createElement('option');
    placeholder.value = '';
    placeholder.textContent = '— select —';
    select.appendChild(placeholder);

    const opts = shuffle([def.answer, ...def.distractors]);
    opts.forEach((opt) => {
      const o = document.createElement('option');
      o.value = opt;
      o.textContent = opt;
      select.appendChild(o);
    });

    span.replaceWith(select);

    select.addEventListener('change', () => {
      select.classList.remove('correct', 'incorrect');
    });
  });

  const totalBlanks = Object.keys(problem.blanks).length;

  // One panel below the form holds every explanation after Submit.
  let panel = document.getElementById('explanations-panel');
  if (!panel) {
    panel = document.createElement('section');
    panel.id = 'explanations-panel';
    panel.className = 'explanations-panel';
    panel.hidden = true;
    form.insertAdjacentElement('afterend', panel);
  }

  const evaluate = () => {
    let correct = 0;
    let unanswered = 0;
    const items = [];
    Object.entries(problem.blanks).forEach(([name, def]) => {
      const select = form.querySelector(`select[data-blank="${name}"]`);
      if (!select) return;

      let status;
      if (select.value === '') {
        unanswered++;
        select.classList.remove('correct');
        select.classList.add('incorrect');
        status = 'unanswered';
      } else if (select.value === def.answer) {
        correct++;
        select.classList.remove('incorrect');
        select.classList.add('correct');
        status = 'correct';
      } else {
        select.classList.remove('correct');
        select.classList.add('incorrect');
        status = 'incorrect';
      }

      const mark = status === 'correct' ? '✓' : '✗';
      items.push(
        `<li class="explain-${status}">` +
        `<span class="explain-mark">${mark}</span>` +
        `<div><strong>${escapeHtml(def.answer)}.</strong> ${escapeHtml(def.explanation)}</div>` +
        `</li>`
      );
    });

    panel.innerHTML = `<h3>Explanations</h3><ul class="explanations-list">${items.join('')}</ul>`;
    panel.hidden = false;

    const allRight = correct === totalBlanks;
    readout.textContent = allRight
      ? `All ${totalBlanks} correct.`
      : `${correct} / ${totalBlanks} correct${unanswered ? ` (${unanswered} unanswered)` : ''}.`;
    readout.classList.toggle('all-correct', allRight);

    // Persist progress.
    const prev = loadState();
    const attempts = (prev.attempts || 0) + 1;
    const state = {
      attempts,
      lastScore: correct,
      total: totalBlanks,
      completed: allRight || prev.completed === true,
      completedAt: allRight ? new Date().toISOString() : prev.completedAt || null,
    };
    saveState(state);
  };

  const reset = () => {
    form.querySelectorAll('select.cloze-select').forEach((s) => {
      s.value = '';
      s.classList.remove('correct', 'incorrect');
    });
    if (panel) { panel.hidden = true; panel.innerHTML = ''; }
    readout.textContent = '';
    readout.classList.remove('all-correct');
  };

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    evaluate();
  });
  resetBtn.addEventListener('click', reset);

  // Restore prior status line on load (do not restore selections — fresh attempt each visit).
  const prev = loadState();
  if (prev.completed) {
    readout.textContent = `Previously completed (${prev.attempts} attempt${prev.attempts === 1 ? '' : 's'}).`;
  } else if (prev.attempts) {
    readout.textContent = `Last attempt: ${prev.lastScore} / ${prev.total}.`;
  }

  function loadState() {
    try { return JSON.parse(localStorage.getItem(storageKey)) || {}; }
    catch { return {}; }
  }
  function saveState(s) {
    try { localStorage.setItem(storageKey, JSON.stringify(s)); } catch {}
  }
  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;',
    }[c]));
  }
})();

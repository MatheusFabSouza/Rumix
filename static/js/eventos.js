const spinner = `
<div class="d-flex justify-content-center align-items-center" style="height:160px;">
  <div class="spinner-border"></div>
</div>`;

let modal;

function csrf() {
  return document.cookie.split('; ').find(c => c.startsWith('csrftoken='))?.split('=')[1];
}

async function getHTML(url, opts={}) {
  opts.headers = { ...(opts.headers||{}), 'X-Requested-With':'XMLHttpRequest' };
  const r = await fetch(url, opts);
  return { ok:r.ok, status:r.status, text: await r.text(), ct:r.headers.get('content-type')||'' };
}

async function loadTable() {
  const box = document.getElementById('div-tabela-eventos');
  box.innerHTML = spinner;
  const r = await getHTML(EVENTOS_CONFIG.tableUrl);
  box.innerHTML = r.ok ? r.text : 'erro';
}

async function loadMessages() {
  if(!EVENTOS_CONFIG.messagesUrl) return;
  const r = await getHTML(EVENTOS_CONFIG.messagesUrl);
  if(r.ok) document.getElementById('div-mensagens').innerHTML = r.text;
}

async function openModal(url) {
  const el = document.getElementById('modalEvento');
  const body = document.getElementById('modal-evento-content');
  body.innerHTML = spinner;
  const r = await getHTML(url);
  body.innerHTML = r.text;
  modal = modal || new bootstrap.Modal(el);
  modal.show();
}

async function submitForm(form) {
  const r = await getHTML(form.action, {
    method:'POST',
    headers:{ 'X-CSRFToken': csrf() },
    body:new FormData(form)
  });

  if(r.status===400){
    document.getElementById('modal-evento-content').innerHTML = r.text;
    return;
  }

  modal.hide();
  await loadTable();
  await loadMessages();
}

document.addEventListener('click', e => {
  const btn = e.target.closest('.btn-detail,.btn-edit,.btn-delete');
  if(btn){ e.preventDefault(); openModal(btn.dataset.url); }

  if(e.target.id==='btn-novo'){ e.preventDefault(); openModal(EVENTOS_CONFIG.createUrl); }
  if(e.target.id==='btn-refresh'){ loadTable(); }
});

document.addEventListener('submit', e => {
  if(e.target.id==='eventoForm'){
    e.preventDefault();
    submitForm(e.target);
  }
});

window.Eventos = {
  init(cfg){
    window.EVENTOS_CONFIG = cfg;
    loadTable();
    loadMessages();
  }
};

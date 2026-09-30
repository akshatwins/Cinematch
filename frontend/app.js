const $=id=>document.getElementById(id);
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"}[c]));

async function api(url){const r=await fetch(url);if(!r.ok)throw new Error("API error");return r.json()}

function card(m){
  return `<article class="card" onclick="openMovie(${m.id})">
    ${m.poster_url?`<img class="poster" src="${m.poster_url}" loading="lazy" alt="${esc(m.title)} poster">`:`<div class="poster"></div>`}
    <div class="info"><div class="title">${esc(m.title)}</div><div class="meta">${m.year||"—"} • ★ ${Number(m.rating||0).toFixed(1)}</div></div>
  </article>`;
}

async function load(){
  const q=$("q").value.trim(), genre=$("genre").value, rating=$("rating").value;
  let url=q?`/api/search?q=${encodeURIComponent(q)}`:`/api/movies?min_rating=${rating}${genre?`&genre=${genre}`:""}`;
  try{$("grid").innerHTML=(await api(url)).map(card).join("")||"<p>No movies found.</p>"}catch(e){$("grid").innerHTML="<p>Could not load movies.</p>"}
}

async function loadGenres(){
  try{const gs=await api("/api/genres");$("genre").innerHTML='<option value="">All genres</option>'+gs.map(g=>`<option value="${g.id}">${esc(g.name)}</option>`).join("")}catch(e){}
}

async function openMovie(id){
  try{
    const m=await api(`/api/movies/${id}`);
    $("detail").classList.remove("hidden");
    $("detail").innerHTML=`<div class="detail-inner">
      ${m.poster_url?`<img src="${m.poster_url}" alt="${esc(m.title)}">`:"<div></div>"}
      <div><div class="eyebrow">MOVIE DETAIL</div><h2>${esc(m.title)}</h2>
      <div class="meta">${m.year||"—"} • ★ ${Number(m.rating||0).toFixed(1)} • ${m.vote_count.toLocaleString()} votes${m.runtime?` • ${m.runtime} min`:""}</div>
      <p>${esc(m.overview)}</p><div class="chips">${m.genres.map(g=>`<span class="chip">${esc(g.name)}</span>`).join("")}</div>
      ${m.trailer_url?`<p><a href="${m.trailer_url}" target="_blank" style="color:#b7ff48">Watch trailer ↗</a></p>`:""}
      </div></div>`;
    $("detail").scrollIntoView({behavior:"smooth"});
    const recs=await api(`/api/movies/${id}/recommendations?limit=10`);
    $("recs").classList.remove("hidden");
    $("recgrid").innerHTML=recs.map(r=>card(r.movie)).join("");
  }catch(e){alert("Movie details are unavailable right now.")}
}

$("q").addEventListener("input",load);$("genre").addEventListener("change",load);$("rating").addEventListener("change",load);
loadGenres();load();

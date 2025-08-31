const API_URL = "http://127.0.0.1:5000/match";

function previewImage(file) {
  const reader = new FileReader();
  reader.onload = e => {
    document.getElementById("preview").innerHTML =
      `<img src="${e.target.result}" style="max-width:200px;border:1px solid #ccc;border-radius:8px">`;
  };
  reader.readAsDataURL(file);
}

async function searchByImage(file) {
  const formData = new FormData();
  formData.append("image", file);

  const res = await fetch(API_URL, {
    method: "POST",
    body: formData
  });

  const data = await res.json();
  renderResults(data);
}

function renderResults(products) {
  const resultsDiv = document.getElementById("results");
  resultsDiv.innerHTML = "";
  products.forEach(p => {
    const card = document.createElement("div");
    card.style.border = "1px solid #ccc";
    card.style.margin = "10px";
    card.style.padding = "10px";
    card.style.borderRadius = "8px";

    card.innerHTML = `
      <img src="${p.image}" style="max-width:150px;border-radius:6px"><br>
      <b>${p.name}</b><br>
      Category: ${p.category}<br>
      Price: ₹${p.price}<br>
      Similarity: ${p.similarity}%
    `;
    resultsDiv.appendChild(card);
  });
}

document.getElementById("fileInput").addEventListener("change", e => {
  if (e.target.files[0]) {
    previewImage(e.target.files[0]);
    searchByImage(e.target.files[0]);
  }
});

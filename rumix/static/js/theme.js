// Detecta o botão e ícone.
const toggle = document.getElementById("theme-toggle");
const icon = document.getElementById("theme-icon");

// Se houver tema salvo, aplica automaticamente.
function setIcon(isDark) {
    icon.style.transform = "rotate(180deg)";
    setTimeout(() => {
        icon.textContent = isDark ? "☀️" : "🌙";
        icon.style.transform = "rotate(0deg)";
    }, 200);
}

// Carrega o tema salvo Ao clicar, alterna o modo escuro/claro e salva a escolha.
if (localStorage.getItem("theme") === "dark") {
    document.body.classList.add("dark");
    setIcon(true);
}

// Atualiza o ícone com efeito visual.
toggle.addEventListener("click", () => {
    const dark = document.body.classList.toggle("dark");
    setIcon(dark);
    localStorage.setItem("theme", dark ? "dark" : "light");
});

console.log("Dark mode ativo!");

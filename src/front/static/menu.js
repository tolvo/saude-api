export const tabelas = {
  Principais: [
    { nome: "CIDADAO", icon: "👤", label: "Cidadão" },
    { nome: "PROFISSIONAL", icon: "👨‍⚕️", label: "Profissional" },
    { nome: "UNIDADE_SAUDE", icon: "🏥", label: "Unidade de Saúde" },
  ],
  Profissionais: [
    { nome: "MEDICO", icon: "🩺", label: "Médico" },
    { nome: "ENFERMEIRO", icon: "💉", label: "Enfermeiro" },
  ],
  Unidades: [
    { nome: "HOSPITAL", icon: "🏥", label: "Hospital" },
    { nome: "UNIDADE_BASICA_SAUDE", icon: "🏥", label: "UBS" },
  ],
  Atendimentos: [
    { nome: "CONSULTA", icon: "📋", label: "Consulta" },
    { nome: "EXAME", icon: "🔬", label: "Exame" },
    { nome: "RECEITA", icon: "💊", label: "Receita" },
  ],
  Procedimentos: [
    { nome: "INTERNACAO", icon: "🛏️", label: "Internação" },
    { nome: "CIRURGIA", icon: "⚕️", label: "Cirurgia" },
    { nome: "VACINACAO", icon: "💉", label: "Vacinação" },
  ],
  Auxiliares: [
    { nome: "VACINA", icon: "💉", label: "Vacina" },
    { nome: "ALERGIA", icon: "⚠️", label: "Alergia" },
    { nome: "PROFISSIONAL_ATUA_US", icon: "🔗", label: "Prof. x Unidade" },
    { nome: "MEDICO_CIRURGIA", icon: "🔗", label: "Médico x Cirurgia" },
    { nome: "ENFERMEIRO_CIRURGIA", icon: "🔗", label: "Enferm. x Cirurgia" },
    {
      nome: "PROFISSIONAL_INTERNACAO",
      icon: "🔗",
      label: "Prof. x Internação",
    },
  ],
};

export function renderMenu() {
  const container = document.getElementById("menu-tabelas");
  if (!container) return;

  let html = "";

  for (const [categoria, items] of Object.entries(tabelas)) {
    html += `<div class="menu-item">
            <h3>${categoria}</h3>`;

    items.forEach((t) => {
      html += `
                <a href="/form/${t.nome}">${t.icon} Inserir ${t.label}</a>
                <a href="/list/${t.nome}">${t.icon} Listar ${t.label}</a>
            `;
    });

    html += `</div>`;
  }

  container.innerHTML = html;
}

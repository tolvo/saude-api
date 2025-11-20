export const tabelas = [
    "CIDADAO",
    "ALERGIA",
    "UNIDADE_SAUDE",
    "VACINA",
    "PROFISSIONAL",
    "ENFERMEIRO",
    "MEDICO",
    "UNIDADE_BASICA_SAUDE",
    "HOSPITAL",
    "INTERNACAO",
    "CIRURGIA",
    "CONSULTA",
    "VACINACAO",
    "EXAME",
    "RECEITA",
    "PROFISSIONAL_ATUA_US",
    "MEDICO_CIRURGIA",
    "ENFERMEIRO_CIRURGIA",
    "PROFISSIONAL_INTERNACAO"
];

export function renderMenu() {
    const ul = document.getElementById("menu-tabelas");
    if (!ul) return;

    tabelas.forEach(t => {
        ul.innerHTML += `
            <li><a href="/form/${t}">Inserir ${t}</a></li>
            <li><a href="/list/${t}">Listar ${t}</a></li>
        `;
    });
}
